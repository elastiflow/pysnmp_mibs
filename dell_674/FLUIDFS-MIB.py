# SNMP MIB module (FLUIDFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/FLUIDFS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:34:50 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fluidFSMIBIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 100)
)
if mibBuilder.loadTexts:
    fluidFSMIBIdentity.setRevisions(
        ("2013-03-01 10:02",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DomainStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notjoined", 0),
          ("unknown", 1),
          ("offline", 2),
          ("problematic", 3),
          ("optimal", 4))
    )



class DomainInfoStatusTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("notrunning", 1))
    )



class ExternalServerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1),
          ("unknown", 2))
    )



class WriteThroughModeTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirroring", 0),
          ("journaling", 1),
          ("intransition", 2))
    )



class ServiceabilityState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("writethroughmode", 1),
          ("noservice", 2))
    )



class ComponentStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("optimal", 0),
          ("notoptimal", 1),
          ("critical", 2),
          ("notavailable", 3),
          ("irrelevant", 4))
    )



class MemberModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("fs8600", 0),
          ("fs8610", 1),
          ("fs8611", 2),
          ("fs8610i", 3),
          ("fs8611i", 4),
          ("fs8700", 5),
          ("kv8710", 6),
          ("vm0002", 7),
          ("vm1000", 8),
          ("vm2000", 9),
          ("un1000", 10),
          ("notavailable", 11))
    )



class AvPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 0),
          ("quarantine", 1),
          ("remove", 2))
    )



class Boolean(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )



class SecurityStyle(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 0),
          ("unix", 1),
          ("ntfs", 2))
    )



class ExternalServerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 0),
          ("staticroute", 1),
          ("dns", 2),
          ("antivirus", 3),
          ("nis", 4),
          ("ldap", 5),
          ("ntp", 6),
          ("iscsiportal", 7),
          ("vm", 8),
          ("auditingserver", 9))
    )



class AccessState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 0),
          ("notoptimal", 1),
          ("optimal", 2))
    )



class TrustedSystemStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )



class IncludeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("include", 0),
          ("exclude", 1))
    )



class Locking(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alllocks", 0),
          ("nobyterangelocks", 1),
          ("onlysharelocks", 2))
    )



class VolumeReplicationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 0),
          ("source", 1),
          ("destination", 2),
          ("sourceanddestination", 3),
          ("promoted", 4),
          ("notavailable", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_EnterpriseSoftware_ObjectIdentity = ObjectIdentity
enterpriseSoftware = _EnterpriseSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000)
)
_StorageMgmt_ObjectIdentity = ObjectIdentity
storageMgmt = _StorageMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000)
)
_FluidFS_ObjectIdentity = ObjectIdentity
fluidFS = _FluidFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200)
)
_FluidFSProduct_ObjectIdentity = ObjectIdentity
fluidFSProduct = _FluidFSProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1)
)
_ActiveDirectoryStatusTable_Object = MibTable
activeDirectoryStatusTable = _ActiveDirectoryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1)
)
if mibBuilder.loadTexts:
    activeDirectoryStatusTable.setStatus("current")
_ActiveDirectoryStatusEntry_Object = MibTableRow
activeDirectoryStatusEntry = _ActiveDirectoryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1)
)
activeDirectoryStatusEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "activeDirectoryStatusTenantId"),
)
if mibBuilder.loadTexts:
    activeDirectoryStatusEntry.setStatus("current")
_ActiveDirectoryStatusConfigured_Type = OctetString
_ActiveDirectoryStatusConfigured_Object = MibTableColumn
activeDirectoryStatusConfigured = _ActiveDirectoryStatusConfigured_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 1),
    _ActiveDirectoryStatusConfigured_Type()
)
activeDirectoryStatusConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusConfigured.setStatus("deprecated")
_ActiveDirectoryStatusStatus_Type = OctetString
_ActiveDirectoryStatusStatus_Object = MibTableColumn
activeDirectoryStatusStatus = _ActiveDirectoryStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 2),
    _ActiveDirectoryStatusStatus_Type()
)
activeDirectoryStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusStatus.setStatus("deprecated")
_ActiveDirectoryStatusDomain_Type = OctetString
_ActiveDirectoryStatusDomain_Object = MibTableColumn
activeDirectoryStatusDomain = _ActiveDirectoryStatusDomain_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 3),
    _ActiveDirectoryStatusDomain_Type()
)
activeDirectoryStatusDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusDomain.setStatus("current")
_ActiveDirectoryStatusConfiguredEnumType_Type = Boolean
_ActiveDirectoryStatusConfiguredEnumType_Object = MibTableColumn
activeDirectoryStatusConfiguredEnumType = _ActiveDirectoryStatusConfiguredEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 4),
    _ActiveDirectoryStatusConfiguredEnumType_Type()
)
activeDirectoryStatusConfiguredEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusConfiguredEnumType.setStatus("current")
_ActiveDirectoryStatusStatusEnumType_Type = DomainStatusType
_ActiveDirectoryStatusStatusEnumType_Object = MibTableColumn
activeDirectoryStatusStatusEnumType = _ActiveDirectoryStatusStatusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 5),
    _ActiveDirectoryStatusStatusEnumType_Type()
)
activeDirectoryStatusStatusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusStatusEnumType.setStatus("current")


class _ActiveDirectoryStatusTenantId_Type(Integer32):
    """Custom type activeDirectoryStatusTenantId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ActiveDirectoryStatusTenantId_Type.__name__ = "Integer32"
_ActiveDirectoryStatusTenantId_Object = MibTableColumn
activeDirectoryStatusTenantId = _ActiveDirectoryStatusTenantId_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 1, 1, 6),
    _ActiveDirectoryStatusTenantId_Type()
)
activeDirectoryStatusTenantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDirectoryStatusTenantId.setStatus("current")
_FluidFsCifsShareTable_Object = MibTable
fluidFsCifsShareTable = _FluidFsCifsShareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6)
)
if mibBuilder.loadTexts:
    fluidFsCifsShareTable.setStatus("current")
_FluidFsCifsShareEntry_Object = MibTableRow
fluidFsCifsShareEntry = _FluidFsCifsShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1)
)
fluidFsCifsShareEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "fluidFsCifsShareIndex"),
)
if mibBuilder.loadTexts:
    fluidFsCifsShareEntry.setStatus("current")


class _FluidFsCifsShareIndex_Type(Integer32):
    """Custom type fluidFsCifsShareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FluidFsCifsShareIndex_Type.__name__ = "Integer32"
_FluidFsCifsShareIndex_Object = MibTableColumn
fluidFsCifsShareIndex = _FluidFsCifsShareIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1, 1),
    _FluidFsCifsShareIndex_Type()
)
fluidFsCifsShareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsCifsShareIndex.setStatus("current")
_FluidFsCifsShareVolumeName_Type = OctetString
_FluidFsCifsShareVolumeName_Object = MibTableColumn
fluidFsCifsShareVolumeName = _FluidFsCifsShareVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1, 2),
    _FluidFsCifsShareVolumeName_Type()
)
fluidFsCifsShareVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsCifsShareVolumeName.setStatus("current")
_FluidFsCifsShareShareName_Type = OctetString
_FluidFsCifsShareShareName_Object = MibTableColumn
fluidFsCifsShareShareName = _FluidFsCifsShareShareName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1, 3),
    _FluidFsCifsShareShareName_Type()
)
fluidFsCifsShareShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsCifsShareShareName.setStatus("current")
_FluidFsCifsSharePath_Type = OctetString
_FluidFsCifsSharePath_Object = MibTableColumn
fluidFsCifsSharePath = _FluidFsCifsSharePath_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1, 4),
    _FluidFsCifsSharePath_Type()
)
fluidFsCifsSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsCifsSharePath.setStatus("current")
_FluidFsCifsShareAccessBasedEnumEnumType_Type = Boolean
_FluidFsCifsShareAccessBasedEnumEnumType_Object = MibTableColumn
fluidFsCifsShareAccessBasedEnumEnumType = _FluidFsCifsShareAccessBasedEnumEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 6, 1, 5),
    _FluidFsCifsShareAccessBasedEnumEnumType_Type()
)
fluidFsCifsShareAccessBasedEnumEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsCifsShareAccessBasedEnumEnumType.setStatus("current")
_ClusterName_ObjectIdentity = ObjectIdentity
clusterName = _ClusterName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 9)
)
_ClusterNameClusterName_Type = OctetString
_ClusterNameClusterName_Object = MibScalar
clusterNameClusterName = _ClusterNameClusterName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 9, 1),
    _ClusterNameClusterName_Type()
)
clusterNameClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNameClusterName.setStatus("current")
_ExternalServerStateTable_Object = MibTable
externalServerStateTable = _ExternalServerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12)
)
if mibBuilder.loadTexts:
    externalServerStateTable.setStatus("current")
