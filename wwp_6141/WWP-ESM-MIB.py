# SNMP MIB module (WWP-ESM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-ESM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:51:13 2025
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

(snmpTrapAddress,
 snmpTrapOID) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "snmpTrapAddress",
    "snmpTrapOID")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpModulesEsm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62)
)
if mibBuilder.loadTexts:
    wwpModulesEsm.setRevisions(
        ("2008-08-20 00:00",
         "2011-04-01 00:00",
         "2011-06-01 00:00",
         "2011-08-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpESM_ObjectIdentity = ObjectIdentity
wwpESM = _WwpESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1)
)
_WwpESMSystem_ObjectIdentity = ObjectIdentity
wwpESMSystem = _WwpESMSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1)
)


class _WwpESMVersion_Type(DisplayString):
    """Custom type wwpESMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpESMVersion_Type.__name__ = "DisplayString"
_WwpESMVersion_Object = MibScalar
wwpESMVersion = _WwpESMVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 1),
    _WwpESMVersion_Type()
)
wwpESMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMVersion.setStatus("current")


class _WwpESMHost_Type(DisplayString):
    """Custom type wwpESMHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpESMHost_Type.__name__ = "DisplayString"
_WwpESMHost_Object = MibScalar
wwpESMHost = _WwpESMHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 2),
    _WwpESMHost_Type()
)
wwpESMHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMHost.setStatus("current")
_WwpESMIpAddress_Type = IpAddress
_WwpESMIpAddress_Object = MibScalar
wwpESMIpAddress = _WwpESMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 3),
    _WwpESMIpAddress_Type()
)
wwpESMIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMIpAddress.setStatus("current")
_WwpESMTotalMemory_Type = Integer32
_WwpESMTotalMemory_Object = MibScalar
wwpESMTotalMemory = _WwpESMTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 4),
    _WwpESMTotalMemory_Type()
)
wwpESMTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMTotalMemory.setStatus("current")
_WwpESMFreeMemory_Type = Integer32
_WwpESMFreeMemory_Object = MibScalar
wwpESMFreeMemory = _WwpESMFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 5),
    _WwpESMFreeMemory_Type()
)
wwpESMFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMFreeMemory.setStatus("current")
_WwpESMStartTime_Type = DateAndTime
_WwpESMStartTime_Object = MibScalar
wwpESMStartTime = _WwpESMStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 6),
    _WwpESMStartTime_Type()
)
wwpESMStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMStartTime.setStatus("current")
_WwpESMUpTime_Type = TimeTicks
_WwpESMUpTime_Object = MibScalar
wwpESMUpTime = _WwpESMUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 7),
    _WwpESMUpTime_Type()
)
wwpESMUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMUpTime.setStatus("current")


class _WwpESMShutdown_Type(DisplayString):
    """Custom type wwpESMShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpESMShutdown_Type.__name__ = "DisplayString"
_WwpESMShutdown_Object = MibScalar
wwpESMShutdown = _WwpESMShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 8),
    _WwpESMShutdown_Type()
)
wwpESMShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpESMShutdown.setStatus("current")
_WwpESMPorts_ObjectIdentity = ObjectIdentity
wwpESMPorts = _WwpESMPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9)
)
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 1),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_EsmSocketPort_Type = Integer32
_EsmSocketPort_Object = MibScalar
esmSocketPort = _EsmSocketPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 2),
    _EsmSocketPort_Type()
)
esmSocketPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmSocketPort.setStatus("current")
_RmiRegistryPort_Type = Integer32
_RmiRegistryPort_Object = MibScalar
rmiRegistryPort = _RmiRegistryPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 3),
    _RmiRegistryPort_Type()
)
rmiRegistryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmiRegistryPort.setStatus("current")
_TrapPortTable_Object = MibTable
trapPortTable = _TrapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    trapPortTable.setStatus("current")
_TrapPortEntry_Object = MibTableRow
trapPortEntry = _TrapPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 4, 1)
)
trapPortEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "seqNum"),
)
if mibBuilder.loadTexts:
    trapPortEntry.setStatus("current")
_SeqNum_Type = Integer32
_SeqNum_Object = MibTableColumn
seqNum = _SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 4, 1, 1),
    _SeqNum_Type()
)
seqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seqNum.setStatus("current")
_Port_Type = Integer32
_Port_Object = MibTableColumn
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 9, 4, 1, 2),
    _Port_Type()
)
port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port.setStatus("current")
_WwpESMSchedulerTable_Object = MibTable
wwpESMSchedulerTable = _WwpESMSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpESMSchedulerTable.setStatus("optional")
_WwpESMschedulerEntry_Object = MibTableRow
wwpESMschedulerEntry = _WwpESMschedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1)
)
wwpESMschedulerEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "wwpESMSchedulerIndex"),
)
if mibBuilder.loadTexts:
    wwpESMschedulerEntry.setStatus("current")
_WwpESMSchedulerIndex_Type = Integer32
_WwpESMSchedulerIndex_Object = MibTableColumn
wwpESMSchedulerIndex = _WwpESMSchedulerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 1),
    _WwpESMSchedulerIndex_Type()
)
wwpESMSchedulerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerIndex.setStatus("current")


class _WwpESMSchedulerDesc_Type(DisplayString):
    """Custom type wwpESMSchedulerDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpESMSchedulerDesc_Type.__name__ = "DisplayString"
_WwpESMSchedulerDesc_Object = MibTableColumn
wwpESMSchedulerDesc = _WwpESMSchedulerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 2),
    _WwpESMSchedulerDesc_Type()
)
wwpESMSchedulerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerDesc.setStatus("current")
_WwpESMSchedulerNumTasks_Type = Integer32
_WwpESMSchedulerNumTasks_Object = MibTableColumn
wwpESMSchedulerNumTasks = _WwpESMSchedulerNumTasks_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 3),
    _WwpESMSchedulerNumTasks_Type()
)
wwpESMSchedulerNumTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerNumTasks.setStatus("current")
_WwpESMSchedulerNumThreads_Type = Integer32
_WwpESMSchedulerNumThreads_Object = MibTableColumn
wwpESMSchedulerNumThreads = _WwpESMSchedulerNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 4),
    _WwpESMSchedulerNumThreads_Type()
)
wwpESMSchedulerNumThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerNumThreads.setStatus("current")
_WwpESMSchedulerActiveThreads_Type = Integer32
_WwpESMSchedulerActiveThreads_Object = MibTableColumn
wwpESMSchedulerActiveThreads = _WwpESMSchedulerActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 5),
    _WwpESMSchedulerActiveThreads_Type()
)
wwpESMSchedulerActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerActiveThreads.setStatus("current")
_WwpESMSchedulerIdleThreads_Type = Integer32
_WwpESMSchedulerIdleThreads_Object = MibTableColumn
wwpESMSchedulerIdleThreads = _WwpESMSchedulerIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 1, 10, 1, 6),
    _WwpESMSchedulerIdleThreads_Type()
)
wwpESMSchedulerIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMSchedulerIdleThreads.setStatus("current")
_WwpESMTopoMib_ObjectIdentity = ObjectIdentity
wwpESMTopoMib = _WwpESMTopoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2)
)
_WwpESMNumObjects_Type = Integer32
_WwpESMNumObjects_Object = MibScalar
wwpESMNumObjects = _WwpESMNumObjects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 1),
    _WwpESMNumObjects_Type()
)
wwpESMNumObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumObjects.setStatus("current")
_WwpESMNumNetworks_Type = Integer32
_WwpESMNumNetworks_Object = MibScalar
wwpESMNumNetworks = _WwpESMNumNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 2),
    _WwpESMNumNetworks_Type()
)
wwpESMNumNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumNetworks.setStatus("current")
_WwpESMNumNodes_Type = Integer32
_WwpESMNumNodes_Object = MibScalar
wwpESMNumNodes = _WwpESMNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 3),
    _WwpESMNumNodes_Type()
)
wwpESMNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumNodes.setStatus("current")
_WwpESMNumInterfaces_Type = Integer32
_WwpESMNumInterfaces_Object = MibScalar
wwpESMNumInterfaces = _WwpESMNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 4),
    _WwpESMNumInterfaces_Type()
)
wwpESMNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumInterfaces.setStatus("current")


class _MoUserPropNames_Type(DisplayString):
    """Custom type moUserPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoUserPropNames_Type.__name__ = "DisplayString"
_MoUserPropNames_Object = MibScalar
moUserPropNames = _MoUserPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 5),
    _MoUserPropNames_Type()
)
moUserPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moUserPropNames.setStatus("current")
_MoTable_Object = MibTable
moTable = _MoTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6)
)
if mibBuilder.loadTexts:
    moTable.setStatus("current")
_MoEntry_Object = MibTableRow
moEntry = _MoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1)
)
moEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    moEntry.setStatus("current")


class _MoNameIndex_Type(DisplayString):
    """Custom type moNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoNameIndex_Type.__name__ = "DisplayString"
_MoNameIndex_Object = MibTableColumn
moNameIndex = _MoNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 1),
    _MoNameIndex_Type()
)
moNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moNameIndex.setStatus("current")


class _MoOwnerName_Type(DisplayString):
    """Custom type moOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoOwnerName_Type.__name__ = "DisplayString"
_MoOwnerName_Object = MibTableColumn
moOwnerName = _MoOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 2),
    _MoOwnerName_Type()
)
moOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moOwnerName.setStatus("current")


class _MoType_Type(DisplayString):
    """Custom type moType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoType_Type.__name__ = "DisplayString"
_MoType_Object = MibTableColumn
moType = _MoType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 3),
    _MoType_Type()
)
moType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moType.setStatus("current")


class _MoFailureCount_Type(Integer32):
    """Custom type moFailureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MoFailureCount_Type.__name__ = "Integer32"
_MoFailureCount_Object = MibTableColumn
moFailureCount = _MoFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 4),
    _MoFailureCount_Type()
)
moFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFailureCount.setStatus("current")


class _MoFailureThreshold_Type(Integer32):
    """Custom type moFailureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MoFailureThreshold_Type.__name__ = "Integer32"
_MoFailureThreshold_Object = MibTableColumn
moFailureThreshold = _MoFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 5),
    _MoFailureThreshold_Type()
)
moFailureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFailureThreshold.setStatus("current")


class _MoManaged_Type(TruthValue):
    """Custom type moManaged based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MoManaged_Type.__name__ = "TruthValue"
_MoManaged_Object = MibTableColumn
moManaged = _MoManaged_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 6),
    _MoManaged_Type()
)
moManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moManaged.setStatus("current")
_MoStatus_Type = Integer32
_MoStatus_Object = MibTableColumn
moStatus = _MoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 7),
    _MoStatus_Type()
)
moStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moStatus.setStatus("current")


class _MoStatusChangeTime_Type(Gauge32):
    """Custom type moStatusChangeTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MoStatusChangeTime_Type.__name__ = "Gauge32"
_MoStatusChangeTime_Object = MibTableColumn
moStatusChangeTime = _MoStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 8),
    _MoStatusChangeTime_Type()
)
moStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moStatusChangeTime.setStatus("current")


class _MoStatusUpdateTime_Type(Gauge32):
    """Custom type moStatusUpdateTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MoStatusUpdateTime_Type.__name__ = "Gauge32"
_MoStatusUpdateTime_Object = MibTableColumn
moStatusUpdateTime = _MoStatusUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 9),
    _MoStatusUpdateTime_Type()
)
moStatusUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moStatusUpdateTime.setStatus("current")
_MoPollInterval_Type = TimeTicks
_MoPollInterval_Object = MibTableColumn
moPollInterval = _MoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 10),
    _MoPollInterval_Type()
)
moPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moPollInterval.setStatus("current")


class _MoUserProperties_Type(DisplayString):
    """Custom type moUserProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoUserProperties_Type.__name__ = "DisplayString"
_MoUserProperties_Object = MibTableColumn
moUserProperties = _MoUserProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 11),
    _MoUserProperties_Type()
)
moUserProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moUserProperties.setStatus("current")


