// WARNING: This file was autogenerated by MBRS generator.
// Do not update it because if you run generator again you changes will be deleted

package ftn.backendservice.repositories;

import ftn.backendservice.domain.entities.Account;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Date;
import java.time.LocalDateTime;

@Repository
public interface AccountRepository extends JpaRepository<Account, Long> {
}