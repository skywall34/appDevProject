package com.example.hongfan.myblog

import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.support.v4.content.FileProvider
import android.support.v7.app.AppCompatActivity
import com.example.hongfan.myblog.R.id.btn_gallary
import kotlinx.android.synthetic.main.activity_upload_pic.*
import java.io.File
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.*


class uploadPics : AppCompatActivity() {

    var currencyPath: String?=null
    val TAKE_PICTURE = 1
    val SELECT_PICTURE=2

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_upload_pic)


        btn_gallary.setOnClickListener{
            dispatchGalleryIntent()

        }


        btn_camera.setOnClickListener{
            dispatchCameraIntent()
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if(requestCode==TAKE_PICTURE&& resultCode==Activity.RESULT_OK){
            try{
                val file=File(currencyPath)
                val uri= Uri.fromFile(file)
                imageView.setImageURI(uri)
            }catch (e:IOException) {
                e.printStackTrace()
            }
        }
        if(requestCode==SELECT_PICTURE && resultCode==Activity.RESULT_OK){
            try{
                val uri=data!!.data
                imageView.setImageURI(uri)
            }catch (e:IOException) {
                e.printStackTrace()
            }
        }
    }

    fun dispatchGalleryIntent() {
        val galleryIntent= Intent()
        galleryIntent.type="image/"
        galleryIntent.action = Intent.ACTION_GET_CONTENT
        startActivityForResult(Intent.createChooser(galleryIntent,"select image"),SELECT_PICTURE)
    }

    fun dispatchCameraIntent() {
        val cameraIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        if (cameraIntent.resolveActivity(packageManager) != null) {
            var photoFile: File? = null
            try {
                photoFile = createImage()

            } catch (e:IOException){
                e.printStackTrace()
            }
            if (photoFile!=null){
                val photoUri=FileProvider.getUriForFile(this,"com.example.hongfan.myblog.fileprovider",photoFile)

                cameraIntent.putExtra(MediaStore.EXTRA_OUTPUT,photoUri)
                startActivityForResult(cameraIntent,TAKE_PICTURE)
            }
        }
    }

    fun createImage():File{
        val timeStamp= SimpleDateFormat("yyyymmdd_hhmmss").format(Date())
        //val timeStamp= getDateTimeInstance()
        val imageName="JPEG"+timeStamp+"_"
        val storageDir=getExternalFilesDir(Environment.DIRECTORY_PICTURES)
        val image = File.createTempFile(imageName,".jpg",storageDir)
        currencyPath=image.absolutePath

        return image

    }
}


