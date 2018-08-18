package com.example.hongfan.myblog

import android.os.Bundle
import android.support.design.widget.TextInputEditText
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_post.*

class post : AppCompatActivity() {

    lateinit var posttitle:TextInputEditText


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_post)

        posttitle = findViewById(R.id.post_title)

        btn_submit.setOnClickListener{

            submitPost()


        }


    }


    private fun submitPost(){

        val title = posttitle.text.toString().trim()

            if (title.isEmpty()){
            posttitle.error="please enter a title"

        return
    }
    }

}
