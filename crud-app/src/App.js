import './App.css';
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios'
import { useCallback, useEffect, useState } from 'react';
import { Forms } from './form';
import { API_URL } from './appConfig';

function App() {

  const [employees, setEmployees] = useState([])
  const [showForm, setShowForm] = useState(false)
  const [editData, setEditData] = useState({})
  const [editFlag, setEditFlag] = useState(false)


  const handleDelete = async (email) => {
    await axios.delete(`${API_URL}/delete/${email}`).then((res) => {
      console.log(res);
      window.location.reload()
    }).catch((err) => {
      console.log(err);
    })
  }

  const handleEdit = (email, name, position) => {
    setEditData({
      email,
      name,
      position
    })
    setEditFlag(true)
    setShowForm(true)
  }


  useEffect(() => {
    async function listData() {
      return await axios.get(`${API_URL}/list`)
    }
    employees.length === 0 && listData().then(res => {
      let dataVal = res.data.data
      setEmployees(dataVal)
    }).catch(err => {
      console.log(err);
    })
  }, [employees])



  return (
    <div className="App">
      <div className='container'>
        {
          showForm && <>
            <Forms setShowForm={setShowForm} showForm={showForm} editData={editData} editFlag={editFlag} setEditFlag={setEditFlag} setEmployees={setEmployees} />
          </>
        }
        {!showForm && <>
          <nav className='navabar'>
            <h3>Employee Details</h3>
          </nav>
          <main >
            <div className="mid-content">
              <button className='pntr' onClick={() => setShowForm(true)}><AddIcon className='icon' /> New</button>
            </div>
            <table>
              <thead>
                <tr className='bg-dark'>
                  <th>SlNo</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Position</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                {
                  employees ? employees.map(({ name, email, position }, index) => {
                    return <tr key={email}>
                      <td>{index + 1}</td>
                      <td>{name}</td>
                      <td>{email}</td>
                      <td>{position}</td>
                      <td>
                        <div className='action-container'>
                          <button className='c-green pntr' onClick={() => handleEdit(email, name, position)}><EditIcon /> Edit</button>
                          <button className='c-red pntr' onClick={() => handleDelete(email)}><DeleteIcon /> Delete</button>
                        </div>
                      </td>
                    </tr>
                  }) : <tr>
                    <td colSpan={5}>
                      <div className='error-data'>
                        <h5>Oops!.. No data available</h5>
                      </div>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </main>
        </>
        }
      </div>
    </div>
  );
}

export default App;
