# SNMP MIB module (VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IETF/VM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:06:02 2025
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

(IANAStorageMediaType,) = mibBuilder.importSymbols(
    "IANA-STORAGE-MEDIA-TYPE-MIB",
    "IANAStorageMediaType")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(UUIDorZero,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUIDorZero")


# MODULE-IDENTITY

vmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 236)
)
if mibBuilder.loadTexts:
    vmMIB.setRevisions(
        ("2015-10-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VirtualMachineIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VirtualMachineIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VirtualMachineAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("suspended", 2),
          ("paused", 3),
          ("shutdown", 4))
    )



class VirtualMachineOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("preparing", 3),
          ("running", 4),
          ("suspending", 5),
          ("suspended", 6),
          ("resuming", 7),
          ("paused", 8),
          ("migrating", 9),
          ("shuttingdown", 10),
          ("shutdown", 11),
          ("crashed", 12))
    )



class VirtualMachineAutoStart(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 3))
    )



class VirtualMachinePersistent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("persistent", 2),
          ("transient", 3))
    )



class VirtualMachineCpuIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VirtualMachineStorageIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VirtualMachineStorageSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("block", 3),
          ("raw", 4),
          ("sparse", 5),
          ("network", 6))
    )



class VirtualMachineStorageAccess(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("readwrite", 2),
          ("readonly", 3))
    )



class VirtualMachineNetworkIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class VirtualMachineList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"


# MIB Managed Objects in the order of their OIDs

_VmNotifications_ObjectIdentity = ObjectIdentity
vmNotifications = _VmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 0)
)
_VmObjects_ObjectIdentity = ObjectIdentity
vmObjects = _VmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 1)
)
_VmHypervisor_ObjectIdentity = ObjectIdentity
vmHypervisor = _VmHypervisor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 1, 1)
)


class _VmHvSoftware_Type(SnmpAdminString):
    """Custom type vmHvSoftware based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmHvSoftware_Type.__name__ = "SnmpAdminString"
_VmHvSoftware_Object = MibScalar
vmHvSoftware = _VmHvSoftware_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 1, 1),
    _VmHvSoftware_Type()
)
vmHvSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmHvSoftware.setStatus("current")


class _VmHvVersion_Type(SnmpAdminString):
    """Custom type vmHvVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmHvVersion_Type.__name__ = "SnmpAdminString"
_VmHvVersion_Object = MibScalar
vmHvVersion = _VmHvVersion_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 1, 2),
    _VmHvVersion_Type()
)
vmHvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmHvVersion.setStatus("current")
_VmHvObjectID_Type = ObjectIdentifier
_VmHvObjectID_Object = MibScalar
vmHvObjectID = _VmHvObjectID_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 1, 3),
    _VmHvObjectID_Type()
)
vmHvObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmHvObjectID.setStatus("current")
_VmHvUpTime_Type = TimeTicks
_VmHvUpTime_Object = MibScalar
vmHvUpTime = _VmHvUpTime_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 1, 4),
    _VmHvUpTime_Type()
)
vmHvUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmHvUpTime.setStatus("current")


class _VmNumber_Type(Integer32):
    """Custom type vmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VmNumber_Type.__name__ = "Integer32"
_VmNumber_Object = MibScalar
vmNumber = _VmNumber_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 2),
    _VmNumber_Type()
)
vmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmNumber.setStatus("current")
_VmTableLastChange_Type = TimeTicks
_VmTableLastChange_Object = MibScalar
vmTableLastChange = _VmTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 3),
    _VmTableLastChange_Type()
)
vmTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmTableLastChange.setStatus("current")
_VmTable_Object = MibTable
vmTable = _VmTable_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4)
)
if mibBuilder.loadTexts:
    vmTable.setStatus("current")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1)
)
vmEntry.setIndexNames(
    (0, "VM-MIB", "vmIndex"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("current")
_VmIndex_Type = VirtualMachineIndex
_VmIndex_Object = MibTableColumn
vmIndex = _VmIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 1),
    _VmIndex_Type()
)
vmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmIndex.setStatus("current")


class _VmName_Type(SnmpAdminString):
    """Custom type vmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmName_Type.__name__ = "SnmpAdminString"
_VmName_Object = MibTableColumn
vmName = _VmName_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 2),
    _VmName_Type()
)
vmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmName.setStatus("current")
_VmUUID_Type = UUIDorZero
_VmUUID_Object = MibTableColumn
vmUUID = _VmUUID_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 3),
    _VmUUID_Type()
)
vmUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmUUID.setStatus("current")


