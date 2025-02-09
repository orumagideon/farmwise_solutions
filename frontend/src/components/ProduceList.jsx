// src/components/ProduceList.jsx
import React, { useEffect, useState } from "react";
import { getProduce } from "../api";
import "./ProduceList.css";

const ProduceList = () => {
  const [produce, setProduce] = useState([]);

  useEffect(() => {
    const fetchProduce = async () => {
      const data = await getProduce();
      setProduce(data);
    };
    fetchProduce();
  }, []);

  return (
    <div className="produce-list">
      <h2>Produce List</h2>
      <ul>
        {produce.map((item) => (
          <li key={item.id} className="produce-item">
            <h3>{item.product_name}</h3>
            <p>{item.description}</p>
            <p>Price: ${item.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProduceList;