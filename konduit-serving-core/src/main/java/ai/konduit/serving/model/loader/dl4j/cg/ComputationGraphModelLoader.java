/*
 *
 *  * ******************************************************************************
 *  *  * Copyright (c) 2015-2019 Skymind Inc.
 *  *  * Copyright (c) 2019 Konduit AI.
 *  *  *
 *  *  * This program and the accompanying materials are made available under the
 *  *  * terms of the Apache License, Version 2.0 which is available at
 *  *  * https://www.apache.org/licenses/LICENSE-2.0.
 *  *  *
 *  *  * Unless required by applicable law or agreed to in writing, software
 *  *  * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 *  *  * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 *  *  * License for the specific language governing permissions and limitations
 *  *  * under the License.
 *  *  *
 *  *  * SPDX-License-Identifier: Apache-2.0
 *  *  *****************************************************************************
 *
 *
 */

package ai.konduit.serving.model.loader.dl4j.cg;

import ai.konduit.serving.model.loader.ModelGuesser;
import ai.konduit.serving.model.loader.ModelLoader;
import io.vertx.core.buffer.Buffer;
import lombok.AllArgsConstructor;
import lombok.Data;
import org.deeplearning4j.nn.graph.ComputationGraph;
import org.deeplearning4j.util.ModelSerializer;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;

@Data
@AllArgsConstructor
public class ComputationGraphModelLoader implements ModelLoader<ComputationGraph> {

    private File pathToModel;

    @Override
    public Buffer saveModel(ComputationGraph model) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        try {
            ModelSerializer.writeModel(model, byteArrayOutputStream, true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return Buffer.buffer(byteArrayOutputStream.toByteArray());
    }

    @Override
    public ComputationGraph loadModel() throws Exception {
        return (ComputationGraph) ModelGuesser.loadModelGuess(pathToModel.getAbsolutePath());
    }
}