class _VmOSType_Type(SnmpAdminString):
    """Custom type vmOSType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmOSType_Type.__name__ = "SnmpAdminString"
_VmOSType_Object = MibTableColumn
vmOSType = _VmOSType_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 4),
    _VmOSType_Type()
)
vmOSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmOSType.setStatus("current")
_VmAdminState_Type = VirtualMachineAdminState
_VmAdminState_Object = MibTableColumn
vmAdminState = _VmAdminState_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 5),
    _VmAdminState_Type()
)
vmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmAdminState.setStatus("current")
_VmOperState_Type = VirtualMachineOperState
_VmOperState_Object = MibTableColumn
vmOperState = _VmOperState_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 6),
    _VmOperState_Type()
)
vmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmOperState.setStatus("current")
_VmAutoStart_Type = VirtualMachineAutoStart
_VmAutoStart_Object = MibTableColumn
vmAutoStart = _VmAutoStart_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 7),
    _VmAutoStart_Type()
)
vmAutoStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmAutoStart.setStatus("current")
_VmPersistent_Type = VirtualMachinePersistent
_VmPersistent_Object = MibTableColumn
vmPersistent = _VmPersistent_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 8),
    _VmPersistent_Type()
)
vmPersistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmPersistent.setStatus("current")


class _VmCurCpuNumber_Type(Integer32):
    """Custom type vmCurCpuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VmCurCpuNumber_Type.__name__ = "Integer32"
_VmCurCpuNumber_Object = MibTableColumn
vmCurCpuNumber = _VmCurCpuNumber_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 9),
    _VmCurCpuNumber_Type()
)
vmCurCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCurCpuNumber.setStatus("current")


class _VmMinCpuNumber_Type(Integer32):
    """Custom type vmMinCpuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmMinCpuNumber_Type.__name__ = "Integer32"
_VmMinCpuNumber_Object = MibTableColumn
vmMinCpuNumber = _VmMinCpuNumber_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 10),
    _VmMinCpuNumber_Type()
)
vmMinCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMinCpuNumber.setStatus("current")


class _VmMaxCpuNumber_Type(Integer32):
    """Custom type vmMaxCpuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmMaxCpuNumber_Type.__name__ = "Integer32"
_VmMaxCpuNumber_Object = MibTableColumn
vmMaxCpuNumber = _VmMaxCpuNumber_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 11),
    _VmMaxCpuNumber_Type()
)
vmMaxCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMaxCpuNumber.setStatus("current")


class _VmMemUnit_Type(Integer32):
    """Custom type vmMemUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmMemUnit_Type.__name__ = "Integer32"
_VmMemUnit_Object = MibTableColumn
vmMemUnit = _VmMemUnit_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 12),
    _VmMemUnit_Type()
)
vmMemUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMemUnit.setStatus("current")


class _VmCurMem_Type(Integer32):
    """Custom type vmCurMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VmCurMem_Type.__name__ = "Integer32"
_VmCurMem_Object = MibTableColumn
vmCurMem = _VmCurMem_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 13),
    _VmCurMem_Type()
)
vmCurMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCurMem.setStatus("current")


class _VmMinMem_Type(Integer32):
    """Custom type vmMinMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmMinMem_Type.__name__ = "Integer32"
_VmMinMem_Object = MibTableColumn
vmMinMem = _VmMinMem_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 14),
    _VmMinMem_Type()
)
vmMinMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMinMem.setStatus("current")


class _VmMaxMem_Type(Integer32):
    """Custom type vmMaxMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmMaxMem_Type.__name__ = "Integer32"
_VmMaxMem_Object = MibTableColumn
vmMaxMem = _VmMaxMem_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 15),
    _VmMaxMem_Type()
)
vmMaxMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMaxMem.setStatus("current")
_VmUpTime_Type = TimeTicks
_VmUpTime_Object = MibTableColumn
vmUpTime = _VmUpTime_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 16),
    _VmUpTime_Type()
)
vmUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmUpTime.setStatus("current")
_VmCpuTime_Type = Counter64
_VmCpuTime_Object = MibTableColumn
vmCpuTime = _VmCpuTime_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 17),
    _VmCpuTime_Type()
)
vmCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCpuTime.setStatus("current")
if mibBuilder.loadTexts:
    vmCpuTime.setUnits("microsecond")
_VmCpuTable_Object = MibTable
vmCpuTable = _VmCpuTable_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 5)
)
if mibBuilder.loadTexts:
    vmCpuTable.setStatus("current")
_VmCpuEntry_Object = MibTableRow
vmCpuEntry = _VmCpuEntry_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 5, 1)
)
vmCpuEntry.setIndexNames(
    (0, "VM-MIB", "vmIndex"),
    (0, "VM-MIB", "vmCpuIndex"),
)
if mibBuilder.loadTexts:
    vmCpuEntry.setStatus("current")
