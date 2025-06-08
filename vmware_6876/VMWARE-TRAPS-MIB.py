# SNMP MIB module (VMWARE-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vmware_6876/VMWARE-TRAPS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:23:14 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vmware_ObjectIdentity = ObjectIdentity
vmware = _Vmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876)
)
_VmwSystem_ObjectIdentity = ObjectIdentity
vmwSystem = _VmwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1)
)
_VmwVirtMachines_ObjectIdentity = ObjectIdentity
vmwVirtMachines = _VmwVirtMachines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2)
)
_VmTable_Object = MibTable
vmTable = _VmTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1)
)
if mibBuilder.loadTexts:
    vmTable.setStatus("mandatory")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1)
)
vmEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "vmIdx"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("mandatory")


class _VmIdx_Type(Integer32):
    """Custom type vmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmIdx_Type.__name__ = "Integer32"
_VmIdx_Object = MibTableColumn
vmIdx = _VmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 1),
    _VmIdx_Type()
)
vmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIdx.setStatus("mandatory")
_VmDisplayName_Type = DisplayString
_VmDisplayName_Object = MibTableColumn
vmDisplayName = _VmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 2),
    _VmDisplayName_Type()
)
vmDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmDisplayName.setStatus("mandatory")
_VmConfigFile_Type = DisplayString
_VmConfigFile_Object = MibTableColumn
vmConfigFile = _VmConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 3),
    _VmConfigFile_Type()
)
vmConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConfigFile.setStatus("mandatory")
_VmGuestOS_Type = DisplayString
_VmGuestOS_Object = MibTableColumn
vmGuestOS = _VmGuestOS_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 4),
    _VmGuestOS_Type()
)
vmGuestOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmGuestOS.setStatus("mandatory")
_VmMemSize_Type = Integer32
_VmMemSize_Object = MibTableColumn
vmMemSize = _VmMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 5),
    _VmMemSize_Type()
)
vmMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMemSize.setStatus("mandatory")
_VmState_Type = DisplayString
_VmState_Object = MibTableColumn
vmState = _VmState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 6),
    _VmState_Type()
)
vmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmState.setStatus("mandatory")
_VmVMID_Type = Integer32
_VmVMID_Object = MibTableColumn
vmVMID = _VmVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 7),
    _VmVMID_Type()
)
vmVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVMID.setStatus("mandatory")
_VmGuestState_Type = DisplayString
_VmGuestState_Object = MibTableColumn
vmGuestState = _VmGuestState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 8),
    _VmGuestState_Type()
)
vmGuestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmGuestState.setStatus("mandatory")
_HbaTable_Object = MibTable
hbaTable = _HbaTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2)
)
if mibBuilder.loadTexts:
    hbaTable.setStatus("mandatory")
_HbaEntry_Object = MibTableRow
hbaEntry = _HbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1)
)
hbaEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "hbaVmIdx"),
    (0, "VMWARE-TRAPS-MIB", "hbaIdx"),
)
if mibBuilder.loadTexts:
    hbaEntry.setStatus("mandatory")


class _HbaVmIdx_Type(Integer32):
    """Custom type hbaVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HbaVmIdx_Type.__name__ = "Integer32"
_HbaVmIdx_Object = MibTableColumn
hbaVmIdx = _HbaVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 1),
    _HbaVmIdx_Type()
)
hbaVmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaVmIdx.setStatus("mandatory")


class _HbaIdx_Type(Integer32):
    """Custom type hbaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HbaIdx_Type.__name__ = "Integer32"
_HbaIdx_Object = MibTableColumn
hbaIdx = _HbaIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 2),
    _HbaIdx_Type()
)
hbaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaIdx.setStatus("mandatory")
_HbaNum_Type = DisplayString
_HbaNum_Object = MibTableColumn
hbaNum = _HbaNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 3),
    _HbaNum_Type()
)
hbaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaNum.setStatus("mandatory")
_HbaVirtDev_Type = DisplayString
_HbaVirtDev_Object = MibTableColumn
hbaVirtDev = _HbaVirtDev_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 4),
    _HbaVirtDev_Type()
)
hbaVirtDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaVirtDev.setStatus("mandatory")
_HbaTgtTable_Object = MibTable
hbaTgtTable = _HbaTgtTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3)
)
if mibBuilder.loadTexts:
    hbaTgtTable.setStatus("mandatory")
_HbaTgtEntry_Object = MibTableRow
hbaTgtEntry = _HbaTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1)
)
hbaTgtEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "hbaTgtVmIdx"),
    (0, "VMWARE-TRAPS-MIB", "hbaTgtIdx"),
)
if mibBuilder.loadTexts:
    hbaTgtEntry.setStatus("mandatory")


class _HbaTgtVmIdx_Type(Integer32):
    """Custom type hbaTgtVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HbaTgtVmIdx_Type.__name__ = "Integer32"
