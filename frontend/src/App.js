import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import PostList from './components/PostList';
import PostDetail from './components/PostDetail';

function App() {
  return (
    <Router>
      <div className="App">
        {/* Aquí podrías tener un Navbar o Layout común */}
        <Routes>
          <Route path="/" element={<PostList />} /> {/* O tu página de inicio */}
          <Route path="/blog" element={<PostList />} />
          <Route path="/blog/:slug" element={<PostDetail />} />
          {/* Otras rutas */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