_VmCpuIndex_Type = VirtualMachineCpuIndex
_VmCpuIndex_Object = MibTableColumn
vmCpuIndex = _VmCpuIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 5, 1, 1),
    _VmCpuIndex_Type()
)
vmCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmCpuIndex.setStatus("current")
_VmCpuCoreTime_Type = Counter64
_VmCpuCoreTime_Object = MibTableColumn
vmCpuCoreTime = _VmCpuCoreTime_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 5, 1, 2),
    _VmCpuCoreTime_Type()
)
vmCpuCoreTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCpuCoreTime.setStatus("current")
if mibBuilder.loadTexts:
    vmCpuCoreTime.setUnits("microsecond")
_VmCpuAffinityTable_Object = MibTable
vmCpuAffinityTable = _VmCpuAffinityTable_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 6)
)
if mibBuilder.loadTexts:
    vmCpuAffinityTable.setStatus("current")
_VmCpuAffinityEntry_Object = MibTableRow
vmCpuAffinityEntry = _VmCpuAffinityEntry_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 6, 1)
)
vmCpuAffinityEntry.setIndexNames(
    (0, "VM-MIB", "vmIndex"),
    (0, "VM-MIB", "vmCpuIndex"),
    (0, "VM-MIB", "vmCpuPhysIndex"),
)
if mibBuilder.loadTexts:
    vmCpuAffinityEntry.setStatus("current")


class _VmCpuPhysIndex_Type(Integer32):
    """Custom type vmCpuPhysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmCpuPhysIndex_Type.__name__ = "Integer32"
_VmCpuPhysIndex_Object = MibTableColumn
vmCpuPhysIndex = _VmCpuPhysIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 6, 1, 2),
    _VmCpuPhysIndex_Type()
)
vmCpuPhysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmCpuPhysIndex.setStatus("current")


class _VmCpuAffinity_Type(Integer32):
    """Custom type vmCpuAffinity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enable", 1),
          ("disable", 2))
    )


_VmCpuAffinity_Type.__name__ = "Integer32"
_VmCpuAffinity_Object = MibTableColumn
vmCpuAffinity = _VmCpuAffinity_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 6, 1, 3),
    _VmCpuAffinity_Type()
)
vmCpuAffinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCpuAffinity.setStatus("current")
_VmStorageTable_Object = MibTable
vmStorageTable = _VmStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7)
)
if mibBuilder.loadTexts:
    vmStorageTable.setStatus("current")
_VmStorageEntry_Object = MibTableRow
vmStorageEntry = _VmStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1)
)
vmStorageEntry.setIndexNames(
    (0, "VM-MIB", "vmStorageVmIndex"),
    (0, "VM-MIB", "vmStorageIndex"),
)
if mibBuilder.loadTexts:
    vmStorageEntry.setStatus("current")
_VmStorageVmIndex_Type = VirtualMachineIndexOrZero
_VmStorageVmIndex_Object = MibTableColumn
vmStorageVmIndex = _VmStorageVmIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 1),
    _VmStorageVmIndex_Type()
)
vmStorageVmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmStorageVmIndex.setStatus("current")
_VmStorageIndex_Type = VirtualMachineStorageIndex
_VmStorageIndex_Object = MibTableColumn
vmStorageIndex = _VmStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 2),
    _VmStorageIndex_Type()
)
vmStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmStorageIndex.setStatus("current")


class _VmStorageParent_Type(Integer32):
    """Custom type vmStorageParent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VmStorageParent_Type.__name__ = "Integer32"
_VmStorageParent_Object = MibTableColumn
vmStorageParent = _VmStorageParent_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 3),
    _VmStorageParent_Type()
)
vmStorageParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageParent.setStatus("current")
_VmStorageSourceType_Type = VirtualMachineStorageSourceType
_VmStorageSourceType_Object = MibTableColumn
vmStorageSourceType = _VmStorageSourceType_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 4),
    _VmStorageSourceType_Type()
)
vmStorageSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageSourceType.setStatus("current")


class _VmStorageSourceTypeString_Type(SnmpAdminString):
    """Custom type vmStorageSourceTypeString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmStorageSourceTypeString_Type.__name__ = "SnmpAdminString"
_VmStorageSourceTypeString_Object = MibTableColumn
vmStorageSourceTypeString = _VmStorageSourceTypeString_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 5),
    _VmStorageSourceTypeString_Type()
)
vmStorageSourceTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageSourceTypeString.setStatus("current")


class _VmStorageResourceID_Type(SnmpAdminString):
    """Custom type vmStorageResourceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmStorageResourceID_Type.__name__ = "SnmpAdminString"
_VmStorageResourceID_Object = MibTableColumn
vmStorageResourceID = _VmStorageResourceID_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 6),
    _VmStorageResourceID_Type()
)
vmStorageResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageResourceID.setStatus("current")
_VmStorageAccess_Type = VirtualMachineStorageAccess
_VmStorageAccess_Object = MibTableColumn
vmStorageAccess = _VmStorageAccess_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 7),
    _VmStorageAccess_Type()
)
vmStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageAccess.setStatus("current")
_VmStorageMediaType_Type = IANAStorageMediaType
_VmStorageMediaType_Object = MibTableColumn
vmStorageMediaType = _VmStorageMediaType_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 8),
    _VmStorageMediaType_Type()
)
vmStorageMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageMediaType.setStatus("current")


class _VmStorageMediaTypeString_Type(SnmpAdminString):
    """Custom type vmStorageMediaTypeString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmStorageMediaTypeString_Type.__name__ = "SnmpAdminString"
_VmStorageMediaTypeString_Object = MibTableColumn
vmStorageMediaTypeString = _VmStorageMediaTypeString_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 9),
    _VmStorageMediaTypeString_Type()
)
vmStorageMediaTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageMediaTypeString.setStatus("current")


class _VmStorageSizeUnit_Type(Integer32):
    """Custom type vmStorageSizeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmStorageSizeUnit_Type.__name__ = "Integer32"
_VmStorageSizeUnit_Object = MibTableColumn
vmStorageSizeUnit = _VmStorageSizeUnit_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 10),
    _VmStorageSizeUnit_Type()
)
vmStorageSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageSizeUnit.setStatus("current")


class _VmStorageDefinedSize_Type(Integer32):
    """Custom type vmStorageDefinedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmStorageDefinedSize_Type.__name__ = "Integer32"
_VmStorageDefinedSize_Object = MibTableColumn
vmStorageDefinedSize = _VmStorageDefinedSize_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 11),
    _VmStorageDefinedSize_Type()
)
vmStorageDefinedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageDefinedSize.setStatus("current")


class _VmStorageAllocatedSize_Type(Integer32):
    """Custom type vmStorageAllocatedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VmStorageAllocatedSize_Type.__name__ = "Integer32"
_VmStorageAllocatedSize_Object = MibTableColumn
vmStorageAllocatedSize = _VmStorageAllocatedSize_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 12),
    _VmStorageAllocatedSize_Type()
)
vmStorageAllocatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageAllocatedSize.setStatus("current")
_VmStorageReadIOs_Type = Counter64
_VmStorageReadIOs_Object = MibTableColumn
vmStorageReadIOs = _VmStorageReadIOs_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 13),
    _VmStorageReadIOs_Type()
)
vmStorageReadIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageReadIOs.setStatus("current")
_VmStorageWriteIOs_Type = Counter64
_VmStorageWriteIOs_Object = MibTableColumn
vmStorageWriteIOs = _VmStorageWriteIOs_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 14),
    _VmStorageWriteIOs_Type()
)
vmStorageWriteIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageWriteIOs.setStatus("current")
_VmStorageReadOctets_Type = Counter64
_VmStorageReadOctets_Object = MibTableColumn
vmStorageReadOctets = _VmStorageReadOctets_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 15),
    _VmStorageReadOctets_Type()
)
vmStorageReadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageReadOctets.setStatus("current")
_VmStorageWriteOctets_Type = Counter64
_VmStorageWriteOctets_Object = MibTableColumn
vmStorageWriteOctets = _VmStorageWriteOctets_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 16),
    _VmStorageWriteOctets_Type()
)
vmStorageWriteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageWriteOctets.setStatus("current")
_VmStorageReadLatency_Type = Counter64
_VmStorageReadLatency_Object = MibTableColumn
vmStorageReadLatency = _VmStorageReadLatency_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 17),
    _VmStorageReadLatency_Type()
)
vmStorageReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageReadLatency.setStatus("current")
_VmStorageWriteLatency_Type = Counter64
_VmStorageWriteLatency_Object = MibTableColumn
vmStorageWriteLatency = _VmStorageWriteLatency_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 18),
    _VmStorageWriteLatency_Type()
)
vmStorageWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageWriteLatency.setStatus("current")
_VmNetworkTable_Object = MibTable
vmNetworkTable = _VmNetworkTable_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8)
)
if mibBuilder.loadTexts:
    vmNetworkTable.setStatus("current")
_VmNetworkEntry_Object = MibTableRow
vmNetworkEntry = _VmNetworkEntry_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1)
)
vmNetworkEntry.setIndexNames(
    (0, "VM-MIB", "vmIndex"),
    (0, "VM-MIB", "vmNetworkIndex"),
)
if mibBuilder.loadTexts:
    vmNetworkEntry.setStatus("current")
_VmNetworkIndex_Type = VirtualMachineNetworkIndex
_VmNetworkIndex_Object = MibTableColumn
vmNetworkIndex = _VmNetworkIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 1),
    _VmNetworkIndex_Type()
)
vmNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmNetworkIndex.setStatus("current")
_VmNetworkIfIndex_Type = InterfaceIndexOrZero
_VmNetworkIfIndex_Object = MibTableColumn
vmNetworkIfIndex = _VmNetworkIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 2),
    _VmNetworkIfIndex_Type()
)
vmNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmNetworkIfIndex.setStatus("current")
_VmNetworkParent_Type = InterfaceIndexOrZero
_VmNetworkParent_Object = MibTableColumn
vmNetworkParent = _VmNetworkParent_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 3),
    _VmNetworkParent_Type()
)
vmNetworkParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmNetworkParent.setStatus("current")


class _VmNetworkModel_Type(SnmpAdminString):
    """Custom type vmNetworkModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmNetworkModel_Type.__name__ = "SnmpAdminString"
