import { useEffect, useState } from "react"
import axios from "axios";
import { API_URL } from "./appConfig";

export const Forms = (props) => {

    const { setShowForm, showForm, editFlag, editData, setEditFlag, setEmployees } = props;

    const [employeeData, setEmployeeData] = useState({
        email: "",
        name: "",
        position: ""
    })

    useEffect(() => {
        editFlag && setEmployeeData(editData)
    }, [editFlag])

    const handleChange = (e) => {
        const { name, value } = e.target
        setEmployeeData(prev => ({
            ...prev,
            [name]: value
        }))
    }

    const handleClose = () => {
        setShowForm(false)
    }

    const handleSubmit = async () => {
        console.log(showForm);
        if (showForm) {
            if (Object.values(employeeData).includes("")) {
                alert("Fill all the fields")
            } else {
                if (editFlag) {
                    await axios.put(`${API_URL}/update`, employeeData).then(res => {
                        console.log(res);
                    }).catch(err => {
                        console.log(err);
                    })
                } else {
                    await axios.post(`${API_URL}/create`, employeeData).then((res) => {
                        console.log(res);
                    }).catch((err) => {
                        console.log(err);
                    })
                }
                setEditFlag(false)
                setShowForm(false)
                setEmployees([])
            }

        }
    }

    return (
        <div className="form">
            <h3>Add Employee</h3>
            <form onSubmit={handleSubmit}>
                <div className="input-container">
                    <input placeholder="Email*" id='email' name="email" type={'email'} value={employeeData.email} onChange={(e) => handleChange(e)} />
                </div>
                <div className="input-container">
                    <input placeholder='Name*' name="name" id='name' type={'text'} value={employeeData.name} onChange={(e) => handleChange(e)} />
                </div>
                <div className="input-container">
                    <input name="position" placeholder="position*" id='name' type={'text'} value={employeeData.position} onChange={(e) => handleChange(e)} />
                </div>
                <div className="btn-container ">
                    <button className="c-green" type="submit">Create</button>
                    <button className="c-red" onClick={handleClose}>Cancel</button>
                </div>
            </form>
        </div>
    )
}