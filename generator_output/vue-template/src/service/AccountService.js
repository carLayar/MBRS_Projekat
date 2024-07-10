import api from '@/service/api';

const PATH = 'api/account'

const getById = (id) => {
    return api.get(`${PATH}/${id}`);
}

const getAll = () => {
    return api.get(`${PATH}/all`);
}

const create = (payload) => {
    return api.post(`${PATH}/create`, payload);
}

const update = (id, payload) => {
    return api.put(`${PATH}/${id}`, payload);
}

export default { getById, getAll, create, update }