_VmNetworkModel_Object = MibTableColumn
vmNetworkModel = _VmNetworkModel_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 4),
    _VmNetworkModel_Type()
)
vmNetworkModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmNetworkModel.setStatus("current")
_VmNetworkPhysAddress_Type = PhysAddress
_VmNetworkPhysAddress_Object = MibTableColumn
vmNetworkPhysAddress = _VmNetworkPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 5),
    _VmNetworkPhysAddress_Type()
)
vmNetworkPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmNetworkPhysAddress.setStatus("current")
_VmPerVMNotificationsEnabled_Type = TruthValue
_VmPerVMNotificationsEnabled_Object = MibScalar
vmPerVMNotificationsEnabled = _VmPerVMNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 9),
    _VmPerVMNotificationsEnabled_Type()
)
vmPerVMNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmPerVMNotificationsEnabled.setStatus("current")
_VmBulkNotificationsEnabled_Type = TruthValue
_VmBulkNotificationsEnabled_Object = MibScalar
vmBulkNotificationsEnabled = _VmBulkNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 10),
    _VmBulkNotificationsEnabled_Type()
)
vmBulkNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmBulkNotificationsEnabled.setStatus("current")
_VmAffectedVMs_Type = VirtualMachineList
_VmAffectedVMs_Object = MibScalar
vmAffectedVMs = _VmAffectedVMs_Object(
    (1, 3, 6, 1, 2, 1, 236, 1, 11),
    _VmAffectedVMs_Type()
)
vmAffectedVMs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmAffectedVMs.setStatus("current")
_VmConformance_ObjectIdentity = ObjectIdentity
vmConformance = _VmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 2)
)
_VmCompliances_ObjectIdentity = ObjectIdentity
vmCompliances = _VmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 2, 1)
)
_VmGroups_ObjectIdentity = ObjectIdentity
vmGroups = _VmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 236, 2, 2)
)

# Managed Objects groups

vmHypervisorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 1)
)
vmHypervisorGroup.setObjects(
      *(("VM-MIB", "vmHvSoftware"),
        ("VM-MIB", "vmHvVersion"),
        ("VM-MIB", "vmHvObjectID"),
        ("VM-MIB", "vmHvUpTime"),
        ("VM-MIB", "vmNumber"),
        ("VM-MIB", "vmTableLastChange"),
        ("VM-MIB", "vmPerVMNotificationsEnabled"),
        ("VM-MIB", "vmBulkNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    vmHypervisorGroup.setStatus("current")

vmVirtualMachineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 2)
)
vmVirtualMachineGroup.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOSType"),
        ("VM-MIB", "vmAdminState"),
        ("VM-MIB", "vmOperState"),
        ("VM-MIB", "vmAutoStart"),
        ("VM-MIB", "vmPersistent"),
        ("VM-MIB", "vmCurCpuNumber"),
        ("VM-MIB", "vmMinCpuNumber"),
        ("VM-MIB", "vmMaxCpuNumber"),
        ("VM-MIB", "vmMemUnit"),
        ("VM-MIB", "vmCurMem"),
        ("VM-MIB", "vmMinMem"),
        ("VM-MIB", "vmMaxMem"),
        ("VM-MIB", "vmUpTime"),
        ("VM-MIB", "vmCpuTime"))
)
if mibBuilder.loadTexts:
    vmVirtualMachineGroup.setStatus("current")

vmCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 3)
)
vmCpuGroup.setObjects(
    ("VM-MIB", "vmCpuCoreTime")
)
if mibBuilder.loadTexts:
    vmCpuGroup.setStatus("current")

vmCpuAffinityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 4)
)
vmCpuAffinityGroup.setObjects(
    ("VM-MIB", "vmCpuAffinity")
)
if mibBuilder.loadTexts:
    vmCpuAffinityGroup.setStatus("current")

vmStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 5)
)
vmStorageGroup.setObjects(
      *(("VM-MIB", "vmStorageParent"),
        ("VM-MIB", "vmStorageSourceType"),
        ("VM-MIB", "vmStorageSourceTypeString"),
        ("VM-MIB", "vmStorageResourceID"),
        ("VM-MIB", "vmStorageAccess"),
        ("VM-MIB", "vmStorageMediaType"),
        ("VM-MIB", "vmStorageMediaTypeString"),
        ("VM-MIB", "vmStorageSizeUnit"),
        ("VM-MIB", "vmStorageDefinedSize"),
        ("VM-MIB", "vmStorageAllocatedSize"),
        ("VM-MIB", "vmStorageReadIOs"),
        ("VM-MIB", "vmStorageWriteIOs"),
        ("VM-MIB", "vmStorageReadOctets"),
        ("VM-MIB", "vmStorageWriteOctets"),
        ("VM-MIB", "vmStorageReadLatency"),
        ("VM-MIB", "vmStorageWriteLatency"))
)
if mibBuilder.loadTexts:
    vmStorageGroup.setStatus("current")

vmNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 6)
)
vmNetworkGroup.setObjects(
      *(("VM-MIB", "vmNetworkIfIndex"),
        ("VM-MIB", "vmNetworkParent"),
        ("VM-MIB", "vmNetworkModel"),
        ("VM-MIB", "vmNetworkPhysAddress"))
)
if mibBuilder.loadTexts:
    vmNetworkGroup.setStatus("current")

vmBulkNotificationsVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 8)
)
vmBulkNotificationsVariablesGroup.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkNotificationsVariablesGroup.setStatus("current")


# Notification objects

vmRunning = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 1)
)
vmRunning.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmRunning.setStatus(
        "current"
    )

vmShuttingdown = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 2)
)
vmShuttingdown.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmShuttingdown.setStatus(
        "current"
    )

vmShutdown = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 3)
)
vmShutdown.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmShutdown.setStatus(
        "current"
    )

vmPaused = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 4)
)
vmPaused.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmPaused.setStatus(
        "current"
    )

vmSuspending = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 5)
)
vmSuspending.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmSuspending.setStatus(
        "current"
    )

vmSuspended = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 6)
)
vmSuspended.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmSuspended.setStatus(
        "current"
    )

vmResuming = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 7)
)
vmResuming.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmResuming.setStatus(
        "current"
    )

vmMigrating = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 8)
)
vmMigrating.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmMigrating.setStatus(
        "current"
    )

vmCrashed = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 9)
)
vmCrashed.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"))
)
if mibBuilder.loadTexts:
    vmCrashed.setStatus(
        "current"
    )

vmDeleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 10)
)
vmDeleted.setObjects(
      *(("VM-MIB", "vmName"),
        ("VM-MIB", "vmUUID"),
        ("VM-MIB", "vmOperState"),
        ("VM-MIB", "vmPersistent"))
)
if mibBuilder.loadTexts:
    vmDeleted.setStatus(
        "current"
    )

vmBulkRunning = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 11)
)
vmBulkRunning.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkRunning.setStatus(
        "current"
    )

vmBulkShuttingdown = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 12)
)
vmBulkShuttingdown.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkShuttingdown.setStatus(
        "current"
    )

vmBulkShutdown = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 13)
)
vmBulkShutdown.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkShutdown.setStatus(
        "current"
    )

vmBulkPaused = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 14)
)
vmBulkPaused.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkPaused.setStatus(
        "current"
    )

vmBulkSuspending = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 15)
)
vmBulkSuspending.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkSuspending.setStatus(
        "current"
    )

vmBulkSuspended = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 16)
)
vmBulkSuspended.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkSuspended.setStatus(
        "current"
    )

vmBulkResuming = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 17)
)
vmBulkResuming.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkResuming.setStatus(
        "current"
    )

vmBulkMigrating = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 18)
)
vmBulkMigrating.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkMigrating.setStatus(
        "current"
    )

vmBulkCrashed = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 19)
)
vmBulkCrashed.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkCrashed.setStatus(
        "current"
    )

vmBulkDeleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 236, 0, 20)
)
vmBulkDeleted.setObjects(
    ("VM-MIB", "vmAffectedVMs")
)
if mibBuilder.loadTexts:
    vmBulkDeleted.setStatus(
        "current"
    )


