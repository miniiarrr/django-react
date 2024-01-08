import React from 'react';
import { Link } from 'react-router-dom';
import {
  Row,
  Col,
  Image,
  ListGroup,
  Button,
  Card,
} from 'react-bootstrap';
import { useParams } from 'react-router';
import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import axios from 'axios';
import { productDetails } from '../actions/productActions';

import Rating from '../components/Rating';
import Loader from '../components/Loader';
import Message from '../components/Message';

function ProductScreen({ match }) {
  const params = useParams();
  const dispatch = useDispatch();
  const productDetailsData = useSelector(
    (state) => state.productDetails
  );
  const { error, loading, product_details } = productDetailsData;

  useEffect(() => {
    dispatch(productDetails(params.id));
  }, [params.id, dispatch]);

  return (
    <div>
      <Link to="/" className="btn btn-light my-3">
        Go Back
      </Link>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            <Col sm={8} md={8} lg={9}>
              <Image
                src={product_details.image}
                alt={product_details.name}
                fluid
              />
            </Col>
            <Col sm={4} md={4} lg={3} xl={2}>
              <Card>
                <ListGroup variant="flush">
                  <ListGroup.Item>
                    <Row>
                      <Col>Price:</Col>
                      <Col>
                        <strong>${product_details.price}</strong>
                      </Col>
                    </Row>
                  </ListGroup.Item>

                  <ListGroup.Item>
                    <Row>
                      <Col>Status:</Col>
                      <Col>
                        {product_details.countInStock >= 1
                          ? 'In Stock'
                          : 'Out of stock'}
                      </Col>
                    </Row>
                  </ListGroup.Item>

                  <ListGroup.Item>
                    <Button
                      className="btn-block"
                      disabled={product_details.countInStock === 0}
                      type="button"
                    >
                      Add to cart
                    </Button>
                  </ListGroup.Item>
                </ListGroup>
              </Card>
            </Col>
          </Row>
          <Row>
            <Col sm={12} md={12}>
              <ListGroup variant="flush">
                <ListGroup.Item>
                  <h3>{product_details.name}</h3>
                </ListGroup.Item>
                <ListGroup.Item>
                  <Rating
                    value={product_details.rating}
                    text={`${product_details.numReviews} reviews`}
                    color={'#f8e825'}
                  />
                </ListGroup.Item>
                <ListGroup.Item>
                  Price: {product_details.price}
                </ListGroup.Item>
                <ListGroup.Item>
                  Description: {product_details.description}
                </ListGroup.Item>
              </ListGroup>
            </Col>
          </Row>
        </div>
      )}
    </div>
  );
}

export default ProductScreen;
