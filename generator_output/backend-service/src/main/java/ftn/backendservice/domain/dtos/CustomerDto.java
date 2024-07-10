// WARNING: This file was autogenerated by MBRS generator.
// Do not update it because if you run generator again you changes will be deleted

package ftn.backendservice.domain.dtos;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
import java.util.List;


@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class CustomerDto {

    private Long id;
    private String name;
    private String surname;
    private String email;
    
    private List<Long> accountIds;
    private Long bankBranchId;
    
}