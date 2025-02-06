--- output

@rifaterdemsahin ➜ /workspaces/ServiceMesh/6_Symbols/SetupDocker (main) $ docker build -t your-service-mesh .
[+] Building 10.9s (10/10) FINISHED                                                                                               docker:default
 => [internal] load build definition from Dockerfile                                                                                        0.0s
 => => transferring dockerfile: 512B                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                          0.3s
 => [internal] load .dockerignore                                                                                                           0.0s
 => => transferring context: 2B                                                                                                             0.0s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:f9364cd6e0c146966f8f23fc4fd85d53f2e604bdde74e3c06565194dc4a02f85                    5.4s
 => => resolve docker.io/library/python:3.9-slim@sha256:f9364cd6e0c146966f8f23fc4fd85d53f2e604bdde74e3c06565194dc4a02f85                    0.0s
 => => sha256:9315c4821e723a7fb42220024e56534ecd042bd9ebb91aa3487c0a90cbbe9710 3.51MB / 3.51MB                                              0.3s
 => => sha256:7e8ac65e25aaa3b7a0cef09164fd2c6879c88b27bc9d50b5be34166a11479656 14.93MB / 14.93MB                                            0.9s
 => => sha256:f9364cd6e0c146966f8f23fc4fd85d53f2e604bdde74e3c06565194dc4a02f85 10.41kB / 10.41kB                                            0.0s
 => => sha256:e278b827219b44d04b4be79af72fb3c4458dbe15d96440d8694bb3fd9d0bbb5c 1.75kB / 1.75kB                                              0.0s
 => => sha256:096343841dd9d6129087a72170c0d3cd51e64a0c00934029a8927625637f51d1 5.28kB / 5.28kB                                              0.0s
 => => sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260 28.21MB / 28.21MB                                            0.7s
 => => sha256:b26995e9f45f14d5d4a45d1d0c50396482c1a6c1fcbbf5e6105cac49ef9afbba 248B / 248B                                                  0.9s
 => => extracting sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260                                                   1.3s
 => => extracting sha256:9315c4821e723a7fb42220024e56534ecd042bd9ebb91aa3487c0a90cbbe9710                                                   0.2s
 => => extracting sha256:7e8ac65e25aaa3b7a0cef09164fd2c6879c88b27bc9d50b5be34166a11479656                                                   0.9s
 => => extracting sha256:b26995e9f45f14d5d4a45d1d0c50396482c1a6c1fcbbf5e6105cac49ef9afbba                                                   0.0s
 => [internal] load build context                                                                                                           0.0s
 => => transferring context: 160B                                                                                                           0.0s
 => [2/5] WORKDIR /app                                                                                                                      0.0s
 => [3/5] COPY requirements.txt .                                                                                                           0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                4.0s
 => [5/5] COPY src/ .                                                                                                                       0.0s 
 => exporting to image                                                                                                                      1.1s
 => => exporting layers                                                                                                                     1.1s
 => => writing image sha256:f28563ece013e51771572d5beb5ffc94bb4d408905b806689c2f9a448af2cba8                                                0.0s
 => => naming to docker.io/library/your-service-mesh                           


 ---
 @rifaterdemsahin ➜ /workspaces/ServiceMesh/6_Symbols/SetupDocker (main) $ docker run -p 5000:5000 your-service-mesh
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [06/Feb/2025 11:55:26] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [06/Feb/2025 11:55:26] "GET /favicon.ico HTTP/1.1" 404 -
^C@rifaterdemsahin ➜ /workspaces/ServiceMesh/6_Symbols/SetupDocker (main) $ 


