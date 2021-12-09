import axios from 'axios';

const host = 'http://127.0.0.1:5000';
const headers = { 
    'Access-Control-Allow-Origin': '*'
};
export default {
    get: (callback) => {
        axios.get(host+'/historicos').then((data) => {
            if (callback){
                callback(data.data);
            }
        })
    },
    send:(payload) =>{
        return new Promise((resolve)=>{
            console.log(payload)
            axios.post(host+'/pacientes', payload, {headers}).then(({data}) => resolve(data.data))
        });
    }
}