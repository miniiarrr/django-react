import { Container } from 'react-bootstrap'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen';


function App() {
  return (
    <BrowserRouter>
    <Header />
    <main className="py-3">
      <Container> 
        <Routes>
          <Route path='/' Component={HomeScreen} exact />
          <Route path='/home' Component={HomeScreen} />
          <Route path='/product/:id' Component={ProductScreen} />
        </Routes>
      </Container>
    </main>
    <Footer />
    </BrowserRouter>
  );
}

export default App;
