import React, { useState, useEffect, useContext } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import ReactDOM from "react-dom";

export const People = (props) => {
  const { store, actions } = useContext(Context);
const params = useParams();

const data = store.people[params.id]
console.log(data);
  return (
    <>
      <div className="jumbotron">
        <img
          className="image"
          src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAMAAAB6zFdcAAAAM1BMVEXMzMyWlpaTk5PPz8+amprKysrCwsKkpKSxsbGrq6ugoKDAwMC8vLy5ubmYmJjLy8u0tLQ9Vkh2AAAEYklEQVR4nO2Z6babOgxGARsbCEPe/2kvkgcMSRtYq6fhdu39oydVHCF9nmRTVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADw72NM61xrTGFZ1FK2qY6WT05ffL54eH3u9+hss2KfKRjj/Lwaau9yeG2vlmE8GbCZBvXZZcsbD/rcenvu91hsUyuND8GYR5MsUwzP1cnSnwrY9Km9baOH+eiheO4fz+kixksomnXTaXhtMOi/LjSaN8t0QgTzzC6aIbS3m4fQ7/rcaDkn7M/hJBTv3CBdsqTg6smNErZmoCk1T/cY5JszTqPPTv5O7z08xNI7p1K4n8vvBEbitGumrXTIKCYNyqyLWorO2Nj/+mH87HNqgnrq3KcfPtMHVcXH/tcP3VcHQg4hf3hEUYJFAlcxtPGa04mBqz/UOSODbH7rwcyp+8co2PcwQ+qhPkSnw1bzzPFmVU7Ga2RI6VrYyuawvPOgi05ss+r0gxl+RjWYSg1yX6saMpKn+LfM5bdIVrK0VItbqUrtXPSgf7Xxpsa3yANeNehKDXLuv9LAeGutLhi9tfOWxmvPHjSobqZBnyZoHBAXNJAvdAlptz1QcC+j5d4aaHj1WrbqHtlWlzSQib/+V/YBXewjUQNjchl8cw20erHP5xwLxUsaSFunQ6gu+j1oMPph8LGiursGLteJOqWvaCDxr23bZr/Da35dKAGtro131yAUtloh7XbEMxrIijqLg6ZMQlVNdbCmfnMNUm2fTgeXNBBDI2W2L41hZPlxlMq4eVS310DXQtv1czwvXNNAat8hJrp3+Ux7jfi6twZ6yh3WFXyZQ+AXNQgTab8Tpgo5HBzs7TWQY7H2YqoKr2lQLfV2HE5s9YHOittrkE8zKaqLGoSrhfEXGmh+1d01yOM2xXtRAy2xDueo/6MG9r0G5sx6MIRtdZdDe9T15hq8xLs/Nx5W9Udz6HMtkuzxEqRJZ6bk/dWDfrPkNt/VoD6sB1W6BMonybyybafpRCiWZWspfer9iGb1iO11t9yNLb2tavNzv3uHYg/7wjY2NRW9Ocv1kz/sAeHQNO6PTEG88jxe7D752irf3XQHXf8+oT6Q1x1zeeXn14qhi5M53LJKm6k5TP1Rc1yOq+JDh/d2Ft08yKTI5ejW5vMd5Y8Sinuvl8lhadJMbS/X/3GexzZa+u6mwqAZaeeW0uhK2ajP2D546AsPobAIz7V/Ldv3hO4uX6nkFyT5YqRos1u92jiVp+NVa5vb63V9cTDLHsy4Pfe7V+uVJqgvQ5o6vT7JlvwCaJ0FwTLsurtfrXqPJFenO6etPbQ3U320POZgse6rq0EIpn323vfT9j50tXjvuyK20KZ77KOdpump0z19KJyO4rNob5bpxYNY+rOvMH8YY4p7r83y2ubNDw8f9j/45OGdTwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAf5X/AH6qJR8G6+UXAAAAAElFTkSuQmCC"
        />
        <h1 className="display-4">{data.name}</h1>
        <span className="para">
          Contrary to popular belief, Lorem Ipsum is not simply random text. It
          has roots in a piece of classical Latin literature from 45 BC, making
          it over 2000 years old. Richard McClintock, a Latin professor at
          Hampden-Sydney College in Virginia, looked up one of the more obscure
          Latin words, consectetur, from a Lorem Ipsum passage, and going
          through the cites of the word in classical literature, discovered the
          undoubtable source.
        </span>
        <hr></hr>
        <div className="details">
          <p>Gender: {data.gender}</p>
          <p>Eye Color: {data.eye_color}</p>
          <p>Hair color: {data.hair_color}</p>
        </div>
      </div>
    </>
  );
};