_HbaTgtVmIdx_Object = MibTableColumn
hbaTgtVmIdx = _HbaTgtVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 1),
    _HbaTgtVmIdx_Type()
)
hbaTgtVmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaTgtVmIdx.setStatus("mandatory")


class _HbaTgtIdx_Type(Integer32):
    """Custom type hbaTgtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HbaTgtIdx_Type.__name__ = "Integer32"
_HbaTgtIdx_Object = MibTableColumn
hbaTgtIdx = _HbaTgtIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 2),
    _HbaTgtIdx_Type()
)
hbaTgtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaTgtIdx.setStatus("mandatory")
_HbaTgtNum_Type = DisplayString
_HbaTgtNum_Object = MibTableColumn
hbaTgtNum = _HbaTgtNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 3),
    _HbaTgtNum_Type()
)
hbaTgtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaTgtNum.setStatus("mandatory")
_NetTable_Object = MibTable
netTable = _NetTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4)
)
if mibBuilder.loadTexts:
    netTable.setStatus("mandatory")
_NetEntry_Object = MibTableRow
netEntry = _NetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1)
)
netEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "netVmIdx"),
    (0, "VMWARE-TRAPS-MIB", "netIdx"),
)
if mibBuilder.loadTexts:
    netEntry.setStatus("mandatory")


class _NetVmIdx_Type(Integer32):
    """Custom type netVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetVmIdx_Type.__name__ = "Integer32"
_NetVmIdx_Object = MibTableColumn
netVmIdx = _NetVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 1),
    _NetVmIdx_Type()
)
netVmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netVmIdx.setStatus("mandatory")


class _NetIdx_Type(Integer32):
    """Custom type netIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NetIdx_Type.__name__ = "Integer32"
_NetIdx_Object = MibTableColumn
netIdx = _NetIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 2),
    _NetIdx_Type()
)
netIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIdx.setStatus("mandatory")
_NetNum_Type = DisplayString
_NetNum_Object = MibTableColumn
netNum = _NetNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 3),
    _NetNum_Type()
)
netNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netNum.setStatus("mandatory")
_NetName_Type = DisplayString
_NetName_Object = MibTableColumn
netName = _NetName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 4),
    _NetName_Type()
)
netName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netName.setStatus("mandatory")
_NetConnType_Type = DisplayString
_NetConnType_Object = MibTableColumn
netConnType = _NetConnType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 5),
    _NetConnType_Type()
)
netConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConnType.setStatus("mandatory")
_FloppyTable_Object = MibTable
floppyTable = _FloppyTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5)
)
if mibBuilder.loadTexts:
    floppyTable.setStatus("mandatory")
_FloppyEntry_Object = MibTableRow
floppyEntry = _FloppyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1)
)
floppyEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "fdVmIdx"),
    (0, "VMWARE-TRAPS-MIB", "fdIdx"),
)
if mibBuilder.loadTexts:
    floppyEntry.setStatus("mandatory")


class _FdVmIdx_Type(Integer32):
    """Custom type fdVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FdVmIdx_Type.__name__ = "Integer32"
_FdVmIdx_Object = MibTableColumn
fdVmIdx = _FdVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 1),
    _FdVmIdx_Type()
)
fdVmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdVmIdx.setStatus("mandatory")


