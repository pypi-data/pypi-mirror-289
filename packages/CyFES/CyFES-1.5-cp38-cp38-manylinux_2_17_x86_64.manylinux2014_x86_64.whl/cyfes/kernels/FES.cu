// MIT License

// Copyright (c) 2024 dechin

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

// nvcc -shared ./FES.cu -Xcompiler -fPIC -o ./libcufes.so
#include "./FES.cuh"

constexpr int THREADS = 64;
constexpr double kT = 8.314 * 300 / 4184;

__global__ void WeightKernel(int CV_LENGTH, double* bias, double* V, double shift, double* weight){
    int idx = blockIdx.x * blockDim.x + threadIdx.x;  
    if (idx < CV_LENGTH){
        V[idx] = bias[idx] / kT - shift;
        weight[idx] = expf(V[idx]);
    }
}

extern "C" int GetWeight(int CV_LENGTH, double* bias, double shift, double* weight){
    double *bias_device, *V_device, *weight_device;
    cudaMalloc(&bias_device, CV_LENGTH * sizeof(double));  
    cudaMalloc(&V_device, CV_LENGTH * sizeof(double));  
    cudaMalloc(&weight_device, CV_LENGTH * sizeof(double));  
    cudaMemcpy(bias_device, bias, CV_LENGTH * sizeof(double), cudaMemcpyHostToDevice); 
    int numBlocks = CV_LENGTH / THREADS + 1;
    WeightKernel<<<numBlocks, THREADS>>>(CV_LENGTH, bias_device, V_device, shift, weight_device); 
    cudaDeviceSynchronize();
    cudaMemcpy(weight, weight_device, CV_LENGTH * sizeof(double), cudaMemcpyDeviceToHost);
    cudaFree(bias_device);  
    cudaFree(V_device);
    cudaFree(weight_device); 
    cudaDeviceReset();
    return 1;
}

__global__ void DistKernel(int CV_LENGTH, CRD* crd, PATH* cv, double* dis){
    int idx = blockIdx.x * blockDim.x + threadIdx.x; 
    double tmp = 0.0;
    if (idx < CV_LENGTH){
        tmp += pow(crd[0].x - cv[idx].crds.x, 2);
        tmp += pow(crd[0].y - cv[idx].crds.y, 2);
        tmp += pow(crd[0].z - cv[idx].crds.z, 2);
        dis[idx] = sqrtf(tmp);
    }
}

extern "C" int GetDist(int CV_LENGTH, CRD* crd, PATH* cv, double* dis){
    CRD* crd_device;
    PATH* cv_device;
    double *dis_device;
    cudaMalloc(&crd_device, sizeof(CRD));
    cudaMalloc(&cv_device, CV_LENGTH*sizeof(PATH));
    cudaMalloc(&dis_device, CV_LENGTH*sizeof(double));
    cudaMemcpy(crd_device, crd, sizeof(CRD), cudaMemcpyHostToDevice);
    cudaMemcpy(cv_device, cv, CV_LENGTH*sizeof(PATH), cudaMemcpyHostToDevice);
    int numBlocks = CV_LENGTH / THREADS + 1;
    DistKernel<<<numBlocks, THREADS>>>(CV_LENGTH, crd_device, cv_device, dis_device);
    cudaDeviceSynchronize();
    cudaMemcpy(dis, dis_device, CV_LENGTH * sizeof(double), cudaMemcpyDeviceToHost);
    cudaFree(crd_device);
    cudaFree(cv_device);
    cudaFree(dis_device);
    cudaDeviceReset();
    return 1;
}

__global__ void GaussDistKernel(int CV_LENGTH, CRD* crd, PATH* cv, double* dis){
    int idx = blockIdx.x * blockDim.x + threadIdx.x; 
    double tmp = 0.0;
    if (idx < CV_LENGTH){
        tmp -= pow(crd[0].x - cv[idx].crds.x, 2);
        tmp -= pow(crd[0].y - cv[idx].crds.y, 2);
        tmp -= pow(crd[0].z - cv[idx].crds.z, 2);
        tmp /= 2.0;
        dis[idx] = expf(tmp);
    }
}

extern "C" int GaussGetDist(int CV_LENGTH, CRD* crd, PATH* cv, double* dis){
    CRD* crd_device;
    PATH* cv_device;
    double *dis_device;
    cudaMalloc(&crd_device, sizeof(CRD));
    cudaMalloc(&cv_device, CV_LENGTH*sizeof(PATH));
    cudaMalloc(&dis_device, CV_LENGTH*sizeof(double));
    cudaMemcpy(crd_device, crd, sizeof(CRD), cudaMemcpyHostToDevice);
    cudaMemcpy(cv_device, cv, CV_LENGTH*sizeof(PATH), cudaMemcpyHostToDevice);
    int numBlocks = CV_LENGTH / THREADS + 1;
    GaussDistKernel<<<numBlocks, THREADS>>>(CV_LENGTH, crd_device, cv_device, dis_device);
    cudaDeviceSynchronize();
    cudaMemcpy(dis, dis_device, CV_LENGTH * sizeof(double), cudaMemcpyDeviceToHost);
    cudaFree(crd_device);
    cudaFree(cv_device);
    cudaFree(dis_device);
    cudaDeviceReset();
    return 1;
}

__global__ void GaussDistHeightKernel(int CV_LENGTH, CRD* crd, PATH* cv, double* dis, double* height){
    int idx = blockIdx.x * blockDim.x + threadIdx.x; 
    double tmp = 0.0;
    if (idx < CV_LENGTH){
        tmp -= pow(crd[0].x - cv[idx].crds.x, 2);
        tmp -= pow(crd[0].y - cv[idx].crds.y, 2);
        tmp -= pow(crd[0].z - cv[idx].crds.z, 2);
        tmp /= 2.0;
        dis[idx] = expf(tmp) * height[idx];
    }
}

extern "C" int GaussGetDistHeight(int CV_LENGTH, CRD* crd, PATH* cv, double* dis, double* height){
    CRD* crd_device;
    PATH* cv_device;
    double *dis_device;
    double *height_device;
    cudaMalloc(&crd_device, sizeof(CRD));
    cudaMalloc(&cv_device, CV_LENGTH*sizeof(PATH));
    cudaMalloc(&dis_device, CV_LENGTH*sizeof(double));
    cudaMalloc(&height_device, CV_LENGTH*sizeof(double));
    cudaMemcpy(crd_device, crd, sizeof(CRD), cudaMemcpyHostToDevice);
    cudaMemcpy(height_device, height, CV_LENGTH*sizeof(double), cudaMemcpyHostToDevice);
    cudaMemcpy(cv_device, cv, CV_LENGTH*sizeof(PATH), cudaMemcpyHostToDevice);
    int numBlocks = CV_LENGTH / THREADS + 1;
    GaussDistHeightKernel<<<numBlocks, THREADS>>>(CV_LENGTH, crd_device, cv_device, dis_device, height_device);
    cudaDeviceSynchronize();
    cudaMemcpy(dis, dis_device, CV_LENGTH * sizeof(double), cudaMemcpyDeviceToHost);
    cudaFree(crd_device);
    cudaFree(cv_device);
    cudaFree(dis_device);
    cudaFree(height_device);
    cudaDeviceReset();
    return 1;
}
