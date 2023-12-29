import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [data, setData] = useState({});
  const [formData, setFormData] = useState({});
  const sendReq = (e) => {
    e.preventDefault();
    axios
      .post('/api/form', { ...formData })
      .then((res) => {
        setData(res.data);
        setFormData({});
        console.log(data);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  return (
    <div>
      {Object.keys(data).length != 0 ? (
        !data.submit ? (
          <form onSubmit={sendReq}>
            <div>
              {data.form.map((element, index) => (
                <div key={index}>
                  {element.field}:{' '}
                  <input
                    type={element.input}
                    onChange={handleChange}
                    name={element.field}
                    value={
                      formData[element.field] ? formData[element.field] : ''
                    }
                  />
                </div>
              ))}
            </div>
            <button type="submit">Submit </button>
          </form>
        ) : (
          <div>Finished Onboarding</div>
        )
      ) : (
        <form onSubmit={sendReq}>
          <div>Start onboarding: </div>
          <button type="submit">Go </button>
        </form>
      )}
    </div>
  );
}

export default App;