class _FdIdx_Type(Integer32):
    """Custom type fdIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FdIdx_Type.__name__ = "Integer32"
_FdIdx_Object = MibTableColumn
fdIdx = _FdIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 2),
    _FdIdx_Type()
)
fdIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdIdx.setStatus("mandatory")
_FdName_Type = DisplayString
_FdName_Object = MibTableColumn
fdName = _FdName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 3),
    _FdName_Type()
)
fdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdName.setStatus("mandatory")
_FdConnected_Type = DisplayString
_FdConnected_Object = MibTableColumn
fdConnected = _FdConnected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 4),
    _FdConnected_Type()
)
fdConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdConnected.setStatus("mandatory")
_CdromTable_Object = MibTable
cdromTable = _CdromTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6)
)
if mibBuilder.loadTexts:
    cdromTable.setStatus("mandatory")
_CdromEntry_Object = MibTableRow
cdromEntry = _CdromEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1)
)
cdromEntry.setIndexNames(
    (0, "VMWARE-TRAPS-MIB", "cdVmIdx"),
    (0, "VMWARE-TRAPS-MIB", "cdromIdx"),
)
if mibBuilder.loadTexts:
    cdromEntry.setStatus("mandatory")


class _CdVmIdx_Type(Integer32):
    """Custom type cdVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdVmIdx_Type.__name__ = "Integer32"
_CdVmIdx_Object = MibTableColumn
cdVmIdx = _CdVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 1),
    _CdVmIdx_Type()
)
cdVmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdVmIdx.setStatus("mandatory")