# Notifications groups

vmPerVMNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 7)
)
vmPerVMNotificationOptionalGroup.setObjects(
      *(("VM-MIB", "vmRunning"),
        ("VM-MIB", "vmShuttingdown"),
        ("VM-MIB", "vmShutdown"),
        ("VM-MIB", "vmPaused"),
        ("VM-MIB", "vmSuspending"),
        ("VM-MIB", "vmSuspended"),
        ("VM-MIB", "vmResuming"),
        ("VM-MIB", "vmMigrating"),
        ("VM-MIB", "vmCrashed"),
        ("VM-MIB", "vmDeleted"))
)
if mibBuilder.loadTexts:
    vmPerVMNotificationOptionalGroup.setStatus(
        "current"
    )

vmBulkNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 236, 2, 2, 9)
)
vmBulkNotificationOptionalGroup.setObjects(
      *(("VM-MIB", "vmBulkRunning"),
        ("VM-MIB", "vmBulkShuttingdown"),
        ("VM-MIB", "vmBulkShutdown"),
        ("VM-MIB", "vmBulkPaused"),
        ("VM-MIB", "vmBulkSuspending"),
        ("VM-MIB", "vmBulkSuspended"),
        ("VM-MIB", "vmBulkResuming"),
        ("VM-MIB", "vmBulkMigrating"),
        ("VM-MIB", "vmBulkCrashed"),
        ("VM-MIB", "vmBulkDeleted"))
)
if mibBuilder.loadTexts:
    vmBulkNotificationOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmFullCompliances = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 236, 2, 1, 1)
)
vmFullCompliances.setObjects(
      *(("VM-MIB", "vmHypervisorGroup"),
        ("VM-MIB", "vmVirtualMachineGroup"),
        ("VM-MIB", "vmCpuGroup"),
        ("VM-MIB", "vmCpuAffinityGroup"),
        ("VM-MIB", "vmStorageGroup"),
        ("VM-MIB", "vmNetworkGroup"),
        ("VM-MIB", "vmPerVMNotificationOptionalGroup"),
        ("VM-MIB", "vmBulkNotificationsVariablesGroup"),
        ("VM-MIB", "vmBulkNotificationOptionalGroup"))
)
if mibBuilder.loadTexts:
    vmFullCompliances.setStatus(
        "current"
    )