_ExternalServerStateEntry_Object = MibTableRow
externalServerStateEntry = _ExternalServerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1)
)
externalServerStateEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "externalServerStateIndex"),
)
if mibBuilder.loadTexts:
    externalServerStateEntry.setStatus("current")


class _ExternalServerStateIndex_Type(Integer32):
    """Custom type externalServerStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ExternalServerStateIndex_Type.__name__ = "Integer32"
_ExternalServerStateIndex_Object = MibTableColumn
externalServerStateIndex = _ExternalServerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 1),
    _ExternalServerStateIndex_Type()
)
externalServerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateIndex.setStatus("current")
_ExternalServerStateHost_Type = OctetString
_ExternalServerStateHost_Object = MibTableColumn
externalServerStateHost = _ExternalServerStateHost_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 2),
    _ExternalServerStateHost_Type()
)
externalServerStateHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateHost.setStatus("current")
_ExternalServerStateType_Type = OctetString
_ExternalServerStateType_Object = MibTableColumn
externalServerStateType = _ExternalServerStateType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 3),
    _ExternalServerStateType_Type()
)
externalServerStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateType.setStatus("deprecated")
_ExternalServerStateState_Type = OctetString
_ExternalServerStateState_Object = MibTableColumn
externalServerStateState = _ExternalServerStateState_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 4),
    _ExternalServerStateState_Type()
)
externalServerStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateState.setStatus("deprecated")
_ExternalServerStateTypeEnumType_Type = ExternalServerType
_ExternalServerStateTypeEnumType_Object = MibTableColumn
externalServerStateTypeEnumType = _ExternalServerStateTypeEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 5),
    _ExternalServerStateTypeEnumType_Type()
)
externalServerStateTypeEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateTypeEnumType.setStatus("current")
_ExternalServerStateStateEnumType_Type = ExternalServerState
_ExternalServerStateStateEnumType_Object = MibTableColumn
externalServerStateStateEnumType = _ExternalServerStateStateEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 12, 1, 6),
    _ExternalServerStateStateEnumType_Type()
)
externalServerStateStateEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalServerStateStateEnumType.setStatus("current")
_NASApplianceTable_Object = MibTable
nASApplianceTable = _NASApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16)
)
if mibBuilder.loadTexts:
    nASApplianceTable.setStatus("current")
_NASApplianceEntry_Object = MibTableRow
nASApplianceEntry = _NASApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1)
)
nASApplianceEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "nASApplianceIndex"),
)
if mibBuilder.loadTexts:
    nASApplianceEntry.setStatus("current")


class _NASApplianceIndex_Type(Integer32):
    """Custom type nASApplianceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NASApplianceIndex_Type.__name__ = "Integer32"
_NASApplianceIndex_Object = MibTableColumn
nASApplianceIndex = _NASApplianceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 1),
    _NASApplianceIndex_Type()
)
nASApplianceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceIndex.setStatus("current")
_NASApplianceId_Type = Integer32
_NASApplianceId_Object = MibTableColumn
nASApplianceId = _NASApplianceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 2),
    _NASApplianceId_Type()
)
nASApplianceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceId.setStatus("current")
_NASApplianceApplianceServiceTag_Type = OctetString
_NASApplianceApplianceServiceTag_Object = MibTableColumn
nASApplianceApplianceServiceTag = _NASApplianceApplianceServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 3),
    _NASApplianceApplianceServiceTag_Type()
)
nASApplianceApplianceServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceApplianceServiceTag.setStatus("current")
_NASApplianceFileSystemMember_Type = OctetString
_NASApplianceFileSystemMember_Object = MibTableColumn
nASApplianceFileSystemMember = _NASApplianceFileSystemMember_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 4),
    _NASApplianceFileSystemMember_Type()
)
nASApplianceFileSystemMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceFileSystemMember.setStatus("deprecated")
_NASApplianceStatus_Type = OctetString
_NASApplianceStatus_Object = MibTableColumn
nASApplianceStatus = _NASApplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 5),
    _NASApplianceStatus_Type()
)
nASApplianceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceStatus.setStatus("deprecated")
_NASApplianceModel_Type = OctetString
_NASApplianceModel_Object = MibTableColumn
nASApplianceModel = _NASApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 6),
    _NASApplianceModel_Type()
)
nASApplianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceModel.setStatus("deprecated")
_NASApplianceFileSystemMemberEnumType_Type = Boolean
_NASApplianceFileSystemMemberEnumType_Object = MibTableColumn
nASApplianceFileSystemMemberEnumType = _NASApplianceFileSystemMemberEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 7),
    _NASApplianceFileSystemMemberEnumType_Type()
)
nASApplianceFileSystemMemberEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceFileSystemMemberEnumType.setStatus("current")
_NASApplianceStatusEnumType_Type = ComponentStatus
_NASApplianceStatusEnumType_Object = MibTableColumn
nASApplianceStatusEnumType = _NASApplianceStatusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 8),
    _NASApplianceStatusEnumType_Type()
)
nASApplianceStatusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceStatusEnumType.setStatus("current")
_NASApplianceModelEnumType_Type = MemberModel
_NASApplianceModelEnumType_Object = MibTableColumn
nASApplianceModelEnumType = _NASApplianceModelEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 9),
    _NASApplianceModelEnumType_Type()
)
nASApplianceModelEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceModelEnumType.setStatus("current")
_NASApplianceApplianceID_Type = Integer32
_NASApplianceApplianceID_Object = MibTableColumn
nASApplianceApplianceID = _NASApplianceApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 10),
    _NASApplianceApplianceID_Type()
)
nASApplianceApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceApplianceID.setStatus("current")
_NASApplianceWriteThroughModeEnumType_Type = WriteThroughModeTypes
_NASApplianceWriteThroughModeEnumType_Object = MibTableColumn
nASApplianceWriteThroughModeEnumType = _NASApplianceWriteThroughModeEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 11),
    _NASApplianceWriteThroughModeEnumType_Type()
)
nASApplianceWriteThroughModeEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceWriteThroughModeEnumType.setStatus("current")
_NASApplianceWriteCachUsage_Type = Integer32
_NASApplianceWriteCachUsage_Object = MibTableColumn
nASApplianceWriteCachUsage = _NASApplianceWriteCachUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 12),
    _NASApplianceWriteCachUsage_Type()
)
nASApplianceWriteCachUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceWriteCachUsage.setStatus("current")
_NASApplianceDomainStatusEnumType_Type = DomainInfoStatusTypes
_NASApplianceDomainStatusEnumType_Object = MibTableColumn
nASApplianceDomainStatusEnumType = _NASApplianceDomainStatusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 16, 1, 13),
    _NASApplianceDomainStatusEnumType_Type()
)
nASApplianceDomainStatusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASApplianceDomainStatusEnumType.setStatus("current")
_StorageSubsystemTable_Object = MibTable
storageSubsystemTable = _StorageSubsystemTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 32)
)
if mibBuilder.loadTexts:
    storageSubsystemTable.setStatus("current")