class _MoDerivedProperties_Type(DisplayString):
    """Custom type moDerivedProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoDerivedProperties_Type.__name__ = "DisplayString"
_MoDerivedProperties_Object = MibTableColumn
moDerivedProperties = _MoDerivedProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 12),
    _MoDerivedProperties_Type()
)
moDerivedProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDerivedProperties.setStatus("current")
_InheritingOid1_Type = ObjectIdentifier
_InheritingOid1_Object = MibTableColumn
inheritingOid1 = _InheritingOid1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 13),
    _InheritingOid1_Type()
)
inheritingOid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid1.setStatus("current")
_InheritingTableName1_Type = DisplayString
_InheritingTableName1_Object = MibTableColumn
inheritingTableName1 = _InheritingTableName1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 6, 1, 14),
    _InheritingTableName1_Type()
)
inheritingTableName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName1.setStatus("current")
_TopoObjTable_Object = MibTable
topoObjTable = _TopoObjTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7)
)
if mibBuilder.loadTexts:
    topoObjTable.setStatus("current")
_TopoObjEntry_Object = MibTableRow
topoObjEntry = _TopoObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1)
)
topoObjEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    topoObjEntry.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_Netmask_Type = IpAddress
_Netmask_Object = MibTableColumn
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 2),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_MoCommunity_Type = DisplayString
_MoCommunity_Object = MibTableColumn
moCommunity = _MoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 3),
    _MoCommunity_Type()
)
moCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCommunity.setStatus("current")
_MoWriteCommunity_Type = DisplayString
_MoWriteCommunity_Object = MibTableColumn
moWriteCommunity = _MoWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 4),
    _MoWriteCommunity_Type()
)
moWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moWriteCommunity.setStatus("current")
_SnmpPort_Type = Integer32
_SnmpPort_Object = MibTableColumn
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 5),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPort.setStatus("current")
_IsDHCP_Type = DisplayString
_IsDHCP_Object = MibTableColumn
isDHCP = _IsDHCP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 6),
    _IsDHCP_Type()
)
isDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDHCP.setStatus("current")
_BaseMibs_Type = DisplayString
_BaseMibs_Object = MibTableColumn
baseMibs = _BaseMibs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 7),
    _BaseMibs_Type()
)
baseMibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseMibs.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibTableColumn
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 8),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 9),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_ContextName_Type = DisplayString
_ContextName_Object = MibTableColumn
contextName = _ContextName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 10),
    _ContextName_Type()
)
contextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextName.setStatus("current")
_InheritingOid2_Type = ObjectIdentifier
_InheritingOid2_Object = MibTableColumn
inheritingOid2 = _InheritingOid2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 11),
    _InheritingOid2_Type()
)
inheritingOid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid2.setStatus("current")
_InheritingTableName2_Type = DisplayString
_InheritingTableName2_Object = MibTableColumn
inheritingTableName2 = _InheritingTableName2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 7, 1, 12),
    _InheritingTableName2_Type()
)
inheritingTableName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName2.setStatus("current")
_NetworkTable_Object = MibTable
networkTable = _NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8)
)
if mibBuilder.loadTexts:
    networkTable.setStatus("current")
_NetworkEntry_Object = MibTableRow
networkEntry = _NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8, 1)
)
networkEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    networkEntry.setStatus("current")
_Discover_Type = DisplayString
_Discover_Object = MibTableColumn
discover = _Discover_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8, 1, 1),
    _Discover_Type()
)
discover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discover.setStatus("current")
_DiscoverStatus_Type = Integer32
_DiscoverStatus_Object = MibTableColumn
discoverStatus = _DiscoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8, 1, 2),
    _DiscoverStatus_Type()
)
discoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discoverStatus.setStatus("current")
_InheritingOid3_Type = ObjectIdentifier
_InheritingOid3_Object = MibTableColumn
inheritingOid3 = _InheritingOid3_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8, 1, 3),
    _InheritingOid3_Type()
)
inheritingOid3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid3.setStatus("current")
_InheritingTableName3_Type = DisplayString
_InheritingTableName3_Object = MibTableColumn
inheritingTableName3 = _InheritingTableName3_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 8, 1, 4),
    _InheritingTableName3_Type()
)
inheritingTableName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName3.setStatus("current")
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 9)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("current")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 9, 1)
)
nodeEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("current")
_IsRouter_Type = DisplayString
_IsRouter_Object = MibTableColumn
isRouter = _IsRouter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 9, 1, 1),
    _IsRouter_Type()
)
isRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isRouter.setStatus("current")
_InheritingOid4_Type = ObjectIdentifier
_InheritingOid4_Object = MibTableColumn
inheritingOid4 = _InheritingOid4_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 9, 1, 2),
    _InheritingOid4_Type()
)
inheritingOid4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid4.setStatus("current")
_InheritingTableName4_Type = DisplayString
_InheritingTableName4_Object = MibTableColumn
inheritingTableName4 = _InheritingTableName4_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 9, 1, 3),
    _InheritingTableName4_Type()
)
inheritingTableName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName4.setStatus("current")
_IpAddressTable_Object = MibTable
ipAddressTable = _IpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10)
)
if mibBuilder.loadTexts:
    ipAddressTable.setStatus("current")
_IpAddressEntry_Object = MibTableRow
ipAddressEntry = _IpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10, 1)
)
ipAddressEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    ipAddressEntry.setStatus("current")
_ParentNode_Type = DisplayString
_ParentNode_Object = MibTableColumn
parentNode = _ParentNode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10, 1, 1),
    _ParentNode_Type()
)
parentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentNode.setStatus("current")
_ParentNet_Type = IpAddress
_ParentNet_Object = MibTableColumn
parentNet = _ParentNet_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10, 1, 2),
    _ParentNet_Type()
)
parentNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentNet.setStatus("current")
_InheritingOid5_Type = ObjectIdentifier
_InheritingOid5_Object = MibTableColumn
inheritingOid5 = _InheritingOid5_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10, 1, 3),
    _InheritingOid5_Type()
)
inheritingOid5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid5.setStatus("current")
_InheritingTableName5_Type = DisplayString
_InheritingTableName5_Object = MibTableColumn
inheritingTableName5 = _InheritingTableName5_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 10, 1, 4),
    _InheritingTableName5_Type()
)
inheritingTableName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName5.setStatus("current")
_SnmpNodeTable_Object = MibTable
snmpNodeTable = _SnmpNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11)
)
if mibBuilder.loadTexts:
    snmpNodeTable.setStatus("current")
_SnmpNodeEntry_Object = MibTableRow
snmpNodeEntry = _SnmpNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1)
)
snmpNodeEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    snmpNodeEntry.setStatus("current")
_HostNetMask_Type = IpAddress
_HostNetMask_Object = MibTableColumn
hostNetMask = _HostNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 1),
    _HostNetMask_Type()
)
hostNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostNetMask.setStatus("current")
_SysDesc_Type = DisplayString
_SysDesc_Object = MibTableColumn
sysDesc = _SysDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 2),
    _SysDesc_Type()
)
sysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDesc.setStatus("current")
_SysName_Type = DisplayString
_SysName_Object = MibTableColumn
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 3),
    _SysName_Type()
)
sysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysOid_Type = ObjectIdentifier
_SysOid_Object = MibTableColumn
sysOid = _SysOid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 4),
    _SysOid_Type()
)
sysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOid.setStatus("current")
_InheritingOid6_Type = ObjectIdentifier
_InheritingOid6_Object = MibTableColumn
inheritingOid6 = _InheritingOid6_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 5),
    _InheritingOid6_Type()
)
inheritingOid6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid6.setStatus("current")
_InheritingTableName6_Type = DisplayString
_InheritingTableName6_Object = MibTableColumn
inheritingTableName6 = _InheritingTableName6_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 11, 1, 6),
    _InheritingTableName6_Type()
)
inheritingTableName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName6.setStatus("current")
_SnmpInterfaceTable_Object = MibTable
snmpInterfaceTable = _SnmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12)
)
if mibBuilder.loadTexts:
    snmpInterfaceTable.setStatus("current")
_SnmpInterfaceEntry_Object = MibTableRow
snmpInterfaceEntry = _SnmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1)
)
snmpInterfaceEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "moNameIndex"),
    (0, "WWP-ESM-MIB", "moOwnerName"),
)
if mibBuilder.loadTexts:
    snmpInterfaceEntry.setStatus("current")
_HostnetMask_Type = IpAddress
_HostnetMask_Object = MibTableColumn
hostnetMask = _HostnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 1),
    _HostnetMask_Type()
)
hostnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostnetMask.setStatus("current")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 2),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_PhysMedia_Type = DisplayString
_PhysMedia_Object = MibTableColumn
physMedia = _PhysMedia_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 3),
    _PhysMedia_Type()
)
physMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physMedia.setStatus("current")
_PhysAddress_Type = DisplayString
_PhysAddress_Object = MibTableColumn
physAddress = _PhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 4),
    _PhysAddress_Type()
)
physAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physAddress.setStatus("current")
_IfSpeed_Type = Integer32
_IfSpeed_Object = MibTableColumn
ifSpeed = _IfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 5),
    _IfSpeed_Type()
)
ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpeed.setStatus("current")
_IfDesc_Type = DisplayString
_IfDesc_Object = MibTableColumn
ifDesc = _IfDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 6),
    _IfDesc_Type()
)
ifDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDesc.setStatus("current")
_SysOID_Type = ObjectIdentifier
_SysOID_Object = MibTableColumn
sysOID = _SysOID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 7),
    _SysOID_Type()
)
sysOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOID.setStatus("current")
_InheritingOid7_Type = ObjectIdentifier
_InheritingOid7_Object = MibTableColumn
inheritingOid7 = _InheritingOid7_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 8),
    _InheritingOid7_Type()
)
inheritingOid7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingOid7.setStatus("current")
_InheritingTableName7_Type = DisplayString
_InheritingTableName7_Object = MibTableColumn
inheritingTableName7 = _InheritingTableName7_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 12, 1, 9),
    _InheritingTableName7_Type()
)
inheritingTableName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inheritingTableName7.setStatus("current")
_MoDerivedPropNameTable_Object = MibTable
moDerivedPropNameTable = _MoDerivedPropNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13)
)
if mibBuilder.loadTexts:
    moDerivedPropNameTable.setStatus("current")
_MoDerivedPropNameEntry_Object = MibTableRow
moDerivedPropNameEntry = _MoDerivedPropNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1)
)
moDerivedPropNameEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "indexNum"),
)
if mibBuilder.loadTexts:
    moDerivedPropNameEntry.setStatus("current")


class _IndexNum_Type(Integer32):
    """Custom type indexNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_IndexNum_Type.__name__ = "Integer32"
_IndexNum_Object = MibTableColumn
indexNum = _IndexNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1, 1),
    _IndexNum_Type()
)
indexNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    indexNum.setStatus("current")


class _ObjClassName_Type(DisplayString):
    """Custom type objClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ObjClassName_Type.__name__ = "DisplayString"
_ObjClassName_Object = MibTableColumn
objClassName = _ObjClassName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1, 2),
    _ObjClassName_Type()
)
objClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    objClassName.setStatus("current")


class _DerivedPropNames_Type(DisplayString):
    """Custom type derivedPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DerivedPropNames_Type.__name__ = "DisplayString"
_DerivedPropNames_Object = MibTableColumn
derivedPropNames = _DerivedPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1, 3),
    _DerivedPropNames_Type()
)
derivedPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivedPropNames.setStatus("current")
_TableOid_Type = ObjectIdentifier
_TableOid_Object = MibTableColumn
tableOid = _TableOid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1, 4),
    _TableOid_Type()
)
tableOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tableOid.setStatus("current")


class _TableName_Type(DisplayString):
    """Custom type tableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TableName_Type.__name__ = "DisplayString"
_TableName_Object = MibTableColumn
tableName = _TableName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 13, 1, 5),
    _TableName_Type()
)
tableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tableName.setStatus("current")
_MoNotificationMib_ObjectIdentity = ObjectIdentity
moNotificationMib = _MoNotificationMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14)
)


class _MoExtraPropNames_Type(DisplayString):
    """Custom type moExtraPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoExtraPropNames_Type.__name__ = "DisplayString"
_MoExtraPropNames_Object = MibScalar
moExtraPropNames = _MoExtraPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 1),
    _MoExtraPropNames_Type()
)
moExtraPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moExtraPropNames.setStatus("current")
_MoNotiPrefix_ObjectIdentity = ObjectIdentity
moNotiPrefix = _MoNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 2)
)
_MoNotifications_ObjectIdentity = ObjectIdentity
moNotifications = _MoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 2, 0)
)
_MoNotiVarbinds_ObjectIdentity = ObjectIdentity
moNotiVarbinds = _MoNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3)
)


class _MoName_Type(DisplayString):
    """Custom type moName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoName_Type.__name__ = "DisplayString"
_MoName_Object = MibScalar
moName = _MoName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 1),
    _MoName_Type()
)
moName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moName.setStatus("current")
_MoownerName_Type = DisplayString
_MoownerName_Object = MibScalar
moownerName = _MoownerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 2),
    _MoownerName_Type()
)
moownerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moownerName.setStatus("current")


class _MoNodeType_Type(DisplayString):
    """Custom type moNodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoNodeType_Type.__name__ = "DisplayString"
_MoNodeType_Object = MibScalar
moNodeType = _MoNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 3),
    _MoNodeType_Type()
)
moNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moNodeType.setStatus("current")


class _MoEnrolTime_Type(Gauge32):
    """Custom type moEnrolTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MoEnrolTime_Type.__name__ = "Gauge32"
_MoEnrolTime_Object = MibScalar
moEnrolTime = _MoEnrolTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 4),
    _MoEnrolTime_Type()
)
moEnrolTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moEnrolTime.setStatus("current")


class _MoDeEnrolTime_Type(Gauge32):
    """Custom type moDeEnrolTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MoDeEnrolTime_Type.__name__ = "Gauge32"
_MoDeEnrolTime_Object = MibScalar
moDeEnrolTime = _MoDeEnrolTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 5),
    _MoDeEnrolTime_Type()
)
moDeEnrolTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDeEnrolTime.setStatus("current")


class _MoDataChangeTime_Type(Gauge32):
    """Custom type moDataChangeTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MoDataChangeTime_Type.__name__ = "Gauge32"
_MoDataChangeTime_Object = MibScalar
moDataChangeTime = _MoDataChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 6),
    _MoDataChangeTime_Type()
)
moDataChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDataChangeTime.setStatus("current")


class _MoExtraProperties_Type(DisplayString):
    """Custom type moExtraProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoExtraProperties_Type.__name__ = "DisplayString"
_MoExtraProperties_Object = MibScalar
moExtraProperties = _MoExtraProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 7),
    _MoExtraProperties_Type()
)
moExtraProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moExtraProperties.setStatus("current")
_MoIpAddress_Type = IpAddress
_MoIpAddress_Object = MibScalar
moIpAddress = _MoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 3, 8),
    _MoIpAddress_Type()
)
moIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moIpAddress.setStatus("current")
_WwpESMFaultMib_ObjectIdentity = ObjectIdentity
wwpESMFaultMib = _WwpESMFaultMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3)
)
_WwpESMNumEvents_Type = Integer32
_WwpESMNumEvents_Object = MibScalar
wwpESMNumEvents = _WwpESMNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 1),
    _WwpESMNumEvents_Type()
)
wwpESMNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumEvents.setStatus("current")
_WwpESMNumAlerts_Type = Integer32
_WwpESMNumAlerts_Object = MibScalar
wwpESMNumAlerts = _WwpESMNumAlerts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 2),
    _WwpESMNumAlerts_Type()
)
wwpESMNumAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMNumAlerts.setStatus("current")
_WwpESMEventsInBuffer_Type = Integer32
_WwpESMEventsInBuffer_Object = MibScalar
wwpESMEventsInBuffer = _WwpESMEventsInBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 3),
    _WwpESMEventsInBuffer_Type()
)
wwpESMEventsInBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMEventsInBuffer.setStatus("current")
_WwpESMAlertsInBuffer_Type = Integer32
_WwpESMAlertsInBuffer_Object = MibScalar
wwpESMAlertsInBuffer = _WwpESMAlertsInBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 4),
    _WwpESMAlertsInBuffer_Type()
)
wwpESMAlertsInBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpESMAlertsInBuffer.setStatus("current")


class _AlertUserPropNames_Type(DisplayString):
    """Custom type alertUserPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertUserPropNames_Type.__name__ = "DisplayString"
_AlertUserPropNames_Object = MibScalar
alertUserPropNames = _AlertUserPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 5),
    _AlertUserPropNames_Type()
)
alertUserPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertUserPropNames.setStatus("current")


class _EventUserPropNames_Type(DisplayString):
    """Custom type eventUserPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventUserPropNames_Type.__name__ = "DisplayString"
_EventUserPropNames_Object = MibScalar
eventUserPropNames = _EventUserPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 6),
    _EventUserPropNames_Type()
)
eventUserPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventUserPropNames.setStatus("current")
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("deprecated")
_AlertEntry_Object = MibTableRow
alertEntry = _AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1)
)
alertEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "alertEntity"),
    (0, "WWP-ESM-MIB", "alertOwnerName"),
)
if mibBuilder.loadTexts:
    alertEntry.setStatus("deprecated")


class _AlertEntity_Type(DisplayString):
    """Custom type alertEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertEntity_Type.__name__ = "DisplayString"
_AlertEntity_Object = MibTableColumn
alertEntity = _AlertEntity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 1),
    _AlertEntity_Type()
)
alertEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertEntity.setStatus("deprecated")


class _AlertOwnerName_Type(DisplayString):
    """Custom type alertOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertOwnerName_Type.__name__ = "DisplayString"
_AlertOwnerName_Object = MibTableColumn
alertOwnerName = _AlertOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 2),
    _AlertOwnerName_Type()
)
alertOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertOwnerName.setStatus("deprecated")
_AlertCreateTime_Type = Gauge32
_AlertCreateTime_Object = MibTableColumn
alertCreateTime = _AlertCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 3),
    _AlertCreateTime_Type()
)
alertCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCreateTime.setStatus("deprecated")


class _AlertSource_Type(DisplayString):
    """Custom type alertSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertSource_Type.__name__ = "DisplayString"
_AlertSource_Object = MibTableColumn
alertSource = _AlertSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 4),
    _AlertSource_Type()
)
alertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSource.setStatus("deprecated")
_AlertModTime_Type = Gauge32
_AlertModTime_Object = MibTableColumn
alertModTime = _AlertModTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 5),
    _AlertModTime_Type()
)
alertModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertModTime.setStatus("deprecated")
_AlertSeverity_Type = Integer32
_AlertSeverity_Object = MibTableColumn
alertSeverity = _AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 6),
    _AlertSeverity_Type()
)
alertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSeverity.setStatus("deprecated")
_AlertPreviousSeverity_Type = Integer32
_AlertPreviousSeverity_Object = MibTableColumn
alertPreviousSeverity = _AlertPreviousSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 7),
    _AlertPreviousSeverity_Type()
)
alertPreviousSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertPreviousSeverity.setStatus("deprecated")


class _AlertCategory_Type(DisplayString):
    """Custom type alertCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertCategory_Type.__name__ = "DisplayString"
_AlertCategory_Object = MibTableColumn
alertCategory = _AlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 8),
    _AlertCategory_Type()
)
alertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCategory.setStatus("deprecated")


class _AlertUserProperties_Type(DisplayString):
    """Custom type alertUserProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertUserProperties_Type.__name__ = "DisplayString"
_AlertUserProperties_Object = MibTableColumn
alertUserProperties = _AlertUserProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 7, 1, 9),
    _AlertUserProperties_Type()
)
alertUserProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUserProperties.setStatus("deprecated")
_AlertNotificationMib_ObjectIdentity = ObjectIdentity
alertNotificationMib = _AlertNotificationMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8)
)


class _AlertExtraPropNames_Type(DisplayString):
    """Custom type alertExtraPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertExtraPropNames_Type.__name__ = "DisplayString"
_AlertExtraPropNames_Object = MibScalar
alertExtraPropNames = _AlertExtraPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 1),
    _AlertExtraPropNames_Type()
)
alertExtraPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertExtraPropNames.setStatus("current")
_AlertNotiPrefix_ObjectIdentity = ObjectIdentity
alertNotiPrefix = _AlertNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2)
)
_AlertNotifications_ObjectIdentity = ObjectIdentity
alertNotifications = _AlertNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0)
)
_AlertNotiVarbinds_ObjectIdentity = ObjectIdentity
alertNotiVarbinds = _AlertNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3)
)


