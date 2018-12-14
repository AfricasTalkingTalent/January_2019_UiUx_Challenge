<?php defined('BASEPATH') or exit('No direct script access allowed');

class Main_model extends CI_Model{
    /***
     * Add to table
     */
    function add($data){
        return $this->db->insert('users',$data['user']) && $this->db->insert('auth',$data['auth']);
    }

    /**
     * Edit table
     */
    function update($data,$key){
        $this->db->where('id',$key);
        return $this->db->update('users',$data);
    }

    /**
     * Delete entry
     */
    function delete($key){
        $this->db->where('id',$key);
        return $this->db->delete('users');
    }

    /**
     * Find auth token by phone number
     */
    function verify_token($phone_number,$auth_token){
        $this->db->where('phone_number',$phone_number);
        $this->db->where('auth_token',$auth_token);
        $this->db->where('verified',0);
        $query = $this->db->get('auth');
        if ($query->num_rows() == 1){
            $this->db->where('phone_number',$phone_number);
            $this->db->where('auth_token',$auth_token);
            $this->db->update('auth',array('verified'=>1));
            return true;
        }else {
            return false;
        }
    }

    /**
     * Check phone number exists
     */
    function check_phone_exists($phone_number){
        $this->db->where('phone_number',$phone_number);
        $query = $this->db->get('users');
        return $query->num_rows() == 0;
    }
}