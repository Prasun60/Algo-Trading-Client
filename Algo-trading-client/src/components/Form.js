import React from "react";
import * as XLSX from "xlsx";
import writeXlsxFile from "write-excel-file";
import "./Form.css";
import axios from "axios";
const Form = () => {
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formEle = document.querySelector("form");
    const formDatab = new FormData(formEle);
    const tradingsymbol1 =
      formDatab.get("indexName1") +
      formDatab.get("expiry1") +
      formDatab.get("strike1") +
      formDatab.get("optionType1");
    console.log(tradingsymbol1);
    formDatab.append("Trading Symbol1", tradingsymbol1);
    console.log(formDatab.values())

    const tradingsymbol2 =
      formDatab.get("indexName2") +
      formDatab.get("expiry2") +
      formDatab.get("strike2") +
      formDatab.get("optionType2");
    console.log(tradingsymbol2);
    formDatab.append("Trading Symbol2", tradingsymbol2);
    console.log(formDatab.values())

    
    await axios.delete("https://sheet.best/api/sheets/9581743f-f5a7-48cb-85a1-595252fdd053/0")




    await axios.post('https://sheet.best/api/sheets/9581743f-f5a7-48cb-85a1-595252fdd053',formDatab).then(response=>{
     formEle.reset();
    })
   

    await axios.get("http://localhost:3001/").then((response)=>{
      console.log(response.msg)
    })


    
  };

  return (
    <div className="container">
      <form className="form" onSubmit={handleSubmit}>
        <label htmlFor="indexName1">Index Name for order 1:</label>
        <select id="indexName1" name="indexName1">
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
        </select>

        <label htmlFor="indexName2">Index Name for order 2:</label>
        <select id="indexName2" name="indexName2">
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
          <option value="FINNIFTY">FINNIFTY</option>
        </select>

        <label htmlFor="expiry1">Expiry for order 1:</label>
        <input type="text" id="expiry1" name="expiry1" />

        <label htmlFor="strike1">Strike for order 1:</label>
        <input type="text" id="strike1" name="strike1" />

        <label htmlFor="optionType1">Option Type for order 1:</label>
        <select id="optionType1" name="optionType1">
          <option value="C">C</option>
          <option value="P">P</option>
        </select>

        <label htmlFor="expiry2">Expiry for order 2:</label>
        <input type="text" id="expiry2" name="expiry2" />

        <label htmlFor="strike2">Strike for order 2:</label>
        <input type="text" id="strike2" name="strike2" />

        <label htmlFor="optionType2">Option Type for order 2:</label>
        <select id="optionType2" name="optionType2">
          <option value="C">C</option>
          <option value="P">P</option>
        </select>

        <label htmlFor="quantity">Quantity:</label>
        <input type="text" id="quantity" name="quantity" />

        <label htmlFor="transactionType1">Transaction Type for order 1:</label>
        <select id="transactionType1" name="transactionType1">
          <option value="BUY">BUY</option>
          <option value="SELL">SELL</option>
        </select>

        <label htmlFor="transactionType2">Transaction Type for order 2:</label>
        <select id="transactionType2" name="transactionType2">
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