class _NotiAlertEntity_Type(DisplayString):
    """Custom type notiAlertEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertEntity_Type.__name__ = "DisplayString"
_NotiAlertEntity_Object = MibScalar
notiAlertEntity = _NotiAlertEntity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 1),
    _NotiAlertEntity_Type()
)
notiAlertEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertEntity.setStatus("current")


class _NotiAlertOwnerName_Type(DisplayString):
    """Custom type notiAlertOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertOwnerName_Type.__name__ = "DisplayString"
_NotiAlertOwnerName_Object = MibScalar
notiAlertOwnerName = _NotiAlertOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 2),
    _NotiAlertOwnerName_Type()
)
notiAlertOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertOwnerName.setStatus("current")


class _NotiAlertDescription_Type(DisplayString):
    """Custom type notiAlertDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertDescription_Type.__name__ = "DisplayString"
_NotiAlertDescription_Object = MibScalar
notiAlertDescription = _NotiAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 3),
    _NotiAlertDescription_Type()
)
notiAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertDescription.setStatus("current")
_NotiAlertTimeStamp_Type = TimeTicks
_NotiAlertTimeStamp_Object = MibScalar
notiAlertTimeStamp = _NotiAlertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 4),
    _NotiAlertTimeStamp_Type()
)
notiAlertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertTimeStamp.setStatus("current")
_NotiAlertNotificationId_Type = Integer32
_NotiAlertNotificationId_Object = MibScalar
notiAlertNotificationId = _NotiAlertNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 5),
    _NotiAlertNotificationId_Type()
)
notiAlertNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertNotificationId.setStatus("current")


class _NotiAlertCategory_Type(DisplayString):
    """Custom type notiAlertCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertCategory_Type.__name__ = "DisplayString"
_NotiAlertCategory_Object = MibScalar
notiAlertCategory = _NotiAlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 6),
    _NotiAlertCategory_Type()
)
notiAlertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertCategory.setStatus("current")


class _NotiAlertExtraProperties_Type(DisplayString):
    """Custom type notiAlertExtraProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertExtraProperties_Type.__name__ = "DisplayString"
_NotiAlertExtraProperties_Object = MibScalar
notiAlertExtraProperties = _NotiAlertExtraProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 7),
    _NotiAlertExtraProperties_Type()
)
notiAlertExtraProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertExtraProperties.setStatus("current")
_NotiAlertIpAddress_Type = IpAddress
_NotiAlertIpAddress_Object = MibScalar
notiAlertIpAddress = _NotiAlertIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 8),
    _NotiAlertIpAddress_Type()
)
notiAlertIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertIpAddress.setStatus("current")
_NotiAlertEmsTime_Type = TimeTicks
_NotiAlertEmsTime_Object = MibScalar
notiAlertEmsTime = _NotiAlertEmsTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 9),
    _NotiAlertEmsTime_Type()
)
notiAlertEmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertEmsTime.setStatus("current")
_NotiAlertNeTime_Type = TimeTicks
_NotiAlertNeTime_Object = MibScalar
notiAlertNeTime = _NotiAlertNeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 10),
    _NotiAlertNeTime_Type()
)
notiAlertNeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertNeTime.setStatus("current")


class _NotiAlertEmsName_Type(DisplayString):
    """Custom type notiAlertEmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertEmsName_Type.__name__ = "DisplayString"
_NotiAlertEmsName_Object = MibScalar
notiAlertEmsName = _NotiAlertEmsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 11),
    _NotiAlertEmsName_Type()
)
notiAlertEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertEmsName.setStatus("current")


class _NotiAlertNeNodeId_Type(DisplayString):
    """Custom type notiAlertNeNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertNeNodeId_Type.__name__ = "DisplayString"
_NotiAlertNeNodeId_Object = MibScalar
notiAlertNeNodeId = _NotiAlertNeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 12),
    _NotiAlertNeNodeId_Type()
)
notiAlertNeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertNeNodeId.setStatus("current")


class _NotiAlertObjectType_Type(DisplayString):
    """Custom type notiAlertObjectType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertObjectType_Type.__name__ = "DisplayString"
_NotiAlertObjectType_Object = MibScalar
notiAlertObjectType = _NotiAlertObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 13),
    _NotiAlertObjectType_Type()
)
notiAlertObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertObjectType.setStatus("current")


class _NotiAlertObjectName_Type(DisplayString):
    """Custom type notiAlertObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertObjectName_Type.__name__ = "DisplayString"
_NotiAlertObjectName_Object = MibScalar
notiAlertObjectName = _NotiAlertObjectName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 14),
    _NotiAlertObjectName_Type()
)
notiAlertObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertObjectName.setStatus("current")


class _NotiAlertSeverity_Type(DisplayString):
    """Custom type notiAlertSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NotiAlertSeverity_Type.__name__ = "DisplayString"
_NotiAlertSeverity_Object = MibScalar
notiAlertSeverity = _NotiAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 15),
    _NotiAlertSeverity_Type()
)
notiAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertSeverity.setStatus("current")


class _NotiAlertServiceAffecting_Type(DisplayString):
    """Custom type notiAlertServiceAffecting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NotiAlertServiceAffecting_Type.__name__ = "DisplayString"
_NotiAlertServiceAffecting_Object = MibScalar
notiAlertServiceAffecting = _NotiAlertServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 16),
    _NotiAlertServiceAffecting_Type()
)
notiAlertServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertServiceAffecting.setStatus("current")


class _NotiAlertProbableCauseDescription_Type(DisplayString):
    """Custom type notiAlertProbableCauseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertProbableCauseDescription_Type.__name__ = "DisplayString"
_NotiAlertProbableCauseDescription_Object = MibScalar
notiAlertProbableCauseDescription = _NotiAlertProbableCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 17),
    _NotiAlertProbableCauseDescription_Type()
)
notiAlertProbableCauseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertProbableCauseDescription.setStatus("current")


class _NotiAlertAdditionalText_Type(DisplayString):
    """Custom type notiAlertAdditionalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotiAlertAdditionalText_Type.__name__ = "DisplayString"
_NotiAlertAdditionalText_Object = MibScalar
notiAlertAdditionalText = _NotiAlertAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 18),
    _NotiAlertAdditionalText_Type()
)
notiAlertAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertAdditionalText.setStatus("current")


class _NotiAlertEventType_Type(DisplayString):
    """Custom type notiAlertEventType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertEventType_Type.__name__ = "DisplayString"
_NotiAlertEventType_Object = MibScalar
notiAlertEventType = _NotiAlertEventType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 19),
    _NotiAlertEventType_Type()
)
notiAlertEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertEventType.setStatus("current")


class _NotiAlertNeNodeName_Type(DisplayString):
    """Custom type notiAlertNeNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotiAlertNeNodeName_Type.__name__ = "DisplayString"
_NotiAlertNeNodeName_Object = MibScalar
notiAlertNeNodeName = _NotiAlertNeNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 3, 20),
    _NotiAlertNeNodeName_Type()
)
notiAlertNeNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiAlertNeNodeName.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1)
)
eventEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "evtID"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")


class _EvtID_Type(Integer32):
    """Custom type evtID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EvtID_Type.__name__ = "Integer32"
_EvtID_Object = MibTableColumn
evtID = _EvtID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 1),
    _EvtID_Type()
)
evtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtID.setStatus("current")


class _EvtSource_Type(DisplayString):
    """Custom type evtSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EvtSource_Type.__name__ = "DisplayString"
_EvtSource_Object = MibTableColumn
evtSource = _EvtSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 2),
    _EvtSource_Type()
)
evtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtSource.setStatus("current")


class _EvtEntity_Type(DisplayString):
    """Custom type evtEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EvtEntity_Type.__name__ = "DisplayString"
_EvtEntity_Object = MibTableColumn
evtEntity = _EvtEntity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 3),
    _EvtEntity_Type()
)
evtEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtEntity.setStatus("current")


class _EvtSeverity_Type(Integer32):
    """Custom type evtSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EvtSeverity_Type.__name__ = "Integer32"
_EvtSeverity_Object = MibTableColumn
evtSeverity = _EvtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 4),
    _EvtSeverity_Type()
)
evtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtSeverity.setStatus("current")


class _EvtCategory_Type(DisplayString):
    """Custom type evtCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EvtCategory_Type.__name__ = "DisplayString"
_EvtCategory_Object = MibTableColumn
evtCategory = _EvtCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 5),
    _EvtCategory_Type()
)
evtCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtCategory.setStatus("current")


class _EvtTime_Type(Gauge32):
    """Custom type evtTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EvtTime_Type.__name__ = "Gauge32"
_EvtTime_Object = MibTableColumn
evtTime = _EvtTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 6),
    _EvtTime_Type()
)
evtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtTime.setStatus("current")


class _EvtText_Type(DisplayString):
    """Custom type evtText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EvtText_Type.__name__ = "DisplayString"
_EvtText_Object = MibTableColumn
evtText = _EvtText_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 7),
    _EvtText_Type()
)
evtText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtText.setStatus("current")


class _EventUserProperties_Type(DisplayString):
    """Custom type eventUserProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventUserProperties_Type.__name__ = "DisplayString"
_EventUserProperties_Object = MibTableColumn
eventUserProperties = _EventUserProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 9, 1, 8),
    _EventUserProperties_Type()
)
eventUserProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventUserProperties.setStatus("current")
_WwpESMSeverityTable_Object = MibTable
wwpESMSeverityTable = _WwpESMSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 10)
)
if mibBuilder.loadTexts:
    wwpESMSeverityTable.setStatus("current")
_WwpESMSeverityEntry_Object = MibTableRow
wwpESMSeverityEntry = _WwpESMSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 10, 1)
)
wwpESMSeverityEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "severityName"),
)
if mibBuilder.loadTexts:
    wwpESMSeverityEntry.setStatus("current")


class _SeverityName_Type(DisplayString):
    """Custom type severityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SeverityName_Type.__name__ = "DisplayString"
_SeverityName_Object = MibTableColumn
severityName = _SeverityName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 10, 1, 1),
    _SeverityName_Type()
)
severityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityName.setStatus("current")


class _NumberOfAlarms_Type(Integer32):
    """Custom type numberOfAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NumberOfAlarms_Type.__name__ = "Integer32"
_NumberOfAlarms_Object = MibTableColumn
numberOfAlarms = _NumberOfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 10, 1, 2),
    _NumberOfAlarms_Type()
)
numberOfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfAlarms.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1)
)
alarmEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "alarmSource"),
    (0, "WWP-ESM-MIB", "alarmOwnerName"),
    (0, "WWP-ESM-MIB", "alarmEntity"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmSource_Type(DisplayString):
    """Custom type alarmSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmSource_Type.__name__ = "DisplayString"
_AlarmSource_Object = MibTableColumn
alarmSource = _AlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 1),
    _AlarmSource_Type()
)
alarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSource.setStatus("current")


class _AlarmOwnerName_Type(DisplayString):
    """Custom type alarmOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmOwnerName_Type.__name__ = "DisplayString"
_AlarmOwnerName_Object = MibTableColumn
alarmOwnerName = _AlarmOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 2),
    _AlarmOwnerName_Type()
)
alarmOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOwnerName.setStatus("current")


class _AlarmEntity_Type(DisplayString):
    """Custom type alarmEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmEntity_Type.__name__ = "DisplayString"
_AlarmEntity_Object = MibTableColumn
alarmEntity = _AlarmEntity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 3),
    _AlarmEntity_Type()
)
alarmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEntity.setStatus("current")
_AlarmSeverity_Type = Integer32
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmPreviousSeverity_Type = Integer32
_AlarmPreviousSeverity_Object = MibTableColumn
alarmPreviousSeverity = _AlarmPreviousSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 5),
    _AlarmPreviousSeverity_Type()
)
alarmPreviousSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPreviousSeverity.setStatus("current")
_AlarmCreateTime_Type = Gauge32
_AlarmCreateTime_Object = MibTableColumn
alarmCreateTime = _AlarmCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 6),
    _AlarmCreateTime_Type()
)
alarmCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCreateTime.setStatus("current")
_AlarmModTime_Type = Gauge32
_AlarmModTime_Object = MibTableColumn
alarmModTime = _AlarmModTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 7),
    _AlarmModTime_Type()
)
alarmModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmModTime.setStatus("current")


class _AlarmCategory_Type(DisplayString):
    """Custom type alarmCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmCategory_Type.__name__ = "DisplayString"
_AlarmCategory_Object = MibTableColumn
alarmCategory = _AlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 8),
    _AlarmCategory_Type()
)
alarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCategory.setStatus("current")


class _AlarmAssignedTo_Type(DisplayString):
    """Custom type alarmAssignedTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmAssignedTo_Type.__name__ = "DisplayString"
_AlarmAssignedTo_Object = MibTableColumn
alarmAssignedTo = _AlarmAssignedTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 9),
    _AlarmAssignedTo_Type()
)
alarmAssignedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAssignedTo.setStatus("current")


class _AlarmUserProperties_Type(DisplayString):
    """Custom type alarmUserProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmUserProperties_Type.__name__ = "DisplayString"
_AlarmUserProperties_Object = MibTableColumn
alarmUserProperties = _AlarmUserProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 11, 1, 10),
    _AlarmUserProperties_Type()
)
alarmUserProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUserProperties.setStatus("current")
_WwpESMPerformanceMib_ObjectIdentity = ObjectIdentity
wwpESMPerformanceMib = _WwpESMPerformanceMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4)
)
_NumPollObjects_Type = Integer32
_NumPollObjects_Object = MibScalar
numPollObjects = _NumPollObjects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 1),
    _NumPollObjects_Type()
)
numPollObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPollObjects.setStatus("current")


class _NumActivePollers_Type(Integer32):
    """Custom type numActivePollers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NumActivePollers_Type.__name__ = "Integer32"
_NumActivePollers_Object = MibScalar
numActivePollers = _NumActivePollers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 2),
    _NumActivePollers_Type()
)
numActivePollers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActivePollers.setStatus("current")
_NumThresholdObjects_Type = Integer32
_NumThresholdObjects_Object = MibScalar
numThresholdObjects = _NumThresholdObjects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 3),
    _NumThresholdObjects_Type()
)
numThresholdObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numThresholdObjects.setStatus("current")
_PollTable_Object = MibTable
pollTable = _PollTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4)
)
if mibBuilder.loadTexts:
    pollTable.setStatus("current")
_PollEntry_Object = MibTableRow
pollEntry = _PollEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1)
)
pollEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "pollid"),
)
if mibBuilder.loadTexts:
    pollEntry.setStatus("current")
_Pollid_Type = Gauge32
_Pollid_Object = MibTableColumn
pollid = _Pollid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 1),
    _Pollid_Type()
)
pollid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollid.setStatus("current")
_PolldataName_Type = DisplayString
_PolldataName_Object = MibTableColumn
polldataName = _PolldataName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 2),
    _PolldataName_Type()
)
polldataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polldataName.setStatus("current")
_Oid_Type = DisplayString
_Oid_Object = MibTableColumn
oid = _Oid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 3),
    _Oid_Type()
)
oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oid.setStatus("current")
_PollingInterval_Type = Gauge32
_PollingInterval_Object = MibTableColumn
pollingInterval = _PollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 4),
    _PollingInterval_Type()
)
pollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollingInterval.setStatus("current")


class _FailureCount_Type(Integer32):
    """Custom type failureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FailureCount_Type.__name__ = "Integer32"
_FailureCount_Object = MibTableColumn
failureCount = _FailureCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 5),
    _FailureCount_Type()
)
failureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failureCount.setStatus("current")


class _FailureThreshold_Type(Integer32):
    """Custom type failureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FailureThreshold_Type.__name__ = "Integer32"
_FailureThreshold_Object = MibTableColumn
failureThreshold = _FailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 6),
    _FailureThreshold_Type()
)
failureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failureThreshold.setStatus("current")
_TimeToPoll_Type = Gauge32
_TimeToPoll_Object = MibTableColumn
timeToPoll = _TimeToPoll_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 7),
    _TimeToPoll_Type()
)
timeToPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeToPoll.setStatus("current")
_PolledTime_Type = Gauge32
_PolledTime_Object = MibTableColumn
polledTime = _PolledTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 8),
    _PolledTime_Type()
)
polledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polledTime.setStatus("current")
_AgentName_Type = DisplayString
_AgentName_Object = MibTableColumn
agentName = _AgentName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 4, 1, 9),
    _AgentName_Type()
)
agentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentName.setStatus("current")
_ThresholdTable_Object = MibTable
thresholdTable = _ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5)
)
if mibBuilder.loadTexts:
    thresholdTable.setStatus("current")