_StorageSubsystemEntry_Object = MibTableRow
storageSubsystemEntry = _StorageSubsystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 32, 1)
)
storageSubsystemEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "storageSubsystemIndex"),
)
if mibBuilder.loadTexts:
    storageSubsystemEntry.setStatus("current")


class _StorageSubsystemIndex_Type(Integer32):
    """Custom type storageSubsystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StorageSubsystemIndex_Type.__name__ = "Integer32"
_StorageSubsystemIndex_Object = MibTableColumn
storageSubsystemIndex = _StorageSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 32, 1, 1),
    _StorageSubsystemIndex_Type()
)
storageSubsystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageSubsystemIndex.setStatus("current")
_StorageSubsystemLunsAccessibility_Type = OctetString
_StorageSubsystemLunsAccessibility_Object = MibTableColumn
storageSubsystemLunsAccessibility = _StorageSubsystemLunsAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 32, 1, 2),
    _StorageSubsystemLunsAccessibility_Type()
)
storageSubsystemLunsAccessibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageSubsystemLunsAccessibility.setStatus("deprecated")
_StorageSubsystemLunsAccessibilityEnumType_Type = AccessState
_StorageSubsystemLunsAccessibilityEnumType_Object = MibTableColumn
storageSubsystemLunsAccessibilityEnumType = _StorageSubsystemLunsAccessibilityEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 32, 1, 3),
    _StorageSubsystemLunsAccessibilityEnumType_Type()
)
storageSubsystemLunsAccessibilityEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageSubsystemLunsAccessibilityEnumType.setStatus("current")
_SystemServiceMode_ObjectIdentity = ObjectIdentity
systemServiceMode = _SystemServiceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 36)
)
_SystemServiceModeState_Type = OctetString
_SystemServiceModeState_Object = MibScalar
systemServiceModeState = _SystemServiceModeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 36, 1),
    _SystemServiceModeState_Type()
)
systemServiceModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServiceModeState.setStatus("deprecated")
_SystemServiceModeStateEnumType_Type = ServiceabilityState
_SystemServiceModeStateEnumType_Object = MibScalar
systemServiceModeStateEnumType = _SystemServiceModeStateEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 36, 2),
    _SystemServiceModeStateEnumType_Type()
)
systemServiceModeStateEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServiceModeStateEnumType.setStatus("current")
_SystemTrafficStatisticsTable_Object = MibTable
systemTrafficStatisticsTable = _SystemTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37)
)
if mibBuilder.loadTexts:
    systemTrafficStatisticsTable.setStatus("current")
_SystemTrafficStatisticsEntry_Object = MibTableRow
systemTrafficStatisticsEntry = _SystemTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1)
)
systemTrafficStatisticsEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "systemTrafficStatisticsIndex"),
)
if mibBuilder.loadTexts:
    systemTrafficStatisticsEntry.setStatus("current")


class _SystemTrafficStatisticsIndex_Type(Integer32):
    """Custom type systemTrafficStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SystemTrafficStatisticsIndex_Type.__name__ = "Integer32"
