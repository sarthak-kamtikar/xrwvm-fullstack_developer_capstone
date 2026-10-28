import React, { useState } from "react";
import "./Register.css";
import Header from "../Header/Header";

const Register = () => {
  const [form, setForm] = useState({
    userName: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  const handleChange = (event) => {
    setForm({
      ...form,
      [event.target.name]: event.target.value,
    });
  };

  const register = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch(
        `${window.location.origin}/djangoapp/register`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        }
      );

      const result = await response.json();

      if (response.ok && result.status === "Registered") {
        alert("Registration successful. Please log in.");
        window.location.href = "/login";
      } else {
        alert(result.message || "Registration could not be completed.");
      }
    } catch (error) {
      alert("Could not connect to the server. Please try again.");
    }
  };

  return (
    <div>
      <Header />
      <div className="register_container">
        <h1 className="header">Register</h1>
        <form onSubmit={register}>
          <div className="inputs">
            <label className="input">
              Username
              <input
                className="input_field"
                name="userName"
                value={form.userName}
                onChange={handleChange}
                required
              />
            </label>

            <label className="input">
              First name
              <input
                className="input_field"
                name="firstName"
                value={form.firstName}
                onChange={handleChange}
                required
              />
            </label>

            <label className="input">
              Last name
              <input
                className="input_field"
                name="lastName"
                value={form.lastName}
                onChange={handleChange}
                required
              />
            </label>

            <label className="input">
              Email
              <input
                className="input_field"
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                required
              />
            </label>

            <label className="input">
              Password
              <input
                className="input_field"
                type="password"
                name="password"
                value={form.password}
                onChange={handleChange}
                required
              />
            </label>
          </div>

          <div className="submit_panel">
            <button className="submit" type="submit">
              Register
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Register;