_ThresholdEntry_Object = MibTableRow
thresholdEntry = _ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1)
)
thresholdEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "thresholdObjectName"),
)
if mibBuilder.loadTexts:
    thresholdEntry.setStatus("current")


class _ThresholdObjectName_Type(DisplayString):
    """Custom type thresholdObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThresholdObjectName_Type.__name__ = "DisplayString"
_ThresholdObjectName_Object = MibTableColumn
thresholdObjectName = _ThresholdObjectName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 1),
    _ThresholdObjectName_Type()
)
thresholdObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdObjectName.setStatus("current")


class _ThresholdKind_Type(DisplayString):
    """Custom type thresholdKind based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThresholdKind_Type.__name__ = "DisplayString"
_ThresholdKind_Object = MibTableColumn
thresholdKind = _ThresholdKind_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 2),
    _ThresholdKind_Type()
)
thresholdKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdKind.setStatus("current")


class _ThresholdMessage_Type(DisplayString):
    """Custom type thresholdMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThresholdMessage_Type.__name__ = "DisplayString"
_ThresholdMessage_Object = MibTableColumn
thresholdMessage = _ThresholdMessage_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 3),
    _ThresholdMessage_Type()
)
thresholdMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMessage.setStatus("current")


class _ThresholdClearMessage_Type(DisplayString):
    """Custom type thresholdClearMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThresholdClearMessage_Type.__name__ = "DisplayString"
_ThresholdClearMessage_Object = MibTableColumn
thresholdClearMessage = _ThresholdClearMessage_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 4),
    _ThresholdClearMessage_Type()
)
thresholdClearMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdClearMessage.setStatus("current")


class _ThresholdSeverity_Type(Integer32):
    """Custom type thresholdSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ThresholdSeverity_Type.__name__ = "Integer32"
_ThresholdSeverity_Object = MibTableColumn
thresholdSeverity = _ThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 5),
    _ThresholdSeverity_Type()
)
thresholdSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdSeverity.setStatus("current")


class _ThresholdCategory_Type(DisplayString):
    """Custom type thresholdCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThresholdCategory_Type.__name__ = "DisplayString"
_ThresholdCategory_Object = MibTableColumn
thresholdCategory = _ThresholdCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 5, 1, 6),
    _ThresholdCategory_Type()
)
thresholdCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdCategory.setStatus("current")
_Statsdata_ObjectIdentity = ObjectIdentity
statsdata = _Statsdata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6)
)
_StatsdataTableName_Type = DisplayString
_StatsdataTableName_Object = MibScalar
statsdataTableName = _StatsdataTableName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 1),
    _StatsdataTableName_Type()
)
statsdataTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsdataTableName.setStatus("current")
_StatsDataTable_Object = MibTable
statsDataTable = _StatsDataTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    statsDataTable.setStatus("current")
_StatsDataEntry_Object = MibTableRow
statsDataEntry = _StatsDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2, 1)
)
statsDataEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "pollID"),
    (0, "WWP-ESM-MIB", "oidindex"),
    (0, "WWP-ESM-MIB", "time"),
)
if mibBuilder.loadTexts:
    statsDataEntry.setStatus("current")
_PollID_Type = Gauge32
_PollID_Object = MibTableColumn
pollID = _PollID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2, 1, 1),
    _PollID_Type()
)
pollID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollID.setStatus("current")
_Time_Type = DisplayString
_Time_Object = MibTableColumn
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2, 1, 2),
    _Time_Type()
)
time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    time.setStatus("current")
_Oidindex_Type = DisplayString
_Oidindex_Object = MibTableColumn
oidindex = _Oidindex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2, 1, 3),
    _Oidindex_Type()
)
oidindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oidindex.setStatus("current")


class _Value_Type(DisplayString):
    """Custom type value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Value_Type.__name__ = "DisplayString"
_Value_Object = MibTableColumn
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 6, 2, 1, 4),
    _Value_Type()
)
value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    value.setStatus("current")
_PerfNotificationMib_ObjectIdentity = ObjectIdentity
perfNotificationMib = _PerfNotificationMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7)
)
_PerfNotiConfigPrefix_ObjectIdentity = ObjectIdentity
perfNotiConfigPrefix = _PerfNotiConfigPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 1)
)
_PerfNotifications_ObjectIdentity = ObjectIdentity
perfNotifications = _PerfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 1, 0)
)
_PerfNotiVarbinds_ObjectIdentity = ObjectIdentity
perfNotiVarbinds = _PerfNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2)
)
_Eventid_Type = Integer32
_Eventid_Object = MibScalar
eventid = _Eventid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2, 1),
    _Eventid_Type()
)
eventid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventid.setStatus("current")
_Eventsource_Type = DisplayString
_Eventsource_Object = MibScalar
eventsource = _Eventsource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2, 2),
    _Eventsource_Type()
)
eventsource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsource.setStatus("current")
_EventEntity_Type = DisplayString
_EventEntity_Object = MibScalar
eventEntity = _EventEntity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2, 3),
    _EventEntity_Type()
)
eventEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEntity.setStatus("current")
_EventGenTime_Type = Gauge32
_EventGenTime_Object = MibScalar
eventGenTime = _EventGenTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2, 4),
    _EventGenTime_Type()
)
eventGenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventGenTime.setStatus("current")
_EventSeverity_Type = Integer32
_EventSeverity_Object = MibScalar
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 2, 5),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_PersistentTrapsMib_ObjectIdentity = ObjectIdentity
persistentTrapsMib = _PersistentTrapsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5)
)
_MaxRows_Type = Integer32
_MaxRows_Object = MibScalar
maxRows = _MaxRows_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 1),
    _MaxRows_Type()
)
maxRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxRows.setStatus("current")


class _SequenceNum_Type(Integer32):
    """Custom type sequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SequenceNum_Type.__name__ = "Integer32"
_SequenceNum_Object = MibScalar
sequenceNum = _SequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 2),
    _SequenceNum_Type()
)
sequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceNum.setStatus("current")
_NotiLogTable_Object = MibTable
notiLogTable = _NotiLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3)
)
if mibBuilder.loadTexts:
    notiLogTable.setStatus("current")
_NotiLogEntry_Object = MibTableRow
notiLogEntry = _NotiLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3, 1)
)
notiLogEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "notiLogIndex"),
)
if mibBuilder.loadTexts:
    notiLogEntry.setStatus("current")


class _NotiLogIndex_Type(Integer32):
    """Custom type notiLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NotiLogIndex_Type.__name__ = "Integer32"
_NotiLogIndex_Object = MibTableColumn
notiLogIndex = _NotiLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3, 1, 1),
    _NotiLogIndex_Type()
)
notiLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiLogIndex.setStatus("current")
_NotiLogTime_Type = Gauge32
_NotiLogTime_Object = MibTableColumn
notiLogTime = _NotiLogTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3, 1, 2),
    _NotiLogTime_Type()
)
notiLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiLogTime.setStatus("current")


class _NotiLogNumVarBinds_Type(Integer32):
    """Custom type notiLogNumVarBinds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NotiLogNumVarBinds_Type.__name__ = "Integer32"
_NotiLogNumVarBinds_Object = MibTableColumn
notiLogNumVarBinds = _NotiLogNumVarBinds_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3, 1, 3),
    _NotiLogNumVarBinds_Type()
)
notiLogNumVarBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiLogNumVarBinds.setStatus("current")
_NotiLogOid_Type = ObjectIdentifier
_NotiLogOid_Object = MibTableColumn
notiLogOid = _NotiLogOid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 3, 1, 4),
    _NotiLogOid_Type()
)
notiLogOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notiLogOid.setStatus("current")
_VarbindLogTable_Object = MibTable
varbindLogTable = _VarbindLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 4)
)
if mibBuilder.loadTexts:
    varbindLogTable.setStatus("current")
_VarbindLogEntry_Object = MibTableRow
varbindLogEntry = _VarbindLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 4, 1)
)
varbindLogEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "notiLogIndex"),
    (0, "WWP-ESM-MIB", "varbindIndex"),
)
if mibBuilder.loadTexts:
    varbindLogEntry.setStatus("current")


class _VarbindIndex_Type(Integer32):
    """Custom type varbindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_VarbindIndex_Type.__name__ = "Integer32"
_VarbindIndex_Object = MibTableColumn
varbindIndex = _VarbindIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 4, 1, 1),
    _VarbindIndex_Type()
)
varbindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varbindIndex.setStatus("current")


class _VarbindType_Type(Integer32):
    """Custom type varbindType based on Integer32"""
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
        *(("displayString", 1),
          ("gauge32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 6))
    )


_VarbindType_Type.__name__ = "Integer32"
_VarbindType_Object = MibTableColumn
varbindType = _VarbindType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 4, 1, 2),
    _VarbindType_Type()
)
varbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varbindType.setStatus("current")


class _VarbindValue_Type(DisplayString):
    """Custom type varbindValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VarbindValue_Type.__name__ = "DisplayString"
_VarbindValue_Object = MibTableColumn
varbindValue = _VarbindValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 5, 4, 1, 3),
    _VarbindValue_Type()
)
varbindValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varbindValue.setStatus("current")
_TftpMib_ObjectIdentity = ObjectIdentity
tftpMib = _TftpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6)
)


class _ServerName_Type(DisplayString):
    """Custom type serverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServerName_Type.__name__ = "DisplayString"
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")


class _PortNum_Type(Integer32):
    """Custom type portNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PortNum_Type.__name__ = "Integer32"
_PortNum_Object = MibScalar
portNum = _PortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 2),
    _PortNum_Type()
)
portNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNum.setStatus("current")


class _SourceFile_Type(DisplayString):
    """Custom type sourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SourceFile_Type.__name__ = "DisplayString"
_SourceFile_Object = MibScalar
sourceFile = _SourceFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 3),
    _SourceFile_Type()
)
sourceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceFile.setStatus("current")


class _DestinationFile_Type(DisplayString):
    """Custom type destinationFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DestinationFile_Type.__name__ = "DisplayString"
_DestinationFile_Object = MibScalar
destinationFile = _DestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 4),
    _DestinationFile_Type()
)
destinationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationFile.setStatus("current")


class _TftpMode_Type(TruthValue):
    """Custom type tftpMode based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netascii", 1),
          ("octet", 2))
    )


_TftpMode_Type.__name__ = "TruthValue"
_TftpMode_Object = MibScalar
tftpMode = _TftpMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 5),
    _TftpMode_Type()
)
tftpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpMode.setStatus("current")


class _Request_Type(TruthValue):
    """Custom type request based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_Request_Type.__name__ = "TruthValue"
_Request_Object = MibScalar
request = _Request_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 6, 6),
    _Request_Type()
)
request.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    request.setStatus("current")
_ProxyService_ObjectIdentity = ObjectIdentity
proxyService = _ProxyService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7)
)
_ProxyTable_Object = MibTable
proxyTable = _ProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1)
)
if mibBuilder.loadTexts:
    proxyTable.setStatus("current")
_ProxyEntry_Object = MibTableRow
proxyEntry = _ProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1)
)
proxyEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "serialNumber"),
)
if mibBuilder.loadTexts:
    proxyEntry.setStatus("current")


class _SerialNumber_Type(Integer32):
    """Custom type serialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SerialNumber_Type.__name__ = "Integer32"
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_HostName_Type = DisplayString
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _DevicePort_Type(Integer32):
    """Custom type devicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DevicePort_Type.__name__ = "Integer32"
_DevicePort_Object = MibTableColumn
devicePort = _DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 3),
    _DevicePort_Type()
)
devicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devicePort.setStatus("current")
_RequestOid_Type = ObjectIdentifier
_RequestOid_Object = MibTableColumn
requestOid = _RequestOid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 4),
    _RequestOid_Type()
)
requestOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requestOid.setStatus("current")


class _Community_Type(DisplayString):
    """Custom type community based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Community_Type.__name__ = "DisplayString"
_Community_Object = MibTableColumn
community = _Community_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 5),
    _Community_Type()
)
community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    community.setStatus("current")


class _Service_Type(Integer32):
    """Custom type service based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wait", 0),
          ("get", 1),
          ("getNext", 2))
    )


_Service_Type.__name__ = "Integer32"
_Service_Object = MibTableColumn
service = _Service_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 6),
    _Service_Type()
)
service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    service.setStatus("current")


class _Result_Type(DisplayString):
    """Custom type result based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Result_Type.__name__ = "DisplayString"
_Result_Object = MibTableColumn
result = _Result_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 7, 1, 1, 7),
    _Result_Type()
)
result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    result.setStatus("current")
_Subagents_ObjectIdentity = ObjectIdentity
subagents = _Subagents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8)
)
_SubAgentTable_Object = MibTable
subAgentTable = _SubAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1)
)
if mibBuilder.loadTexts:
    subAgentTable.setStatus("current")
_SubAgentEntry_Object = MibTableRow
subAgentEntry = _SubAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1)
)
subAgentEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "subAgentoid"),
)
if mibBuilder.loadTexts:
    subAgentEntry.setStatus("current")
_SubAgentoid_Type = ObjectIdentifier
_SubAgentoid_Object = MibTableColumn
subAgentoid = _SubAgentoid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 1),
    _SubAgentoid_Type()
)
subAgentoid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subAgentoid.setStatus("current")


class _SubAgent_Type(DisplayString):
    """Custom type subAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubAgent_Type.__name__ = "DisplayString"
_SubAgent_Object = MibTableColumn
subAgent = _SubAgent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 2),
    _SubAgent_Type()
)
subAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subAgent.setStatus("current")
_SubAgentPort_Type = Unsigned32
_SubAgentPort_Object = MibTableColumn
subAgentPort = _SubAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 3),
    _SubAgentPort_Type()
)
subAgentPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subAgentPort.setStatus("current")
_SubAgentVersion_Type = Integer32
_SubAgentVersion_Object = MibTableColumn
subAgentVersion = _SubAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 4),
    _SubAgentVersion_Type()
)
subAgentVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subAgentVersion.setStatus("current")


class _SubAgentCommunity_Type(DisplayString):
    """Custom type subAgentCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubAgentCommunity_Type.__name__ = "DisplayString"
_SubAgentCommunity_Object = MibTableColumn
subAgentCommunity = _SubAgentCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 5),
    _SubAgentCommunity_Type()
)
subAgentCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subAgentCommunity.setStatus("current")
_Timeout_Type = Unsigned32
_Timeout_Object = MibTableColumn
timeout = _Timeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 6),
    _Timeout_Type()
)
timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeout.setStatus("current")
_SubAgentRetries_Type = Unsigned32
_SubAgentRetries_Object = MibTableColumn
subAgentRetries = _SubAgentRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 7),
    _SubAgentRetries_Type()
)
subAgentRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subAgentRetries.setStatus("current")


class _RowStatus_Type(RowStatus):
    """Custom type rowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_RowStatus_Type.__name__ = "RowStatus"
_RowStatus_Object = MibTableColumn
rowStatus = _RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 8, 1, 1, 8),
    _RowStatus_Type()
)
rowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rowStatus.setStatus("current")
_TrapForwardingModule_ObjectIdentity = ObjectIdentity
trapForwardingModule = _TrapForwardingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9)
)
_V1v2TrapForwardingTable_Object = MibTable
v1v2TrapForwardingTable = _V1v2TrapForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1)
)
if mibBuilder.loadTexts:
    v1v2TrapForwardingTable.setStatus("current")
_V1v2TrapForwardingEntry_Object = MibTableRow
v1v2TrapForwardingEntry = _V1v2TrapForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1)
)
v1v2TrapForwardingEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "v1v2ManagerHost"),
    (0, "WWP-ESM-MIB", "v1v2ManagerPort"),
)
if mibBuilder.loadTexts:
    v1v2TrapForwardingEntry.setStatus("current")


class _V1v2ManagerHost_Type(IpAddress):
    """Custom type v1v2ManagerHost based on IpAddress"""
    defaultHexValue = "7F000001"


