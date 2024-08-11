// Copyright (c) 2019-2024 ISciences, LLC.
// All rights reserved.
//
// This software is licensed under the Apache License, Version 2.0 (the "License").
// You may not use this file except in compliance with the License. You may
// obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <set>
#include <string>

#include "box.h"
#include "feature_sequential_processor.h"
#include "geos_utils.h"
#include "grid.h"
#include "operation.h"

namespace exactextract {

void
FeatureSequentialProcessor::process()
{
    while (m_shp.next()) {
        const Feature& f_in = m_shp.feature();

        auto geom = f_in.geometry();

        progress(f_in, m_include_cols.empty() ? "." : m_include_cols.front());

        Box feature_bbox = exactextract::geos_get_box(m_geos_context, geom);

        auto grid = common_grid(m_operations.begin(), m_operations.end());

        if (feature_bbox.intersects(grid.extent())) {
            // Crop grid to portion overlapping feature
            auto cropped_grid = grid.crop(feature_bbox);

            for (const auto& subgrid : subdivide(cropped_grid, m_max_cells_in_memory)) {
                std::unique_ptr<Raster<float>> coverage;

                std::set<std::string> processed;

                std::map<RasterSource*, RasterVariant> values_map;
                std::map<RasterSource*, RasterVariant> weights_map;

                for (const auto& op : m_operations) {
                    // Avoid processing same values/weights for different stats
                    if (processed.find(op->key()) != processed.end()) {
                        continue;
                    } else {
                        processed.insert(op->key());
                    }

                    if (!op->intersects(subgrid.extent())) {
                        continue;
                    }

                    // Lazy-initialize coverage
                    if (coverage == nullptr) {
                        coverage = std::make_unique<Raster<float>>(
                          raster_cell_intersection(subgrid, m_geos_context, geom));
                    }

                    if (values_map.find(op->values) == values_map.end()) {
                        values_map[op->values] = op->values->read_box(subgrid.extent().intersection(op->values->grid().extent()));
                    }

                    if (op->weighted()) {
                        if (weights_map.find(op->weights) == weights_map.end()) {
                            weights_map[op->weights] = op->weights->read_box(subgrid.extent().intersection(op->weights->grid().extent()));
                        }

                        m_reg.update_stats(f_in, *op, *coverage, values_map[op->values], weights_map[op->weights]);
                    } else {
                        m_reg.update_stats(f_in, *op, *coverage, values_map[op->values]);
                    }

                    progress();
                }
            }
        }

        write_result(f_in);
    }
}
}
