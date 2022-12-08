import './App.css';
import { data } from "./data";

function App() {
  return (
    <div className="App">
      <div className='container'>
        <nav className='navabar'>
          <h3>CRUD-APP</h3>
        </nav>
        <main >
          <table>
            <thead>
              <tr className='bg-dark'>
                <th>Name</th>
                <th>Email</th>
                <th>Position</th>
                <th>Edit</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              {
                data.map(({ name, email, position }) => {
                  return <tr>
                    <td>{name}</td>
                    <td>{email}</td>
                    <td>{position}</td>
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
