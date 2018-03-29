package oli.clicker_hero;

import android.app.VoiceInteractor;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    public void POST(RequestQueue rq, final String key, final String value) {

        String url = "http://192.168.178.87:1234";
        StringRequest request = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                System.out.println(response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                System.out.println(error);
            }
        }) {

            protected Map<String, String> getParams() {

                Map<String, String> data = new HashMap<String, String>();
                data.put(key, value);
                return data;

            }

        };

        rq.add(request);

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final RequestQueue queue = Volley.newRequestQueue(this);

        final Button posttest = findViewById(R.id.posttest);

        posttest.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {

                POST(queue,"testKey", "testValue");

            }

        });

    }

}