_SystemTrafficStatisticsIndex_Object = MibTableColumn
systemTrafficStatisticsIndex = _SystemTrafficStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 1),
    _SystemTrafficStatisticsIndex_Type()
)
systemTrafficStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsIndex.setStatus("current")
_SystemTrafficStatisticsTimestamp_Type = OctetString
_SystemTrafficStatisticsTimestamp_Object = MibTableColumn
systemTrafficStatisticsTimestamp = _SystemTrafficStatisticsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 2),
    _SystemTrafficStatisticsTimestamp_Type()
)
systemTrafficStatisticsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsTimestamp.setStatus("current")
_SystemTrafficStatisticsNFSReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNFSReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNFSReadMBsPerSec = _SystemTrafficStatisticsNFSReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 3),
    _SystemTrafficStatisticsNFSReadMBsPerSec_Type()
)
systemTrafficStatisticsNFSReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNFSReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNFSWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNFSWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNFSWriteMBsPerSec = _SystemTrafficStatisticsNFSWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 4),
    _SystemTrafficStatisticsNFSWriteMBsPerSec_Type()
)
systemTrafficStatisticsNFSWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNFSWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNDMPReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNDMPReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNDMPReadMBsPerSec = _SystemTrafficStatisticsNDMPReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 5),
    _SystemTrafficStatisticsNDMPReadMBsPerSec_Type()
)
systemTrafficStatisticsNDMPReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNDMPReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNDMPWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNDMPWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNDMPWriteMBsPerSec = _SystemTrafficStatisticsNDMPWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 6),
    _SystemTrafficStatisticsNDMPWriteMBsPerSec_Type()
)
systemTrafficStatisticsNDMPWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNDMPWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsCIFSReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsCIFSReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsCIFSReadMBsPerSec = _SystemTrafficStatisticsCIFSReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 7),
    _SystemTrafficStatisticsCIFSReadMBsPerSec_Type()
)
systemTrafficStatisticsCIFSReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsCIFSReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsCIFSWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsCIFSWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsCIFSWriteMBsPerSec = _SystemTrafficStatisticsCIFSWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 8),
    _SystemTrafficStatisticsCIFSWriteMBsPerSec_Type()
)
systemTrafficStatisticsCIFSWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsCIFSWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsReplicationReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsReplicationReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsReplicationReadMBsPerSec = _SystemTrafficStatisticsReplicationReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 9),
    _SystemTrafficStatisticsReplicationReadMBsPerSec_Type()
)
systemTrafficStatisticsReplicationReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsReplicationReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsReplicationWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsReplicationWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsReplicationWriteMBsPerSec = _SystemTrafficStatisticsReplicationWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 10),
    _SystemTrafficStatisticsReplicationWriteMBsPerSec_Type()
)
systemTrafficStatisticsReplicationWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsReplicationWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNetworkOverheadReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNetworkOverheadReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNetworkOverheadReadMBsPerSec = _SystemTrafficStatisticsNetworkOverheadReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 11),
    _SystemTrafficStatisticsNetworkOverheadReadMBsPerSec_Type()
)
systemTrafficStatisticsNetworkOverheadReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNetworkOverheadReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNetworkOverheadWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsNetworkOverheadWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsNetworkOverheadWriteMBsPerSec = _SystemTrafficStatisticsNetworkOverheadWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 12),
    _SystemTrafficStatisticsNetworkOverheadWriteMBsPerSec_Type()
)
systemTrafficStatisticsNetworkOverheadWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNetworkOverheadWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsStorageSubSystemReadMBsPerSec_Type = Integer32
_SystemTrafficStatisticsStorageSubSystemReadMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsStorageSubSystemReadMBsPerSec = _SystemTrafficStatisticsStorageSubSystemReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 13),
    _SystemTrafficStatisticsStorageSubSystemReadMBsPerSec_Type()
)
systemTrafficStatisticsStorageSubSystemReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsStorageSubSystemReadMBsPerSec.setStatus("current")
_SystemTrafficStatisticsStorageSubSystemWriteMBsPerSec_Type = Integer32
_SystemTrafficStatisticsStorageSubSystemWriteMBsPerSec_Object = MibTableColumn
systemTrafficStatisticsStorageSubSystemWriteMBsPerSec = _SystemTrafficStatisticsStorageSubSystemWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 14),
    _SystemTrafficStatisticsStorageSubSystemWriteMBsPerSec_Type()
)
systemTrafficStatisticsStorageSubSystemWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsStorageSubSystemWriteMBsPerSec.setStatus("current")
_SystemTrafficStatisticsNFSIOPSRead_Type = Integer32
_SystemTrafficStatisticsNFSIOPSRead_Object = MibTableColumn
systemTrafficStatisticsNFSIOPSRead = _SystemTrafficStatisticsNFSIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 15),
    _SystemTrafficStatisticsNFSIOPSRead_Type()
)
systemTrafficStatisticsNFSIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNFSIOPSRead.setStatus("current")
_SystemTrafficStatisticsNFSIOPSWrite_Type = Integer32
_SystemTrafficStatisticsNFSIOPSWrite_Object = MibTableColumn
systemTrafficStatisticsNFSIOPSWrite = _SystemTrafficStatisticsNFSIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 16),
    _SystemTrafficStatisticsNFSIOPSWrite_Type()
)
systemTrafficStatisticsNFSIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNFSIOPSWrite.setStatus("current")
_SystemTrafficStatisticsNFSIOPSOther_Type = Integer32
_SystemTrafficStatisticsNFSIOPSOther_Object = MibTableColumn
systemTrafficStatisticsNFSIOPSOther = _SystemTrafficStatisticsNFSIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 17),
    _SystemTrafficStatisticsNFSIOPSOther_Type()
)
systemTrafficStatisticsNFSIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsNFSIOPSOther.setStatus("current")
_SystemTrafficStatisticsCIFSIOPSRead_Type = Integer32
_SystemTrafficStatisticsCIFSIOPSRead_Object = MibTableColumn
systemTrafficStatisticsCIFSIOPSRead = _SystemTrafficStatisticsCIFSIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 18),
    _SystemTrafficStatisticsCIFSIOPSRead_Type()
)
systemTrafficStatisticsCIFSIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsCIFSIOPSRead.setStatus("current")
_SystemTrafficStatisticsCIFSIOPSWrite_Type = Integer32
_SystemTrafficStatisticsCIFSIOPSWrite_Object = MibTableColumn
systemTrafficStatisticsCIFSIOPSWrite = _SystemTrafficStatisticsCIFSIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 19),
    _SystemTrafficStatisticsCIFSIOPSWrite_Type()
)
systemTrafficStatisticsCIFSIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsCIFSIOPSWrite.setStatus("current")
_SystemTrafficStatisticsCIFSIOPSOther_Type = Integer32
_SystemTrafficStatisticsCIFSIOPSOther_Object = MibTableColumn
systemTrafficStatisticsCIFSIOPSOther = _SystemTrafficStatisticsCIFSIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 37, 1, 20),
    _SystemTrafficStatisticsCIFSIOPSOther_Type()
)
systemTrafficStatisticsCIFSIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTrafficStatisticsCIFSIOPSOther.setStatus("current")
_NASPool_ObjectIdentity = ObjectIdentity
nASPool = _NASPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38)
)
_NASPoolTotalCapacityMB_Type = OctetString
_NASPoolTotalCapacityMB_Object = MibScalar
nASPoolTotalCapacityMB = _NASPoolTotalCapacityMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 1),
    _NASPoolTotalCapacityMB_Type()
)
nASPoolTotalCapacityMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalCapacityMB.setStatus("current")
_NASPoolTotalReservedMB_Type = OctetString
_NASPoolTotalReservedMB_Object = MibScalar
nASPoolTotalReservedMB = _NASPoolTotalReservedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 2),
    _NASPoolTotalReservedMB_Type()
)
nASPoolTotalReservedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalReservedMB.setStatus("current")
_NASPoolTotalUsedMB_Type = OctetString
_NASPoolTotalUsedMB_Object = MibScalar
nASPoolTotalUsedMB = _NASPoolTotalUsedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 3),
    _NASPoolTotalUsedMB_Type()
)
nASPoolTotalUsedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalUsedMB.setStatus("current")
_NASPoolTotalUnusedMB_Type = OctetString
_NASPoolTotalUnusedMB_Object = MibScalar
nASPoolTotalUnusedMB = _NASPoolTotalUnusedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 4),
    _NASPoolTotalUnusedMB_Type()
)
nASPoolTotalUnusedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalUnusedMB.setStatus("current")
_NASPoolTotalUnusedReservedMB_Type = OctetString
_NASPoolTotalUnusedReservedMB_Object = MibScalar
nASPoolTotalUnusedReservedMB = _NASPoolTotalUnusedReservedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 5),
    _NASPoolTotalUnusedReservedMB_Type()
)
nASPoolTotalUnusedReservedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalUnusedReservedMB.setStatus("current")
_NASPoolTotalUnusedUnreservedMB_Type = OctetString
_NASPoolTotalUnusedUnreservedMB_Object = MibScalar
nASPoolTotalUnusedUnreservedMB = _NASPoolTotalUnusedUnreservedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 6),
    _NASPoolTotalUnusedUnreservedMB_Type()
)
nASPoolTotalUnusedUnreservedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalUnusedUnreservedMB.setStatus("current")
_NASPoolTotalOverCommittedMB_Type = OctetString
_NASPoolTotalOverCommittedMB_Object = MibScalar
nASPoolTotalOverCommittedMB = _NASPoolTotalOverCommittedMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 7),
    _NASPoolTotalOverCommittedMB_Type()
)
nASPoolTotalOverCommittedMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalOverCommittedMB.setStatus("current")
_NASPoolTotalOptimizationSavedSpaceMB_Type = OctetString
_NASPoolTotalOptimizationSavedSpaceMB_Object = MibScalar
nASPoolTotalOptimizationSavedSpaceMB = _NASPoolTotalOptimizationSavedSpaceMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 8),
    _NASPoolTotalOptimizationSavedSpaceMB_Type()
)
nASPoolTotalOptimizationSavedSpaceMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolTotalOptimizationSavedSpaceMB.setStatus("current")
_NASPoolNumberOfVirtualVolumes_Type = Integer32
_NASPoolNumberOfVirtualVolumes_Object = MibScalar
nASPoolNumberOfVirtualVolumes = _NASPoolNumberOfVirtualVolumes_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 9),
    _NASPoolNumberOfVirtualVolumes_Type()
)
nASPoolNumberOfVirtualVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfVirtualVolumes.setStatus("current")
_NASPoolNumberOfVirtualVolumesWithSnapshots_Type = Integer32
_NASPoolNumberOfVirtualVolumesWithSnapshots_Object = MibScalar
nASPoolNumberOfVirtualVolumesWithSnapshots = _NASPoolNumberOfVirtualVolumesWithSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 10),
    _NASPoolNumberOfVirtualVolumesWithSnapshots_Type()
)
nASPoolNumberOfVirtualVolumesWithSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfVirtualVolumesWithSnapshots.setStatus("current")
_NASPoolNumberOfVirtualVolumesWithReplication_Type = Integer32
_NASPoolNumberOfVirtualVolumesWithReplication_Object = MibScalar
nASPoolNumberOfVirtualVolumesWithReplication = _NASPoolNumberOfVirtualVolumesWithReplication_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 11),
    _NASPoolNumberOfVirtualVolumesWithReplication_Type()
)
nASPoolNumberOfVirtualVolumesWithReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfVirtualVolumesWithReplication.setStatus("current")
_NASPoolNumberOfVirtualVolumesWithDataReduction_Type = Integer32
_NASPoolNumberOfVirtualVolumesWithDataReduction_Object = MibScalar
nASPoolNumberOfVirtualVolumesWithDataReduction = _NASPoolNumberOfVirtualVolumesWithDataReduction_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 12),
    _NASPoolNumberOfVirtualVolumesWithDataReduction_Type()
)
nASPoolNumberOfVirtualVolumesWithDataReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfVirtualVolumesWithDataReduction.setStatus("current")
_NASPoolNumberOfNfsExports_Type = Integer32
_NASPoolNumberOfNfsExports_Object = MibScalar
nASPoolNumberOfNfsExports = _NASPoolNumberOfNfsExports_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 13),
    _NASPoolNumberOfNfsExports_Type()
)
nASPoolNumberOfNfsExports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfNfsExports.setStatus("current")
_NASPoolNumberOfCifsShares_Type = Integer32
_NASPoolNumberOfCifsShares_Object = MibScalar
nASPoolNumberOfCifsShares = _NASPoolNumberOfCifsShares_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 14),
    _NASPoolNumberOfCifsShares_Type()
)
nASPoolNumberOfCifsShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfCifsShares.setStatus("current")
_NASPoolNumberOfSnapshots_Type = Integer32
_NASPoolNumberOfSnapshots_Object = MibScalar
nASPoolNumberOfSnapshots = _NASPoolNumberOfSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 15),
    _NASPoolNumberOfSnapshots_Type()
)
nASPoolNumberOfSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfSnapshots.setStatus("current")
_NASPoolNumberOfClonedVolumes_Type = Integer32
_NASPoolNumberOfClonedVolumes_Object = MibScalar
nASPoolNumberOfClonedVolumes = _NASPoolNumberOfClonedVolumes_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 38, 16),
    _NASPoolNumberOfClonedVolumes_Type()
)
nASPoolNumberOfClonedVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASPoolNumberOfClonedVolumes.setStatus("current")
_ClusterPartenrshipsTable_Object = MibTable
clusterPartenrshipsTable = _ClusterPartenrshipsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39)
)
if mibBuilder.loadTexts:
    clusterPartenrshipsTable.setStatus("current")
