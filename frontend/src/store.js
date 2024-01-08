import {
  configureStore,
  combineReducers,
  applyMiddleware,
} from '@reduxjs/toolkit';
import { thunk } from 'redux-thunk';
import { composeWithDevTools } from '@redux-devtools/extension';
import productListReducer from './reducers/productReducers';

const reducer = combineReducers({ productListReducer });

const store = configureStore({ reducer });

export default store;
