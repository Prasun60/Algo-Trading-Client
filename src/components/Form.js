import React from "react";
import * as XLSX from "xlsx";
import "./Form.css";
import axios from "axios";

const Form = () => {
  const handleSubmit = (event) => {
    event.preventDefault();
    const formEle = document.querySelector("form");
    const formDatab = new FormData(formEle);
    const tradingsymbol = formDatab.get("indexName")+formDatab.get("expiry")+formDatab.get("strike")+formDatab.get("optionType");
    console.log(tradingsymbol);
    formDatab.append("Trading Symbol",tradingsymbol);
    
    axios.post('https://sheet.best/api/sheets/9581743f-f5a7-48cb-85a1-595252fdd053',formDatab).then(response=>{
     formEle.reset();
    })
  };

  return (
    <div className="container">
      <form className="form" onSubmit={handleSubmit}>
        <label htmlFor="indexName">Index Name:</label>
        <select id="indexName" name="indexName">
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
        </select>

        <label htmlFor="expiry">Expiry:</label>
        <input type="text" id="expiry" name="expiry" />

        <label htmlFor="strike">Strike:</label>
        <input type="text" id="strike" name="strike" />

        <label htmlFor="optionType">Option Type:</label>
        <select id="optionType" name="optionType">
          <option value="C">C</option>
          <option value="P">P</option>
        </select>

        <label htmlFor="quantity">Quantity:</label>
        <input type="text" id="quantity" name="quantity" />

        <label htmlFor="transactionType">Transaction Type:</label>
        <select id="transactionType" name="transactionType">
          <option value="BUY">BUY</option>
          <option value="SELL">SELL</option>
        </select>

        <label htmlFor="slicingQuantity">Slicing Quantity:</label>
        <input type="text" id="slicingQuantity" name="slicingQuantity" />

        <label htmlFor="orderType">Order Type:</label>
        <select id="orderType" name="orderType">
          <option value="Market">Market</option>
          <option value="Limit">Limit</option>
        </select>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Form;