_ClusterPartenrshipsEntry_Object = MibTableRow
clusterPartenrshipsEntry = _ClusterPartenrshipsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1)
)
clusterPartenrshipsEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "clusterPartenrshipsIndex"),
)
if mibBuilder.loadTexts:
    clusterPartenrshipsEntry.setStatus("current")


class _ClusterPartenrshipsIndex_Type(Integer32):
    """Custom type clusterPartenrshipsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClusterPartenrshipsIndex_Type.__name__ = "Integer32"
_ClusterPartenrshipsIndex_Object = MibTableColumn
clusterPartenrshipsIndex = _ClusterPartenrshipsIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 1),
    _ClusterPartenrshipsIndex_Type()
)
clusterPartenrshipsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsIndex.setStatus("current")
_ClusterPartenrshipsClusterName_Type = OctetString
_ClusterPartenrshipsClusterName_Object = MibTableColumn
clusterPartenrshipsClusterName = _ClusterPartenrshipsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 2),
    _ClusterPartenrshipsClusterName_Type()
)
clusterPartenrshipsClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsClusterName.setStatus("current")
_ClusterPartenrshipsClusterIP_Type = OctetString
_ClusterPartenrshipsClusterIP_Object = MibTableColumn
clusterPartenrshipsClusterIP = _ClusterPartenrshipsClusterIP_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 3),
    _ClusterPartenrshipsClusterIP_Type()
)
clusterPartenrshipsClusterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsClusterIP.setStatus("current")
_ClusterPartenrshipsStatus_Type = OctetString
_ClusterPartenrshipsStatus_Object = MibTableColumn
clusterPartenrshipsStatus = _ClusterPartenrshipsStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 4),
    _ClusterPartenrshipsStatus_Type()
)
clusterPartenrshipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsStatus.setStatus("deprecated")
_ClusterPartenrshipsClusterName2_Type = OctetString
_ClusterPartenrshipsClusterName2_Object = MibTableColumn
clusterPartenrshipsClusterName2 = _ClusterPartenrshipsClusterName2_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 5),
    _ClusterPartenrshipsClusterName2_Type()
)
clusterPartenrshipsClusterName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsClusterName2.setStatus("current")
_ClusterPartenrshipsStatusEnumType_Type = TrustedSystemStatus
_ClusterPartenrshipsStatusEnumType_Object = MibTableColumn
clusterPartenrshipsStatusEnumType = _ClusterPartenrshipsStatusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 39, 1, 6),
    _ClusterPartenrshipsStatusEnumType_Type()
)
clusterPartenrshipsStatusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPartenrshipsStatusEnumType.setStatus("current")
_NASVolumeTable_Object = MibTable
nASVolumeTable = _NASVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41)
)
if mibBuilder.loadTexts:
    nASVolumeTable.setStatus("current")
_NASVolumeEntry_Object = MibTableRow
nASVolumeEntry = _NASVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1)
)
nASVolumeEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "nASVolumeIndex"),
)
if mibBuilder.loadTexts:
    nASVolumeEntry.setStatus("current")


class _NASVolumeIndex_Type(Integer32):
    """Custom type nASVolumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NASVolumeIndex_Type.__name__ = "Integer32"
_NASVolumeIndex_Object = MibTableColumn
nASVolumeIndex = _NASVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 1),
    _NASVolumeIndex_Type()
)
nASVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeIndex.setStatus("current")
_NASVolumeVolumeName_Type = OctetString
_NASVolumeVolumeName_Object = MibTableColumn
nASVolumeVolumeName = _NASVolumeVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 2),
    _NASVolumeVolumeName_Type()
)
nASVolumeVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeVolumeName.setStatus("current")
_NASVolumeSizeMB_Type = OctetString
_NASVolumeSizeMB_Object = MibTableColumn
nASVolumeSizeMB = _NASVolumeSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 3),
    _NASVolumeSizeMB_Type()
)
nASVolumeSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeSizeMB.setStatus("current")
_NASVolumeUsedSpaceMB_Type = OctetString
_NASVolumeUsedSpaceMB_Object = MibTableColumn
nASVolumeUsedSpaceMB = _NASVolumeUsedSpaceMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 4),
    _NASVolumeUsedSpaceMB_Type()
)
nASVolumeUsedSpaceMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeUsedSpaceMB.setStatus("current")
_NASVolumeSecurityStyleEnumType_Type = SecurityStyle
_NASVolumeSecurityStyleEnumType_Object = MibTableColumn
nASVolumeSecurityStyleEnumType = _NASVolumeSecurityStyleEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 5),
    _NASVolumeSecurityStyleEnumType_Type()
)
nASVolumeSecurityStyleEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeSecurityStyleEnumType.setStatus("current")
_NASVolumeIsCloneEnumType_Type = Boolean
_NASVolumeIsCloneEnumType_Object = MibTableColumn
nASVolumeIsCloneEnumType = _NASVolumeIsCloneEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 6),
    _NASVolumeIsCloneEnumType_Type()
)
nASVolumeIsCloneEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeIsCloneEnumType.setStatus("current")
_NASVolumeMetadataRedundancyEnabledEnumType_Type = Boolean
_NASVolumeMetadataRedundancyEnabledEnumType_Object = MibTableColumn
nASVolumeMetadataRedundancyEnabledEnumType = _NASVolumeMetadataRedundancyEnabledEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 7),
    _NASVolumeMetadataRedundancyEnabledEnumType_Type()
)
nASVolumeMetadataRedundancyEnabledEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeMetadataRedundancyEnabledEnumType.setStatus("current")
_NASVolumeOptimizationSavedSpaceMB_Type = OctetString
_NASVolumeOptimizationSavedSpaceMB_Object = MibTableColumn
nASVolumeOptimizationSavedSpaceMB = _NASVolumeOptimizationSavedSpaceMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 8),
    _NASVolumeOptimizationSavedSpaceMB_Type()
)
nASVolumeOptimizationSavedSpaceMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeOptimizationSavedSpaceMB.setStatus("current")
_NASVolumeNumberOfSnapshots_Type = Integer32
_NASVolumeNumberOfSnapshots_Object = MibTableColumn
nASVolumeNumberOfSnapshots = _NASVolumeNumberOfSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 9),
    _NASVolumeNumberOfSnapshots_Type()
)
nASVolumeNumberOfSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeNumberOfSnapshots.setStatus("current")
_NASVolumeReplicationStatusEnumType_Type = VolumeReplicationStatus
_NASVolumeReplicationStatusEnumType_Object = MibTableColumn
nASVolumeReplicationStatusEnumType = _NASVolumeReplicationStatusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 41, 1, 10),
    _NASVolumeReplicationStatusEnumType_Type()
)
nASVolumeReplicationStatusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nASVolumeReplicationStatusEnumType.setStatus("current")
_FluidFsNfsExportTable_Object = MibTable
fluidFsNfsExportTable = _FluidFsNfsExportTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 46)
)
if mibBuilder.loadTexts:
    fluidFsNfsExportTable.setStatus("current")
