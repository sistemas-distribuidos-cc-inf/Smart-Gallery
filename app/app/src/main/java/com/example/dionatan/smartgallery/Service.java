package com.example.dionatan.smartgallery;

import android.graphics.Bitmap;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Path;

/**
 * Created by dionatan on 07/12/17.
 */

public interface Service {
//        @POST("image")
//        Call<String> enviarImage(@Body Bitmap image);

        @Multipart
        @POST("/image")
        Call<String> enviarImage(@Part MultipartBody.Part file,
                                 @Part("imagem") RequestBody name);

}