class _CdromIdx_Type(Integer32):
    """Custom type cdromIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CdromIdx_Type.__name__ = "Integer32"
_CdromIdx_Object = MibTableColumn
cdromIdx = _CdromIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 2),
    _CdromIdx_Type()
)
cdromIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdromIdx.setStatus("mandatory")
_CdromName_Type = DisplayString
_CdromName_Object = MibTableColumn
cdromName = _CdromName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 3),
    _CdromName_Type()
)
cdromName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdromName.setStatus("mandatory")
_CdromConnected_Type = DisplayString
_CdromConnected_Object = MibTableColumn
cdromConnected = _CdromConnected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 4),
    _CdromConnected_Type()
)
cdromConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdromConnected.setStatus("mandatory")
_VmwResources_ObjectIdentity = ObjectIdentity
vmwResources = _VmwResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3)
)
_VmwProductSpecific_ObjectIdentity = ObjectIdentity
vmwProductSpecific = _VmwProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4)
)
_VmwTraps_ObjectIdentity = ObjectIdentity
vmwTraps = _VmwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 50)
)
_VmID_Type = Integer32
_VmID_Object = MibScalar
vmID = _VmID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 101),
    _VmID_Type()
)
vmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmID.setStatus("mandatory")
_VmConfig_Type = DisplayString
_VmConfig_Object = MibScalar
vmConfig = _VmConfig_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 102),
    _VmConfig_Type()
)
vmConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConfig.setStatus("mandatory")
_VpxdTrapType_Type = DisplayString
_VpxdTrapType_Object = MibScalar
vpxdTrapType = _VpxdTrapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 301),
    _VpxdTrapType_Type()
)
vpxdTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdTrapType.setStatus("mandatory")
_VpxdHostName_Type = DisplayString
_VpxdHostName_Object = MibScalar
vpxdHostName = _VpxdHostName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 302),
    _VpxdHostName_Type()
)
vpxdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdHostName.setStatus("mandatory")
_VpxdVMName_Type = DisplayString
_VpxdVMName_Object = MibScalar
vpxdVMName = _VpxdVMName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 303),
    _VpxdVMName_Type()
)
vpxdVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdVMName.setStatus("mandatory")
_VpxdOldStatus_Type = DisplayString
_VpxdOldStatus_Object = MibScalar
vpxdOldStatus = _VpxdOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 304),
    _VpxdOldStatus_Type()
)
vpxdOldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdOldStatus.setStatus("mandatory")
_VpxdNewStatus_Type = DisplayString
_VpxdNewStatus_Object = MibScalar
vpxdNewStatus = _VpxdNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 305),
    _VpxdNewStatus_Type()
)
vpxdNewStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdNewStatus.setStatus("mandatory")
_VpxdObjValue_Type = DisplayString
_VpxdObjValue_Object = MibScalar
vpxdObjValue = _VpxdObjValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 306),
    _VpxdObjValue_Type()
)
vpxdObjValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdObjValue.setStatus("mandatory")
_VmwOID_ObjectIdentity = ObjectIdentity
vmwOID = _VmwOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 60)
)
_VmwExperimental_ObjectIdentity = ObjectIdentity
vmwExperimental = _VmwExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 700)
)

# Managed Objects groups


# Notification objects

vmPoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 1)
)
vmPoweredOn.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfig"),
        ("VMWARE-TRAPS-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmPoweredOn.setStatus(
        ""
    )

vmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 2)
)
vmPoweredOff.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfig"),
        ("VMWARE-TRAPS-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmPoweredOff.setStatus(
        ""
    )

vmHBLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 3)
)
vmHBLost.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfig"),
        ("VMWARE-TRAPS-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmHBLost.setStatus(
        ""
    )

vmHBDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 4)
)
vmHBDetected.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfig"),
        ("VMWARE-TRAPS-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmHBDetected.setStatus(
        ""
    )

vmSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 5)
)
vmSuspended.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfig"),
        ("VMWARE-TRAPS-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmSuspended.setStatus(
        ""
    )

vpxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 50, 0, 201)
)
vpxdTrap.setObjects(
      *(("VMWARE-TRAPS-MIB", "vpxdTrapType"),
        ("VMWARE-TRAPS-MIB", "vpxdHostName"),
        ("VMWARE-TRAPS-MIB", "vpxdVMName"),
        ("VMWARE-TRAPS-MIB", "vpxdNewStatus"),
        ("VMWARE-TRAPS-MIB", "vpxdOldStatus"),
        ("VMWARE-TRAPS-MIB", "vpxdObjValue"))
)
if mibBuilder.loadTexts:
    vpxdTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-TRAPS-MIB",
    **{"vmware": vmware,
       "vmPoweredOn": vmPoweredOn,
       "vmPoweredOff": vmPoweredOff,
       "vmHBLost": vmHBLost,
       "vmHBDetected": vmHBDetected,
       "vmSuspended": vmSuspended,
       "vmwSystem": vmwSystem,
       "vmwVirtMachines": vmwVirtMachines,
       "vmTable": vmTable,
       "vmEntry": vmEntry,
       "vmIdx": vmIdx,
       "vmDisplayName": vmDisplayName,
       "vmConfigFile": vmConfigFile,
       "vmGuestOS": vmGuestOS,
       "vmMemSize": vmMemSize,
       "vmState": vmState,
       "vmVMID": vmVMID,
       "vmGuestState": vmGuestState,
       "hbaTable": hbaTable,
       "hbaEntry": hbaEntry,
       "hbaVmIdx": hbaVmIdx,
       "hbaIdx": hbaIdx,
       "hbaNum": hbaNum,
       "hbaVirtDev": hbaVirtDev,
       "hbaTgtTable": hbaTgtTable,
       "hbaTgtEntry": hbaTgtEntry,
       "hbaTgtVmIdx": hbaTgtVmIdx,
       "hbaTgtIdx": hbaTgtIdx,
       "hbaTgtNum": hbaTgtNum,
       "netTable": netTable,
       "netEntry": netEntry,
       "netVmIdx": netVmIdx,
       "netIdx": netIdx,
       "netNum": netNum,
       "netName": netName,
       "netConnType": netConnType,
       "floppyTable": floppyTable,
       "floppyEntry": floppyEntry,
       "fdVmIdx": fdVmIdx,
       "fdIdx": fdIdx,
       "fdName": fdName,
       "fdConnected": fdConnected,
       "cdromTable": cdromTable,
       "cdromEntry": cdromEntry,
       "cdVmIdx": cdVmIdx,
       "cdromIdx": cdromIdx,
       "cdromName": cdromName,
       "cdromConnected": cdromConnected,
       "vmwResources": vmwResources,
       "vmwProductSpecific": vmwProductSpecific,
       "vmwTraps": vmwTraps,
       "vpxdTrap": vpxdTrap,
       "vmID": vmID,
       "vmConfig": vmConfig,
       "vpxdTrapType": vpxdTrapType,
       "vpxdHostName": vpxdHostName,
       "vpxdVMName": vpxdVMName,
       "vpxdOldStatus": vpxdOldStatus,
       "vpxdNewStatus": vpxdNewStatus,
       "vpxdObjValue": vpxdObjValue,
       "vmwOID": vmwOID,
       "vmwExperimental": vmwExperimental}
)