_FluidFsNfsExportEntry_Object = MibTableRow
fluidFsNfsExportEntry = _FluidFsNfsExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 46, 1)
)
fluidFsNfsExportEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "fluidFsNfsExportIndex"),
)
if mibBuilder.loadTexts:
    fluidFsNfsExportEntry.setStatus("current")


class _FluidFsNfsExportIndex_Type(Integer32):
    """Custom type fluidFsNfsExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FluidFsNfsExportIndex_Type.__name__ = "Integer32"
_FluidFsNfsExportIndex_Object = MibTableColumn
fluidFsNfsExportIndex = _FluidFsNfsExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 46, 1, 1),
    _FluidFsNfsExportIndex_Type()
)
fluidFsNfsExportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsNfsExportIndex.setStatus("current")
_FluidFsNfsExportVolumeName_Type = OctetString
_FluidFsNfsExportVolumeName_Object = MibTableColumn
fluidFsNfsExportVolumeName = _FluidFsNfsExportVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 46, 1, 2),
    _FluidFsNfsExportVolumeName_Type()
)
fluidFsNfsExportVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsNfsExportVolumeName.setStatus("current")
_FluidFsNfsExportPath_Type = OctetString
_FluidFsNfsExportPath_Object = MibTableColumn
fluidFsNfsExportPath = _FluidFsNfsExportPath_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 46, 1, 3),
    _FluidFsNfsExportPath_Type()
)
fluidFsNfsExportPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fluidFsNfsExportPath.setStatus("current")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 47)
)
_VersionVersion_Type = OctetString
_VersionVersion_Object = MibScalar
versionVersion = _VersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 47, 1),
    _VersionVersion_Type()
)
versionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionVersion.setStatus("current")
_VersionProductName_Type = OctetString
_VersionProductName_Object = MibScalar
versionProductName = _VersionProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 47, 2),
    _VersionProductName_Type()
)
versionProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProductName.setStatus("current")
_VersionProductDescription_Type = OctetString
_VersionProductDescription_Object = MibScalar
versionProductDescription = _VersionProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 47, 3),
    _VersionProductDescription_Type()
)
versionProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProductDescription.setStatus("current")
_VersionProductVendor_Type = OctetString
_VersionProductVendor_Object = MibScalar
versionProductVendor = _VersionProductVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 47, 4),
    _VersionProductVendor_Type()
)
versionProductVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProductVendor.setStatus("current")
_ExampleTable_Object = MibTable
exampleTable = _ExampleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999)
)
if mibBuilder.loadTexts:
    exampleTable.setStatus("current")
_ExampleEntry_Object = MibTableRow
exampleEntry = _ExampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1)
)
exampleEntry.setIndexNames(
    (0, "FLUIDFS-MIB", "exampleIndex"),
)
if mibBuilder.loadTexts:
    exampleEntry.setStatus("current")


class _ExampleIndex_Type(Integer32):
    """Custom type exampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ExampleIndex_Type.__name__ = "Integer32"