_V1v2ManagerHost_Type.__name__ = "IpAddress"
_V1v2ManagerHost_Object = MibTableColumn
v1v2ManagerHost = _V1v2ManagerHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 1),
    _V1v2ManagerHost_Type()
)
v1v2ManagerHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v1v2ManagerHost.setStatus("current")


class _V1v2ManagerPort_Type(Integer32):
    """Custom type v1v2ManagerPort based on Integer32"""
    defaultValue = 162


_V1v2ManagerPort_Type.__name__ = "Integer32"
_V1v2ManagerPort_Object = MibTableColumn
v1v2ManagerPort = _V1v2ManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 2),
    _V1v2ManagerPort_Type()
)
v1v2ManagerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v1v2ManagerPort.setStatus("current")
_V1v2ManagerVersion_Type = Integer32
_V1v2ManagerVersion_Object = MibTableColumn
v1v2ManagerVersion = _V1v2ManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 3),
    _V1v2ManagerVersion_Type()
)
v1v2ManagerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v1v2ManagerVersion.setStatus("current")


class _V1v2ManagerCommunity_Type(DisplayString):
    """Custom type v1v2ManagerCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_V1v2ManagerCommunity_Type.__name__ = "DisplayString"
_V1v2ManagerCommunity_Object = MibTableColumn
v1v2ManagerCommunity = _V1v2ManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 4),
    _V1v2ManagerCommunity_Type()
)
v1v2ManagerCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v1v2ManagerCommunity.setStatus("current")


class _V1v2ManagerTimeOut_Type(Unsigned32):
    """Custom type v1v2ManagerTimeOut based on Unsigned32"""
    defaultValue = 5


_V1v2ManagerTimeOut_Type.__name__ = "Unsigned32"
_V1v2ManagerTimeOut_Object = MibTableColumn
v1v2ManagerTimeOut = _V1v2ManagerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 5),
    _V1v2ManagerTimeOut_Type()
)
v1v2ManagerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v1v2ManagerTimeOut.setStatus("current")


class _V1v2ManagerRetries_Type(Unsigned32):
    """Custom type v1v2ManagerRetries based on Unsigned32"""
    defaultValue = 0


_V1v2ManagerRetries_Type.__name__ = "Unsigned32"
_V1v2ManagerRetries_Object = MibTableColumn
v1v2ManagerRetries = _V1v2ManagerRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 6),
    _V1v2ManagerRetries_Type()
)
v1v2ManagerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v1v2ManagerRetries.setStatus("current")
_V1v2ManagerStatus_Type = RowStatus
_V1v2ManagerStatus_Object = MibTableColumn
v1v2ManagerStatus = _V1v2ManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 1, 1, 7),
    _V1v2ManagerStatus_Type()
)
v1v2ManagerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v1v2ManagerStatus.setStatus("current")
_V3TrapForwardingTable_Object = MibTable
v3TrapForwardingTable = _V3TrapForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2)
)
if mibBuilder.loadTexts:
    v3TrapForwardingTable.setStatus("current")
_V3TrapForwardingEntry_Object = MibTableRow
v3TrapForwardingEntry = _V3TrapForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1)
)
v3TrapForwardingEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "v3ManagerHost"),
    (0, "WWP-ESM-MIB", "v3ManagerPort"),
)
if mibBuilder.loadTexts:
    v3TrapForwardingEntry.setStatus("current")


class _V3ManagerHost_Type(IpAddress):
    """Custom type v3ManagerHost based on IpAddress"""
    defaultHexValue = "7F000001"


_V3ManagerHost_Type.__name__ = "IpAddress"
_V3ManagerHost_Object = MibTableColumn
v3ManagerHost = _V3ManagerHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 1),
    _V3ManagerHost_Type()
)
v3ManagerHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v3ManagerHost.setStatus("current")


class _V3ManagerPort_Type(Integer32):
    """Custom type v3ManagerPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_V3ManagerPort_Type.__name__ = "Integer32"
_V3ManagerPort_Object = MibTableColumn
v3ManagerPort = _V3ManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 2),
    _V3ManagerPort_Type()
)
v3ManagerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v3ManagerPort.setStatus("current")
_V3ManagerVersion_Type = Integer32
_V3ManagerVersion_Object = MibTableColumn
v3ManagerVersion = _V3ManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 3),
    _V3ManagerVersion_Type()
)
v3ManagerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerVersion.setStatus("current")


class _V3ManagerCommunity_Type(DisplayString):
    """Custom type v3ManagerCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_V3ManagerCommunity_Type.__name__ = "DisplayString"
_V3ManagerCommunity_Object = MibTableColumn
v3ManagerCommunity = _V3ManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 4),
    _V3ManagerCommunity_Type()
)
v3ManagerCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerCommunity.setStatus("current")
_V3ManagerUserName_Type = DisplayString
_V3ManagerUserName_Object = MibTableColumn
v3ManagerUserName = _V3ManagerUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 5),
    _V3ManagerUserName_Type()
)
v3ManagerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerUserName.setStatus("current")


class _V3ManagerUserSecModel_Type(Unsigned32):
    """Custom type v3ManagerUserSecModel based on Unsigned32"""
    defaultValue = 3


_V3ManagerUserSecModel_Type.__name__ = "Unsigned32"
_V3ManagerUserSecModel_Object = MibTableColumn
v3ManagerUserSecModel = _V3ManagerUserSecModel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 6),
    _V3ManagerUserSecModel_Type()
)
v3ManagerUserSecModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerUserSecModel.setStatus("current")
_V3ManagerUserSecLevel_Type = Integer32
_V3ManagerUserSecLevel_Object = MibTableColumn
v3ManagerUserSecLevel = _V3ManagerUserSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 7),
    _V3ManagerUserSecLevel_Type()
)
v3ManagerUserSecLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerUserSecLevel.setStatus("current")
_V3ManagerUserContextName_Type = DisplayString
_V3ManagerUserContextName_Object = MibTableColumn
v3ManagerUserContextName = _V3ManagerUserContextName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 8),
    _V3ManagerUserContextName_Type()
)
v3ManagerUserContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerUserContextName.setStatus("current")


class _V3ManagerTimeOut_Type(Unsigned32):
    """Custom type v3ManagerTimeOut based on Unsigned32"""
    defaultValue = 5


_V3ManagerTimeOut_Type.__name__ = "Unsigned32"
_V3ManagerTimeOut_Object = MibTableColumn
v3ManagerTimeOut = _V3ManagerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 9),
    _V3ManagerTimeOut_Type()
)
v3ManagerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerTimeOut.setStatus("current")


class _V3ManagerRetries_Type(Unsigned32):
    """Custom type v3ManagerRetries based on Unsigned32"""
    defaultValue = 0


_V3ManagerRetries_Type.__name__ = "Unsigned32"
_V3ManagerRetries_Object = MibTableColumn
v3ManagerRetries = _V3ManagerRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 10),
    _V3ManagerRetries_Type()
)
v3ManagerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerRetries.setStatus("current")
_V3ManagerStatus_Type = RowStatus
_V3ManagerStatus_Object = MibTableColumn
v3ManagerStatus = _V3ManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 9, 2, 1, 11),
    _V3ManagerStatus_Type()
)
v3ManagerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v3ManagerStatus.setStatus("current")
_EsmConfiguration_ObjectIdentity = ObjectIdentity
esmConfiguration = _EsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10)
)
_TopologyConfiguration_ObjectIdentity = ObjectIdentity
topologyConfiguration = _TopologyConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1)
)


class _AutoDiscover_Type(TruthValue):
    """Custom type autoDiscover based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AutoDiscover_Type.__name__ = "TruthValue"
_AutoDiscover_Object = MibScalar
autoDiscover = _AutoDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 1),
    _AutoDiscover_Type()
)
autoDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDiscover.setStatus("current")


class _DiscoverLocalNet_Type(TruthValue):
    """Custom type discoverLocalNet based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_DiscoverLocalNet_Type.__name__ = "TruthValue"
_DiscoverLocalNet_Object = MibScalar
discoverLocalNet = _DiscoverLocalNet_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 2),
    _DiscoverLocalNet_Type()
)
discoverLocalNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoverLocalNet.setStatus("current")
_DiscoverInterval_Type = Integer32
_DiscoverInterval_Object = MibScalar
discoverInterval = _DiscoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 3),
    _DiscoverInterval_Type()
)
discoverInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoverInterval.setStatus("current")


class _Enablelog_Type(TruthValue):
    """Custom type enablelog based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Enablelog_Type.__name__ = "TruthValue"
_Enablelog_Object = MibScalar
enablelog = _Enablelog_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 4),
    _Enablelog_Type()
)
enablelog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablelog.setStatus("current")
_RediscoveryConfiguration_ObjectIdentity = ObjectIdentity
rediscoveryConfiguration = _RediscoveryConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5)
)


class _ReDiscover_Type(TruthValue):
    """Custom type reDiscover based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ReDiscover_Type.__name__ = "TruthValue"
_ReDiscover_Object = MibScalar
reDiscover = _ReDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5, 1),
    _ReDiscover_Type()
)
reDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reDiscover.setStatus("current")
_ReDiscoverInterval_Type = Integer32
_ReDiscoverInterval_Object = MibScalar
reDiscoverInterval = _ReDiscoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5, 2),
    _ReDiscoverInterval_Type()
)
reDiscoverInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reDiscoverInterval.setStatus("current")
_Hour_Type = DisplayString
_Hour_Object = MibScalar
hour = _Hour_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5, 3),
    _Hour_Type()
)
hour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hour.setStatus("current")
_DayOfWeek_Type = DisplayString
_DayOfWeek_Object = MibScalar
dayOfWeek = _DayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5, 4),
    _DayOfWeek_Type()
)
dayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayOfWeek.setStatus("current")
_DayOfMonth_Type = DisplayString
_DayOfMonth_Object = MibScalar
dayOfMonth = _DayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 5, 5),
    _DayOfMonth_Type()
)
dayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayOfMonth.setStatus("current")
_SnmpPingConfiguration_ObjectIdentity = ObjectIdentity
snmpPingConfiguration = _SnmpPingConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6)
)


class _EnableSnmpPing_Type(TruthValue):
    """Custom type enableSnmpPing based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EnableSnmpPing_Type.__name__ = "TruthValue"
_EnableSnmpPing_Object = MibScalar
enableSnmpPing = _EnableSnmpPing_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 1),
    _EnableSnmpPing_Type()
)
enableSnmpPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSnmpPing.setStatus("current")
_SnmpPingRetries_Type = Integer32
_SnmpPingRetries_Object = MibScalar
snmpPingRetries = _SnmpPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 2),
    _SnmpPingRetries_Type()
)
snmpPingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPingRetries.setStatus("current")
_SnmpPingTimeout_Type = Integer32
_SnmpPingTimeout_Object = MibScalar
snmpPingTimeout = _SnmpPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 3),
    _SnmpPingTimeout_Type()
)
snmpPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPingTimeout.setStatus("current")
_Snmpport_Type = DisplayString
_Snmpport_Object = MibScalar
snmpport = _Snmpport_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 4),
    _Snmpport_Type()
)
snmpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpport.setStatus("current")
_ReadCommunity_Type = DisplayString
_ReadCommunity_Object = MibScalar
readCommunity = _ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 5),
    _ReadCommunity_Type()
)
readCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readCommunity.setStatus("current")
_WriteCommunity_Type = DisplayString
_WriteCommunity_Object = MibScalar
writeCommunity = _WriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 6),
    _WriteCommunity_Type()
)
writeCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeCommunity.setStatus("current")
_SnmpV3Configuration_ObjectIdentity = ObjectIdentity
snmpV3Configuration = _SnmpV3Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 7)
)


class _EnableV3_Type(TruthValue):
    """Custom type enableV3 based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EnableV3_Type.__name__ = "TruthValue"
_EnableV3_Object = MibScalar
enableV3 = _EnableV3_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 7, 1),
    _EnableV3_Type()
)
enableV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableV3.setStatus("current")
_V3Username_Type = DisplayString
_V3Username_Object = MibScalar
v3Username = _V3Username_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 7, 2),
    _V3Username_Type()
)
v3Username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3Username.setStatus("current")
_V3Contextname_Type = DisplayString
_V3Contextname_Object = MibScalar
v3Contextname = _V3Contextname_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 6, 7, 3),
    _V3Contextname_Type()
)
v3Contextname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3Contextname.setStatus("current")
_IcmpPingConfiguration_ObjectIdentity = ObjectIdentity
icmpPingConfiguration = _IcmpPingConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 7)
)


class _EnableIcmp_Type(TruthValue):
    """Custom type enableIcmp based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EnableIcmp_Type.__name__ = "TruthValue"
_EnableIcmp_Object = MibScalar
enableIcmp = _EnableIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 7, 1),
    _EnableIcmp_Type()
)
enableIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIcmp.setStatus("current")
_IcmpPingRetries_Type = Integer32
_IcmpPingRetries_Object = MibScalar
icmpPingRetries = _IcmpPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 7, 2),
    _IcmpPingRetries_Type()
)
icmpPingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpPingRetries.setStatus("current")
_NativePingConfiguration_ObjectIdentity = ObjectIdentity
nativePingConfiguration = _NativePingConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8)
)


class _NativePingRetries_Type(Integer32):
    """Custom type nativePingRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NativePingRetries_Type.__name__ = "Integer32"
_NativePingRetries_Object = MibScalar
nativePingRetries = _NativePingRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 1),
    _NativePingRetries_Type()
)
nativePingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nativePingRetries.setStatus("current")


class _NativePingTimeOut_Type(Integer32):
    """Custom type nativePingTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NativePingTimeOut_Type.__name__ = "Integer32"
_NativePingTimeOut_Object = MibScalar
nativePingTimeOut = _NativePingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 2),
    _NativePingTimeOut_Type()
)
nativePingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nativePingTimeOut.setStatus("current")


class _DebugLevel_Type(Integer32):
    """Custom type debugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DebugLevel_Type.__name__ = "Integer32"
_DebugLevel_Object = MibScalar
debugLevel = _DebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 3),
    _DebugLevel_Type()
)
debugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugLevel.setStatus("current")


class _EnableSweep_Type(TruthValue):
    """Custom type enableSweep based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EnableSweep_Type.__name__ = "TruthValue"
_EnableSweep_Object = MibScalar
enableSweep = _EnableSweep_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 4),
    _EnableSweep_Type()
)
enableSweep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSweep.setStatus("current")


class _SweepPkts_Type(Integer32):
    """Custom type sweepPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SweepPkts_Type.__name__ = "Integer32"
_SweepPkts_Object = MibScalar
sweepPkts = _SweepPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 5),
    _SweepPkts_Type()
)
sweepPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sweepPkts.setStatus("current")


class _SweepSleepInterval_Type(Integer32):
    """Custom type sweepSleepInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SweepSleepInterval_Type.__name__ = "Integer32"
_SweepSleepInterval_Object = MibScalar
sweepSleepInterval = _SweepSleepInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 8, 6),
    _SweepSleepInterval_Type()
)
sweepSleepInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sweepSleepInterval.setStatus("current")
_NetworkDiscoveryTable_Object = MibTable
networkDiscoveryTable = _NetworkDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9)
)
if mibBuilder.loadTexts:
    networkDiscoveryTable.setStatus("current")
_NetworkDiscoveryEntry_Object = MibTableRow
networkDiscoveryEntry = _NetworkDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1)
)
networkDiscoveryEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "networkDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    networkDiscoveryEntry.setStatus("current")
_NetworkDiscoveryIndex_Type = Integer32
_NetworkDiscoveryIndex_Object = MibTableColumn
networkDiscoveryIndex = _NetworkDiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 1),
    _NetworkDiscoveryIndex_Type()
)
networkDiscoveryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDiscoveryIndex.setStatus("current")
_NetIPAddress_Type = IpAddress
_NetIPAddress_Object = MibTableColumn
netIPAddress = _NetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 2),
    _NetIPAddress_Type()
)
netIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIPAddress.setStatus("current")
_NetMask_Type = IpAddress
_NetMask_Object = MibTableColumn
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 3),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("current")
_StartIPAddress_Type = DisplayString
_StartIPAddress_Object = MibTableColumn
startIPAddress = _StartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 4),
    _StartIPAddress_Type()
)
startIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startIPAddress.setStatus("current")
_EndIPAddress_Type = DisplayString
_EndIPAddress_Object = MibTableColumn
endIPAddress = _EndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 5),
    _EndIPAddress_Type()
)
endIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endIPAddress.setStatus("current")


