package com.example.hongfan.myblog

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Toast
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.Response.Listener
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.Volley
import kotlinx.android.synthetic.main.activity_profile.*
import org.json.JSONObject

class profile : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_profile)

        val url = "http://travelforumproject.appspot.com/routerurls/users/"
        var jsonObj= JSONObject()
        jsonObj.put("username",username.text)
        jsonObj.put("email",email.text)

        val que = Volley.newRequestQueue(this)
        val req= JsonObjectRequest(Request.Method.GET,url,null,
                Listener {
                    response ->  Toast(response["success"].toString())

                },Response.ErrorListener {
            Toast("WRONG") })
        que.add(req)

    }
}