_ExampleIndex_Object = MibTableColumn
exampleIndex = _ExampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 1),
    _ExampleIndex_Type()
)
exampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleIndex.setStatus("current")
_ExampleShareName_Type = OctetString
_ExampleShareName_Object = MibTableColumn
exampleShareName = _ExampleShareName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 2),
    _ExampleShareName_Type()
)
exampleShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleShareName.setStatus("current")
_ExamplePath_Type = OctetString
_ExamplePath_Object = MibTableColumn
examplePath = _ExamplePath_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 3),
    _ExamplePath_Type()
)
examplePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    examplePath.setStatus("current")
_ExampleComment_Type = OctetString
_ExampleComment_Object = MibTableColumn
exampleComment = _ExampleComment_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 4),
    _ExampleComment_Type()
)
exampleComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleComment.setStatus("current")
_ExampleHideFiles_Type = OctetString
_ExampleHideFiles_Object = MibTableColumn
exampleHideFiles = _ExampleHideFiles_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 5),
    _ExampleHideFiles_Type()
)
exampleHideFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHideFiles.setStatus("current")
_ExampleAllowGuests_Type = OctetString
_ExampleAllowGuests_Object = MibTableColumn
exampleAllowGuests = _ExampleAllowGuests_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 6),
    _ExampleAllowGuests_Type()
)
exampleAllowGuests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAllowGuests.setStatus("deprecated")
_ExampleLocking_Type = OctetString
_ExampleLocking_Object = MibTableColumn
exampleLocking = _ExampleLocking_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 7),
    _ExampleLocking_Type()
)
exampleLocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleLocking.setStatus("deprecated")
_ExampleAntiVirus_Type = OctetString
_ExampleAntiVirus_Object = MibTableColumn
exampleAntiVirus = _ExampleAntiVirus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 8),
    _ExampleAntiVirus_Type()
)
exampleAntiVirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAntiVirus.setStatus("deprecated")
_ExampleAvPolicy_Type = OctetString
_ExampleAvPolicy_Object = MibTableColumn
exampleAvPolicy = _ExampleAvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 9),
    _ExampleAvPolicy_Type()
)
exampleAvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvPolicy.setStatus("deprecated")
_ExampleAvExtensions_Type = OctetString
_ExampleAvExtensions_Object = MibTableColumn
exampleAvExtensions = _ExampleAvExtensions_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 10),
    _ExampleAvExtensions_Type()
)
exampleAvExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvExtensions.setStatus("deprecated")
_ExampleAvExtensionsPolicy_Type = OctetString
_ExampleAvExtensionsPolicy_Object = MibTableColumn
exampleAvExtensionsPolicy = _ExampleAvExtensionsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 11),
    _ExampleAvExtensionsPolicy_Type()
)
exampleAvExtensionsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvExtensionsPolicy.setStatus("deprecated")
_ExampleAvExcludeDirs_Type = OctetString
_ExampleAvExcludeDirs_Object = MibTableColumn
exampleAvExcludeDirs = _ExampleAvExcludeDirs_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 12),
    _ExampleAvExcludeDirs_Type()
)
exampleAvExcludeDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvExcludeDirs.setStatus("current")
_ExampleGenericField_Type = Integer32
_ExampleGenericField_Object = MibTableColumn
exampleGenericField = _ExampleGenericField_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 13),
    _ExampleGenericField_Type()
)
exampleGenericField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleGenericField.setStatus("current")
_ExampleAllowGuestsEnumType_Type = Boolean
_ExampleAllowGuestsEnumType_Object = MibTableColumn
exampleAllowGuestsEnumType = _ExampleAllowGuestsEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 14),
    _ExampleAllowGuestsEnumType_Type()
)
exampleAllowGuestsEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAllowGuestsEnumType.setStatus("current")
_ExampleLockingEnumType_Type = Locking
_ExampleLockingEnumType_Object = MibTableColumn
exampleLockingEnumType = _ExampleLockingEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 15),
    _ExampleLockingEnumType_Type()
)
exampleLockingEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleLockingEnumType.setStatus("current")
_ExampleAntiVirusEnumType_Type = Boolean
_ExampleAntiVirusEnumType_Object = MibTableColumn
exampleAntiVirusEnumType = _ExampleAntiVirusEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 16),
    _ExampleAntiVirusEnumType_Type()
)
exampleAntiVirusEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAntiVirusEnumType.setStatus("current")
_ExampleAvPolicyEnumType_Type = AvPolicyType
_ExampleAvPolicyEnumType_Object = MibTableColumn
exampleAvPolicyEnumType = _ExampleAvPolicyEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 17),
    _ExampleAvPolicyEnumType_Type()
)
exampleAvPolicyEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvPolicyEnumType.setStatus("current")
_ExampleAvExtensions2_Type = OctetString
_ExampleAvExtensions2_Object = MibTableColumn
exampleAvExtensions2 = _ExampleAvExtensions2_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 18),
    _ExampleAvExtensions2_Type()
)
exampleAvExtensions2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvExtensions2.setStatus("current")
_ExampleAvExtensions2PolicyEnumType_Type = IncludeType
_ExampleAvExtensions2PolicyEnumType_Object = MibTableColumn
exampleAvExtensions2PolicyEnumType = _ExampleAvExtensions2PolicyEnumType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 19),
    _ExampleAvExtensions2PolicyEnumType_Type()
)
exampleAvExtensions2PolicyEnumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAvExtensions2PolicyEnumType.setStatus("current")
_ExampleStaticValue_Type = OctetString
_ExampleStaticValue_Object = MibTableColumn
exampleStaticValue = _ExampleStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 20),
    _ExampleStaticValue_Type()
)
exampleStaticValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleStaticValue.setStatus("current")
_ExampleRestrictedStaticValue1_Type = OctetString
_ExampleRestrictedStaticValue1_Object = MibTableColumn
exampleRestrictedStaticValue1 = _ExampleRestrictedStaticValue1_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 21),
    _ExampleRestrictedStaticValue1_Type()
)
exampleRestrictedStaticValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRestrictedStaticValue1.setStatus("current")
_ExampleRestrictedStaticValue2_Type = OctetString
_ExampleRestrictedStaticValue2_Object = MibTableColumn
exampleRestrictedStaticValue2 = _ExampleRestrictedStaticValue2_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 22),
    _ExampleRestrictedStaticValue2_Type()
)
exampleRestrictedStaticValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRestrictedStaticValue2.setStatus("current")
_ExampleRestrictedStaticValue3_Type = OctetString
_ExampleRestrictedStaticValue3_Object = MibTableColumn
exampleRestrictedStaticValue3 = _ExampleRestrictedStaticValue3_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 23),
    _ExampleRestrictedStaticValue3_Type()
)
exampleRestrictedStaticValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRestrictedStaticValue3.setStatus("current")
_ExampleRestrictedStaticValue4_Type = OctetString
_ExampleRestrictedStaticValue4_Object = MibTableColumn
exampleRestrictedStaticValue4 = _ExampleRestrictedStaticValue4_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 200, 1, 99999, 1, 24),
    _ExampleRestrictedStaticValue4_Type()
)
exampleRestrictedStaticValue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRestrictedStaticValue4.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FLUIDFS-MIB",
    **{"DomainStatusType": DomainStatusType,
       "DomainInfoStatusTypes": DomainInfoStatusTypes,
       "ExternalServerState": ExternalServerState,
       "WriteThroughModeTypes": WriteThroughModeTypes,
       "ServiceabilityState": ServiceabilityState,
       "ComponentStatus": ComponentStatus,
       "MemberModel": MemberModel,
       "AvPolicyType": AvPolicyType,
       "Boolean": Boolean,
       "SecurityStyle": SecurityStyle,
       "ExternalServerType": ExternalServerType,
       "AccessState": AccessState,
       "TrustedSystemStatus": TrustedSystemStatus,
       "IncludeType": IncludeType,
       "Locking": Locking,
       "VolumeReplicationStatus": VolumeReplicationStatus,
       "dell": dell,
       "enterpriseSoftware": enterpriseSoftware,
       "storageMgmt": storageMgmt,
       "fluidFS": fluidFS,
       "fluidFSProduct": fluidFSProduct,
       "activeDirectoryStatusTable": activeDirectoryStatusTable,
       "activeDirectoryStatusEntry": activeDirectoryStatusEntry,
       "activeDirectoryStatusConfigured": activeDirectoryStatusConfigured,
       "activeDirectoryStatusStatus": activeDirectoryStatusStatus,
       "activeDirectoryStatusDomain": activeDirectoryStatusDomain,
       "activeDirectoryStatusConfiguredEnumType": activeDirectoryStatusConfiguredEnumType,
       "activeDirectoryStatusStatusEnumType": activeDirectoryStatusStatusEnumType,
       "activeDirectoryStatusTenantId": activeDirectoryStatusTenantId,
       "fluidFsCifsShareTable": fluidFsCifsShareTable,
       "fluidFsCifsShareEntry": fluidFsCifsShareEntry,
       "fluidFsCifsShareIndex": fluidFsCifsShareIndex,
       "fluidFsCifsShareVolumeName": fluidFsCifsShareVolumeName,
       "fluidFsCifsShareShareName": fluidFsCifsShareShareName,
       "fluidFsCifsSharePath": fluidFsCifsSharePath,
       "fluidFsCifsShareAccessBasedEnumEnumType": fluidFsCifsShareAccessBasedEnumEnumType,
       "clusterName": clusterName,
       "clusterNameClusterName": clusterNameClusterName,
       "externalServerStateTable": externalServerStateTable,
       "externalServerStateEntry": externalServerStateEntry,
       "externalServerStateIndex": externalServerStateIndex,
       "externalServerStateHost": externalServerStateHost,
       "externalServerStateType": externalServerStateType,
       "externalServerStateState": externalServerStateState,
       "externalServerStateTypeEnumType": externalServerStateTypeEnumType,
       "externalServerStateStateEnumType": externalServerStateStateEnumType,
       "nASApplianceTable": nASApplianceTable,
       "nASApplianceEntry": nASApplianceEntry,
       "nASApplianceIndex": nASApplianceIndex,
       "nASApplianceId": nASApplianceId,
       "nASApplianceApplianceServiceTag": nASApplianceApplianceServiceTag,
       "nASApplianceFileSystemMember": nASApplianceFileSystemMember,
       "nASApplianceStatus": nASApplianceStatus,
       "nASApplianceModel": nASApplianceModel,
       "nASApplianceFileSystemMemberEnumType": nASApplianceFileSystemMemberEnumType,
       "nASApplianceStatusEnumType": nASApplianceStatusEnumType,
       "nASApplianceModelEnumType": nASApplianceModelEnumType,
       "nASApplianceApplianceID": nASApplianceApplianceID,
       "nASApplianceWriteThroughModeEnumType": nASApplianceWriteThroughModeEnumType,
       "nASApplianceWriteCachUsage": nASApplianceWriteCachUsage,
       "nASApplianceDomainStatusEnumType": nASApplianceDomainStatusEnumType,
       "storageSubsystemTable": storageSubsystemTable,
       "storageSubsystemEntry": storageSubsystemEntry,
       "storageSubsystemIndex": storageSubsystemIndex,
       "storageSubsystemLunsAccessibility": storageSubsystemLunsAccessibility,
       "storageSubsystemLunsAccessibilityEnumType": storageSubsystemLunsAccessibilityEnumType,
       "systemServiceMode": systemServiceMode,
       "systemServiceModeState": systemServiceModeState,
       "systemServiceModeStateEnumType": systemServiceModeStateEnumType,
       "systemTrafficStatisticsTable": systemTrafficStatisticsTable,
       "systemTrafficStatisticsEntry": systemTrafficStatisticsEntry,
       "systemTrafficStatisticsIndex": systemTrafficStatisticsIndex,
       "systemTrafficStatisticsTimestamp": systemTrafficStatisticsTimestamp,
       "systemTrafficStatisticsNFSReadMBsPerSec": systemTrafficStatisticsNFSReadMBsPerSec,
       "systemTrafficStatisticsNFSWriteMBsPerSec": systemTrafficStatisticsNFSWriteMBsPerSec,
       "systemTrafficStatisticsNDMPReadMBsPerSec": systemTrafficStatisticsNDMPReadMBsPerSec,
       "systemTrafficStatisticsNDMPWriteMBsPerSec": systemTrafficStatisticsNDMPWriteMBsPerSec,
       "systemTrafficStatisticsCIFSReadMBsPerSec": systemTrafficStatisticsCIFSReadMBsPerSec,
       "systemTrafficStatisticsCIFSWriteMBsPerSec": systemTrafficStatisticsCIFSWriteMBsPerSec,
       "systemTrafficStatisticsReplicationReadMBsPerSec": systemTrafficStatisticsReplicationReadMBsPerSec,
       "systemTrafficStatisticsReplicationWriteMBsPerSec": systemTrafficStatisticsReplicationWriteMBsPerSec,
       "systemTrafficStatisticsNetworkOverheadReadMBsPerSec": systemTrafficStatisticsNetworkOverheadReadMBsPerSec,
       "systemTrafficStatisticsNetworkOverheadWriteMBsPerSec": systemTrafficStatisticsNetworkOverheadWriteMBsPerSec,
       "systemTrafficStatisticsStorageSubSystemReadMBsPerSec": systemTrafficStatisticsStorageSubSystemReadMBsPerSec,
       "systemTrafficStatisticsStorageSubSystemWriteMBsPerSec": systemTrafficStatisticsStorageSubSystemWriteMBsPerSec,
       "systemTrafficStatisticsNFSIOPSRead": systemTrafficStatisticsNFSIOPSRead,
       "systemTrafficStatisticsNFSIOPSWrite": systemTrafficStatisticsNFSIOPSWrite,
       "systemTrafficStatisticsNFSIOPSOther": systemTrafficStatisticsNFSIOPSOther,
       "systemTrafficStatisticsCIFSIOPSRead": systemTrafficStatisticsCIFSIOPSRead,
       "systemTrafficStatisticsCIFSIOPSWrite": systemTrafficStatisticsCIFSIOPSWrite,
       "systemTrafficStatisticsCIFSIOPSOther": systemTrafficStatisticsCIFSIOPSOther,
       "nASPool": nASPool,
       "nASPoolTotalCapacityMB": nASPoolTotalCapacityMB,
       "nASPoolTotalReservedMB": nASPoolTotalReservedMB,
       "nASPoolTotalUsedMB": nASPoolTotalUsedMB,
       "nASPoolTotalUnusedMB": nASPoolTotalUnusedMB,
       "nASPoolTotalUnusedReservedMB": nASPoolTotalUnusedReservedMB,
       "nASPoolTotalUnusedUnreservedMB": nASPoolTotalUnusedUnreservedMB,
       "nASPoolTotalOverCommittedMB": nASPoolTotalOverCommittedMB,
       "nASPoolTotalOptimizationSavedSpaceMB": nASPoolTotalOptimizationSavedSpaceMB,
       "nASPoolNumberOfVirtualVolumes": nASPoolNumberOfVirtualVolumes,
       "nASPoolNumberOfVirtualVolumesWithSnapshots": nASPoolNumberOfVirtualVolumesWithSnapshots,
       "nASPoolNumberOfVirtualVolumesWithReplication": nASPoolNumberOfVirtualVolumesWithReplication,
       "nASPoolNumberOfVirtualVolumesWithDataReduction": nASPoolNumberOfVirtualVolumesWithDataReduction,
       "nASPoolNumberOfNfsExports": nASPoolNumberOfNfsExports,
       "nASPoolNumberOfCifsShares": nASPoolNumberOfCifsShares,
       "nASPoolNumberOfSnapshots": nASPoolNumberOfSnapshots,
       "nASPoolNumberOfClonedVolumes": nASPoolNumberOfClonedVolumes,
       "clusterPartenrshipsTable": clusterPartenrshipsTable,
       "clusterPartenrshipsEntry": clusterPartenrshipsEntry,
       "clusterPartenrshipsIndex": clusterPartenrshipsIndex,
       "clusterPartenrshipsClusterName": clusterPartenrshipsClusterName,
       "clusterPartenrshipsClusterIP": clusterPartenrshipsClusterIP,
       "clusterPartenrshipsStatus": clusterPartenrshipsStatus,
       "clusterPartenrshipsClusterName2": clusterPartenrshipsClusterName2,
       "clusterPartenrshipsStatusEnumType": clusterPartenrshipsStatusEnumType,
       "nASVolumeTable": nASVolumeTable,
       "nASVolumeEntry": nASVolumeEntry,
       "nASVolumeIndex": nASVolumeIndex,
       "nASVolumeVolumeName": nASVolumeVolumeName,
       "nASVolumeSizeMB": nASVolumeSizeMB,
       "nASVolumeUsedSpaceMB": nASVolumeUsedSpaceMB,
       "nASVolumeSecurityStyleEnumType": nASVolumeSecurityStyleEnumType,
       "nASVolumeIsCloneEnumType": nASVolumeIsCloneEnumType,
       "nASVolumeMetadataRedundancyEnabledEnumType": nASVolumeMetadataRedundancyEnabledEnumType,
       "nASVolumeOptimizationSavedSpaceMB": nASVolumeOptimizationSavedSpaceMB,
       "nASVolumeNumberOfSnapshots": nASVolumeNumberOfSnapshots,
       "nASVolumeReplicationStatusEnumType": nASVolumeReplicationStatusEnumType,
       "fluidFsNfsExportTable": fluidFsNfsExportTable,
       "fluidFsNfsExportEntry": fluidFsNfsExportEntry,
       "fluidFsNfsExportIndex": fluidFsNfsExportIndex,
       "fluidFsNfsExportVolumeName": fluidFsNfsExportVolumeName,
       "fluidFsNfsExportPath": fluidFsNfsExportPath,
       "version": version,
       "versionVersion": versionVersion,
       "versionProductName": versionProductName,
       "versionProductDescription": versionProductDescription,
       "versionProductVendor": versionProductVendor,
       "exampleTable": exampleTable,
       "exampleEntry": exampleEntry,
       "exampleIndex": exampleIndex,
       "exampleShareName": exampleShareName,
       "examplePath": examplePath,
       "exampleComment": exampleComment,
       "exampleHideFiles": exampleHideFiles,
       "exampleAllowGuests": exampleAllowGuests,
       "exampleLocking": exampleLocking,
       "exampleAntiVirus": exampleAntiVirus,
       "exampleAvPolicy": exampleAvPolicy,
       "exampleAvExtensions": exampleAvExtensions,
       "exampleAvExtensionsPolicy": exampleAvExtensionsPolicy,
       "exampleAvExcludeDirs": exampleAvExcludeDirs,
       "exampleGenericField": exampleGenericField,
       "exampleAllowGuestsEnumType": exampleAllowGuestsEnumType,
       "exampleLockingEnumType": exampleLockingEnumType,
       "exampleAntiVirusEnumType": exampleAntiVirusEnumType,
       "exampleAvPolicyEnumType": exampleAvPolicyEnumType,
       "exampleAvExtensions2": exampleAvExtensions2,
       "exampleAvExtensions2PolicyEnumType": exampleAvExtensions2PolicyEnumType,
       "exampleStaticValue": exampleStaticValue,
       "exampleRestrictedStaticValue1": exampleRestrictedStaticValue1,
       "exampleRestrictedStaticValue2": exampleRestrictedStaticValue2,
       "exampleRestrictedStaticValue3": exampleRestrictedStaticValue3,
       "exampleRestrictedStaticValue4": exampleRestrictedStaticValue4,
       "fluidFSMIBIdentity": fluidFSMIBIdentity}
)