class _DoDiscovery_Type(TruthValue):
    """Custom type doDiscovery based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_DoDiscovery_Type.__name__ = "TruthValue"
_DoDiscovery_Object = MibTableColumn
doDiscovery = _DoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 6),
    _DoDiscovery_Type()
)
doDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doDiscovery.setStatus("current")


class _Dhcp_Type(TruthValue):
    """Custom type dhcp based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Dhcp_Type.__name__ = "TruthValue"
_Dhcp_Object = MibTableColumn
dhcp = _Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 9, 1, 7),
    _Dhcp_Type()
)
dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp.setStatus("current")
_NodeDiscoveryTable_Object = MibTable
nodeDiscoveryTable = _NodeDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10)
)
if mibBuilder.loadTexts:
    nodeDiscoveryTable.setStatus("current")
_NodeDiscoveryEntry_Object = MibTableRow
nodeDiscoveryEntry = _NodeDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1)
)
nodeDiscoveryEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "nodeIP"),
)
if mibBuilder.loadTexts:
    nodeDiscoveryEntry.setStatus("current")
_NodeIP_Type = IpAddress
_NodeIP_Object = MibTableColumn
nodeIP = _NodeIP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 1),
    _NodeIP_Type()
)
nodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIP.setStatus("current")
_NodeNetMask_Type = IpAddress
_NodeNetMask_Object = MibTableColumn
nodeNetMask = _NodeNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 2),
    _NodeNetMask_Type()
)
nodeNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeNetMask.setStatus("current")
_NodeDiscoverEnable_Type = TruthValue
_NodeDiscoverEnable_Object = MibTableColumn
nodeDiscoverEnable = _NodeDiscoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 3),
    _NodeDiscoverEnable_Type()
)
nodeDiscoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeDiscoverEnable.setStatus("current")
_SnmpAgentPort_Type = Integer32
_SnmpAgentPort_Object = MibTableColumn
snmpAgentPort = _SnmpAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 4),
    _SnmpAgentPort_Type()
)
snmpAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentPort.setStatus("current")
_NodeCommunity_Type = DisplayString
_NodeCommunity_Object = MibTableColumn
nodeCommunity = _NodeCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 5),
    _NodeCommunity_Type()
)
nodeCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeCommunity.setStatus("current")
_SnmpVersion_Type = TruthValue
_SnmpVersion_Object = MibTableColumn
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 6),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_V3UserName_Type = DisplayString
_V3UserName_Object = MibTableColumn
v3UserName = _V3UserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 7),
    _V3UserName_Type()
)
v3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3UserName.setStatus("current")
_V3ContextName_Type = DisplayString
_V3ContextName_Object = MibTableColumn
v3ContextName = _V3ContextName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 10, 1, 8),
    _V3ContextName_Type()
)
v3ContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3ContextName.setStatus("current")
_MoCriteriaTable_Object = MibTable
moCriteriaTable = _MoCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11)
)
if mibBuilder.loadTexts:
    moCriteriaTable.setStatus("current")
_MoCriteriaEntry_Object = MibTableRow
moCriteriaEntry = _MoCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11, 1)
)
moCriteriaEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "criteriaIndex"),
)
if mibBuilder.loadTexts:
    moCriteriaEntry.setStatus("current")
_CriteriaIndex_Type = Integer32
_CriteriaIndex_Object = MibTableColumn
criteriaIndex = _CriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11, 1, 1),
    _CriteriaIndex_Type()
)
criteriaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criteriaIndex.setStatus("current")
_PropertyName_Type = TruthValue
_PropertyName_Object = MibTableColumn
propertyName = _PropertyName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11, 1, 2),
    _PropertyName_Type()
)
propertyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propertyName.setStatus("current")
_PropertyValue_Type = DisplayString
_PropertyValue_Object = MibTableColumn
propertyValue = _PropertyValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11, 1, 3),
    _PropertyValue_Type()
)
propertyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propertyValue.setStatus("current")


class _Allow_Type(TruthValue):
    """Custom type allow based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Allow_Type.__name__ = "TruthValue"
_Allow_Object = MibTableColumn
allow = _Allow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 11, 1, 4),
    _Allow_Type()
)
allow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allow.setStatus("current")
_DiscoveryFilterTable_Object = MibTable
discoveryFilterTable = _DiscoveryFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 12)
)
if mibBuilder.loadTexts:
    discoveryFilterTable.setStatus("current")
_DiscoveryFilterEntry_Object = MibTableRow
discoveryFilterEntry = _DiscoveryFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 12, 1)
)
discoveryFilterEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "discFilterIndex"),
)
if mibBuilder.loadTexts:
    discoveryFilterEntry.setStatus("current")
_DiscFilterIndex_Type = Integer32
_DiscFilterIndex_Object = MibTableColumn
discFilterIndex = _DiscFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 12, 1, 1),
    _DiscFilterIndex_Type()
)
discFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discFilterIndex.setStatus("current")
_DiscFilterClassName_Type = DisplayString
_DiscFilterClassName_Object = MibTableColumn
discFilterClassName = _DiscFilterClassName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 1, 12, 1, 2),
    _DiscFilterClassName_Type()
)
discFilterClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discFilterClassName.setStatus("current")
_FaultConfIguration_ObjectIdentity = ObjectIdentity
faultConfIguration = _FaultConfIguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2)
)
_TrapFilterTable_Object = MibTable
trapFilterTable = _TrapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    trapFilterTable.setStatus("current")
_TrapFilterEntry_Object = MibTableRow
trapFilterEntry = _TrapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1)
)
trapFilterEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "trapFilterIndex"),
)
if mibBuilder.loadTexts:
    trapFilterEntry.setStatus("current")
_TrapFilterIndex_Type = Integer32
_TrapFilterIndex_Object = MibTableColumn
trapFilterIndex = _TrapFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 1),
    _TrapFilterIndex_Type()
)
trapFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilterIndex.setStatus("current")
_AlertFilterClassName_Type = DisplayString
_AlertFilterClassName_Object = MibTableColumn
alertFilterClassName = _AlertFilterClassName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 2),
    _AlertFilterClassName_Type()
)
alertFilterClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertFilterClassName.setStatus("current")
_TrapFilterName_Type = DisplayString
_TrapFilterName_Object = MibTableColumn
trapFilterName = _TrapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 3),
    _TrapFilterName_Type()
)
trapFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFilterName.setStatus("current")


class _TrapFilterEnable_Type(TruthValue):
    """Custom type trapFilterEnable based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TrapFilterEnable_Type.__name__ = "TruthValue"
_TrapFilterEnable_Object = MibTableColumn
trapFilterEnable = _TrapFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 4),
    _TrapFilterEnable_Type()
)
trapFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFilterEnable.setStatus("current")
_GenericType_Type = DisplayString
_GenericType_Object = MibTableColumn
genericType = _GenericType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 6),
    _GenericType_Type()
)
genericType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericType.setStatus("current")
_SpecificType_Type = DisplayString
_SpecificType_Object = MibTableColumn
specificType = _SpecificType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 7),
    _SpecificType_Type()
)
specificType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificType.setStatus("current")
_EnterpriseOID_Type = DisplayString
_EnterpriseOID_Object = MibTableColumn
enterpriseOID = _EnterpriseOID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 8),
    _EnterpriseOID_Type()
)
enterpriseOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseOID.setStatus("current")
_TrapOID_Type = DisplayString
_TrapOID_Object = MibTableColumn
trapOID = _TrapOID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 9),
    _TrapOID_Type()
)
trapOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOID.setStatus("current")


class _SetFilter_Type(TruthValue):
    """Custom type setFilter based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_SetFilter_Type.__name__ = "TruthValue"
_SetFilter_Object = MibTableColumn
setFilter = _SetFilter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 2, 1, 1, 10),
    _SetFilter_Type()
)
setFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFilter.setStatus("current")
_PerformanceConfiguration_ObjectIdentity = ObjectIdentity
performanceConfiguration = _PerformanceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 3)
)
_PollingFiltersTable_Object = MibTable
pollingFiltersTable = _PollingFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    pollingFiltersTable.setStatus("current")
_PollingFiltersEntry_Object = MibTableRow
pollingFiltersEntry = _PollingFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 3, 1, 1)
)
pollingFiltersEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "pollingFilterIndex"),
)
if mibBuilder.loadTexts:
    pollingFiltersEntry.setStatus("current")
_PollingFilterIndex_Type = Integer32
_PollingFilterIndex_Object = MibTableColumn
pollingFilterIndex = _PollingFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 3, 1, 1, 1),
    _PollingFilterIndex_Type()
)
pollingFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollingFilterIndex.setStatus("current")


class _PollingFilterClassName_Type(DisplayString):
    """Custom type pollingFilterClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PollingFilterClassName_Type.__name__ = "DisplayString"
_PollingFilterClassName_Object = MibTableColumn
pollingFilterClassName = _PollingFilterClassName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 3, 1, 1, 2),
    _PollingFilterClassName_Type()
)
pollingFilterClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollingFilterClassName.setStatus("current")
_LogConfiguration_ObjectIdentity = ObjectIdentity
logConfiguration = _LogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4)
)
_Stdout_ObjectIdentity = ObjectIdentity
stdout = _Stdout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1)
)


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Directory_Type(DisplayString):
    """Custom type directory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Directory_Type.__name__ = "DisplayString"
_Directory_Object = MibScalar
directory = _Directory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 2),
    _Directory_Type()
)
directory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directory.setStatus("current")
_NumFiles_Type = Integer32
_NumFiles_Object = MibScalar
numFiles = _NumFiles_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 3),
    _NumFiles_Type()
)
numFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numFiles.setStatus("current")
_NumLines_Type = Integer32
_NumLines_Object = MibScalar
numLines = _NumLines_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 4),
    _NumLines_Type()
)
numLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numLines.setStatus("current")


class _Logging_Type(TruthValue):
    """Custom type logging based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Logging_Type.__name__ = "TruthValue"
_Logging_Object = MibScalar
logging = _Logging_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 5),
    _Logging_Type()
)
logging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logging.setStatus("current")


class _Timestamp_Type(TruthValue):
    """Custom type timestamp based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Timestamp_Type.__name__ = "TruthValue"
_Timestamp_Object = MibScalar
timestamp = _Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 1, 6),
    _Timestamp_Type()
)
timestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timestamp.setStatus("current")
_Stderr_ObjectIdentity = ObjectIdentity
stderr = _Stderr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2)
)


class _Filename_Type(DisplayString):
    """Custom type filename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Filename_Type.__name__ = "DisplayString"
_Filename_Object = MibScalar
filename = _Filename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 1),
    _Filename_Type()
)
filename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filename.setStatus("current")


class _LogDirectory_Type(DisplayString):
    """Custom type logDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDirectory_Type.__name__ = "DisplayString"
_LogDirectory_Object = MibScalar
logDirectory = _LogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 2),
    _LogDirectory_Type()
)
logDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDirectory.setStatus("current")
_Filenum_Type = Integer32
_Filenum_Object = MibScalar
filenum = _Filenum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 3),
    _Filenum_Type()
)
filenum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filenum.setStatus("current")
_Linenum_Type = Integer32
_Linenum_Object = MibScalar
linenum = _Linenum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 4),
    _Linenum_Type()
)
linenum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linenum.setStatus("current")


class _Log_Type(TruthValue):
    """Custom type log based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Log_Type.__name__ = "TruthValue"
_Log_Object = MibScalar
log = _Log_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 5),
    _Log_Type()
)
log.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    log.setStatus("current")


class _LogTime_Type(TruthValue):
    """Custom type logTime based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_LogTime_Type.__name__ = "TruthValue"
_LogTime_Object = MibScalar
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 2, 6),
    _LogTime_Type()
)
logTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTime.setStatus("current")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1)
)
logEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")


class _LogFileName_Type(DisplayString):
    """Custom type logFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogFileName_Type.__name__ = "DisplayString"
_LogFileName_Object = MibTableColumn
logFileName = _LogFileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 2),
    _LogFileName_Type()
)
logFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFileName.setStatus("current")


class _LogDirName_Type(DisplayString):
    """Custom type logDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDirName_Type.__name__ = "DisplayString"
_LogDirName_Object = MibTableColumn
logDirName = _LogDirName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 3),
    _LogDirName_Type()
)
logDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDirName.setStatus("current")
_MaxLines_Type = Integer32
_MaxLines_Object = MibTableColumn
maxLines = _MaxLines_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 4),
    _MaxLines_Type()
)
maxLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLines.setStatus("current")
_MaxFiles_Type = Integer32
_MaxFiles_Object = MibTableColumn
maxFiles = _MaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 5),
    _MaxFiles_Type()
)
maxFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxFiles.setStatus("current")
_LinesCached_Type = Integer32
_LinesCached_Object = MibTableColumn
linesCached = _LinesCached_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 6),
    _LinesCached_Type()
)
linesCached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linesCached.setStatus("current")


class _TimeStamp_Type(TruthValue):
    """Custom type timeStamp based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TimeStamp_Type.__name__ = "TruthValue"
_TimeStamp_Object = MibTableColumn
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 3, 1, 7),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_LogUserTable_Object = MibTable
logUserTable = _LogUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4)
)
if mibBuilder.loadTexts:
    logUserTable.setStatus("current")
_LogUserEntry_Object = MibTableRow
logUserEntry = _LogUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1)
)
logUserEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "logIndex"),
    (0, "WWP-ESM-MIB", "logUserIndex"),
)
if mibBuilder.loadTexts:
    logUserEntry.setStatus("current")
_LogUserIndex_Type = Integer32
_LogUserIndex_Object = MibTableColumn
logUserIndex = _LogUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1, 1),
    _LogUserIndex_Type()
)
logUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUserIndex.setStatus("current")


class _LogUserName_Type(DisplayString):
    """Custom type logUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogUserName_Type.__name__ = "DisplayString"
_LogUserName_Object = MibTableColumn
logUserName = _LogUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1, 2),
    _LogUserName_Type()
)
logUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUserName.setStatus("current")
_DisplayName_Type = DisplayString
_DisplayName_Object = MibTableColumn
displayName = _DisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1, 3),
    _DisplayName_Type()
)
displayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayName.setStatus("current")
_LogLevel_Type = Integer32
_LogLevel_Object = MibTableColumn
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1, 4),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLevel.setStatus("current")


class _EnableLog_Type(TruthValue):
    """Custom type enableLog based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EnableLog_Type.__name__ = "TruthValue"
_EnableLog_Object = MibTableColumn
enableLog = _EnableLog_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 10, 4, 4, 1, 5),
    _EnableLog_Type()
)
enableLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLog.setStatus("current")
_AgentConfiguration_ObjectIdentity = ObjectIdentity
agentConfiguration = _AgentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11)
)
_V1v2AuthenticationTables_ObjectIdentity = ObjectIdentity
v1v2AuthenticationTables = _V1v2AuthenticationTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1, 1)
)
aclEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "aclCommunity"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")


class _AclCommunity_Type(DisplayString):
    """Custom type aclCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AclCommunity_Type.__name__ = "DisplayString"
_AclCommunity_Object = MibTableColumn
aclCommunity = _AclCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1, 1, 1),
    _AclCommunity_Type()
)
aclCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclCommunity.setStatus("current")


class _AclAccess_Type(Integer32):
    """Custom type aclAccess based on Integer32"""
    defaultValue = 3


_AclAccess_Type.__name__ = "Integer32"
_AclAccess_Object = MibTableColumn
aclAccess = _AclAccess_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1, 1, 2),
    _AclAccess_Type()
)
aclAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAccess.setStatus("current")
_AclManagers_Type = DisplayString
_AclManagers_Object = MibTableColumn
aclManagers = _AclManagers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1, 1, 3),
    _AclManagers_Type()
)
aclManagers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclManagers.setStatus("current")
_AclStatus_Type = RowStatus
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 1, 1, 4),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_VaclTable_Object = MibTable
vaclTable = _VaclTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    vaclTable.setStatus("current")
_VaclEntry_Object = MibTableRow
vaclEntry = _VaclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 2, 1)
)
vaclEntry.setIndexNames(
    (0, "WWP-ESM-MIB", "aclCommunity"),
)
if mibBuilder.loadTexts:
    vaclEntry.setStatus("current")
_VaclmibViews_Type = DisplayString
_VaclmibViews_Object = MibTableColumn
vaclmibViews = _VaclmibViews_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 2, 1, 1),
    _VaclmibViews_Type()
)
vaclmibViews.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vaclmibViews.setStatus("current")
_VaclviewStatus_Type = RowStatus
_VaclviewStatus_Object = MibTableColumn
vaclviewStatus = _VaclviewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 11, 1, 2, 1, 2),
    _VaclviewStatus_Type()
)
vaclviewStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vaclviewStatus.setStatus("current")
_IsmMib_ObjectIdentity = ObjectIdentity
ismMib = _IsmMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12)
)
_IsmNotificationMib_ObjectIdentity = ObjectIdentity
ismNotificationMib = _IsmNotificationMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1)
)


class _IsmExtraPropNames_Type(DisplayString):
    """Custom type ismExtraPropNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsmExtraPropNames_Type.__name__ = "DisplayString"