vmReadOnlyCompliances = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 236, 2, 1, 2)
)
vmReadOnlyCompliances.setObjects(
      *(("VM-MIB", "vmHypervisorGroup"),
        ("VM-MIB", "vmVirtualMachineGroup"),
        ("VM-MIB", "vmCpuGroup"),
        ("VM-MIB", "vmCpuAffinityGroup"),
        ("VM-MIB", "vmStorageGroup"),
        ("VM-MIB", "vmNetworkGroup"))
)
if mibBuilder.loadTexts:
    vmReadOnlyCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VM-MIB",
    **{"VirtualMachineIndex": VirtualMachineIndex,
       "VirtualMachineIndexOrZero": VirtualMachineIndexOrZero,
       "VirtualMachineAdminState": VirtualMachineAdminState,
       "VirtualMachineOperState": VirtualMachineOperState,
       "VirtualMachineAutoStart": VirtualMachineAutoStart,
       "VirtualMachinePersistent": VirtualMachinePersistent,
       "VirtualMachineCpuIndex": VirtualMachineCpuIndex,
       "VirtualMachineStorageIndex": VirtualMachineStorageIndex,
       "VirtualMachineStorageSourceType": VirtualMachineStorageSourceType,
       "VirtualMachineStorageAccess": VirtualMachineStorageAccess,
       "VirtualMachineNetworkIndex": VirtualMachineNetworkIndex,
       "VirtualMachineList": VirtualMachineList,
       "vmMIB": vmMIB,
       "vmNotifications": vmNotifications,
       "vmRunning": vmRunning,
       "vmShuttingdown": vmShuttingdown,
       "vmShutdown": vmShutdown,
       "vmPaused": vmPaused,
       "vmSuspending": vmSuspending,
       "vmSuspended": vmSuspended,
       "vmResuming": vmResuming,
       "vmMigrating": vmMigrating,
       "vmCrashed": vmCrashed,
       "vmDeleted": vmDeleted,
       "vmBulkRunning": vmBulkRunning,
       "vmBulkShuttingdown": vmBulkShuttingdown,
       "vmBulkShutdown": vmBulkShutdown,
       "vmBulkPaused": vmBulkPaused,
       "vmBulkSuspending": vmBulkSuspending,
       "vmBulkSuspended": vmBulkSuspended,
       "vmBulkResuming": vmBulkResuming,
       "vmBulkMigrating": vmBulkMigrating,
       "vmBulkCrashed": vmBulkCrashed,
       "vmBulkDeleted": vmBulkDeleted,
       "vmObjects": vmObjects,
       "vmHypervisor": vmHypervisor,
       "vmHvSoftware": vmHvSoftware,
       "vmHvVersion": vmHvVersion,
       "vmHvObjectID": vmHvObjectID,
       "vmHvUpTime": vmHvUpTime,
       "vmNumber": vmNumber,
       "vmTableLastChange": vmTableLastChange,
       "vmTable": vmTable,
       "vmEntry": vmEntry,
       "vmIndex": vmIndex,
       "vmName": vmName,
       "vmUUID": vmUUID,
       "vmOSType": vmOSType,
       "vmAdminState": vmAdminState,
       "vmOperState": vmOperState,
       "vmAutoStart": vmAutoStart,
       "vmPersistent": vmPersistent,
       "vmCurCpuNumber": vmCurCpuNumber,
       "vmMinCpuNumber": vmMinCpuNumber,
       "vmMaxCpuNumber": vmMaxCpuNumber,
       "vmMemUnit": vmMemUnit,
       "vmCurMem": vmCurMem,
       "vmMinMem": vmMinMem,
       "vmMaxMem": vmMaxMem,
       "vmUpTime": vmUpTime,
       "vmCpuTime": vmCpuTime,
       "vmCpuTable": vmCpuTable,
       "vmCpuEntry": vmCpuEntry,
       "vmCpuIndex": vmCpuIndex,
       "vmCpuCoreTime": vmCpuCoreTime,
       "vmCpuAffinityTable": vmCpuAffinityTable,
       "vmCpuAffinityEntry": vmCpuAffinityEntry,
       "vmCpuPhysIndex": vmCpuPhysIndex,
       "vmCpuAffinity": vmCpuAffinity,
       "vmStorageTable": vmStorageTable,
       "vmStorageEntry": vmStorageEntry,
       "vmStorageVmIndex": vmStorageVmIndex,
       "vmStorageIndex": vmStorageIndex,
       "vmStorageParent": vmStorageParent,
       "vmStorageSourceType": vmStorageSourceType,
       "vmStorageSourceTypeString": vmStorageSourceTypeString,
       "vmStorageResourceID": vmStorageResourceID,
       "vmStorageAccess": vmStorageAccess,
       "vmStorageMediaType": vmStorageMediaType,
       "vmStorageMediaTypeString": vmStorageMediaTypeString,
       "vmStorageSizeUnit": vmStorageSizeUnit,
       "vmStorageDefinedSize": vmStorageDefinedSize,
       "vmStorageAllocatedSize": vmStorageAllocatedSize,
       "vmStorageReadIOs": vmStorageReadIOs,
       "vmStorageWriteIOs": vmStorageWriteIOs,
       "vmStorageReadOctets": vmStorageReadOctets,
       "vmStorageWriteOctets": vmStorageWriteOctets,
       "vmStorageReadLatency": vmStorageReadLatency,
       "vmStorageWriteLatency": vmStorageWriteLatency,
       "vmNetworkTable": vmNetworkTable,
       "vmNetworkEntry": vmNetworkEntry,
       "vmNetworkIndex": vmNetworkIndex,
       "vmNetworkIfIndex": vmNetworkIfIndex,
       "vmNetworkParent": vmNetworkParent,
       "vmNetworkModel": vmNetworkModel,
       "vmNetworkPhysAddress": vmNetworkPhysAddress,
       "vmPerVMNotificationsEnabled": vmPerVMNotificationsEnabled,
       "vmBulkNotificationsEnabled": vmBulkNotificationsEnabled,
       "vmAffectedVMs": vmAffectedVMs,
       "vmConformance": vmConformance,
       "vmCompliances": vmCompliances,
       "vmFullCompliances": vmFullCompliances,
       "vmReadOnlyCompliances": vmReadOnlyCompliances,
       "vmGroups": vmGroups,
       "vmHypervisorGroup": vmHypervisorGroup,
       "vmVirtualMachineGroup": vmVirtualMachineGroup,
       "vmCpuGroup": vmCpuGroup,
       "vmCpuAffinityGroup": vmCpuAffinityGroup,
       "vmStorageGroup": vmStorageGroup,
       "vmNetworkGroup": vmNetworkGroup,
       "vmPerVMNotificationOptionalGroup": vmPerVMNotificationOptionalGroup,
       "vmBulkNotificationsVariablesGroup": vmBulkNotificationsVariablesGroup,
       "vmBulkNotificationOptionalGroup": vmBulkNotificationOptionalGroup}
)
