// src/pages/Equipment.jsx
import React, { useEffect, useState } from "react";
import { getEquipment } from "../api"; // Corrected the function import
import "./Equipment.css";

const Equipment = () => {
  const [equipmentList, setEquipmentList] = useState([]);

  useEffect(() => {
    const fetchEquipment = async () => {
      try {
        const data = await getEquipment();
        setEquipmentList(data);
      } catch (error) {
        console.error("Error fetching equipment:", error);
      }
    };

    fetchEquipment();
  }, []);

  return (
    <div className="equipment-page">
      <h1>Available Equipment for Lease</h1>
      <ul className="equipment-list">
        {equipmentList.length > 0 ? (
          equipmentList.map((equipment) => (
            <li key={equipment.id} className="equipment-item">
              <h3>{equipment.name}</h3>
              <p>{equipment.description}</p>
              <p>Price: ${equipment.price}</p>
            </li>
          ))
        ) : (
          <p>No equipment available at the moment.</p>
        )}
      </ul>
    </div>
  );
};

export default Equipment;