_IsmExtraPropNames_Object = MibScalar
ismExtraPropNames = _IsmExtraPropNames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 1),
    _IsmExtraPropNames_Type()
)
ismExtraPropNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ismExtraPropNames.setStatus("current")
_IsmNotiPrefix_ObjectIdentity = ObjectIdentity
ismNotiPrefix = _IsmNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2)
)
_IsmNotifications_ObjectIdentity = ObjectIdentity
ismNotifications = _IsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0)
)
_IsmNotiVarbinds_ObjectIdentity = ObjectIdentity
ismNotiVarbinds = _IsmNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3)
)
_CurrentState_Type = DisplayString
_CurrentState_Object = MibScalar
currentState = _CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 1),
    _CurrentState_Type()
)
currentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentState.setStatus("current")
_PreviousState_Type = DisplayString
_PreviousState_Object = MibScalar
previousState = _PreviousState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 2),
    _PreviousState_Type()
)
previousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    previousState.setStatus("current")


class _UniqueIdentifier_Type(DisplayString):
    """Custom type uniqueIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UniqueIdentifier_Type.__name__ = "DisplayString"
_UniqueIdentifier_Object = MibScalar
uniqueIdentifier = _UniqueIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 3),
    _UniqueIdentifier_Type()
)
uniqueIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniqueIdentifier.setStatus("current")


class _StateChangeTime_Type(Gauge32):
    """Custom type stateChangeTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StateChangeTime_Type.__name__ = "Gauge32"
_StateChangeTime_Object = MibScalar
stateChangeTime = _StateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 4),
    _StateChangeTime_Type()
)
stateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateChangeTime.setStatus("current")


class _StatsCounters_Type(DisplayString):
    """Custom type statsCounters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StatsCounters_Type.__name__ = "DisplayString"
_StatsCounters_Object = MibScalar
statsCounters = _StatsCounters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 5),
    _StatsCounters_Type()
)
statsCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCounters.setStatus("current")


class _NodeChangeTime_Type(Gauge32):
    """Custom type nodeChangeTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NodeChangeTime_Type.__name__ = "Gauge32"
_NodeChangeTime_Object = MibScalar
nodeChangeTime = _NodeChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 6),
    _NodeChangeTime_Type()
)
nodeChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeChangeTime.setStatus("current")


class _Node_Type(DisplayString):
    """Custom type node based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Node_Type.__name__ = "DisplayString"
_Node_Object = MibScalar
node = _Node_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 7),
    _Node_Type()
)
node.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    node.setStatus("current")


class _IsmExtraProperties_Type(DisplayString):
    """Custom type ismExtraProperties based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsmExtraProperties_Type.__name__ = "DisplayString"
_IsmExtraProperties_Object = MibScalar
ismExtraProperties = _IsmExtraProperties_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 8),
    _IsmExtraProperties_Type()
)
ismExtraProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ismExtraProperties.setStatus("current")


class _Text_Type(DisplayString):
    """Custom type text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Text_Type.__name__ = "DisplayString"
_Text_Object = MibScalar
text = _Text_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 9),
    _Text_Type()
)
text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    text.setStatus("current")


class _NotifTime_Type(Gauge32):
    """Custom type notifTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NotifTime_Type.__name__ = "Gauge32"
_NotifTime_Object = MibScalar
notifTime = _NotifTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 10),
    _NotifTime_Type()
)
notifTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifTime.setStatus("current")
_Status_Type = DisplayString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 3, 11),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")

# Managed Objects groups


# Notification objects

moEnrolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 2, 0, 1)
)
moEnrolNotification.setObjects(
      *(("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "moName"),
        ("WWP-ESM-MIB", "moownerName"),
        ("WWP-ESM-MIB", "moType"),
        ("WWP-ESM-MIB", "moEnrolTime"),
        ("WWP-ESM-MIB", "moExtraProperties"),
        ("WWP-ESM-MIB", "moIpAddress"))
)
if mibBuilder.loadTexts:
    moEnrolNotification.setStatus(
        "current"
    )

moDeenrolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 2, 0, 2)
)
moDeenrolNotification.setObjects(
      *(("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "moName"),
        ("WWP-ESM-MIB", "moownerName"),
        ("WWP-ESM-MIB", "moType"),
        ("WWP-ESM-MIB", "moDeEnrolTime"),
        ("WWP-ESM-MIB", "moExtraProperties"),
        ("WWP-ESM-MIB", "moIpAddress"))
)
if mibBuilder.loadTexts:
    moDeenrolNotification.setStatus(
        "current"
    )

moAttrChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 2, 14, 2, 0, 3)
)
moAttrChangeNotification.setObjects(
      *(("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "moName"),
        ("WWP-ESM-MIB", "moownerName"),
        ("WWP-ESM-MIB", "moType"),
        ("WWP-ESM-MIB", "moDataChangeTime"),
        ("WWP-ESM-MIB", "moExtraProperties"),
        ("WWP-ESM-MIB", "moIpAddress"))
)
if mibBuilder.loadTexts:
    moAttrChangeNotification.setStatus(
        "current"
    )

alertCriticalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 1)
)
alertCriticalNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertOwnerName"),
        ("WWP-ESM-MIB", "notiAlertCategory"),
        ("WWP-ESM-MIB", "notiAlertDescription"),
        ("WWP-ESM-MIB", "notiAlertTimeStamp"),
        ("WWP-ESM-MIB", "notiAlertNotificationId"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"),
        ("WWP-ESM-MIB", "notiAlertIpAddress"))
)
if mibBuilder.loadTexts:
    alertCriticalNotification.setStatus(
        "current"
    )

alertMajorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 2)
)
alertMajorNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "notiAlertCategory"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertOwnerName"),
        ("WWP-ESM-MIB", "notiAlertDescription"),
        ("WWP-ESM-MIB", "notiAlertNotificationId"),
        ("WWP-ESM-MIB", "notiAlertTimeStamp"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"),
        ("WWP-ESM-MIB", "notiAlertIpAddress"))
)
if mibBuilder.loadTexts:
    alertMajorNotification.setStatus(
        "current"
    )

alertMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 3)
)
alertMinorNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "notiAlertCategory"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertOwnerName"),
        ("WWP-ESM-MIB", "notiAlertDescription"),
        ("WWP-ESM-MIB", "notiAlertTimeStamp"),
        ("WWP-ESM-MIB", "notiAlertNotificationId"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"),
        ("WWP-ESM-MIB", "notiAlertIpAddress"))
)
if mibBuilder.loadTexts:
    alertMinorNotification.setStatus(
        "current"
    )

alertWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 4)
)
alertWarningNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "notiAlertCategory"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertOwnerName"),
        ("WWP-ESM-MIB", "notiAlertDescription"),
        ("WWP-ESM-MIB", "notiAlertTimeStamp"),
        ("WWP-ESM-MIB", "notiAlertNotificationId"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"),
        ("WWP-ESM-MIB", "notiAlertIpAddress"))
)
if mibBuilder.loadTexts:
    alertWarningNotification.setStatus(
        "current"
    )

alertClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 5)
)
alertClearNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("WWP-ESM-MIB", "sequenceNum"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertOwnerName"),
        ("WWP-ESM-MIB", "notiAlertDescription"),
        ("WWP-ESM-MIB", "notiAlertTimeStamp"),
        ("WWP-ESM-MIB", "notiAlertcategory"),
        ("WWP-ESM-MIB", "notiAlertNotificationId"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"),
        ("WWP-ESM-MIB", "notiAlertIpAddress"))
)
if mibBuilder.loadTexts:
    alertClearNotification.setStatus(
        "current"
    )

alertCustomNBINotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 3, 8, 2, 0, 6)
)
alertCustomNBINotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RFC1213-MIB", "snmpTrapOID"),
        ("RFC1213-MIB", "snmpTrapAddress"),
        ("WWP-ESM-MIB", "notiAlertEmsTime"),
        ("WWP-ESM-MIB", "notiAlertNeTime"),
        ("WWP-ESM-MIB", "notiAlertEmsName"),
        ("WWP-ESM-MIB", "notiAlertEntity"),
        ("WWP-ESM-MIB", "notiAlertNeNodeId"),
        ("WWP-ESM-MIB", "notiAlertNeNodeName"),
        ("WWP-ESM-MIB", "notiAlertObjectType"),
        ("WWP-ESM-MIB", "notiAlertObjectName"),
        ("WWP-ESM-MIB", "notiAlertSeverity"),
        ("WWP-ESM-MIB", "notiAlertServiceAffecting"),
        ("WWP-ESM-MIB", "notiAlertCategory"),
        ("WWP-ESM-MIB", "notiAlertProbableCauseDescription"),
        ("WWP-ESM-MIB", "notiAlertAdditionalText"),
        ("WWP-ESM-MIB", "notiAlertEventType"),
        ("WWP-ESM-MIB", "notiAlertExtraProperties"))
)
if mibBuilder.loadTexts:
    alertCustomNBINotification.setStatus(
        "current"
    )

thresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 4, 7, 1, 0, 1)
)
thresholdNotification.setObjects(
      *(("WWP-ESM-MIB", "thresholdObjectName"),
        ("WWP-ESM-MIB", "thresholdKind"),
        ("WWP-ESM-MIB", "thresholdMessage"),
        ("WWP-ESM-MIB", "thresholdSeverity"))
)
if mibBuilder.loadTexts:
    thresholdNotification.setStatus(
        "current"
    )

ismStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 1)
)
ismStateChangeNotification.setObjects(
      *(("WWP-ESM-MIB", "currentState"),
        ("WWP-ESM-MIB", "previousState"),
        ("WWP-ESM-MIB", "uniqueIdentifier"),
        ("WWP-ESM-MIB", "statsCounters"),
        ("WWP-ESM-MIB", "stateChangeTime"),
        ("WWP-ESM-MIB", "ismExtraProperties"))
)
if mibBuilder.loadTexts:
    ismStateChangeNotification.setStatus(
        "current"
    )

ismNodeChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 2)
)
ismNodeChangeNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "nodeChangeTime"),
        ("WWP-ESM-MIB", "ismExtraProperties"))
)
if mibBuilder.loadTexts:
    ismNodeChangeNotification.setStatus(
        "current"
    )

ismNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 3)
)
ismNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismNotification.setStatus(
        "current"
    )

ismBadParameterNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 4)
)
ismBadParameterNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismBadParameterNotification.setStatus(
        "current"
    )

ismConstraintViolationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 5)
)
ismConstraintViolationNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismConstraintViolationNotification.setStatus(
        "current"
    )

ismMisconfigurationDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 6)
)
ismMisconfigurationDetectedNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismMisconfigurationDetectedNotification.setStatus(
        "current"
    )

ismUnsupportedConfigurationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 7)
)
ismUnsupportedConfigurationNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismUnsupportedConfigurationNotification.setStatus(
        "current"
    )

ismInvalidPathSelectionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 8)
)
ismInvalidPathSelectionNotification.setObjects(
      *(("WWP-ESM-MIB", "node"),
        ("WWP-ESM-MIB", "text"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"))
)
if mibBuilder.loadTexts:
    ismInvalidPathSelectionNotification.setStatus(
        "current"
    )

ismModifyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 62, 1, 12, 1, 2, 0, 9)
)
ismModifyNotification.setObjects(
      *(("WWP-ESM-MIB", "currentState"),
        ("WWP-ESM-MIB", "uniqueIdentifier"),
        ("WWP-ESM-MIB", "ismExtraProperties"),
        ("WWP-ESM-MIB", "notifTime"),
        ("WWP-ESM-MIB", "status"))
)
if mibBuilder.loadTexts:
    ismModifyNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-ESM-MIB",
    **{"wwpModulesEsm": wwpModulesEsm,
       "wwpESM": wwpESM,
       "wwpESMSystem": wwpESMSystem,
       "wwpESMVersion": wwpESMVersion,
       "wwpESMHost": wwpESMHost,
       "wwpESMIpAddress": wwpESMIpAddress,
       "wwpESMTotalMemory": wwpESMTotalMemory,
       "wwpESMFreeMemory": wwpESMFreeMemory,
       "wwpESMStartTime": wwpESMStartTime,
       "wwpESMUpTime": wwpESMUpTime,
       "wwpESMShutdown": wwpESMShutdown,
       "wwpESMPorts": wwpESMPorts,
       "httpPort": httpPort,
       "esmSocketPort": esmSocketPort,
       "rmiRegistryPort": rmiRegistryPort,
       "trapPortTable": trapPortTable,
       "trapPortEntry": trapPortEntry,
       "seqNum": seqNum,
       "port": port,
       "wwpESMSchedulerTable": wwpESMSchedulerTable,
       "wwpESMschedulerEntry": wwpESMschedulerEntry,
       "wwpESMSchedulerIndex": wwpESMSchedulerIndex,
       "wwpESMSchedulerDesc": wwpESMSchedulerDesc,
       "wwpESMSchedulerNumTasks": wwpESMSchedulerNumTasks,
       "wwpESMSchedulerNumThreads": wwpESMSchedulerNumThreads,
       "wwpESMSchedulerActiveThreads": wwpESMSchedulerActiveThreads,
       "wwpESMSchedulerIdleThreads": wwpESMSchedulerIdleThreads,
       "wwpESMTopoMib": wwpESMTopoMib,
       "wwpESMNumObjects": wwpESMNumObjects,
       "wwpESMNumNetworks": wwpESMNumNetworks,
       "wwpESMNumNodes": wwpESMNumNodes,
       "wwpESMNumInterfaces": wwpESMNumInterfaces,
       "moUserPropNames": moUserPropNames,
       "moTable": moTable,
       "moEntry": moEntry,
       "moNameIndex": moNameIndex,
       "moOwnerName": moOwnerName,
       "moType": moType,
       "moFailureCount": moFailureCount,
       "moFailureThreshold": moFailureThreshold,
       "moManaged": moManaged,
       "moStatus": moStatus,
       "moStatusChangeTime": moStatusChangeTime,
       "moStatusUpdateTime": moStatusUpdateTime,
       "moPollInterval": moPollInterval,
       "moUserProperties": moUserProperties,
       "moDerivedProperties": moDerivedProperties,
       "inheritingOid1": inheritingOid1,
       "inheritingTableName1": inheritingTableName1,
       "topoObjTable": topoObjTable,
       "topoObjEntry": topoObjEntry,
       "ipAddress": ipAddress,
       "netmask": netmask,
       "moCommunity": moCommunity,
       "moWriteCommunity": moWriteCommunity,
       "snmpPort": snmpPort,
       "isDHCP": isDHCP,
       "baseMibs": baseMibs,
       "version": version,
       "userName": userName,
       "contextName": contextName,
       "inheritingOid2": inheritingOid2,
       "inheritingTableName2": inheritingTableName2,
       "networkTable": networkTable,
       "networkEntry": networkEntry,
       "discover": discover,
       "discoverStatus": discoverStatus,
       "inheritingOid3": inheritingOid3,
       "inheritingTableName3": inheritingTableName3,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "isRouter": isRouter,
       "inheritingOid4": inheritingOid4,
       "inheritingTableName4": inheritingTableName4,
       "ipAddressTable": ipAddressTable,
       "ipAddressEntry": ipAddressEntry,
       "parentNode": parentNode,
       "parentNet": parentNet,
       "inheritingOid5": inheritingOid5,
       "inheritingTableName5": inheritingTableName5,
       "snmpNodeTable": snmpNodeTable,
       "snmpNodeEntry": snmpNodeEntry,
       "hostNetMask": hostNetMask,
       "sysDesc": sysDesc,
       "sysName": sysName,
       "sysOid": sysOid,
       "inheritingOid6": inheritingOid6,
       "inheritingTableName6": inheritingTableName6,
       "snmpInterfaceTable": snmpInterfaceTable,
       "snmpInterfaceEntry": snmpInterfaceEntry,
       "hostnetMask": hostnetMask,
       "ifIndex": ifIndex,
       "physMedia": physMedia,
       "physAddress": physAddress,
       "ifSpeed": ifSpeed,
       "ifDesc": ifDesc,
       "sysOID": sysOID,
       "inheritingOid7": inheritingOid7,
       "inheritingTableName7": inheritingTableName7,
       "moDerivedPropNameTable": moDerivedPropNameTable,
       "moDerivedPropNameEntry": moDerivedPropNameEntry,
       "indexNum": indexNum,
       "objClassName": objClassName,
       "derivedPropNames": derivedPropNames,
       "tableOid": tableOid,
       "tableName": tableName,
       "moNotificationMib": moNotificationMib,
       "moExtraPropNames": moExtraPropNames,
       "moNotiPrefix": moNotiPrefix,
       "moNotifications": moNotifications,
       "moEnrolNotification": moEnrolNotification,
       "moDeenrolNotification": moDeenrolNotification,
       "moAttrChangeNotification": moAttrChangeNotification,
       "moNotiVarbinds": moNotiVarbinds,
       "moName": moName,
       "moownerName": moownerName,
       "moNodeType": moNodeType,
       "moEnrolTime": moEnrolTime,
       "moDeEnrolTime": moDeEnrolTime,
       "moDataChangeTime": moDataChangeTime,
       "moExtraProperties": moExtraProperties,
       "moIpAddress": moIpAddress,
       "wwpESMFaultMib": wwpESMFaultMib,
       "wwpESMNumEvents": wwpESMNumEvents,
       "wwpESMNumAlerts": wwpESMNumAlerts,
       "wwpESMEventsInBuffer": wwpESMEventsInBuffer,
       "wwpESMAlertsInBuffer": wwpESMAlertsInBuffer,
       "alertUserPropNames": alertUserPropNames,
       "eventUserPropNames": eventUserPropNames,
       "alertTable": alertTable,
       "alertEntry": alertEntry,
       "alertEntity": alertEntity,
       "alertOwnerName": alertOwnerName,
       "alertCreateTime": alertCreateTime,
       "alertSource": alertSource,
       "alertModTime": alertModTime,
       "alertSeverity": alertSeverity,
       "alertPreviousSeverity": alertPreviousSeverity,
       "alertCategory": alertCategory,
       "alertUserProperties": alertUserProperties,
       "alertNotificationMib": alertNotificationMib,
       "alertExtraPropNames": alertExtraPropNames,
       "alertNotiPrefix": alertNotiPrefix,
       "alertNotifications": alertNotifications,
       "alertCriticalNotification": alertCriticalNotification,
       "alertMajorNotification": alertMajorNotification,
       "alertMinorNotification": alertMinorNotification,
       "alertWarningNotification": alertWarningNotification,
       "alertClearNotification": alertClearNotification,
       "alertCustomNBINotification": alertCustomNBINotification,
       "alertNotiVarbinds": alertNotiVarbinds,
       "notiAlertEntity": notiAlertEntity,
       "notiAlertOwnerName": notiAlertOwnerName,
       "notiAlertDescription": notiAlertDescription,
       "notiAlertTimeStamp": notiAlertTimeStamp,
       "notiAlertNotificationId": notiAlertNotificationId,
       "notiAlertCategory": notiAlertCategory,
       "notiAlertExtraProperties": notiAlertExtraProperties,
       "notiAlertIpAddress": notiAlertIpAddress,
       "notiAlertEmsTime": notiAlertEmsTime,
       "notiAlertNeTime": notiAlertNeTime,
       "notiAlertEmsName": notiAlertEmsName,
       "notiAlertNeNodeId": notiAlertNeNodeId,
       "notiAlertObjectType": notiAlertObjectType,
       "notiAlertObjectName": notiAlertObjectName,
       "notiAlertSeverity": notiAlertSeverity,
       "notiAlertServiceAffecting": notiAlertServiceAffecting,
       "notiAlertProbableCauseDescription": notiAlertProbableCauseDescription,
       "notiAlertAdditionalText": notiAlertAdditionalText,
       "notiAlertEventType": notiAlertEventType,
       "notiAlertNeNodeName": notiAlertNeNodeName,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "evtID": evtID,
       "evtSource": evtSource,
       "evtEntity": evtEntity,
       "evtSeverity": evtSeverity,
       "evtCategory": evtCategory,
       "evtTime": evtTime,
       "evtText": evtText,
       "eventUserProperties": eventUserProperties,
       "wwpESMSeverityTable": wwpESMSeverityTable,
       "wwpESMSeverityEntry": wwpESMSeverityEntry,
       "severityName": severityName,
       "numberOfAlarms": numberOfAlarms,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmSource": alarmSource,
       "alarmOwnerName": alarmOwnerName,
       "alarmEntity": alarmEntity,
       "alarmSeverity": alarmSeverity,
       "alarmPreviousSeverity": alarmPreviousSeverity,
       "alarmCreateTime": alarmCreateTime,
       "alarmModTime": alarmModTime,
       "alarmCategory": alarmCategory,
       "alarmAssignedTo": alarmAssignedTo,
       "alarmUserProperties": alarmUserProperties,
       "wwpESMPerformanceMib": wwpESMPerformanceMib,
       "numPollObjects": numPollObjects,
       "numActivePollers": numActivePollers,
       "numThresholdObjects": numThresholdObjects,
       "pollTable": pollTable,
       "pollEntry": pollEntry,
       "pollid": pollid,
       "polldataName": polldataName,
       "oid": oid,
       "pollingInterval": pollingInterval,
       "failureCount": failureCount,
       "failureThreshold": failureThreshold,
       "timeToPoll": timeToPoll,
       "polledTime": polledTime,
       "agentName": agentName,
       "thresholdTable": thresholdTable,
       "thresholdEntry": thresholdEntry,
       "thresholdObjectName": thresholdObjectName,
       "thresholdKind": thresholdKind,
       "thresholdMessage": thresholdMessage,
       "thresholdClearMessage": thresholdClearMessage,
       "thresholdSeverity": thresholdSeverity,
       "thresholdCategory": thresholdCategory,
       "statsdata": statsdata,
       "statsdataTableName": statsdataTableName,
       "statsDataTable": statsDataTable,
       "statsDataEntry": statsDataEntry,
       "pollID": pollID,
       "time": time,
       "oidindex": oidindex,
       "value": value,
       "perfNotificationMib": perfNotificationMib,
       "perfNotiConfigPrefix": perfNotiConfigPrefix,
       "perfNotifications": perfNotifications,
       "thresholdNotification": thresholdNotification,
       "perfNotiVarbinds": perfNotiVarbinds,
       "eventid": eventid,
       "eventsource": eventsource,
       "eventEntity": eventEntity,
       "eventGenTime": eventGenTime,
       "eventSeverity": eventSeverity,
       "persistentTrapsMib": persistentTrapsMib,
       "maxRows": maxRows,
       "sequenceNum": sequenceNum,
       "notiLogTable": notiLogTable,
       "notiLogEntry": notiLogEntry,
       "notiLogIndex": notiLogIndex,
       "notiLogTime": notiLogTime,
       "notiLogNumVarBinds": notiLogNumVarBinds,
       "notiLogOid": notiLogOid,
       "varbindLogTable": varbindLogTable,
       "varbindLogEntry": varbindLogEntry,
       "varbindIndex": varbindIndex,
       "varbindType": varbindType,
       "varbindValue": varbindValue,
       "tftpMib": tftpMib,
       "serverName": serverName,
       "portNum": portNum,
       "sourceFile": sourceFile,
       "destinationFile": destinationFile,
       "tftpMode": tftpMode,
       "request": request,
       "proxyService": proxyService,
       "proxyTable": proxyTable,
       "proxyEntry": proxyEntry,
       "serialNumber": serialNumber,
       "hostName": hostName,
       "devicePort": devicePort,
       "requestOid": requestOid,
       "community": community,
       "service": service,
       "result": result,
       "subagents": subagents,
       "subAgentTable": subAgentTable,
       "subAgentEntry": subAgentEntry,
       "subAgentoid": subAgentoid,
       "subAgent": subAgent,
       "subAgentPort": subAgentPort,
       "subAgentVersion": subAgentVersion,
       "subAgentCommunity": subAgentCommunity,
       "timeout": timeout,
       "subAgentRetries": subAgentRetries,
       "rowStatus": rowStatus,
       "trapForwardingModule": trapForwardingModule,
       "v1v2TrapForwardingTable": v1v2TrapForwardingTable,
       "v1v2TrapForwardingEntry": v1v2TrapForwardingEntry,
       "v1v2ManagerHost": v1v2ManagerHost,
       "v1v2ManagerPort": v1v2ManagerPort,
       "v1v2ManagerVersion": v1v2ManagerVersion,
       "v1v2ManagerCommunity": v1v2ManagerCommunity,
       "v1v2ManagerTimeOut": v1v2ManagerTimeOut,
       "v1v2ManagerRetries": v1v2ManagerRetries,
       "v1v2ManagerStatus": v1v2ManagerStatus,
       "v3TrapForwardingTable": v3TrapForwardingTable,
       "v3TrapForwardingEntry": v3TrapForwardingEntry,
       "v3ManagerHost": v3ManagerHost,
       "v3ManagerPort": v3ManagerPort,
       "v3ManagerVersion": v3ManagerVersion,
       "v3ManagerCommunity": v3ManagerCommunity,
       "v3ManagerUserName": v3ManagerUserName,
       "v3ManagerUserSecModel": v3ManagerUserSecModel,
       "v3ManagerUserSecLevel": v3ManagerUserSecLevel,
       "v3ManagerUserContextName": v3ManagerUserContextName,
       "v3ManagerTimeOut": v3ManagerTimeOut,
       "v3ManagerRetries": v3ManagerRetries,
       "v3ManagerStatus": v3ManagerStatus,
       "esmConfiguration": esmConfiguration,
       "topologyConfiguration": topologyConfiguration,
       "autoDiscover": autoDiscover,
       "discoverLocalNet": discoverLocalNet,
       "discoverInterval": discoverInterval,
       "enablelog": enablelog,
       "rediscoveryConfiguration": rediscoveryConfiguration,
       "reDiscover": reDiscover,
       "reDiscoverInterval": reDiscoverInterval,
       "hour": hour,
       "dayOfWeek": dayOfWeek,
       "dayOfMonth": dayOfMonth,
       "snmpPingConfiguration": snmpPingConfiguration,
       "enableSnmpPing": enableSnmpPing,
       "snmpPingRetries": snmpPingRetries,
       "snmpPingTimeout": snmpPingTimeout,
       "snmpport": snmpport,
       "readCommunity": readCommunity,
       "writeCommunity": writeCommunity,
       "snmpV3Configuration": snmpV3Configuration,
       "enableV3": enableV3,
       "v3Username": v3Username,
       "v3Contextname": v3Contextname,
       "icmpPingConfiguration": icmpPingConfiguration,
       "enableIcmp": enableIcmp,
       "icmpPingRetries": icmpPingRetries,
       "nativePingConfiguration": nativePingConfiguration,
       "nativePingRetries": nativePingRetries,
       "nativePingTimeOut": nativePingTimeOut,
       "debugLevel": debugLevel,
       "enableSweep": enableSweep,
       "sweepPkts": sweepPkts,
       "sweepSleepInterval": sweepSleepInterval,
       "networkDiscoveryTable": networkDiscoveryTable,
       "networkDiscoveryEntry": networkDiscoveryEntry,
       "networkDiscoveryIndex": networkDiscoveryIndex,
       "netIPAddress": netIPAddress,
       "netMask": netMask,
       "startIPAddress": startIPAddress,
       "endIPAddress": endIPAddress,
       "doDiscovery": doDiscovery,
       "dhcp": dhcp,
       "nodeDiscoveryTable": nodeDiscoveryTable,
       "nodeDiscoveryEntry": nodeDiscoveryEntry,
       "nodeIP": nodeIP,
       "nodeNetMask": nodeNetMask,
       "nodeDiscoverEnable": nodeDiscoverEnable,
       "snmpAgentPort": snmpAgentPort,
       "nodeCommunity": nodeCommunity,
       "snmpVersion": snmpVersion,
       "v3UserName": v3UserName,
       "v3ContextName": v3ContextName,
       "moCriteriaTable": moCriteriaTable,
       "moCriteriaEntry": moCriteriaEntry,
       "criteriaIndex": criteriaIndex,
       "propertyName": propertyName,
       "propertyValue": propertyValue,
       "allow": allow,
       "discoveryFilterTable": discoveryFilterTable,
       "discoveryFilterEntry": discoveryFilterEntry,
       "discFilterIndex": discFilterIndex,
       "discFilterClassName": discFilterClassName,
       "faultConfIguration": faultConfIguration,
       "trapFilterTable": trapFilterTable,
       "trapFilterEntry": trapFilterEntry,
       "trapFilterIndex": trapFilterIndex,
       "alertFilterClassName": alertFilterClassName,
       "trapFilterName": trapFilterName,
       "trapFilterEnable": trapFilterEnable,
       "genericType": genericType,
       "specificType": specificType,
       "enterpriseOID": enterpriseOID,
       "trapOID": trapOID,
       "setFilter": setFilter,
       "performanceConfiguration": performanceConfiguration,
       "pollingFiltersTable": pollingFiltersTable,
       "pollingFiltersEntry": pollingFiltersEntry,
       "pollingFilterIndex": pollingFilterIndex,
       "pollingFilterClassName": pollingFilterClassName,
       "logConfiguration": logConfiguration,
       "stdout": stdout,
       "name": name,
       "directory": directory,
       "numFiles": numFiles,
       "numLines": numLines,
       "logging": logging,
       "timestamp": timestamp,
       "stderr": stderr,
       "filename": filename,
       "logDirectory": logDirectory,
       "filenum": filenum,
       "linenum": linenum,
       "log": log,
       "logTime": logTime,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logFileName": logFileName,
       "logDirName": logDirName,
       "maxLines": maxLines,
       "maxFiles": maxFiles,
       "linesCached": linesCached,
       "timeStamp": timeStamp,
       "logUserTable": logUserTable,
       "logUserEntry": logUserEntry,
       "logUserIndex": logUserIndex,
       "logUserName": logUserName,
       "displayName": displayName,
       "logLevel": logLevel,
       "enableLog": enableLog,
       "agentConfiguration": agentConfiguration,
       "v1v2AuthenticationTables": v1v2AuthenticationTables,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclCommunity": aclCommunity,
       "aclAccess": aclAccess,
       "aclManagers": aclManagers,
       "aclStatus": aclStatus,
       "vaclTable": vaclTable,
       "vaclEntry": vaclEntry,
       "vaclmibViews": vaclmibViews,
       "vaclviewStatus": vaclviewStatus,
       "ismMib": ismMib,
       "ismNotificationMib": ismNotificationMib,
       "ismExtraPropNames": ismExtraPropNames,
       "ismNotiPrefix": ismNotiPrefix,
       "ismNotifications": ismNotifications,
       "ismStateChangeNotification": ismStateChangeNotification,
       "ismNodeChangeNotification": ismNodeChangeNotification,
       "ismNotification": ismNotification,
       "ismBadParameterNotification": ismBadParameterNotification,
       "ismConstraintViolationNotification": ismConstraintViolationNotification,
       "ismMisconfigurationDetectedNotification": ismMisconfigurationDetectedNotification,
       "ismUnsupportedConfigurationNotification": ismUnsupportedConfigurationNotification,
       "ismInvalidPathSelectionNotification": ismInvalidPathSelectionNotification,
       "ismModifyNotification": ismModifyNotification,
       "ismNotiVarbinds": ismNotiVarbinds,
       "currentState": currentState,
       "previousState": previousState,
       "uniqueIdentifier": uniqueIdentifier,
       "stateChangeTime": stateChangeTime,
       "statsCounters": statsCounters,
       "nodeChangeTime": nodeChangeTime,
       "node": node,
       "ismExtraProperties": ismExtraProperties,
       "text": text,
       "notifTime": notifTime,
       "status": status}
)
