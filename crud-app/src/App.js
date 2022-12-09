import './App.css';
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import { data } from "./data";
import axios from 'axios'
import { useEffect, useState } from 'react';

function App() {

  const [employees, setEmployees] = useState([])

  useEffect(() => {
    async function listData() {
      return await axios.get('https://playground-s-11-a59c6697.uw.r.appspot.com/list')
    }
    setEmployees(listData().data)
  }, [])

  return (
    <div className="App">
      <div className='container'>
        <nav className='navabar'>
          <h3>Employee Details</h3>
        </nav>
        <main >
          <div className="mid-content">
            <button className='pntr'><AddIcon className='icon' /> New</button>
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
                employees.map(({ name, email, position }, index) => {
                  return <tr>
                    <td>{index + 1}</td>
                    <td>{name}</td>
                    <td>{email}</td>
                    <td>{position}</td>
                    <td>
                      <div className='action-container'>
                        <button className='c-green pntr'><EditIcon /> Edit</button>
                        <button className='c-red pntr'><DeleteIcon /> Delete</button>
                      </div>
                    </td>
                  </tr>
                })
              }
            </tbody>
          </table>
        </main>
      </div>
    </div>
  );
}

export default App;
