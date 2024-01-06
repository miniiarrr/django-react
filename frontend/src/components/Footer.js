import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

function Footer() {
  return (
    <footer className='text-center py-3'>
        <Container>
            <Row>
                <Col>Copyright &copy; Miniiar</Col>
            </Row>
        </Container>
    </footer>
  )
}

export default Footer