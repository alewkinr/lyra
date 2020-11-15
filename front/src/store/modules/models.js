// import shop from '../../api/shop'
import _ from 'lodash';    

// initial state
// shape: [{ id, quantity }]
const state = () => ({
  items: [],
})

// getters
const getters = {
  model: (state) => {
    return (id) => {
      _.find(state.items, {id: id})
    }
  }
}

// actions
const actions = {
  
}

// mutations
const mutations = {
  
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}