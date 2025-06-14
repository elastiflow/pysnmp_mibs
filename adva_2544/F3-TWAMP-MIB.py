# SNMP MIB module (F3-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-TWAMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex")

(IpMode,) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "IpMode")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3TwampMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33)
)
if mibBuilder.loadTexts:
    f3TwampMIB.setRevisions(
        ("2014-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TwampControlClientStatus(TextualConvention, Integer32):
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
        *(("init", 1),
          ("twampControlDisabled", 2),
          ("twampControlEnabled", 3),
          ("waitForConnectionAck", 4))
    )



class TwampServerStatus(TextualConvention, Integer32):
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
        *(("init", 1),
          ("twampControlDisabled", 2),
          ("twampControlEnabled", 3))
    )



class TwampClientConnStatus(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("waitingForServerGreeting", 2),
          ("waitingForServerStart", 3),
          ("requestSessions", 4),
          ("waitingForStartAck", 5),
          ("testInProgress", 6),
          ("waitingForTestCompletions", 7))
    )



class TwampServerConnStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("waitingForSessions", 2),
          ("testInProgress", 3),
          ("waitingForSessionIntransitTimeouts", 4),
          ("end", 5))
    )



class TwampSessionSenderStatus(TextualConvention, Integer32):
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
        *(("init", 1),
          ("idle", 2),
          ("testInProgress", 3),
          ("waitingForTestCompletion", 4))
    )



class TwampSessionReflectorStatus(TextualConvention, Integer32):
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
        *(("init", 1),
          ("testReady", 2),
          ("waitingForIntransitTimeout", 3),
          ("end", 4))
    )



class TwampSessionStatus(TextualConvention, Integer32):
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
        *(("init", 1),
          ("testInProgress", 2),
          ("idle", 3))
    )



class TwampPktSchedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("expPseudoRandom", 2))
    )



class TwampTestPattern(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("allZeros", 1)
    )



class TwampPmIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("curr", 1),
          ("rollover", 2))
    )



class TwampHistoryIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("interval1min", 1),
          ("interval5min", 2),
          ("interval10min", 3),
          ("interval15min", 4),
          ("interval60min", 5))
    )



class TwampDistStatsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("twoWayPd", 1),
          ("oneWayS2RPd", 2),
          ("oneWayR2SPd", 3),
          ("oneWayS2RPdv", 4),
          ("oneWayR2SPdv", 5))
    )



class TwampStartTimeType(TextualConvention, Integer32):
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
        *(("immediate", 1),
          ("relative", 2),
          ("fixed", 3))
    )



class TwampServerAction(TextualConvention, Integer32):
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
        *(("noAction", 1),
          ("addSessReflector", 2),
          ("rmvSessReflector", 3))
    )



class TwampControlClientAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("addSessSender", 2),
          ("rmvSessSender", 3),
          ("startSessions", 4),
          ("stopSessions", 5))
    )



class TwampSessionAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearSequenceNumber", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3TwampConfigObjects_ObjectIdentity = ObjectIdentity
f3TwampConfigObjects = _F3TwampConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1)
)
_F3TwampIpInterfaceTable_Object = MibTable
f3TwampIpInterfaceTable = _F3TwampIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1)
)
if mibBuilder.loadTexts:
    f3TwampIpInterfaceTable.setStatus("current")
_F3TwampIpInterfaceEntry_Object = MibTableRow
f3TwampIpInterfaceEntry = _F3TwampIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1)
)
f3TwampIpInterfaceEntry.setIndexNames(
    (0, "F3-TWAMP-MIB", "f3TwampIpInterfaceName"),
)
if mibBuilder.loadTexts:
    f3TwampIpInterfaceEntry.setStatus("current")


class _F3TwampIpInterfaceName_Type(DisplayString):
    """Custom type f3TwampIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3TwampIpInterfaceName_Type.__name__ = "DisplayString"
_F3TwampIpInterfaceName_Object = MibTableColumn
f3TwampIpInterfaceName = _F3TwampIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 1),
    _F3TwampIpInterfaceName_Type()
)
f3TwampIpInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceName.setStatus("current")
_F3TwampIpInterfacePort_Type = VariablePointer
_F3TwampIpInterfacePort_Object = MibTableColumn
f3TwampIpInterfacePort = _F3TwampIpInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 2),
    _F3TwampIpInterfacePort_Type()
)
f3TwampIpInterfacePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfacePort.setStatus("current")
_F3TwampIpInterfaceIpMode_Type = IpMode
_F3TwampIpInterfaceIpMode_Object = MibTableColumn
f3TwampIpInterfaceIpMode = _F3TwampIpInterfaceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 3),
    _F3TwampIpInterfaceIpMode_Type()
)
f3TwampIpInterfaceIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceIpMode.setStatus("current")
_F3TwampIpInterfaceIpv4Address_Type = IpAddress
_F3TwampIpInterfaceIpv4Address_Object = MibTableColumn
f3TwampIpInterfaceIpv4Address = _F3TwampIpInterfaceIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 4),
    _F3TwampIpInterfaceIpv4Address_Type()
)
f3TwampIpInterfaceIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceIpv4Address.setStatus("current")
_F3TwampIpInterfaceIpv4Mask_Type = IpAddress
_F3TwampIpInterfaceIpv4Mask_Object = MibTableColumn
f3TwampIpInterfaceIpv4Mask = _F3TwampIpInterfaceIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 5),
    _F3TwampIpInterfaceIpv4Mask_Type()
)
f3TwampIpInterfaceIpv4Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceIpv4Mask.setStatus("current")


class _F3TwampIpInterfaceMtu_Type(Integer32):
    """Custom type f3TwampIpInterfaceMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_F3TwampIpInterfaceMtu_Type.__name__ = "Integer32"
_F3TwampIpInterfaceMtu_Object = MibTableColumn
f3TwampIpInterfaceMtu = _F3TwampIpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 6),
    _F3TwampIpInterfaceMtu_Type()
)
f3TwampIpInterfaceMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceMtu.setStatus("current")
_F3TwampIpInterfaceStorageType_Type = StorageType
_F3TwampIpInterfaceStorageType_Object = MibTableColumn
f3TwampIpInterfaceStorageType = _F3TwampIpInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 7),
    _F3TwampIpInterfaceStorageType_Type()
)
f3TwampIpInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceStorageType.setStatus("current")
_F3TwampIpInterfaceRowStatus_Type = RowStatus
_F3TwampIpInterfaceRowStatus_Object = MibTableColumn
f3TwampIpInterfaceRowStatus = _F3TwampIpInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 1, 1, 8),
    _F3TwampIpInterfaceRowStatus_Type()
)
f3TwampIpInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampIpInterfaceRowStatus.setStatus("current")
_F3TwampServerTable_Object = MibTable
f3TwampServerTable = _F3TwampServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2)
)
if mibBuilder.loadTexts:
    f3TwampServerTable.setStatus("current")
_F3TwampServerEntry_Object = MibTableRow
f3TwampServerEntry = _F3TwampServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1)
)
f3TwampServerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampServerIndex"),
)
if mibBuilder.loadTexts:
    f3TwampServerEntry.setStatus("current")


class _F3TwampServerIndex_Type(Integer32):
    """Custom type f3TwampServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampServerIndex_Type.__name__ = "Integer32"
_F3TwampServerIndex_Object = MibTableColumn
f3TwampServerIndex = _F3TwampServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 1),
    _F3TwampServerIndex_Type()
)
f3TwampServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampServerIndex.setStatus("current")
_F3TwampServerAdminState_Type = AdminState
_F3TwampServerAdminState_Object = MibTableColumn
f3TwampServerAdminState = _F3TwampServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 2),
    _F3TwampServerAdminState_Type()
)
f3TwampServerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampServerAdminState.setStatus("current")
_F3TwampServerOperationalState_Type = OperationalState
_F3TwampServerOperationalState_Object = MibTableColumn
f3TwampServerOperationalState = _F3TwampServerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 3),
    _F3TwampServerOperationalState_Type()
)
f3TwampServerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampServerOperationalState.setStatus("current")
_F3TwampServerSecondaryState_Type = SecondaryState
_F3TwampServerSecondaryState_Object = MibTableColumn
f3TwampServerSecondaryState = _F3TwampServerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 4),
    _F3TwampServerSecondaryState_Type()
)
f3TwampServerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampServerSecondaryState.setStatus("current")


class _F3TwampServerAlias_Type(DisplayString):
    """Custom type f3TwampServerAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3TwampServerAlias_Type.__name__ = "DisplayString"
_F3TwampServerAlias_Object = MibTableColumn
f3TwampServerAlias = _F3TwampServerAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 5),
    _F3TwampServerAlias_Type()
)
f3TwampServerAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerAlias.setStatus("current")
_F3TwampServerPort_Type = VariablePointer
_F3TwampServerPort_Object = MibTableColumn
f3TwampServerPort = _F3TwampServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 6),
    _F3TwampServerPort_Type()
)
f3TwampServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerPort.setStatus("current")
_F3TwampServerStatus_Type = TwampServerStatus
_F3TwampServerStatus_Object = MibTableColumn
f3TwampServerStatus = _F3TwampServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 7),
    _F3TwampServerStatus_Type()
)
f3TwampServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampServerStatus.setStatus("current")


class _F3TwampServerSessionIdleTimeout_Type(Unsigned32):
    """Custom type f3TwampServerSessionIdleTimeout based on Unsigned32"""
    defaultValue = 5


_F3TwampServerSessionIdleTimeout_Type.__name__ = "Unsigned32"
_F3TwampServerSessionIdleTimeout_Object = MibTableColumn
f3TwampServerSessionIdleTimeout = _F3TwampServerSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 8),
    _F3TwampServerSessionIdleTimeout_Type()
)
f3TwampServerSessionIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerSessionIdleTimeout.setStatus("current")


class _F3TwampServerSessionAgingTimeout_Type(Unsigned32):
    """Custom type f3TwampServerSessionAgingTimeout based on Unsigned32"""
    defaultValue = 900


_F3TwampServerSessionAgingTimeout_Type.__name__ = "Unsigned32"
_F3TwampServerSessionAgingTimeout_Object = MibTableColumn
f3TwampServerSessionAgingTimeout = _F3TwampServerSessionAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 9),
    _F3TwampServerSessionAgingTimeout_Type()
)
f3TwampServerSessionAgingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerSessionAgingTimeout.setStatus("current")
_F3TwampServerActionObject_Type = VariablePointer
_F3TwampServerActionObject_Object = MibTableColumn
f3TwampServerActionObject = _F3TwampServerActionObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 10),
    _F3TwampServerActionObject_Type()
)
f3TwampServerActionObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerActionObject.setStatus("current")
_F3TwampServerAction_Type = TwampServerAction
_F3TwampServerAction_Object = MibTableColumn
f3TwampServerAction = _F3TwampServerAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 11),
    _F3TwampServerAction_Type()
)
f3TwampServerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerAction.setStatus("current")
_F3TwampServerStorageType_Type = StorageType
_F3TwampServerStorageType_Object = MibTableColumn
f3TwampServerStorageType = _F3TwampServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 12),
    _F3TwampServerStorageType_Type()
)
f3TwampServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerStorageType.setStatus("current")
_F3TwampServerRowStatus_Type = RowStatus
_F3TwampServerRowStatus_Object = MibTableColumn
f3TwampServerRowStatus = _F3TwampServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 2, 1, 13),
    _F3TwampServerRowStatus_Type()
)
f3TwampServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampServerRowStatus.setStatus("current")
_F3TwampServerSessionReflectorTable_Object = MibTable
f3TwampServerSessionReflectorTable = _F3TwampServerSessionReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 3)
)
if mibBuilder.loadTexts:
    f3TwampServerSessionReflectorTable.setStatus("current")
_F3TwampServerSessionReflectorEntry_Object = MibTableRow
f3TwampServerSessionReflectorEntry = _F3TwampServerSessionReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 3, 1)
)
f3TwampServerSessionReflectorEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampServerIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampServerSessionReflectorIndex"),
)
if mibBuilder.loadTexts:
    f3TwampServerSessionReflectorEntry.setStatus("current")


class _F3TwampServerSessionReflectorIndex_Type(Integer32):
    """Custom type f3TwampServerSessionReflectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampServerSessionReflectorIndex_Type.__name__ = "Integer32"
_F3TwampServerSessionReflectorIndex_Object = MibTableColumn
f3TwampServerSessionReflectorIndex = _F3TwampServerSessionReflectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 3, 1, 1),
    _F3TwampServerSessionReflectorIndex_Type()
)
f3TwampServerSessionReflectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampServerSessionReflectorIndex.setStatus("current")
_F3TwampServerSessionReflector_Type = VariablePointer
_F3TwampServerSessionReflector_Object = MibTableColumn
f3TwampServerSessionReflector = _F3TwampServerSessionReflector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 3, 1, 2),
    _F3TwampServerSessionReflector_Type()
)
f3TwampServerSessionReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampServerSessionReflector.setStatus("current")
_F3TwampSessionReflectorTable_Object = MibTable
f3TwampSessionReflectorTable = _F3TwampSessionReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4)
)
if mibBuilder.loadTexts:
    f3TwampSessionReflectorTable.setStatus("current")
_F3TwampSessionReflectorEntry_Object = MibTableRow
f3TwampSessionReflectorEntry = _F3TwampSessionReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1)
)
f3TwampSessionReflectorEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionReflectorIndex"),
)
if mibBuilder.loadTexts:
    f3TwampSessionReflectorEntry.setStatus("current")


class _F3TwampSessionReflectorIndex_Type(Integer32):
    """Custom type f3TwampSessionReflectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampSessionReflectorIndex_Type.__name__ = "Integer32"
_F3TwampSessionReflectorIndex_Object = MibTableColumn
f3TwampSessionReflectorIndex = _F3TwampSessionReflectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 1),
    _F3TwampSessionReflectorIndex_Type()
)
f3TwampSessionReflectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorIndex.setStatus("current")
_F3TwampSessionReflectorAdminState_Type = AdminState
_F3TwampSessionReflectorAdminState_Object = MibTableColumn
f3TwampSessionReflectorAdminState = _F3TwampSessionReflectorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 2),
    _F3TwampSessionReflectorAdminState_Type()
)
f3TwampSessionReflectorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorAdminState.setStatus("current")
_F3TwampSessionReflectorOperationalState_Type = OperationalState
_F3TwampSessionReflectorOperationalState_Object = MibTableColumn
f3TwampSessionReflectorOperationalState = _F3TwampSessionReflectorOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 3),
    _F3TwampSessionReflectorOperationalState_Type()
)
f3TwampSessionReflectorOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorOperationalState.setStatus("current")
_F3TwampSessionReflectorSecondaryState_Type = SecondaryState
_F3TwampSessionReflectorSecondaryState_Object = MibTableColumn
f3TwampSessionReflectorSecondaryState = _F3TwampSessionReflectorSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 4),
    _F3TwampSessionReflectorSecondaryState_Type()
)
f3TwampSessionReflectorSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorSecondaryState.setStatus("current")


class _F3TwampSessionReflectorAlias_Type(DisplayString):
    """Custom type f3TwampSessionReflectorAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3TwampSessionReflectorAlias_Type.__name__ = "DisplayString"
_F3TwampSessionReflectorAlias_Object = MibTableColumn
f3TwampSessionReflectorAlias = _F3TwampSessionReflectorAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 5),
    _F3TwampSessionReflectorAlias_Type()
)
f3TwampSessionReflectorAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorAlias.setStatus("current")


class _F3TwampSessionReflectorIpInterface_Type(DisplayString):
    """Custom type f3TwampSessionReflectorIpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3TwampSessionReflectorIpInterface_Type.__name__ = "DisplayString"
_F3TwampSessionReflectorIpInterface_Object = MibTableColumn
f3TwampSessionReflectorIpInterface = _F3TwampSessionReflectorIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 6),
    _F3TwampSessionReflectorIpInterface_Type()
)
f3TwampSessionReflectorIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorIpInterface.setStatus("current")


class _F3TwampSessionReflectorUdpPort_Type(Unsigned32):
    """Custom type f3TwampSessionReflectorUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3TwampSessionReflectorUdpPort_Type.__name__ = "Unsigned32"
_F3TwampSessionReflectorUdpPort_Object = MibTableColumn
f3TwampSessionReflectorUdpPort = _F3TwampSessionReflectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 7),
    _F3TwampSessionReflectorUdpPort_Type()
)
f3TwampSessionReflectorUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorUdpPort.setStatus("current")


class _F3TwampSessionReflectorUseSenderSeqNum_Type(TruthValue):
    """Custom type f3TwampSessionReflectorUseSenderSeqNum based on TruthValue"""
    defaultValue = 2


_F3TwampSessionReflectorUseSenderSeqNum_Type.__name__ = "TruthValue"
_F3TwampSessionReflectorUseSenderSeqNum_Object = MibTableColumn
f3TwampSessionReflectorUseSenderSeqNum = _F3TwampSessionReflectorUseSenderSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 8),
    _F3TwampSessionReflectorUseSenderSeqNum_Type()
)
f3TwampSessionReflectorUseSenderSeqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorUseSenderSeqNum.setStatus("current")
_F3TwampSessionReflectorUserCreated_Type = TruthValue
_F3TwampSessionReflectorUserCreated_Object = MibTableColumn
f3TwampSessionReflectorUserCreated = _F3TwampSessionReflectorUserCreated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 9),
    _F3TwampSessionReflectorUserCreated_Type()
)
f3TwampSessionReflectorUserCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorUserCreated.setStatus("current")
_F3TwampSessionReflectorStatus_Type = TwampSessionReflectorStatus
_F3TwampSessionReflectorStatus_Object = MibTableColumn
f3TwampSessionReflectorStatus = _F3TwampSessionReflectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 10),
    _F3TwampSessionReflectorStatus_Type()
)
f3TwampSessionReflectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorStatus.setStatus("current")
_F3TwampSessionReflectorAssocServer_Type = VariablePointer
_F3TwampSessionReflectorAssocServer_Object = MibTableColumn
f3TwampSessionReflectorAssocServer = _F3TwampSessionReflectorAssocServer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 11),
    _F3TwampSessionReflectorAssocServer_Type()
)
f3TwampSessionReflectorAssocServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorAssocServer.setStatus("current")
_F3TwampSessionReflectorStorageType_Type = StorageType
_F3TwampSessionReflectorStorageType_Object = MibTableColumn
f3TwampSessionReflectorStorageType = _F3TwampSessionReflectorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 12),
    _F3TwampSessionReflectorStorageType_Type()
)
f3TwampSessionReflectorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorStorageType.setStatus("current")
_F3TwampSessionReflectorRowStatus_Type = RowStatus
_F3TwampSessionReflectorRowStatus_Object = MibTableColumn
f3TwampSessionReflectorRowStatus = _F3TwampSessionReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 4, 1, 13),
    _F3TwampSessionReflectorRowStatus_Type()
)
f3TwampSessionReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionReflectorRowStatus.setStatus("current")
_F3TwampSessionTable_Object = MibTable
f3TwampSessionTable = _F3TwampSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5)
)
if mibBuilder.loadTexts:
    f3TwampSessionTable.setStatus("current")
_F3TwampSessionEntry_Object = MibTableRow
f3TwampSessionEntry = _F3TwampSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1)
)
f3TwampSessionEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionReflectorIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSsIpv4Address"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSsUdpPort"),
)
if mibBuilder.loadTexts:
    f3TwampSessionEntry.setStatus("current")
_F3TwampSessionSsIpv4Address_Type = IpAddress
_F3TwampSessionSsIpv4Address_Object = MibTableColumn
f3TwampSessionSsIpv4Address = _F3TwampSessionSsIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 1),
    _F3TwampSessionSsIpv4Address_Type()
)
f3TwampSessionSsIpv4Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampSessionSsIpv4Address.setStatus("current")


class _F3TwampSessionSsUdpPort_Type(Unsigned32):
    """Custom type f3TwampSessionSsUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3TwampSessionSsUdpPort_Type.__name__ = "Unsigned32"
_F3TwampSessionSsUdpPort_Object = MibTableColumn
f3TwampSessionSsUdpPort = _F3TwampSessionSsUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 2),
    _F3TwampSessionSsUdpPort_Type()
)
f3TwampSessionSsUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampSessionSsUdpPort.setStatus("current")
_F3TwampSessionStatus_Type = TwampSessionStatus
_F3TwampSessionStatus_Object = MibTableColumn
f3TwampSessionStatus = _F3TwampSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 3),
    _F3TwampSessionStatus_Type()
)
f3TwampSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionStatus.setStatus("current")
_F3TwampSessionVlanEnabled_Type = TruthValue
_F3TwampSessionVlanEnabled_Object = MibTableColumn
f3TwampSessionVlanEnabled = _F3TwampSessionVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 4),
    _F3TwampSessionVlanEnabled_Type()
)
f3TwampSessionVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionVlanEnabled.setStatus("current")
_F3TwampSessionOuterVlanEtherType_Type = Unsigned32
_F3TwampSessionOuterVlanEtherType_Object = MibTableColumn
f3TwampSessionOuterVlanEtherType = _F3TwampSessionOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 5),
    _F3TwampSessionOuterVlanEtherType_Type()
)
f3TwampSessionOuterVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionOuterVlanEtherType.setStatus("current")
_F3TwampSessionOuterVlanId_Type = VlanId
_F3TwampSessionOuterVlanId_Object = MibTableColumn
f3TwampSessionOuterVlanId = _F3TwampSessionOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 6),
    _F3TwampSessionOuterVlanId_Type()
)
f3TwampSessionOuterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionOuterVlanId.setStatus("current")
_F3TwampSessionOuterVlanPriority_Type = VlanPriority
_F3TwampSessionOuterVlanPriority_Object = MibTableColumn
f3TwampSessionOuterVlanPriority = _F3TwampSessionOuterVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 7),
    _F3TwampSessionOuterVlanPriority_Type()
)
f3TwampSessionOuterVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionOuterVlanPriority.setStatus("current")
_F3TwampSessionInnerVlanEnabled_Type = TruthValue
_F3TwampSessionInnerVlanEnabled_Object = MibTableColumn
f3TwampSessionInnerVlanEnabled = _F3TwampSessionInnerVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 8),
    _F3TwampSessionInnerVlanEnabled_Type()
)
f3TwampSessionInnerVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionInnerVlanEnabled.setStatus("current")
_F3TwampSessionInnerVlanEtherType_Type = Unsigned32
_F3TwampSessionInnerVlanEtherType_Object = MibTableColumn
f3TwampSessionInnerVlanEtherType = _F3TwampSessionInnerVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 9),
    _F3TwampSessionInnerVlanEtherType_Type()
)
f3TwampSessionInnerVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionInnerVlanEtherType.setStatus("current")
_F3TwampSessionInnerVlanId_Type = VlanId
_F3TwampSessionInnerVlanId_Object = MibTableColumn
f3TwampSessionInnerVlanId = _F3TwampSessionInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 10),
    _F3TwampSessionInnerVlanId_Type()
)
f3TwampSessionInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionInnerVlanId.setStatus("current")
_F3TwampSessionInnerVlanPriority_Type = VlanPriority
_F3TwampSessionInnerVlanPriority_Object = MibTableColumn
f3TwampSessionInnerVlanPriority = _F3TwampSessionInnerVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 11),
    _F3TwampSessionInnerVlanPriority_Type()
)
f3TwampSessionInnerVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionInnerVlanPriority.setStatus("current")


class _F3TwampSessionDscpValue_Type(Unsigned32):
    """Custom type f3TwampSessionDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_F3TwampSessionDscpValue_Type.__name__ = "Unsigned32"
_F3TwampSessionDscpValue_Object = MibTableColumn
f3TwampSessionDscpValue = _F3TwampSessionDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 12),
    _F3TwampSessionDscpValue_Type()
)
f3TwampSessionDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionDscpValue.setStatus("current")
_F3TwampSessionSequenceNumber_Type = Unsigned32
_F3TwampSessionSequenceNumber_Object = MibTableColumn
f3TwampSessionSequenceNumber = _F3TwampSessionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 13),
    _F3TwampSessionSequenceNumber_Type()
)
f3TwampSessionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSequenceNumber.setStatus("current")
_F3TwampSessionAction_Type = TwampSessionAction
_F3TwampSessionAction_Object = MibTableColumn
f3TwampSessionAction = _F3TwampSessionAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 5, 1, 14),
    _F3TwampSessionAction_Type()
)
f3TwampSessionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampSessionAction.setStatus("current")
_F3TwampControlClientTable_Object = MibTable
f3TwampControlClientTable = _F3TwampControlClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6)
)
if mibBuilder.loadTexts:
    f3TwampControlClientTable.setStatus("current")
_F3TwampControlClientEntry_Object = MibTableRow
f3TwampControlClientEntry = _F3TwampControlClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1)
)
f3TwampControlClientEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampControlClientIndex"),
)
if mibBuilder.loadTexts:
    f3TwampControlClientEntry.setStatus("current")


class _F3TwampControlClientIndex_Type(Integer32):
    """Custom type f3TwampControlClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampControlClientIndex_Type.__name__ = "Integer32"
_F3TwampControlClientIndex_Object = MibTableColumn
f3TwampControlClientIndex = _F3TwampControlClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 1),
    _F3TwampControlClientIndex_Type()
)
f3TwampControlClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampControlClientIndex.setStatus("current")
_F3TwampControlClientAdminState_Type = AdminState
_F3TwampControlClientAdminState_Object = MibTableColumn
f3TwampControlClientAdminState = _F3TwampControlClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 2),
    _F3TwampControlClientAdminState_Type()
)
f3TwampControlClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampControlClientAdminState.setStatus("current")
_F3TwampControlClientOperationalState_Type = OperationalState
_F3TwampControlClientOperationalState_Object = MibTableColumn
f3TwampControlClientOperationalState = _F3TwampControlClientOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 3),
    _F3TwampControlClientOperationalState_Type()
)
f3TwampControlClientOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampControlClientOperationalState.setStatus("current")
_F3TwampControlClientSecondaryState_Type = SecondaryState
_F3TwampControlClientSecondaryState_Object = MibTableColumn
f3TwampControlClientSecondaryState = _F3TwampControlClientSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 4),
    _F3TwampControlClientSecondaryState_Type()
)
f3TwampControlClientSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampControlClientSecondaryState.setStatus("current")


class _F3TwampControlClientAlias_Type(DisplayString):
    """Custom type f3TwampControlClientAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3TwampControlClientAlias_Type.__name__ = "DisplayString"
_F3TwampControlClientAlias_Object = MibTableColumn
f3TwampControlClientAlias = _F3TwampControlClientAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 5),
    _F3TwampControlClientAlias_Type()
)
f3TwampControlClientAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientAlias.setStatus("current")
_F3TwampControlClientPort_Type = VariablePointer
_F3TwampControlClientPort_Object = MibTableColumn
f3TwampControlClientPort = _F3TwampControlClientPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 6),
    _F3TwampControlClientPort_Type()
)
f3TwampControlClientPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientPort.setStatus("current")
_F3TwampControlClientStatus_Type = TwampControlClientStatus
_F3TwampControlClientStatus_Object = MibTableColumn
f3TwampControlClientStatus = _F3TwampControlClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 7),
    _F3TwampControlClientStatus_Type()
)
f3TwampControlClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampControlClientStatus.setStatus("current")
_F3TwampControlClientActionObject_Type = VariablePointer
_F3TwampControlClientActionObject_Object = MibTableColumn
f3TwampControlClientActionObject = _F3TwampControlClientActionObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 8),
    _F3TwampControlClientActionObject_Type()
)
f3TwampControlClientActionObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientActionObject.setStatus("current")
_F3TwampControlClientAction_Type = TwampControlClientAction
_F3TwampControlClientAction_Object = MibTableColumn
f3TwampControlClientAction = _F3TwampControlClientAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 9),
    _F3TwampControlClientAction_Type()
)
f3TwampControlClientAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientAction.setStatus("current")
_F3TwampControlClientStorageType_Type = StorageType
_F3TwampControlClientStorageType_Object = MibTableColumn
f3TwampControlClientStorageType = _F3TwampControlClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 10),
    _F3TwampControlClientStorageType_Type()
)
f3TwampControlClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientStorageType.setStatus("current")
_F3TwampControlClientRowStatus_Type = RowStatus
_F3TwampControlClientRowStatus_Object = MibTableColumn
f3TwampControlClientRowStatus = _F3TwampControlClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 6, 1, 11),
    _F3TwampControlClientRowStatus_Type()
)
f3TwampControlClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampControlClientRowStatus.setStatus("current")
_F3TwampControlClientSessionSenderTable_Object = MibTable
f3TwampControlClientSessionSenderTable = _F3TwampControlClientSessionSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 7)
)
if mibBuilder.loadTexts:
    f3TwampControlClientSessionSenderTable.setStatus("current")
_F3TwampControlClientSessionSenderEntry_Object = MibTableRow
f3TwampControlClientSessionSenderEntry = _F3TwampControlClientSessionSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 7, 1)
)
f3TwampControlClientSessionSenderEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampControlClientIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampControlClientSessionSenderIndex"),
)
if mibBuilder.loadTexts:
    f3TwampControlClientSessionSenderEntry.setStatus("current")


class _F3TwampControlClientSessionSenderIndex_Type(Integer32):
    """Custom type f3TwampControlClientSessionSenderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampControlClientSessionSenderIndex_Type.__name__ = "Integer32"
_F3TwampControlClientSessionSenderIndex_Object = MibTableColumn
f3TwampControlClientSessionSenderIndex = _F3TwampControlClientSessionSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 7, 1, 1),
    _F3TwampControlClientSessionSenderIndex_Type()
)
f3TwampControlClientSessionSenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampControlClientSessionSenderIndex.setStatus("current")
_F3TwampControlClientSessionSender_Type = VariablePointer
_F3TwampControlClientSessionSender_Object = MibTableColumn
f3TwampControlClientSessionSender = _F3TwampControlClientSessionSender_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 7, 1, 2),
    _F3TwampControlClientSessionSender_Type()
)
f3TwampControlClientSessionSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampControlClientSessionSender.setStatus("current")
_F3TwampSessionSenderTable_Object = MibTable
f3TwampSessionSenderTable = _F3TwampSessionSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8)
)
if mibBuilder.loadTexts:
    f3TwampSessionSenderTable.setStatus("current")
_F3TwampSessionSenderEntry_Object = MibTableRow
f3TwampSessionSenderEntry = _F3TwampSessionSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1)
)
f3TwampSessionSenderEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
)
if mibBuilder.loadTexts:
    f3TwampSessionSenderEntry.setStatus("current")


class _F3TwampSessionSenderIndex_Type(Integer32):
    """Custom type f3TwampSessionSenderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_F3TwampSessionSenderIndex_Type.__name__ = "Integer32"
_F3TwampSessionSenderIndex_Object = MibTableColumn
f3TwampSessionSenderIndex = _F3TwampSessionSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 1),
    _F3TwampSessionSenderIndex_Type()
)
f3TwampSessionSenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampSessionSenderIndex.setStatus("current")
_F3TwampSessionSenderAdminState_Type = AdminState
_F3TwampSessionSenderAdminState_Object = MibTableColumn
f3TwampSessionSenderAdminState = _F3TwampSessionSenderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 2),
    _F3TwampSessionSenderAdminState_Type()
)
f3TwampSessionSenderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderAdminState.setStatus("current")
_F3TwampSessionSenderOperationalState_Type = OperationalState
_F3TwampSessionSenderOperationalState_Object = MibTableColumn
f3TwampSessionSenderOperationalState = _F3TwampSessionSenderOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 3),
    _F3TwampSessionSenderOperationalState_Type()
)
f3TwampSessionSenderOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderOperationalState.setStatus("current")
_F3TwampSessionSenderSecondaryState_Type = SecondaryState
_F3TwampSessionSenderSecondaryState_Object = MibTableColumn
f3TwampSessionSenderSecondaryState = _F3TwampSessionSenderSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 4),
    _F3TwampSessionSenderSecondaryState_Type()
)
f3TwampSessionSenderSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderSecondaryState.setStatus("current")


class _F3TwampSessionSenderAlias_Type(DisplayString):
    """Custom type f3TwampSessionSenderAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3TwampSessionSenderAlias_Type.__name__ = "DisplayString"
_F3TwampSessionSenderAlias_Object = MibTableColumn
f3TwampSessionSenderAlias = _F3TwampSessionSenderAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 5),
    _F3TwampSessionSenderAlias_Type()
)
f3TwampSessionSenderAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderAlias.setStatus("current")


class _F3TwampSessionSenderIpInterface_Type(DisplayString):
    """Custom type f3TwampSessionSenderIpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_F3TwampSessionSenderIpInterface_Type.__name__ = "DisplayString"
_F3TwampSessionSenderIpInterface_Object = MibTableColumn
f3TwampSessionSenderIpInterface = _F3TwampSessionSenderIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 6),
    _F3TwampSessionSenderIpInterface_Type()
)
f3TwampSessionSenderIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderIpInterface.setStatus("current")


class _F3TwampSessionSenderUdpPort_Type(Unsigned32):
    """Custom type f3TwampSessionSenderUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3TwampSessionSenderUdpPort_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderUdpPort_Object = MibTableColumn
f3TwampSessionSenderUdpPort = _F3TwampSessionSenderUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 7),
    _F3TwampSessionSenderUdpPort_Type()
)
f3TwampSessionSenderUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderUdpPort.setStatus("current")


class _F3TwampSessionSenderPktSchedTimeInterval_Type(Unsigned32):
    """Custom type f3TwampSessionSenderPktSchedTimeInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600000),
    )


_F3TwampSessionSenderPktSchedTimeInterval_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderPktSchedTimeInterval_Object = MibTableColumn
f3TwampSessionSenderPktSchedTimeInterval = _F3TwampSessionSenderPktSchedTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 8),
    _F3TwampSessionSenderPktSchedTimeInterval_Type()
)
f3TwampSessionSenderPktSchedTimeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderPktSchedTimeInterval.setStatus("current")
_F3TwampSessionSenderSrIpv4Address_Type = IpAddress
_F3TwampSessionSenderSrIpv4Address_Object = MibTableColumn
f3TwampSessionSenderSrIpv4Address = _F3TwampSessionSenderSrIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 9),
    _F3TwampSessionSenderSrIpv4Address_Type()
)
f3TwampSessionSenderSrIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderSrIpv4Address.setStatus("current")


class _F3TwampSessionSenderSrUdpPort_Type(Unsigned32):
    """Custom type f3TwampSessionSenderSrUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3TwampSessionSenderSrUdpPort_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderSrUdpPort_Object = MibTableColumn
f3TwampSessionSenderSrUdpPort = _F3TwampSessionSenderSrUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 10),
    _F3TwampSessionSenderSrUdpPort_Type()
)
f3TwampSessionSenderSrUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderSrUdpPort.setStatus("current")


class _F3TwampSessionSenderDscpValue_Type(Unsigned32):
    """Custom type f3TwampSessionSenderDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_F3TwampSessionSenderDscpValue_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderDscpValue_Object = MibTableColumn
f3TwampSessionSenderDscpValue = _F3TwampSessionSenderDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 11),
    _F3TwampSessionSenderDscpValue_Type()
)
f3TwampSessionSenderDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderDscpValue.setStatus("current")


class _F3TwampSessionSenderNumPkts_Type(Unsigned32):
    """Custom type f3TwampSessionSenderNumPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_F3TwampSessionSenderNumPkts_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderNumPkts_Object = MibTableColumn
f3TwampSessionSenderNumPkts = _F3TwampSessionSenderNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 12),
    _F3TwampSessionSenderNumPkts_Type()
)
f3TwampSessionSenderNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderNumPkts.setStatus("current")


class _F3TwampSessionSenderPktSize_Type(Unsigned32):
    """Custom type f3TwampSessionSenderPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 1526),
    )


_F3TwampSessionSenderPktSize_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderPktSize_Object = MibTableColumn
f3TwampSessionSenderPktSize = _F3TwampSessionSenderPktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 13),
    _F3TwampSessionSenderPktSize_Type()
)
f3TwampSessionSenderPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderPktSize.setStatus("current")
_F3TwampSessionSenderTestPattern_Type = TwampTestPattern
_F3TwampSessionSenderTestPattern_Object = MibTableColumn
f3TwampSessionSenderTestPattern = _F3TwampSessionSenderTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 14),
    _F3TwampSessionSenderTestPattern_Type()
)
f3TwampSessionSenderTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderTestPattern.setStatus("current")
_F3TwampSessionSenderStartTimeType_Type = TwampStartTimeType
_F3TwampSessionSenderStartTimeType_Object = MibTableColumn
f3TwampSessionSenderStartTimeType = _F3TwampSessionSenderStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 15),
    _F3TwampSessionSenderStartTimeType_Type()
)
f3TwampSessionSenderStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderStartTimeType.setStatus("current")


class _F3TwampSessionSenderStartDate_Type(DisplayString):
    """Custom type f3TwampSessionSenderStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_F3TwampSessionSenderStartDate_Type.__name__ = "DisplayString"
_F3TwampSessionSenderStartDate_Object = MibTableColumn
f3TwampSessionSenderStartDate = _F3TwampSessionSenderStartDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 16),
    _F3TwampSessionSenderStartDate_Type()
)
f3TwampSessionSenderStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderStartDate.setStatus("current")


class _F3TwampSessionSenderStartTime_Type(DisplayString):
    """Custom type f3TwampSessionSenderStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_F3TwampSessionSenderStartTime_Type.__name__ = "DisplayString"
_F3TwampSessionSenderStartTime_Object = MibTableColumn
f3TwampSessionSenderStartTime = _F3TwampSessionSenderStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 17),
    _F3TwampSessionSenderStartTime_Type()
)
f3TwampSessionSenderStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderStartTime.setStatus("current")


class _F3TwampSessionSenderRespTimeout_Type(Unsigned32):
    """Custom type f3TwampSessionSenderRespTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_F3TwampSessionSenderRespTimeout_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderRespTimeout_Object = MibTableColumn
f3TwampSessionSenderRespTimeout = _F3TwampSessionSenderRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 18),
    _F3TwampSessionSenderRespTimeout_Type()
)
f3TwampSessionSenderRespTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderRespTimeout.setStatus("current")
_F3TwampSessionSenderVlanEnabled_Type = TruthValue
_F3TwampSessionSenderVlanEnabled_Object = MibTableColumn
f3TwampSessionSenderVlanEnabled = _F3TwampSessionSenderVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 19),
    _F3TwampSessionSenderVlanEnabled_Type()
)
f3TwampSessionSenderVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderVlanEnabled.setStatus("current")
_F3TwampSessionSenderOuterVlanId_Type = VlanId
_F3TwampSessionSenderOuterVlanId_Object = MibTableColumn
f3TwampSessionSenderOuterVlanId = _F3TwampSessionSenderOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 20),
    _F3TwampSessionSenderOuterVlanId_Type()
)
f3TwampSessionSenderOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderOuterVlanId.setStatus("current")
_F3TwampSessionSenderOuterVlanPriority_Type = VlanPriority
_F3TwampSessionSenderOuterVlanPriority_Object = MibTableColumn
f3TwampSessionSenderOuterVlanPriority = _F3TwampSessionSenderOuterVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 21),
    _F3TwampSessionSenderOuterVlanPriority_Type()
)
f3TwampSessionSenderOuterVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderOuterVlanPriority.setStatus("current")
_F3TwampSessionSenderOuterVlanEtherType_Type = Unsigned32
_F3TwampSessionSenderOuterVlanEtherType_Object = MibTableColumn
f3TwampSessionSenderOuterVlanEtherType = _F3TwampSessionSenderOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 22),
    _F3TwampSessionSenderOuterVlanEtherType_Type()
)
f3TwampSessionSenderOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderOuterVlanEtherType.setStatus("current")
_F3TwampSessionSenderInnerVlanEnabled_Type = TruthValue
_F3TwampSessionSenderInnerVlanEnabled_Object = MibTableColumn
f3TwampSessionSenderInnerVlanEnabled = _F3TwampSessionSenderInnerVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 23),
    _F3TwampSessionSenderInnerVlanEnabled_Type()
)
f3TwampSessionSenderInnerVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderInnerVlanEnabled.setStatus("current")
_F3TwampSessionSenderInnerVlanId_Type = VlanId
_F3TwampSessionSenderInnerVlanId_Object = MibTableColumn
f3TwampSessionSenderInnerVlanId = _F3TwampSessionSenderInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 24),
    _F3TwampSessionSenderInnerVlanId_Type()
)
f3TwampSessionSenderInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderInnerVlanId.setStatus("current")
_F3TwampSessionSenderInnerVlanPriority_Type = VlanPriority
_F3TwampSessionSenderInnerVlanPriority_Object = MibTableColumn
f3TwampSessionSenderInnerVlanPriority = _F3TwampSessionSenderInnerVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 25),
    _F3TwampSessionSenderInnerVlanPriority_Type()
)
f3TwampSessionSenderInnerVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderInnerVlanPriority.setStatus("current")
_F3TwampSessionSenderInnerVlanEtherType_Type = Unsigned32
_F3TwampSessionSenderInnerVlanEtherType_Object = MibTableColumn
f3TwampSessionSenderInnerVlanEtherType = _F3TwampSessionSenderInnerVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 26),
    _F3TwampSessionSenderInnerVlanEtherType_Type()
)
f3TwampSessionSenderInnerVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderInnerVlanEtherType.setStatus("current")


class _F3TwampSessionSenderSeqNumber_Type(Unsigned32):
    """Custom type f3TwampSessionSenderSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_F3TwampSessionSenderSeqNumber_Type.__name__ = "Unsigned32"
_F3TwampSessionSenderSeqNumber_Object = MibTableColumn
f3TwampSessionSenderSeqNumber = _F3TwampSessionSenderSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 27),
    _F3TwampSessionSenderSeqNumber_Type()
)
f3TwampSessionSenderSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderSeqNumber.setStatus("current")
_F3TwampSessionSenderStatus_Type = TwampSessionSenderStatus
_F3TwampSessionSenderStatus_Object = MibTableColumn
f3TwampSessionSenderStatus = _F3TwampSessionSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 28),
    _F3TwampSessionSenderStatus_Type()
)
f3TwampSessionSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderStatus.setStatus("current")
_F3TwampSessionSenderAssocControlClient_Type = VariablePointer
_F3TwampSessionSenderAssocControlClient_Object = MibTableColumn
f3TwampSessionSenderAssocControlClient = _F3TwampSessionSenderAssocControlClient_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 29),
    _F3TwampSessionSenderAssocControlClient_Type()
)
f3TwampSessionSenderAssocControlClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampSessionSenderAssocControlClient.setStatus("current")
_F3TwampSessionSenderHistoryBins_Type = Unsigned32
_F3TwampSessionSenderHistoryBins_Object = MibTableColumn
f3TwampSessionSenderHistoryBins = _F3TwampSessionSenderHistoryBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 30),
    _F3TwampSessionSenderHistoryBins_Type()
)
f3TwampSessionSenderHistoryBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderHistoryBins.setStatus("current")
_F3TwampSessionSenderHistoryInterval_Type = TwampHistoryIntervalType
_F3TwampSessionSenderHistoryInterval_Object = MibTableColumn
f3TwampSessionSenderHistoryInterval = _F3TwampSessionSenderHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 31),
    _F3TwampSessionSenderHistoryInterval_Type()
)
f3TwampSessionSenderHistoryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderHistoryInterval.setStatus("current")
_F3TwampSessionSenderDistHistoryBins_Type = Unsigned32
_F3TwampSessionSenderDistHistoryBins_Object = MibTableColumn
f3TwampSessionSenderDistHistoryBins = _F3TwampSessionSenderDistHistoryBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 32),
    _F3TwampSessionSenderDistHistoryBins_Type()
)
f3TwampSessionSenderDistHistoryBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderDistHistoryBins.setStatus("current")
_F3TwampSessionSenderDistHistoryInterval_Type = TwampHistoryIntervalType
_F3TwampSessionSenderDistHistoryInterval_Object = MibTableColumn
f3TwampSessionSenderDistHistoryInterval = _F3TwampSessionSenderDistHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 33),
    _F3TwampSessionSenderDistHistoryInterval_Type()
)
f3TwampSessionSenderDistHistoryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderDistHistoryInterval.setStatus("current")
_F3TwampSessionSenderStorageType_Type = StorageType
_F3TwampSessionSenderStorageType_Object = MibTableColumn
f3TwampSessionSenderStorageType = _F3TwampSessionSenderStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 34),
    _F3TwampSessionSenderStorageType_Type()
)
f3TwampSessionSenderStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderStorageType.setStatus("current")
_F3TwampSessionSenderRowStatus_Type = RowStatus
_F3TwampSessionSenderRowStatus_Object = MibTableColumn
f3TwampSessionSenderRowStatus = _F3TwampSessionSenderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 8, 1, 35),
    _F3TwampSessionSenderRowStatus_Type()
)
f3TwampSessionSenderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TwampSessionSenderRowStatus.setStatus("current")
_F3TwampStatsTable_Object = MibTable
f3TwampStatsTable = _F3TwampStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9)
)
if mibBuilder.loadTexts:
    f3TwampStatsTable.setStatus("current")
_F3TwampStatsEntry_Object = MibTableRow
f3TwampStatsEntry = _F3TwampStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1)
)
f3TwampStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampStatsIndex"),
)
if mibBuilder.loadTexts:
    f3TwampStatsEntry.setStatus("current")
_F3TwampStatsIndex_Type = TwampPmIntervalType
_F3TwampStatsIndex_Object = MibTableColumn
f3TwampStatsIndex = _F3TwampStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 1),
    _F3TwampStatsIndex_Type()
)
f3TwampStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampStatsIndex.setStatus("current")
_F3TwampStatsValid_Type = TruthValue
_F3TwampStatsValid_Object = MibTableColumn
f3TwampStatsValid = _F3TwampStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 2),
    _F3TwampStatsValid_Type()
)
f3TwampStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsValid.setStatus("current")
_F3TwampStatsAction_Type = CmPmBinAction
_F3TwampStatsAction_Object = MibTableColumn
f3TwampStatsAction = _F3TwampStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 3),
    _F3TwampStatsAction_Type()
)
f3TwampStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampStatsAction.setStatus("current")
_F3TwampStatsTime_Type = DateAndTime
_F3TwampStatsTime_Object = MibTableColumn
f3TwampStatsTime = _F3TwampStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 4),
    _F3TwampStatsTime_Type()
)
f3TwampStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsTime.setStatus("current")
_F3TwampStatsS2RPkts_Type = PerfCounter64
_F3TwampStatsS2RPkts_Object = MibTableColumn
f3TwampStatsS2RPkts = _F3TwampStatsS2RPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 5),
    _F3TwampStatsS2RPkts_Type()
)
f3TwampStatsS2RPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsS2RPkts.setStatus("current")
_F3TwampStatsR2SPkts_Type = PerfCounter64
_F3TwampStatsR2SPkts_Object = MibTableColumn
f3TwampStatsR2SPkts = _F3TwampStatsR2SPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 6),
    _F3TwampStatsR2SPkts_Type()
)
f3TwampStatsR2SPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsR2SPkts.setStatus("current")
_F3TwampStatsS2RLostPkts_Type = PerfCounter64
_F3TwampStatsS2RLostPkts_Object = MibTableColumn
f3TwampStatsS2RLostPkts = _F3TwampStatsS2RLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 7),
    _F3TwampStatsS2RLostPkts_Type()
)
f3TwampStatsS2RLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsS2RLostPkts.setStatus("current")
_F3TwampStatsR2SLostPkts_Type = PerfCounter64
_F3TwampStatsR2SLostPkts_Object = MibTableColumn
f3TwampStatsR2SLostPkts = _F3TwampStatsR2SLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 8),
    _F3TwampStatsR2SLostPkts_Type()
)
f3TwampStatsR2SLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsR2SLostPkts.setStatus("current")
_F3TwampStatsS2RSyncErrs_Type = PerfCounter64
_F3TwampStatsS2RSyncErrs_Object = MibTableColumn
f3TwampStatsS2RSyncErrs = _F3TwampStatsS2RSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 9),
    _F3TwampStatsS2RSyncErrs_Type()
)
f3TwampStatsS2RSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsS2RSyncErrs.setStatus("current")
_F3TwampStatsR2SSyncErrs_Type = PerfCounter64
_F3TwampStatsR2SSyncErrs_Object = MibTableColumn
f3TwampStatsR2SSyncErrs = _F3TwampStatsR2SSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 10),
    _F3TwampStatsR2SSyncErrs_Type()
)
f3TwampStatsR2SSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsR2SSyncErrs.setStatus("current")
_F3TwampStatsOutOfSeqErrs_Type = PerfCounter64
_F3TwampStatsOutOfSeqErrs_Object = MibTableColumn
f3TwampStatsOutOfSeqErrs = _F3TwampStatsOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 11),
    _F3TwampStatsOutOfSeqErrs_Type()
)
f3TwampStatsOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsOutOfSeqErrs.setStatus("current")
_F3TwampStatsSeqGaps_Type = PerfCounter64
_F3TwampStatsSeqGaps_Object = MibTableColumn
f3TwampStatsSeqGaps = _F3TwampStatsSeqGaps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 12),
    _F3TwampStatsSeqGaps_Type()
)
f3TwampStatsSeqGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSeqGaps.setStatus("current")
_F3TwampStatsMinTwoWayPD_Type = Unsigned32
_F3TwampStatsMinTwoWayPD_Object = MibTableColumn
f3TwampStatsMinTwoWayPD = _F3TwampStatsMinTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 13),
    _F3TwampStatsMinTwoWayPD_Type()
)
f3TwampStatsMinTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinTwoWayPD.setStatus("current")
_F3TwampStatsMaxTwoWayPD_Type = Unsigned32
_F3TwampStatsMaxTwoWayPD_Object = MibTableColumn
f3TwampStatsMaxTwoWayPD = _F3TwampStatsMaxTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 14),
    _F3TwampStatsMaxTwoWayPD_Type()
)
f3TwampStatsMaxTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxTwoWayPD.setStatus("current")
_F3TwampStatsAvgTwoWayPD_Type = Unsigned32
_F3TwampStatsAvgTwoWayPD_Object = MibTableColumn
f3TwampStatsAvgTwoWayPD = _F3TwampStatsAvgTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 15),
    _F3TwampStatsAvgTwoWayPD_Type()
)
f3TwampStatsAvgTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgTwoWayPD.setStatus("current")
_F3TwampStatsSumTwoWayPD_Type = Unsigned32
_F3TwampStatsSumTwoWayPD_Object = MibTableColumn
f3TwampStatsSumTwoWayPD = _F3TwampStatsSumTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 16),
    _F3TwampStatsSumTwoWayPD_Type()
)
f3TwampStatsSumTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumTwoWayPD.setStatus("current")
_F3TwampStatsSumOfSqTwoWayPD_Type = Unsigned32
_F3TwampStatsSumOfSqTwoWayPD_Object = MibTableColumn
f3TwampStatsSumOfSqTwoWayPD = _F3TwampStatsSumOfSqTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 17),
    _F3TwampStatsSumOfSqTwoWayPD_Type()
)
f3TwampStatsSumOfSqTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqTwoWayPD.setStatus("current")
_F3TwampStatsMinOneWayS2RPD_Type = Unsigned32
_F3TwampStatsMinOneWayS2RPD_Object = MibTableColumn
f3TwampStatsMinOneWayS2RPD = _F3TwampStatsMinOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 18),
    _F3TwampStatsMinOneWayS2RPD_Type()
)
f3TwampStatsMinOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayS2RPD.setStatus("current")
_F3TwampStatsMaxOneWayS2RPD_Type = Unsigned32
_F3TwampStatsMaxOneWayS2RPD_Object = MibTableColumn
f3TwampStatsMaxOneWayS2RPD = _F3TwampStatsMaxOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 19),
    _F3TwampStatsMaxOneWayS2RPD_Type()
)
f3TwampStatsMaxOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayS2RPD.setStatus("current")
_F3TwampStatsAvgOneWayS2RPD_Type = Unsigned32
_F3TwampStatsAvgOneWayS2RPD_Object = MibTableColumn
f3TwampStatsAvgOneWayS2RPD = _F3TwampStatsAvgOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 20),
    _F3TwampStatsAvgOneWayS2RPD_Type()
)
f3TwampStatsAvgOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayS2RPD.setStatus("current")
_F3TwampStatsSumOneWayS2RPD_Type = Unsigned32
_F3TwampStatsSumOneWayS2RPD_Object = MibTableColumn
f3TwampStatsSumOneWayS2RPD = _F3TwampStatsSumOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 21),
    _F3TwampStatsSumOneWayS2RPD_Type()
)
f3TwampStatsSumOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayS2RPD.setStatus("current")
_F3TwampStatsSumOfSqOneWayS2RPD_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayS2RPD_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayS2RPD = _F3TwampStatsSumOfSqOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 22),
    _F3TwampStatsSumOfSqOneWayS2RPD_Type()
)
f3TwampStatsSumOfSqOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayS2RPD.setStatus("current")
_F3TwampStatsMinOneWayR2SPD_Type = Unsigned32
_F3TwampStatsMinOneWayR2SPD_Object = MibTableColumn
f3TwampStatsMinOneWayR2SPD = _F3TwampStatsMinOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 23),
    _F3TwampStatsMinOneWayR2SPD_Type()
)
f3TwampStatsMinOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayR2SPD.setStatus("current")
_F3TwampStatsMaxOneWayR2SPD_Type = Unsigned32
_F3TwampStatsMaxOneWayR2SPD_Object = MibTableColumn
f3TwampStatsMaxOneWayR2SPD = _F3TwampStatsMaxOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 24),
    _F3TwampStatsMaxOneWayR2SPD_Type()
)
f3TwampStatsMaxOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayR2SPD.setStatus("current")
_F3TwampStatsAvgOneWayR2SPD_Type = Unsigned32
_F3TwampStatsAvgOneWayR2SPD_Object = MibTableColumn
f3TwampStatsAvgOneWayR2SPD = _F3TwampStatsAvgOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 25),
    _F3TwampStatsAvgOneWayR2SPD_Type()
)
f3TwampStatsAvgOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayR2SPD.setStatus("current")
_F3TwampStatsSumOneWayR2SPD_Type = Unsigned32
_F3TwampStatsSumOneWayR2SPD_Object = MibTableColumn
f3TwampStatsSumOneWayR2SPD = _F3TwampStatsSumOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 26),
    _F3TwampStatsSumOneWayR2SPD_Type()
)
f3TwampStatsSumOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayR2SPD.setStatus("current")
_F3TwampStatsSumOfSqOneWayR2SPD_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayR2SPD_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayR2SPD = _F3TwampStatsSumOfSqOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 27),
    _F3TwampStatsSumOfSqOneWayR2SPD_Type()
)
f3TwampStatsSumOfSqOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayR2SPD.setStatus("current")
_F3TwampStatsMinOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsMinOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsMinOneWayS2RAbsPDV = _F3TwampStatsMinOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 28),
    _F3TwampStatsMinOneWayS2RAbsPDV_Type()
)
f3TwampStatsMinOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsMaxOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayS2RAbsPDV = _F3TwampStatsMaxOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 29),
    _F3TwampStatsMaxOneWayS2RAbsPDV_Type()
)
f3TwampStatsMaxOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsAvgOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayS2RAbsPDV = _F3TwampStatsAvgOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 30),
    _F3TwampStatsAvgOneWayS2RAbsPDV_Type()
)
f3TwampStatsAvgOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsSumOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsSumOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsSumOneWayS2RAbsPDV = _F3TwampStatsSumOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 31),
    _F3TwampStatsSumOneWayS2RAbsPDV_Type()
)
f3TwampStatsSumOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayS2RAbsPDV = _F3TwampStatsSumOfSqOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 32),
    _F3TwampStatsSumOfSqOneWayS2RAbsPDV_Type()
)
f3TwampStatsSumOfSqOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsNumOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampStatsNumOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampStatsNumOneWayS2RAbsPDV = _F3TwampStatsNumOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 33),
    _F3TwampStatsNumOneWayS2RAbsPDV_Type()
)
f3TwampStatsNumOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayS2RAbsPDV.setStatus("current")
_F3TwampStatsMinOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsMinOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsMinOneWayR2SAbsPDV = _F3TwampStatsMinOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 34),
    _F3TwampStatsMinOneWayR2SAbsPDV_Type()
)
f3TwampStatsMinOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsMaxOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayR2SAbsPDV = _F3TwampStatsMaxOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 35),
    _F3TwampStatsMaxOneWayR2SAbsPDV_Type()
)
f3TwampStatsMaxOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsAvgOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayR2SAbsPDV = _F3TwampStatsAvgOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 36),
    _F3TwampStatsAvgOneWayR2SAbsPDV_Type()
)
f3TwampStatsAvgOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsSumOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsSumOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsSumOneWayR2SAbsPDV = _F3TwampStatsSumOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 37),
    _F3TwampStatsSumOneWayR2SAbsPDV_Type()
)
f3TwampStatsSumOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayR2SAbsPDV = _F3TwampStatsSumOfSqOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 38),
    _F3TwampStatsSumOfSqOneWayR2SAbsPDV_Type()
)
f3TwampStatsSumOfSqOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsNumOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampStatsNumOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampStatsNumOneWayR2SAbsPDV = _F3TwampStatsNumOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 39),
    _F3TwampStatsNumOneWayR2SAbsPDV_Type()
)
f3TwampStatsNumOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayR2SAbsPDV.setStatus("current")
_F3TwampStatsMinOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsMinOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsMinOneWayS2RNegPDV = _F3TwampStatsMinOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 40),
    _F3TwampStatsMinOneWayS2RNegPDV_Type()
)
f3TwampStatsMinOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsMaxOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayS2RNegPDV = _F3TwampStatsMaxOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 41),
    _F3TwampStatsMaxOneWayS2RNegPDV_Type()
)
f3TwampStatsMaxOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsAvgOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayS2RNegPDV = _F3TwampStatsAvgOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 42),
    _F3TwampStatsAvgOneWayS2RNegPDV_Type()
)
f3TwampStatsAvgOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsSumOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsSumOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsSumOneWayS2RNegPDV = _F3TwampStatsSumOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 43),
    _F3TwampStatsSumOneWayS2RNegPDV_Type()
)
f3TwampStatsSumOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayS2RNegPDV = _F3TwampStatsSumOfSqOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 44),
    _F3TwampStatsSumOfSqOneWayS2RNegPDV_Type()
)
f3TwampStatsSumOfSqOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsNumOneWayS2RNegPDV_Type = Unsigned32
_F3TwampStatsNumOneWayS2RNegPDV_Object = MibTableColumn
f3TwampStatsNumOneWayS2RNegPDV = _F3TwampStatsNumOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 45),
    _F3TwampStatsNumOneWayS2RNegPDV_Type()
)
f3TwampStatsNumOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayS2RNegPDV.setStatus("current")
_F3TwampStatsMinOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsMinOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsMinOneWayR2SNegPDV = _F3TwampStatsMinOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 46),
    _F3TwampStatsMinOneWayR2SNegPDV_Type()
)
f3TwampStatsMinOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsMaxOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayR2SNegPDV = _F3TwampStatsMaxOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 47),
    _F3TwampStatsMaxOneWayR2SNegPDV_Type()
)
f3TwampStatsMaxOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsAvgOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayR2SNegPDV = _F3TwampStatsAvgOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 48),
    _F3TwampStatsAvgOneWayR2SNegPDV_Type()
)
f3TwampStatsAvgOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsSumOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsSumOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsSumOneWayR2SNegPDV = _F3TwampStatsSumOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 49),
    _F3TwampStatsSumOneWayR2SNegPDV_Type()
)
f3TwampStatsSumOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayR2SNegPDV = _F3TwampStatsSumOfSqOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 50),
    _F3TwampStatsSumOfSqOneWayR2SNegPDV_Type()
)
f3TwampStatsSumOfSqOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsNumOneWayR2SNegPDV_Type = Unsigned32
_F3TwampStatsNumOneWayR2SNegPDV_Object = MibTableColumn
f3TwampStatsNumOneWayR2SNegPDV = _F3TwampStatsNumOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 51),
    _F3TwampStatsNumOneWayR2SNegPDV_Type()
)
f3TwampStatsNumOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayR2SNegPDV.setStatus("current")
_F3TwampStatsMinOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsMinOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsMinOneWayS2RPosPDV = _F3TwampStatsMinOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 52),
    _F3TwampStatsMinOneWayS2RPosPDV_Type()
)
f3TwampStatsMinOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsMaxOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayS2RPosPDV = _F3TwampStatsMaxOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 53),
    _F3TwampStatsMaxOneWayS2RPosPDV_Type()
)
f3TwampStatsMaxOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsAvgOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayS2RPosPDV = _F3TwampStatsAvgOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 54),
    _F3TwampStatsAvgOneWayS2RPosPDV_Type()
)
f3TwampStatsAvgOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsSumOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsSumOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsSumOneWayS2RPosPDV = _F3TwampStatsSumOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 55),
    _F3TwampStatsSumOneWayS2RPosPDV_Type()
)
f3TwampStatsSumOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayS2RPosPDV = _F3TwampStatsSumOfSqOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 56),
    _F3TwampStatsSumOfSqOneWayS2RPosPDV_Type()
)
f3TwampStatsSumOfSqOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsNumOneWayS2RPosPDV_Type = Unsigned32
_F3TwampStatsNumOneWayS2RPosPDV_Object = MibTableColumn
f3TwampStatsNumOneWayS2RPosPDV = _F3TwampStatsNumOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 57),
    _F3TwampStatsNumOneWayS2RPosPDV_Type()
)
f3TwampStatsNumOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayS2RPosPDV.setStatus("current")
_F3TwampStatsMinOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsMinOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsMinOneWayR2SPosPDV = _F3TwampStatsMinOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 58),
    _F3TwampStatsMinOneWayR2SPosPDV_Type()
)
f3TwampStatsMinOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMinOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsMaxOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsMaxOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsMaxOneWayR2SPosPDV = _F3TwampStatsMaxOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 59),
    _F3TwampStatsMaxOneWayR2SPosPDV_Type()
)
f3TwampStatsMaxOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsMaxOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsAvgOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsAvgOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsAvgOneWayR2SPosPDV = _F3TwampStatsAvgOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 60),
    _F3TwampStatsAvgOneWayR2SPosPDV_Type()
)
f3TwampStatsAvgOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsAvgOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsSumOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsSumOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsSumOneWayR2SPosPDV = _F3TwampStatsSumOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 61),
    _F3TwampStatsSumOneWayR2SPosPDV_Type()
)
f3TwampStatsSumOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsSumOfSqOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsSumOfSqOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsSumOfSqOneWayR2SPosPDV = _F3TwampStatsSumOfSqOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 62),
    _F3TwampStatsSumOfSqOneWayR2SPosPDV_Type()
)
f3TwampStatsSumOfSqOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsSumOfSqOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsNumOneWayR2SPosPDV_Type = Unsigned32
_F3TwampStatsNumOneWayR2SPosPDV_Object = MibTableColumn
f3TwampStatsNumOneWayR2SPosPDV = _F3TwampStatsNumOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 63),
    _F3TwampStatsNumOneWayR2SPosPDV_Type()
)
f3TwampStatsNumOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayR2SPosPDV.setStatus("current")
_F3TwampStatsNumTwoWayPD_Type = Unsigned32
_F3TwampStatsNumTwoWayPD_Object = MibTableColumn
f3TwampStatsNumTwoWayPD = _F3TwampStatsNumTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 64),
    _F3TwampStatsNumTwoWayPD_Type()
)
f3TwampStatsNumTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumTwoWayPD.setStatus("current")
_F3TwampStatsNumOneWayS2RPD_Type = Unsigned32
_F3TwampStatsNumOneWayS2RPD_Object = MibTableColumn
f3TwampStatsNumOneWayS2RPD = _F3TwampStatsNumOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 65),
    _F3TwampStatsNumOneWayS2RPD_Type()
)
f3TwampStatsNumOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayS2RPD.setStatus("current")
_F3TwampStatsNumOneWayR2SPD_Type = Unsigned32
_F3TwampStatsNumOneWayR2SPD_Object = MibTableColumn
f3TwampStatsNumOneWayR2SPD = _F3TwampStatsNumOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 9, 1, 66),
    _F3TwampStatsNumOneWayR2SPD_Type()
)
f3TwampStatsNumOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsNumOneWayR2SPD.setStatus("current")
_F3TwampHistoryTable_Object = MibTable
f3TwampHistoryTable = _F3TwampHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10)
)
if mibBuilder.loadTexts:
    f3TwampHistoryTable.setStatus("current")
_F3TwampHistoryEntry_Object = MibTableRow
f3TwampHistoryEntry = _F3TwampHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1)
)
f3TwampHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3TwampHistoryEntry.setStatus("current")
_F3TwampHistoryIndex_Type = Integer32
_F3TwampHistoryIndex_Object = MibTableColumn
f3TwampHistoryIndex = _F3TwampHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 1),
    _F3TwampHistoryIndex_Type()
)
f3TwampHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampHistoryIndex.setStatus("current")
_F3TwampHistoryValid_Type = TruthValue
_F3TwampHistoryValid_Object = MibTableColumn
f3TwampHistoryValid = _F3TwampHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 2),
    _F3TwampHistoryValid_Type()
)
f3TwampHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryValid.setStatus("current")
_F3TwampHistoryAction_Type = CmPmBinAction
_F3TwampHistoryAction_Object = MibTableColumn
f3TwampHistoryAction = _F3TwampHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 3),
    _F3TwampHistoryAction_Type()
)
f3TwampHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampHistoryAction.setStatus("current")
_F3TwampHistoryTime_Type = DateAndTime
_F3TwampHistoryTime_Object = MibTableColumn
f3TwampHistoryTime = _F3TwampHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 4),
    _F3TwampHistoryTime_Type()
)
f3TwampHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryTime.setStatus("current")
_F3TwampHistoryS2RPkts_Type = PerfCounter64
_F3TwampHistoryS2RPkts_Object = MibTableColumn
f3TwampHistoryS2RPkts = _F3TwampHistoryS2RPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 5),
    _F3TwampHistoryS2RPkts_Type()
)
f3TwampHistoryS2RPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryS2RPkts.setStatus("current")
_F3TwampHistoryR2SPkts_Type = PerfCounter64
_F3TwampHistoryR2SPkts_Object = MibTableColumn
f3TwampHistoryR2SPkts = _F3TwampHistoryR2SPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 6),
    _F3TwampHistoryR2SPkts_Type()
)
f3TwampHistoryR2SPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryR2SPkts.setStatus("current")
_F3TwampHistoryS2RLostPkts_Type = PerfCounter64
_F3TwampHistoryS2RLostPkts_Object = MibTableColumn
f3TwampHistoryS2RLostPkts = _F3TwampHistoryS2RLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 7),
    _F3TwampHistoryS2RLostPkts_Type()
)
f3TwampHistoryS2RLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryS2RLostPkts.setStatus("current")
_F3TwampHistoryR2SLostPkts_Type = PerfCounter64
_F3TwampHistoryR2SLostPkts_Object = MibTableColumn
f3TwampHistoryR2SLostPkts = _F3TwampHistoryR2SLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 8),
    _F3TwampHistoryR2SLostPkts_Type()
)
f3TwampHistoryR2SLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryR2SLostPkts.setStatus("current")
_F3TwampHistoryS2RSyncErrs_Type = PerfCounter64
_F3TwampHistoryS2RSyncErrs_Object = MibTableColumn
f3TwampHistoryS2RSyncErrs = _F3TwampHistoryS2RSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 9),
    _F3TwampHistoryS2RSyncErrs_Type()
)
f3TwampHistoryS2RSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryS2RSyncErrs.setStatus("current")
_F3TwampHistoryR2SSyncErrs_Type = PerfCounter64
_F3TwampHistoryR2SSyncErrs_Object = MibTableColumn
f3TwampHistoryR2SSyncErrs = _F3TwampHistoryR2SSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 10),
    _F3TwampHistoryR2SSyncErrs_Type()
)
f3TwampHistoryR2SSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryR2SSyncErrs.setStatus("current")
_F3TwampHistoryOutOfSeqErrs_Type = PerfCounter64
_F3TwampHistoryOutOfSeqErrs_Object = MibTableColumn
f3TwampHistoryOutOfSeqErrs = _F3TwampHistoryOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 11),
    _F3TwampHistoryOutOfSeqErrs_Type()
)
f3TwampHistoryOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryOutOfSeqErrs.setStatus("current")
_F3TwampHistorySeqGaps_Type = PerfCounter64
_F3TwampHistorySeqGaps_Object = MibTableColumn
f3TwampHistorySeqGaps = _F3TwampHistorySeqGaps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 12),
    _F3TwampHistorySeqGaps_Type()
)
f3TwampHistorySeqGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySeqGaps.setStatus("current")
_F3TwampHistoryMinTwoWayPD_Type = Unsigned32
_F3TwampHistoryMinTwoWayPD_Object = MibTableColumn
f3TwampHistoryMinTwoWayPD = _F3TwampHistoryMinTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 13),
    _F3TwampHistoryMinTwoWayPD_Type()
)
f3TwampHistoryMinTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinTwoWayPD.setStatus("current")
_F3TwampHistoryMaxTwoWayPD_Type = Unsigned32
_F3TwampHistoryMaxTwoWayPD_Object = MibTableColumn
f3TwampHistoryMaxTwoWayPD = _F3TwampHistoryMaxTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 14),
    _F3TwampHistoryMaxTwoWayPD_Type()
)
f3TwampHistoryMaxTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxTwoWayPD.setStatus("current")
_F3TwampHistoryAvgTwoWayPD_Type = Unsigned32
_F3TwampHistoryAvgTwoWayPD_Object = MibTableColumn
f3TwampHistoryAvgTwoWayPD = _F3TwampHistoryAvgTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 15),
    _F3TwampHistoryAvgTwoWayPD_Type()
)
f3TwampHistoryAvgTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgTwoWayPD.setStatus("current")
_F3TwampHistorySumTwoWayPD_Type = Unsigned32
_F3TwampHistorySumTwoWayPD_Object = MibTableColumn
f3TwampHistorySumTwoWayPD = _F3TwampHistorySumTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 16),
    _F3TwampHistorySumTwoWayPD_Type()
)
f3TwampHistorySumTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumTwoWayPD.setStatus("current")
_F3TwampHistorySumOfSqTwoWayPD_Type = Unsigned32
_F3TwampHistorySumOfSqTwoWayPD_Object = MibTableColumn
f3TwampHistorySumOfSqTwoWayPD = _F3TwampHistorySumOfSqTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 17),
    _F3TwampHistorySumOfSqTwoWayPD_Type()
)
f3TwampHistorySumOfSqTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqTwoWayPD.setStatus("current")
_F3TwampHistoryMinOneWayS2RPD_Type = Unsigned32
_F3TwampHistoryMinOneWayS2RPD_Object = MibTableColumn
f3TwampHistoryMinOneWayS2RPD = _F3TwampHistoryMinOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 18),
    _F3TwampHistoryMinOneWayS2RPD_Type()
)
f3TwampHistoryMinOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayS2RPD.setStatus("current")
_F3TwampHistoryMaxOneWayS2RPD_Type = Unsigned32
_F3TwampHistoryMaxOneWayS2RPD_Object = MibTableColumn
f3TwampHistoryMaxOneWayS2RPD = _F3TwampHistoryMaxOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 19),
    _F3TwampHistoryMaxOneWayS2RPD_Type()
)
f3TwampHistoryMaxOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayS2RPD.setStatus("current")
_F3TwampHistoryAvgOneWayS2RPD_Type = Unsigned32
_F3TwampHistoryAvgOneWayS2RPD_Object = MibTableColumn
f3TwampHistoryAvgOneWayS2RPD = _F3TwampHistoryAvgOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 20),
    _F3TwampHistoryAvgOneWayS2RPD_Type()
)
f3TwampHistoryAvgOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayS2RPD.setStatus("current")
_F3TwampHistorySumOneWayS2RPD_Type = Unsigned32
_F3TwampHistorySumOneWayS2RPD_Object = MibTableColumn
f3TwampHistorySumOneWayS2RPD = _F3TwampHistorySumOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 21),
    _F3TwampHistorySumOneWayS2RPD_Type()
)
f3TwampHistorySumOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayS2RPD.setStatus("current")
_F3TwampHistorySumOfSqOneWayS2RPD_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayS2RPD_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayS2RPD = _F3TwampHistorySumOfSqOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 22),
    _F3TwampHistorySumOfSqOneWayS2RPD_Type()
)
f3TwampHistorySumOfSqOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayS2RPD.setStatus("current")
_F3TwampHistoryMinOneWayR2SPD_Type = Unsigned32
_F3TwampHistoryMinOneWayR2SPD_Object = MibTableColumn
f3TwampHistoryMinOneWayR2SPD = _F3TwampHistoryMinOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 23),
    _F3TwampHistoryMinOneWayR2SPD_Type()
)
f3TwampHistoryMinOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayR2SPD.setStatus("current")
_F3TwampHistoryMaxOneWayR2SPD_Type = Unsigned32
_F3TwampHistoryMaxOneWayR2SPD_Object = MibTableColumn
f3TwampHistoryMaxOneWayR2SPD = _F3TwampHistoryMaxOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 24),
    _F3TwampHistoryMaxOneWayR2SPD_Type()
)
f3TwampHistoryMaxOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayR2SPD.setStatus("current")
_F3TwampHistoryAvgOneWayR2SPD_Type = Unsigned32
_F3TwampHistoryAvgOneWayR2SPD_Object = MibTableColumn
f3TwampHistoryAvgOneWayR2SPD = _F3TwampHistoryAvgOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 25),
    _F3TwampHistoryAvgOneWayR2SPD_Type()
)
f3TwampHistoryAvgOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayR2SPD.setStatus("current")
_F3TwampHistorySumOneWayR2SPD_Type = Unsigned32
_F3TwampHistorySumOneWayR2SPD_Object = MibTableColumn
f3TwampHistorySumOneWayR2SPD = _F3TwampHistorySumOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 26),
    _F3TwampHistorySumOneWayR2SPD_Type()
)
f3TwampHistorySumOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayR2SPD.setStatus("current")
_F3TwampHistorySumOfSqOneWayR2SPD_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayR2SPD_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayR2SPD = _F3TwampHistorySumOfSqOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 27),
    _F3TwampHistorySumOfSqOneWayR2SPD_Type()
)
f3TwampHistorySumOfSqOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayR2SPD.setStatus("current")
_F3TwampHistoryMinOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayS2RAbsPDV = _F3TwampHistoryMinOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 28),
    _F3TwampHistoryMinOneWayS2RAbsPDV_Type()
)
f3TwampHistoryMinOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistoryMaxOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayS2RAbsPDV = _F3TwampHistoryMaxOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 29),
    _F3TwampHistoryMaxOneWayS2RAbsPDV_Type()
)
f3TwampHistoryMaxOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistoryAvgOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayS2RAbsPDV = _F3TwampHistoryAvgOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 30),
    _F3TwampHistoryAvgOneWayS2RAbsPDV_Type()
)
f3TwampHistoryAvgOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistorySumOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistorySumOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistorySumOneWayS2RAbsPDV = _F3TwampHistorySumOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 31),
    _F3TwampHistorySumOneWayS2RAbsPDV_Type()
)
f3TwampHistorySumOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayS2RAbsPDV = _F3TwampHistorySumOfSqOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 32),
    _F3TwampHistorySumOfSqOneWayS2RAbsPDV_Type()
)
f3TwampHistorySumOfSqOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistoryNumOneWayS2RAbsPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayS2RAbsPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayS2RAbsPDV = _F3TwampHistoryNumOneWayS2RAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 33),
    _F3TwampHistoryNumOneWayS2RAbsPDV_Type()
)
f3TwampHistoryNumOneWayS2RAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayS2RAbsPDV.setStatus("current")
_F3TwampHistoryMinOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayR2SAbsPDV = _F3TwampHistoryMinOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 34),
    _F3TwampHistoryMinOneWayR2SAbsPDV_Type()
)
f3TwampHistoryMinOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistoryMaxOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayR2SAbsPDV = _F3TwampHistoryMaxOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 35),
    _F3TwampHistoryMaxOneWayR2SAbsPDV_Type()
)
f3TwampHistoryMaxOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistoryAvgOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayR2SAbsPDV = _F3TwampHistoryAvgOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 36),
    _F3TwampHistoryAvgOneWayR2SAbsPDV_Type()
)
f3TwampHistoryAvgOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistorySumOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistorySumOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistorySumOneWayR2SAbsPDV = _F3TwampHistorySumOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 37),
    _F3TwampHistorySumOneWayR2SAbsPDV_Type()
)
f3TwampHistorySumOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayR2SAbsPDV = _F3TwampHistorySumOfSqOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 38),
    _F3TwampHistorySumOfSqOneWayR2SAbsPDV_Type()
)
f3TwampHistorySumOfSqOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistoryNumOneWayR2SAbsPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayR2SAbsPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayR2SAbsPDV = _F3TwampHistoryNumOneWayR2SAbsPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 39),
    _F3TwampHistoryNumOneWayR2SAbsPDV_Type()
)
f3TwampHistoryNumOneWayR2SAbsPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayR2SAbsPDV.setStatus("current")
_F3TwampHistoryMinOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayS2RNegPDV = _F3TwampHistoryMinOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 40),
    _F3TwampHistoryMinOneWayS2RNegPDV_Type()
)
f3TwampHistoryMinOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayS2RNegPDV.setStatus("current")
_F3TwampHistoryMaxOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayS2RNegPDV = _F3TwampHistoryMaxOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 41),
    _F3TwampHistoryMaxOneWayS2RNegPDV_Type()
)
f3TwampHistoryMaxOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayS2RNegPDV.setStatus("current")
_F3TwampHistoryAvgOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayS2RNegPDV = _F3TwampHistoryAvgOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 42),
    _F3TwampHistoryAvgOneWayS2RNegPDV_Type()
)
f3TwampHistoryAvgOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayS2RNegPDV.setStatus("current")
_F3TwampHistorySumOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistorySumOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistorySumOneWayS2RNegPDV = _F3TwampHistorySumOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 43),
    _F3TwampHistorySumOneWayS2RNegPDV_Type()
)
f3TwampHistorySumOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayS2RNegPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayS2RNegPDV = _F3TwampHistorySumOfSqOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 44),
    _F3TwampHistorySumOfSqOneWayS2RNegPDV_Type()
)
f3TwampHistorySumOfSqOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayS2RNegPDV.setStatus("current")
_F3TwampHistoryNumOneWayS2RNegPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayS2RNegPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayS2RNegPDV = _F3TwampHistoryNumOneWayS2RNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 45),
    _F3TwampHistoryNumOneWayS2RNegPDV_Type()
)
f3TwampHistoryNumOneWayS2RNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayS2RNegPDV.setStatus("current")
_F3TwampHistoryMinOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayR2SNegPDV = _F3TwampHistoryMinOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 46),
    _F3TwampHistoryMinOneWayR2SNegPDV_Type()
)
f3TwampHistoryMinOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayR2SNegPDV.setStatus("current")
_F3TwampHistoryMaxOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayR2SNegPDV = _F3TwampHistoryMaxOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 47),
    _F3TwampHistoryMaxOneWayR2SNegPDV_Type()
)
f3TwampHistoryMaxOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayR2SNegPDV.setStatus("current")
_F3TwampHistoryAvgOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayR2SNegPDV = _F3TwampHistoryAvgOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 48),
    _F3TwampHistoryAvgOneWayR2SNegPDV_Type()
)
f3TwampHistoryAvgOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayR2SNegPDV.setStatus("current")
_F3TwampHistorySumOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistorySumOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistorySumOneWayR2SNegPDV = _F3TwampHistorySumOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 49),
    _F3TwampHistorySumOneWayR2SNegPDV_Type()
)
f3TwampHistorySumOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayR2SNegPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayR2SNegPDV = _F3TwampHistorySumOfSqOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 50),
    _F3TwampHistorySumOfSqOneWayR2SNegPDV_Type()
)
f3TwampHistorySumOfSqOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayR2SNegPDV.setStatus("current")
_F3TwampHistoryNumOneWayR2SNegPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayR2SNegPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayR2SNegPDV = _F3TwampHistoryNumOneWayR2SNegPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 51),
    _F3TwampHistoryNumOneWayR2SNegPDV_Type()
)
f3TwampHistoryNumOneWayR2SNegPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayR2SNegPDV.setStatus("current")
_F3TwampHistoryMinOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayS2RPosPDV = _F3TwampHistoryMinOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 52),
    _F3TwampHistoryMinOneWayS2RPosPDV_Type()
)
f3TwampHistoryMinOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayS2RPosPDV.setStatus("current")
_F3TwampHistoryMaxOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayS2RPosPDV = _F3TwampHistoryMaxOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 53),
    _F3TwampHistoryMaxOneWayS2RPosPDV_Type()
)
f3TwampHistoryMaxOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayS2RPosPDV.setStatus("current")
_F3TwampHistoryAvgOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayS2RPosPDV = _F3TwampHistoryAvgOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 54),
    _F3TwampHistoryAvgOneWayS2RPosPDV_Type()
)
f3TwampHistoryAvgOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayS2RPosPDV.setStatus("current")
_F3TwampHistorySumOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistorySumOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistorySumOneWayS2RPosPDV = _F3TwampHistorySumOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 55),
    _F3TwampHistorySumOneWayS2RPosPDV_Type()
)
f3TwampHistorySumOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayS2RPosPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayS2RPosPDV = _F3TwampHistorySumOfSqOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 56),
    _F3TwampHistorySumOfSqOneWayS2RPosPDV_Type()
)
f3TwampHistorySumOfSqOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayS2RPosPDV.setStatus("current")
_F3TwampHistoryNumOneWayS2RPosPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayS2RPosPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayS2RPosPDV = _F3TwampHistoryNumOneWayS2RPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 57),
    _F3TwampHistoryNumOneWayS2RPosPDV_Type()
)
f3TwampHistoryNumOneWayS2RPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayS2RPosPDV.setStatus("current")
_F3TwampHistoryMinOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistoryMinOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistoryMinOneWayR2SPosPDV = _F3TwampHistoryMinOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 58),
    _F3TwampHistoryMinOneWayR2SPosPDV_Type()
)
f3TwampHistoryMinOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMinOneWayR2SPosPDV.setStatus("current")
_F3TwampHistoryMaxOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistoryMaxOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistoryMaxOneWayR2SPosPDV = _F3TwampHistoryMaxOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 59),
    _F3TwampHistoryMaxOneWayR2SPosPDV_Type()
)
f3TwampHistoryMaxOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryMaxOneWayR2SPosPDV.setStatus("current")
_F3TwampHistoryAvgOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistoryAvgOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistoryAvgOneWayR2SPosPDV = _F3TwampHistoryAvgOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 60),
    _F3TwampHistoryAvgOneWayR2SPosPDV_Type()
)
f3TwampHistoryAvgOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryAvgOneWayR2SPosPDV.setStatus("current")
_F3TwampHistorySumOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistorySumOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistorySumOneWayR2SPosPDV = _F3TwampHistorySumOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 61),
    _F3TwampHistorySumOneWayR2SPosPDV_Type()
)
f3TwampHistorySumOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOneWayR2SPosPDV.setStatus("current")
_F3TwampHistorySumOfSqOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistorySumOfSqOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistorySumOfSqOneWayR2SPosPDV = _F3TwampHistorySumOfSqOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 62),
    _F3TwampHistorySumOfSqOneWayR2SPosPDV_Type()
)
f3TwampHistorySumOfSqOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistorySumOfSqOneWayR2SPosPDV.setStatus("current")
_F3TwampHistoryNumOneWayR2SPosPDV_Type = Unsigned32
_F3TwampHistoryNumOneWayR2SPosPDV_Object = MibTableColumn
f3TwampHistoryNumOneWayR2SPosPDV = _F3TwampHistoryNumOneWayR2SPosPDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 63),
    _F3TwampHistoryNumOneWayR2SPosPDV_Type()
)
f3TwampHistoryNumOneWayR2SPosPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayR2SPosPDV.setStatus("current")
_F3TwampHistoryNumTwoWayPD_Type = Unsigned32
_F3TwampHistoryNumTwoWayPD_Object = MibTableColumn
f3TwampHistoryNumTwoWayPD = _F3TwampHistoryNumTwoWayPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 64),
    _F3TwampHistoryNumTwoWayPD_Type()
)
f3TwampHistoryNumTwoWayPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumTwoWayPD.setStatus("current")
_F3TwampHistoryNumOneWayS2RPD_Type = Unsigned32
_F3TwampHistoryNumOneWayS2RPD_Object = MibTableColumn
f3TwampHistoryNumOneWayS2RPD = _F3TwampHistoryNumOneWayS2RPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 65),
    _F3TwampHistoryNumOneWayS2RPD_Type()
)
f3TwampHistoryNumOneWayS2RPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayS2RPD.setStatus("current")
_F3TwampHistoryNumOneWayR2SPD_Type = Unsigned32
_F3TwampHistoryNumOneWayR2SPD_Object = MibTableColumn
f3TwampHistoryNumOneWayR2SPD = _F3TwampHistoryNumOneWayR2SPD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 10, 1, 66),
    _F3TwampHistoryNumOneWayR2SPD_Type()
)
f3TwampHistoryNumOneWayR2SPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampHistoryNumOneWayR2SPD.setStatus("current")
_F3TwampDistStatsConfigTable_Object = MibTable
f3TwampDistStatsConfigTable = _F3TwampDistStatsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11)
)
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigTable.setStatus("current")
_F3TwampDistStatsConfigEntry_Object = MibTableRow
f3TwampDistStatsConfigEntry = _F3TwampDistStatsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11, 1)
)
f3TwampDistStatsConfigEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsConfigIndex"),
)
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigEntry.setStatus("current")
_F3TwampDistStatsConfigIndex_Type = TwampDistStatsType
_F3TwampDistStatsConfigIndex_Object = MibTableColumn
f3TwampDistStatsConfigIndex = _F3TwampDistStatsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11, 1, 1),
    _F3TwampDistStatsConfigIndex_Type()
)
f3TwampDistStatsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigIndex.setStatus("current")
_F3TwampDistStatsConfigMinVal_Type = Integer32
_F3TwampDistStatsConfigMinVal_Object = MibTableColumn
f3TwampDistStatsConfigMinVal = _F3TwampDistStatsConfigMinVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11, 1, 2),
    _F3TwampDistStatsConfigMinVal_Type()
)
f3TwampDistStatsConfigMinVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigMinVal.setStatus("current")
_F3TwampDistStatsConfigMaxVal_Type = Integer32
_F3TwampDistStatsConfigMaxVal_Object = MibTableColumn
f3TwampDistStatsConfigMaxVal = _F3TwampDistStatsConfigMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11, 1, 3),
    _F3TwampDistStatsConfigMaxVal_Type()
)
f3TwampDistStatsConfigMaxVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigMaxVal.setStatus("current")
_F3TwampDistStatsConfigNumBins_Type = Unsigned32
_F3TwampDistStatsConfigNumBins_Object = MibTableColumn
f3TwampDistStatsConfigNumBins = _F3TwampDistStatsConfigNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 11, 1, 4),
    _F3TwampDistStatsConfigNumBins_Type()
)
f3TwampDistStatsConfigNumBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampDistStatsConfigNumBins.setStatus("current")
_F3TwampDistStatsTable_Object = MibTable
f3TwampDistStatsTable = _F3TwampDistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12)
)
if mibBuilder.loadTexts:
    f3TwampDistStatsTable.setStatus("current")
_F3TwampDistStatsEntry_Object = MibTableRow
f3TwampDistStatsEntry = _F3TwampDistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1)
)
f3TwampDistStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsConfigIndex"),
)
if mibBuilder.loadTexts:
    f3TwampDistStatsEntry.setStatus("current")
_F3TwampDistStatsValid_Type = TruthValue
_F3TwampDistStatsValid_Object = MibTableColumn
f3TwampDistStatsValid = _F3TwampDistStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 1),
    _F3TwampDistStatsValid_Type()
)
f3TwampDistStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsValid.setStatus("current")
_F3TwampDistStatsTime_Type = DateAndTime
_F3TwampDistStatsTime_Object = MibTableColumn
f3TwampDistStatsTime = _F3TwampDistStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 2),
    _F3TwampDistStatsTime_Type()
)
f3TwampDistStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsTime.setStatus("current")
_F3TwampDistStatsAction_Type = CmPmBinAction
_F3TwampDistStatsAction_Object = MibTableColumn
f3TwampDistStatsAction = _F3TwampDistStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 3),
    _F3TwampDistStatsAction_Type()
)
f3TwampDistStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampDistStatsAction.setStatus("current")
_F3TwampDistStatsNumBins_Type = Integer32
_F3TwampDistStatsNumBins_Object = MibTableColumn
f3TwampDistStatsNumBins = _F3TwampDistStatsNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 4),
    _F3TwampDistStatsNumBins_Type()
)
f3TwampDistStatsNumBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsNumBins.setStatus("current")
_F3TwampDistStatsLTMin_Type = PerfCounter64
_F3TwampDistStatsLTMin_Object = MibTableColumn
f3TwampDistStatsLTMin = _F3TwampDistStatsLTMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 5),
    _F3TwampDistStatsLTMin_Type()
)
f3TwampDistStatsLTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsLTMin.setStatus("current")
_F3TwampDistStatsGTMax_Type = PerfCounter64
_F3TwampDistStatsGTMax_Object = MibTableColumn
f3TwampDistStatsGTMax = _F3TwampDistStatsGTMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 12, 1, 6),
    _F3TwampDistStatsGTMax_Type()
)
f3TwampDistStatsGTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsGTMax.setStatus("current")
_F3TwampDistStatsBinTable_Object = MibTable
f3TwampDistStatsBinTable = _F3TwampDistStatsBinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13)
)
if mibBuilder.loadTexts:
    f3TwampDistStatsBinTable.setStatus("current")
_F3TwampDistStatsBinEntry_Object = MibTableRow
f3TwampDistStatsBinEntry = _F3TwampDistStatsBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13, 1)
)
f3TwampDistStatsBinEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsConfigIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsBinIndex"),
)
if mibBuilder.loadTexts:
    f3TwampDistStatsBinEntry.setStatus("current")


class _F3TwampDistStatsBinIndex_Type(Integer32):
    """Custom type f3TwampDistStatsBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_F3TwampDistStatsBinIndex_Type.__name__ = "Integer32"
_F3TwampDistStatsBinIndex_Object = MibTableColumn
f3TwampDistStatsBinIndex = _F3TwampDistStatsBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13, 1, 1),
    _F3TwampDistStatsBinIndex_Type()
)
f3TwampDistStatsBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampDistStatsBinIndex.setStatus("current")
_F3TwampDistStatsBinLower_Type = Integer32
_F3TwampDistStatsBinLower_Object = MibTableColumn
f3TwampDistStatsBinLower = _F3TwampDistStatsBinLower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13, 1, 2),
    _F3TwampDistStatsBinLower_Type()
)
f3TwampDistStatsBinLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsBinLower.setStatus("current")
_F3TwampDistStatsBinUpper_Type = Integer32
_F3TwampDistStatsBinUpper_Object = MibTableColumn
f3TwampDistStatsBinUpper = _F3TwampDistStatsBinUpper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13, 1, 3),
    _F3TwampDistStatsBinUpper_Type()
)
f3TwampDistStatsBinUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsBinUpper.setStatus("current")
_F3TwampDistStatsBinNumSamples_Type = PerfCounter64
_F3TwampDistStatsBinNumSamples_Object = MibTableColumn
f3TwampDistStatsBinNumSamples = _F3TwampDistStatsBinNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 13, 1, 4),
    _F3TwampDistStatsBinNumSamples_Type()
)
f3TwampDistStatsBinNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistStatsBinNumSamples.setStatus("current")
_F3TwampDistHistoryTable_Object = MibTable
f3TwampDistHistoryTable = _F3TwampDistHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14)
)
if mibBuilder.loadTexts:
    f3TwampDistHistoryTable.setStatus("current")
_F3TwampDistHistoryEntry_Object = MibTableRow
f3TwampDistHistoryEntry = _F3TwampDistHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1)
)
f3TwampDistHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsConfigIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3TwampDistHistoryEntry.setStatus("current")


class _F3TwampDistHistoryIndex_Type(Integer32):
    """Custom type f3TwampDistHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3TwampDistHistoryIndex_Type.__name__ = "Integer32"
_F3TwampDistHistoryIndex_Object = MibTableColumn
f3TwampDistHistoryIndex = _F3TwampDistHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 1),
    _F3TwampDistHistoryIndex_Type()
)
f3TwampDistHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampDistHistoryIndex.setStatus("current")
_F3TwampDistHistoryValid_Type = TruthValue
_F3TwampDistHistoryValid_Object = MibTableColumn
f3TwampDistHistoryValid = _F3TwampDistHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 2),
    _F3TwampDistHistoryValid_Type()
)
f3TwampDistHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryValid.setStatus("current")
_F3TwampDistHistoryTime_Type = DateAndTime
_F3TwampDistHistoryTime_Object = MibTableColumn
f3TwampDistHistoryTime = _F3TwampDistHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 3),
    _F3TwampDistHistoryTime_Type()
)
f3TwampDistHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryTime.setStatus("current")
_F3TwampDistHistoryAction_Type = CmPmBinAction
_F3TwampDistHistoryAction_Object = MibTableColumn
f3TwampDistHistoryAction = _F3TwampDistHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 4),
    _F3TwampDistHistoryAction_Type()
)
f3TwampDistHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampDistHistoryAction.setStatus("current")
_F3TwampDistHistoryNumBins_Type = Integer32
_F3TwampDistHistoryNumBins_Object = MibTableColumn
f3TwampDistHistoryNumBins = _F3TwampDistHistoryNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 5),
    _F3TwampDistHistoryNumBins_Type()
)
f3TwampDistHistoryNumBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryNumBins.setStatus("current")
_F3TwampDistHistoryLTMin_Type = PerfCounter64
_F3TwampDistHistoryLTMin_Object = MibTableColumn
f3TwampDistHistoryLTMin = _F3TwampDistHistoryLTMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 6),
    _F3TwampDistHistoryLTMin_Type()
)
f3TwampDistHistoryLTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryLTMin.setStatus("current")
_F3TwampDistHistoryGTMax_Type = PerfCounter64
_F3TwampDistHistoryGTMax_Object = MibTableColumn
f3TwampDistHistoryGTMax = _F3TwampDistHistoryGTMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 14, 1, 7),
    _F3TwampDistHistoryGTMax_Type()
)
f3TwampDistHistoryGTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryGTMax.setStatus("current")
_F3TwampDistHistoryBinTable_Object = MibTable
f3TwampDistHistoryBinTable = _F3TwampDistHistoryBinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15)
)
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinTable.setStatus("current")
_F3TwampDistHistoryBinEntry_Object = MibTableRow
f3TwampDistHistoryBinEntry = _F3TwampDistHistoryBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15, 1)
)
f3TwampDistHistoryBinEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistStatsConfigIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistHistoryIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampDistHistoryBinIndex"),
)
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinEntry.setStatus("current")


class _F3TwampDistHistoryBinIndex_Type(Integer32):
    """Custom type f3TwampDistHistoryBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_F3TwampDistHistoryBinIndex_Type.__name__ = "Integer32"
_F3TwampDistHistoryBinIndex_Object = MibTableColumn
f3TwampDistHistoryBinIndex = _F3TwampDistHistoryBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15, 1, 1),
    _F3TwampDistHistoryBinIndex_Type()
)
f3TwampDistHistoryBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinIndex.setStatus("current")
_F3TwampDistHistoryBinLower_Type = Integer32
_F3TwampDistHistoryBinLower_Object = MibTableColumn
f3TwampDistHistoryBinLower = _F3TwampDistHistoryBinLower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15, 1, 2),
    _F3TwampDistHistoryBinLower_Type()
)
f3TwampDistHistoryBinLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinLower.setStatus("current")
_F3TwampDistHistoryBinUpper_Type = Integer32
_F3TwampDistHistoryBinUpper_Object = MibTableColumn
f3TwampDistHistoryBinUpper = _F3TwampDistHistoryBinUpper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15, 1, 3),
    _F3TwampDistHistoryBinUpper_Type()
)
f3TwampDistHistoryBinUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinUpper.setStatus("current")
_F3TwampDistHistoryBinNumSamples_Type = PerfCounter64
_F3TwampDistHistoryBinNumSamples_Object = MibTableColumn
f3TwampDistHistoryBinNumSamples = _F3TwampDistHistoryBinNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 15, 1, 4),
    _F3TwampDistHistoryBinNumSamples_Type()
)
f3TwampDistHistoryBinNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampDistHistoryBinNumSamples.setStatus("current")
_F3TwampStatsThresholdTable_Object = MibTable
f3TwampStatsThresholdTable = _F3TwampStatsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16)
)
if mibBuilder.loadTexts:
    f3TwampStatsThresholdTable.setStatus("current")
_F3TwampStatsThresholdEntry_Object = MibTableRow
f3TwampStatsThresholdEntry = _F3TwampStatsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1)
)
f3TwampStatsThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampSessionSenderIndex"),
    (0, "F3-TWAMP-MIB", "f3TwampStatsThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3TwampStatsThresholdEntry.setStatus("current")


class _F3TwampStatsThresholdIndex_Type(Integer32):
    """Custom type f3TwampStatsThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3TwampStatsThresholdIndex_Type.__name__ = "Integer32"
_F3TwampStatsThresholdIndex_Object = MibTableColumn
f3TwampStatsThresholdIndex = _F3TwampStatsThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1, 1),
    _F3TwampStatsThresholdIndex_Type()
)
f3TwampStatsThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsThresholdIndex.setStatus("current")
_F3TwampStatsThresholdVariable_Type = VariablePointer
_F3TwampStatsThresholdVariable_Object = MibTableColumn
f3TwampStatsThresholdVariable = _F3TwampStatsThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1, 2),
    _F3TwampStatsThresholdVariable_Type()
)
f3TwampStatsThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsThresholdVariable.setStatus("current")
_F3TwampStatsThresholdAbsValueLo_Type = Unsigned32
_F3TwampStatsThresholdAbsValueLo_Object = MibTableColumn
f3TwampStatsThresholdAbsValueLo = _F3TwampStatsThresholdAbsValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1, 3),
    _F3TwampStatsThresholdAbsValueLo_Type()
)
f3TwampStatsThresholdAbsValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampStatsThresholdAbsValueLo.setStatus("current")
_F3TwampStatsThresholdAbsValueHi_Type = Unsigned32
_F3TwampStatsThresholdAbsValueHi_Object = MibTableColumn
f3TwampStatsThresholdAbsValueHi = _F3TwampStatsThresholdAbsValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1, 4),
    _F3TwampStatsThresholdAbsValueHi_Type()
)
f3TwampStatsThresholdAbsValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TwampStatsThresholdAbsValueHi.setStatus("current")
_F3TwampStatsThresholdMonValue_Type = PerfCounter64
_F3TwampStatsThresholdMonValue_Object = MibTableColumn
f3TwampStatsThresholdMonValue = _F3TwampStatsThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 1, 16, 1, 5),
    _F3TwampStatsThresholdMonValue_Type()
)
f3TwampStatsThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TwampStatsThresholdMonValue.setStatus("current")
_F3TwampCounterObjects_ObjectIdentity = ObjectIdentity
f3TwampCounterObjects = _F3TwampCounterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 2)
)
_F3TwampActionObjects_ObjectIdentity = ObjectIdentity
f3TwampActionObjects = _F3TwampActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 3)
)
_F3TwampConformance_ObjectIdentity = ObjectIdentity
f3TwampConformance = _F3TwampConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4)
)
_F3TwampCompliances_ObjectIdentity = ObjectIdentity
f3TwampCompliances = _F3TwampCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 1)
)
_F3TwampGroups_ObjectIdentity = ObjectIdentity
f3TwampGroups = _F3TwampGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2)
)
_F3TwampNotifications_ObjectIdentity = ObjectIdentity
f3TwampNotifications = _F3TwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 5)
)

# Managed Objects groups

f3TwampIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 1)
)
f3TwampIpInterfaceGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampIpInterfacePort"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceIpMode"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceIpv4Address"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceIpv4Mask"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceMtu"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceStorageType"),
        ("F3-TWAMP-MIB", "f3TwampIpInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    f3TwampIpInterfaceGroup.setStatus("current")

f3TwampServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 2)
)
f3TwampServerGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampServerAdminState"),
        ("F3-TWAMP-MIB", "f3TwampServerOperationalState"),
        ("F3-TWAMP-MIB", "f3TwampServerSecondaryState"),
        ("F3-TWAMP-MIB", "f3TwampServerAlias"),
        ("F3-TWAMP-MIB", "f3TwampServerPort"),
        ("F3-TWAMP-MIB", "f3TwampServerStatus"),
        ("F3-TWAMP-MIB", "f3TwampServerSessionIdleTimeout"),
        ("F3-TWAMP-MIB", "f3TwampServerSessionAgingTimeout"),
        ("F3-TWAMP-MIB", "f3TwampServerActionObject"),
        ("F3-TWAMP-MIB", "f3TwampServerAction"),
        ("F3-TWAMP-MIB", "f3TwampServerStorageType"),
        ("F3-TWAMP-MIB", "f3TwampServerRowStatus"))
)
if mibBuilder.loadTexts:
    f3TwampServerGroup.setStatus("current")

f3TwampServerSessionReflectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 3)
)
f3TwampServerSessionReflectorGroup.setObjects(
    ("F3-TWAMP-MIB", "f3TwampServerSessionReflector")
)
if mibBuilder.loadTexts:
    f3TwampServerSessionReflectorGroup.setStatus("current")

f3TwampSessionReflectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 4)
)
f3TwampSessionReflectorGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampSessionReflectorAdminState"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorOperationalState"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorSecondaryState"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorAlias"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorIpInterface"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorUdpPort"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorUseSenderSeqNum"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorUserCreated"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorStatus"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorAssocServer"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorStorageType"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorRowStatus"))
)
if mibBuilder.loadTexts:
    f3TwampSessionReflectorGroup.setStatus("current")

f3TwampSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 5)
)
f3TwampSessionGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampSessionStatus"),
        ("F3-TWAMP-MIB", "f3TwampSessionVlanEnabled"),
        ("F3-TWAMP-MIB", "f3TwampSessionOuterVlanEtherType"),
        ("F3-TWAMP-MIB", "f3TwampSessionOuterVlanId"),
        ("F3-TWAMP-MIB", "f3TwampSessionOuterVlanPriority"),
        ("F3-TWAMP-MIB", "f3TwampSessionInnerVlanEnabled"),
        ("F3-TWAMP-MIB", "f3TwampSessionInnerVlanEtherType"),
        ("F3-TWAMP-MIB", "f3TwampSessionInnerVlanId"),
        ("F3-TWAMP-MIB", "f3TwampSessionInnerVlanPriority"),
        ("F3-TWAMP-MIB", "f3TwampSessionDscpValue"),
        ("F3-TWAMP-MIB", "f3TwampSessionSequenceNumber"),
        ("F3-TWAMP-MIB", "f3TwampSessionAction"))
)
if mibBuilder.loadTexts:
    f3TwampSessionGroup.setStatus("current")

f3TwampControlClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 6)
)
f3TwampControlClientGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampControlClientAdminState"),
        ("F3-TWAMP-MIB", "f3TwampControlClientOperationalState"),
        ("F3-TWAMP-MIB", "f3TwampControlClientSecondaryState"),
        ("F3-TWAMP-MIB", "f3TwampControlClientAlias"),
        ("F3-TWAMP-MIB", "f3TwampControlClientPort"),
        ("F3-TWAMP-MIB", "f3TwampControlClientStatus"),
        ("F3-TWAMP-MIB", "f3TwampControlClientActionObject"),
        ("F3-TWAMP-MIB", "f3TwampControlClientAction"),
        ("F3-TWAMP-MIB", "f3TwampControlClientStorageType"),
        ("F3-TWAMP-MIB", "f3TwampControlClientRowStatus"))
)
if mibBuilder.loadTexts:
    f3TwampControlClientGroup.setStatus("current")

f3TwampControlClientSessionSenderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 7)
)
f3TwampControlClientSessionSenderGroup.setObjects(
    ("F3-TWAMP-MIB", "f3TwampControlClientSessionSender")
)
if mibBuilder.loadTexts:
    f3TwampControlClientSessionSenderGroup.setStatus("current")

f3TwampSessionSenderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 8)
)
f3TwampSessionSenderGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampSessionSenderAdminState"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderOperationalState"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderSecondaryState"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderAlias"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderIpInterface"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderUdpPort"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderPktSchedTimeInterval"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderSrIpv4Address"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderSrUdpPort"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderDscpValue"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderNumPkts"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderPktSize"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderTestPattern"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderStartTimeType"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderStartDate"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderStartTime"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderRespTimeout"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderVlanEnabled"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderOuterVlanId"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderOuterVlanPriority"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderOuterVlanEtherType"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderInnerVlanEnabled"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderInnerVlanId"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderInnerVlanPriority"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderInnerVlanEtherType"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderSeqNumber"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderStatus"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderAssocControlClient"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderHistoryBins"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderHistoryInterval"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderDistHistoryBins"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderDistHistoryInterval"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderStorageType"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderRowStatus"))
)
if mibBuilder.loadTexts:
    f3TwampSessionSenderGroup.setStatus("current")

f3TwampStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 9)
)
f3TwampStatisticsGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampStatsValid"),
        ("F3-TWAMP-MIB", "f3TwampStatsAction"),
        ("F3-TWAMP-MIB", "f3TwampStatsTime"),
        ("F3-TWAMP-MIB", "f3TwampStatsS2RPkts"),
        ("F3-TWAMP-MIB", "f3TwampStatsR2SPkts"),
        ("F3-TWAMP-MIB", "f3TwampStatsS2RLostPkts"),
        ("F3-TWAMP-MIB", "f3TwampStatsR2SLostPkts"),
        ("F3-TWAMP-MIB", "f3TwampStatsS2RSyncErrs"),
        ("F3-TWAMP-MIB", "f3TwampStatsR2SSyncErrs"),
        ("F3-TWAMP-MIB", "f3TwampStatsOutOfSeqErrs"),
        ("F3-TWAMP-MIB", "f3TwampStatsSeqGaps"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMinOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsMaxOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsAvgOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsSumOfSqOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampStatsNumOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryValid"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAction"),
        ("F3-TWAMP-MIB", "f3TwampHistoryTime"),
        ("F3-TWAMP-MIB", "f3TwampHistoryS2RPkts"),
        ("F3-TWAMP-MIB", "f3TwampHistoryR2SPkts"),
        ("F3-TWAMP-MIB", "f3TwampHistoryS2RLostPkts"),
        ("F3-TWAMP-MIB", "f3TwampHistoryR2SLostPkts"),
        ("F3-TWAMP-MIB", "f3TwampHistoryS2RSyncErrs"),
        ("F3-TWAMP-MIB", "f3TwampHistoryR2SSyncErrs"),
        ("F3-TWAMP-MIB", "f3TwampHistoryOutOfSeqErrs"),
        ("F3-TWAMP-MIB", "f3TwampHistorySeqGaps"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayR2SPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayS2RAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayR2SAbsPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayS2RNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayR2SNegPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayS2RPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMinOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryMaxOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryAvgOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistorySumOfSqOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayR2SPosPDV"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumTwoWayPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayS2RPD"),
        ("F3-TWAMP-MIB", "f3TwampHistoryNumOneWayR2SPD"))
)
if mibBuilder.loadTexts:
    f3TwampStatisticsGroup.setStatus("current")

f3TwampDistributionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 10)
)
f3TwampDistributionStatisticsGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampDistStatsConfigMinVal"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsConfigMaxVal"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsConfigNumBins"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsValid"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsTime"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsAction"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsNumBins"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsLTMin"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsGTMax"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsBinLower"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsBinUpper"),
        ("F3-TWAMP-MIB", "f3TwampDistStatsBinNumSamples"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryValid"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryTime"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryAction"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryNumBins"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryLTMin"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryGTMax"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryBinLower"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryBinUpper"),
        ("F3-TWAMP-MIB", "f3TwampDistHistoryBinNumSamples"))
)
if mibBuilder.loadTexts:
    f3TwampDistributionStatisticsGroup.setStatus("current")

f3TwampThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 2, 11)
)
f3TwampThresholdGroup.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampStatsThresholdVariable"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdAbsValueLo"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdAbsValueHi"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3TwampThresholdGroup.setStatus("current")


# Notification objects

twampSessionSenderThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 5, 1)
)
twampSessionSenderThresholdCrossingAlert.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampStatsThresholdIndex"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdVariable"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdAbsValueLo"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdAbsValueHi"),
        ("F3-TWAMP-MIB", "f3TwampStatsThresholdMonValue"))
)
if mibBuilder.loadTexts:
    twampSessionSenderThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3TwampCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 33, 4, 1, 1)
)
f3TwampCompliance.setObjects(
      *(("F3-TWAMP-MIB", "f3TwampIpInterfaceGroup"),
        ("F3-TWAMP-MIB", "f3TwampServerGroup"),
        ("F3-TWAMP-MIB", "f3TwampServerSessionReflectorGroup"),
        ("F3-TWAMP-MIB", "f3TwampSessionReflectorGroup"),
        ("F3-TWAMP-MIB", "f3TwampSessionGroup"),
        ("F3-TWAMP-MIB", "f3TwampControlClientGroup"),
        ("F3-TWAMP-MIB", "f3TwampControlClientSessionSenderGroup"),
        ("F3-TWAMP-MIB", "f3TwampSessionSenderGroup"),
        ("F3-TWAMP-MIB", "f3TwampStatisticsGroup"),
        ("F3-TWAMP-MIB", "f3TwampDistributionStatisticsGroup"),
        ("F3-TWAMP-MIB", "f3TwampThresholdGroup"))
)
if mibBuilder.loadTexts:
    f3TwampCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-TWAMP-MIB",
    **{"TwampControlClientStatus": TwampControlClientStatus,
       "TwampServerStatus": TwampServerStatus,
       "TwampClientConnStatus": TwampClientConnStatus,
       "TwampServerConnStatus": TwampServerConnStatus,
       "TwampSessionSenderStatus": TwampSessionSenderStatus,
       "TwampSessionReflectorStatus": TwampSessionReflectorStatus,
       "TwampSessionStatus": TwampSessionStatus,
       "TwampPktSchedType": TwampPktSchedType,
       "TwampTestPattern": TwampTestPattern,
       "TwampPmIntervalType": TwampPmIntervalType,
       "TwampHistoryIntervalType": TwampHistoryIntervalType,
       "TwampDistStatsType": TwampDistStatsType,
       "TwampStartTimeType": TwampStartTimeType,
       "TwampServerAction": TwampServerAction,
       "TwampControlClientAction": TwampControlClientAction,
       "TwampSessionAction": TwampSessionAction,
       "f3TwampMIB": f3TwampMIB,
       "f3TwampConfigObjects": f3TwampConfigObjects,
       "f3TwampIpInterfaceTable": f3TwampIpInterfaceTable,
       "f3TwampIpInterfaceEntry": f3TwampIpInterfaceEntry,
       "f3TwampIpInterfaceName": f3TwampIpInterfaceName,
       "f3TwampIpInterfacePort": f3TwampIpInterfacePort,
       "f3TwampIpInterfaceIpMode": f3TwampIpInterfaceIpMode,
       "f3TwampIpInterfaceIpv4Address": f3TwampIpInterfaceIpv4Address,
       "f3TwampIpInterfaceIpv4Mask": f3TwampIpInterfaceIpv4Mask,
       "f3TwampIpInterfaceMtu": f3TwampIpInterfaceMtu,
       "f3TwampIpInterfaceStorageType": f3TwampIpInterfaceStorageType,
       "f3TwampIpInterfaceRowStatus": f3TwampIpInterfaceRowStatus,
       "f3TwampServerTable": f3TwampServerTable,
       "f3TwampServerEntry": f3TwampServerEntry,
       "f3TwampServerIndex": f3TwampServerIndex,
       "f3TwampServerAdminState": f3TwampServerAdminState,
       "f3TwampServerOperationalState": f3TwampServerOperationalState,
       "f3TwampServerSecondaryState": f3TwampServerSecondaryState,
       "f3TwampServerAlias": f3TwampServerAlias,
       "f3TwampServerPort": f3TwampServerPort,
       "f3TwampServerStatus": f3TwampServerStatus,
       "f3TwampServerSessionIdleTimeout": f3TwampServerSessionIdleTimeout,
       "f3TwampServerSessionAgingTimeout": f3TwampServerSessionAgingTimeout,
       "f3TwampServerActionObject": f3TwampServerActionObject,
       "f3TwampServerAction": f3TwampServerAction,
       "f3TwampServerStorageType": f3TwampServerStorageType,
       "f3TwampServerRowStatus": f3TwampServerRowStatus,
       "f3TwampServerSessionReflectorTable": f3TwampServerSessionReflectorTable,
       "f3TwampServerSessionReflectorEntry": f3TwampServerSessionReflectorEntry,
       "f3TwampServerSessionReflectorIndex": f3TwampServerSessionReflectorIndex,
       "f3TwampServerSessionReflector": f3TwampServerSessionReflector,
       "f3TwampSessionReflectorTable": f3TwampSessionReflectorTable,
       "f3TwampSessionReflectorEntry": f3TwampSessionReflectorEntry,
       "f3TwampSessionReflectorIndex": f3TwampSessionReflectorIndex,
       "f3TwampSessionReflectorAdminState": f3TwampSessionReflectorAdminState,
       "f3TwampSessionReflectorOperationalState": f3TwampSessionReflectorOperationalState,
       "f3TwampSessionReflectorSecondaryState": f3TwampSessionReflectorSecondaryState,
       "f3TwampSessionReflectorAlias": f3TwampSessionReflectorAlias,
       "f3TwampSessionReflectorIpInterface": f3TwampSessionReflectorIpInterface,
       "f3TwampSessionReflectorUdpPort": f3TwampSessionReflectorUdpPort,
       "f3TwampSessionReflectorUseSenderSeqNum": f3TwampSessionReflectorUseSenderSeqNum,
       "f3TwampSessionReflectorUserCreated": f3TwampSessionReflectorUserCreated,
       "f3TwampSessionReflectorStatus": f3TwampSessionReflectorStatus,
       "f3TwampSessionReflectorAssocServer": f3TwampSessionReflectorAssocServer,
       "f3TwampSessionReflectorStorageType": f3TwampSessionReflectorStorageType,
       "f3TwampSessionReflectorRowStatus": f3TwampSessionReflectorRowStatus,
       "f3TwampSessionTable": f3TwampSessionTable,
       "f3TwampSessionEntry": f3TwampSessionEntry,
       "f3TwampSessionSsIpv4Address": f3TwampSessionSsIpv4Address,
       "f3TwampSessionSsUdpPort": f3TwampSessionSsUdpPort,
       "f3TwampSessionStatus": f3TwampSessionStatus,
       "f3TwampSessionVlanEnabled": f3TwampSessionVlanEnabled,
       "f3TwampSessionOuterVlanEtherType": f3TwampSessionOuterVlanEtherType,
       "f3TwampSessionOuterVlanId": f3TwampSessionOuterVlanId,
       "f3TwampSessionOuterVlanPriority": f3TwampSessionOuterVlanPriority,
       "f3TwampSessionInnerVlanEnabled": f3TwampSessionInnerVlanEnabled,
       "f3TwampSessionInnerVlanEtherType": f3TwampSessionInnerVlanEtherType,
       "f3TwampSessionInnerVlanId": f3TwampSessionInnerVlanId,
       "f3TwampSessionInnerVlanPriority": f3TwampSessionInnerVlanPriority,
       "f3TwampSessionDscpValue": f3TwampSessionDscpValue,
       "f3TwampSessionSequenceNumber": f3TwampSessionSequenceNumber,
       "f3TwampSessionAction": f3TwampSessionAction,
       "f3TwampControlClientTable": f3TwampControlClientTable,
       "f3TwampControlClientEntry": f3TwampControlClientEntry,
       "f3TwampControlClientIndex": f3TwampControlClientIndex,
       "f3TwampControlClientAdminState": f3TwampControlClientAdminState,
       "f3TwampControlClientOperationalState": f3TwampControlClientOperationalState,
       "f3TwampControlClientSecondaryState": f3TwampControlClientSecondaryState,
       "f3TwampControlClientAlias": f3TwampControlClientAlias,
       "f3TwampControlClientPort": f3TwampControlClientPort,
       "f3TwampControlClientStatus": f3TwampControlClientStatus,
       "f3TwampControlClientActionObject": f3TwampControlClientActionObject,
       "f3TwampControlClientAction": f3TwampControlClientAction,
       "f3TwampControlClientStorageType": f3TwampControlClientStorageType,
       "f3TwampControlClientRowStatus": f3TwampControlClientRowStatus,
       "f3TwampControlClientSessionSenderTable": f3TwampControlClientSessionSenderTable,
       "f3TwampControlClientSessionSenderEntry": f3TwampControlClientSessionSenderEntry,
       "f3TwampControlClientSessionSenderIndex": f3TwampControlClientSessionSenderIndex,
       "f3TwampControlClientSessionSender": f3TwampControlClientSessionSender,
       "f3TwampSessionSenderTable": f3TwampSessionSenderTable,
       "f3TwampSessionSenderEntry": f3TwampSessionSenderEntry,
       "f3TwampSessionSenderIndex": f3TwampSessionSenderIndex,
       "f3TwampSessionSenderAdminState": f3TwampSessionSenderAdminState,
       "f3TwampSessionSenderOperationalState": f3TwampSessionSenderOperationalState,
       "f3TwampSessionSenderSecondaryState": f3TwampSessionSenderSecondaryState,
       "f3TwampSessionSenderAlias": f3TwampSessionSenderAlias,
       "f3TwampSessionSenderIpInterface": f3TwampSessionSenderIpInterface,
       "f3TwampSessionSenderUdpPort": f3TwampSessionSenderUdpPort,
       "f3TwampSessionSenderPktSchedTimeInterval": f3TwampSessionSenderPktSchedTimeInterval,
       "f3TwampSessionSenderSrIpv4Address": f3TwampSessionSenderSrIpv4Address,
       "f3TwampSessionSenderSrUdpPort": f3TwampSessionSenderSrUdpPort,
       "f3TwampSessionSenderDscpValue": f3TwampSessionSenderDscpValue,
       "f3TwampSessionSenderNumPkts": f3TwampSessionSenderNumPkts,
       "f3TwampSessionSenderPktSize": f3TwampSessionSenderPktSize,
       "f3TwampSessionSenderTestPattern": f3TwampSessionSenderTestPattern,
       "f3TwampSessionSenderStartTimeType": f3TwampSessionSenderStartTimeType,
       "f3TwampSessionSenderStartDate": f3TwampSessionSenderStartDate,
       "f3TwampSessionSenderStartTime": f3TwampSessionSenderStartTime,
       "f3TwampSessionSenderRespTimeout": f3TwampSessionSenderRespTimeout,
       "f3TwampSessionSenderVlanEnabled": f3TwampSessionSenderVlanEnabled,
       "f3TwampSessionSenderOuterVlanId": f3TwampSessionSenderOuterVlanId,
       "f3TwampSessionSenderOuterVlanPriority": f3TwampSessionSenderOuterVlanPriority,
       "f3TwampSessionSenderOuterVlanEtherType": f3TwampSessionSenderOuterVlanEtherType,
       "f3TwampSessionSenderInnerVlanEnabled": f3TwampSessionSenderInnerVlanEnabled,
       "f3TwampSessionSenderInnerVlanId": f3TwampSessionSenderInnerVlanId,
       "f3TwampSessionSenderInnerVlanPriority": f3TwampSessionSenderInnerVlanPriority,
       "f3TwampSessionSenderInnerVlanEtherType": f3TwampSessionSenderInnerVlanEtherType,
       "f3TwampSessionSenderSeqNumber": f3TwampSessionSenderSeqNumber,
       "f3TwampSessionSenderStatus": f3TwampSessionSenderStatus,
       "f3TwampSessionSenderAssocControlClient": f3TwampSessionSenderAssocControlClient,
       "f3TwampSessionSenderHistoryBins": f3TwampSessionSenderHistoryBins,
       "f3TwampSessionSenderHistoryInterval": f3TwampSessionSenderHistoryInterval,
       "f3TwampSessionSenderDistHistoryBins": f3TwampSessionSenderDistHistoryBins,
       "f3TwampSessionSenderDistHistoryInterval": f3TwampSessionSenderDistHistoryInterval,
       "f3TwampSessionSenderStorageType": f3TwampSessionSenderStorageType,
       "f3TwampSessionSenderRowStatus": f3TwampSessionSenderRowStatus,
       "f3TwampStatsTable": f3TwampStatsTable,
       "f3TwampStatsEntry": f3TwampStatsEntry,
       "f3TwampStatsIndex": f3TwampStatsIndex,
       "f3TwampStatsValid": f3TwampStatsValid,
       "f3TwampStatsAction": f3TwampStatsAction,
       "f3TwampStatsTime": f3TwampStatsTime,
       "f3TwampStatsS2RPkts": f3TwampStatsS2RPkts,
       "f3TwampStatsR2SPkts": f3TwampStatsR2SPkts,
       "f3TwampStatsS2RLostPkts": f3TwampStatsS2RLostPkts,
       "f3TwampStatsR2SLostPkts": f3TwampStatsR2SLostPkts,
       "f3TwampStatsS2RSyncErrs": f3TwampStatsS2RSyncErrs,
       "f3TwampStatsR2SSyncErrs": f3TwampStatsR2SSyncErrs,
       "f3TwampStatsOutOfSeqErrs": f3TwampStatsOutOfSeqErrs,
       "f3TwampStatsSeqGaps": f3TwampStatsSeqGaps,
       "f3TwampStatsMinTwoWayPD": f3TwampStatsMinTwoWayPD,
       "f3TwampStatsMaxTwoWayPD": f3TwampStatsMaxTwoWayPD,
       "f3TwampStatsAvgTwoWayPD": f3TwampStatsAvgTwoWayPD,
       "f3TwampStatsSumTwoWayPD": f3TwampStatsSumTwoWayPD,
       "f3TwampStatsSumOfSqTwoWayPD": f3TwampStatsSumOfSqTwoWayPD,
       "f3TwampStatsMinOneWayS2RPD": f3TwampStatsMinOneWayS2RPD,
       "f3TwampStatsMaxOneWayS2RPD": f3TwampStatsMaxOneWayS2RPD,
       "f3TwampStatsAvgOneWayS2RPD": f3TwampStatsAvgOneWayS2RPD,
       "f3TwampStatsSumOneWayS2RPD": f3TwampStatsSumOneWayS2RPD,
       "f3TwampStatsSumOfSqOneWayS2RPD": f3TwampStatsSumOfSqOneWayS2RPD,
       "f3TwampStatsMinOneWayR2SPD": f3TwampStatsMinOneWayR2SPD,
       "f3TwampStatsMaxOneWayR2SPD": f3TwampStatsMaxOneWayR2SPD,
       "f3TwampStatsAvgOneWayR2SPD": f3TwampStatsAvgOneWayR2SPD,
       "f3TwampStatsSumOneWayR2SPD": f3TwampStatsSumOneWayR2SPD,
       "f3TwampStatsSumOfSqOneWayR2SPD": f3TwampStatsSumOfSqOneWayR2SPD,
       "f3TwampStatsMinOneWayS2RAbsPDV": f3TwampStatsMinOneWayS2RAbsPDV,
       "f3TwampStatsMaxOneWayS2RAbsPDV": f3TwampStatsMaxOneWayS2RAbsPDV,
       "f3TwampStatsAvgOneWayS2RAbsPDV": f3TwampStatsAvgOneWayS2RAbsPDV,
       "f3TwampStatsSumOneWayS2RAbsPDV": f3TwampStatsSumOneWayS2RAbsPDV,
       "f3TwampStatsSumOfSqOneWayS2RAbsPDV": f3TwampStatsSumOfSqOneWayS2RAbsPDV,
       "f3TwampStatsNumOneWayS2RAbsPDV": f3TwampStatsNumOneWayS2RAbsPDV,
       "f3TwampStatsMinOneWayR2SAbsPDV": f3TwampStatsMinOneWayR2SAbsPDV,
       "f3TwampStatsMaxOneWayR2SAbsPDV": f3TwampStatsMaxOneWayR2SAbsPDV,
       "f3TwampStatsAvgOneWayR2SAbsPDV": f3TwampStatsAvgOneWayR2SAbsPDV,
       "f3TwampStatsSumOneWayR2SAbsPDV": f3TwampStatsSumOneWayR2SAbsPDV,
       "f3TwampStatsSumOfSqOneWayR2SAbsPDV": f3TwampStatsSumOfSqOneWayR2SAbsPDV,
       "f3TwampStatsNumOneWayR2SAbsPDV": f3TwampStatsNumOneWayR2SAbsPDV,
       "f3TwampStatsMinOneWayS2RNegPDV": f3TwampStatsMinOneWayS2RNegPDV,
       "f3TwampStatsMaxOneWayS2RNegPDV": f3TwampStatsMaxOneWayS2RNegPDV,
       "f3TwampStatsAvgOneWayS2RNegPDV": f3TwampStatsAvgOneWayS2RNegPDV,
       "f3TwampStatsSumOneWayS2RNegPDV": f3TwampStatsSumOneWayS2RNegPDV,
       "f3TwampStatsSumOfSqOneWayS2RNegPDV": f3TwampStatsSumOfSqOneWayS2RNegPDV,
       "f3TwampStatsNumOneWayS2RNegPDV": f3TwampStatsNumOneWayS2RNegPDV,
       "f3TwampStatsMinOneWayR2SNegPDV": f3TwampStatsMinOneWayR2SNegPDV,
       "f3TwampStatsMaxOneWayR2SNegPDV": f3TwampStatsMaxOneWayR2SNegPDV,
       "f3TwampStatsAvgOneWayR2SNegPDV": f3TwampStatsAvgOneWayR2SNegPDV,
       "f3TwampStatsSumOneWayR2SNegPDV": f3TwampStatsSumOneWayR2SNegPDV,
       "f3TwampStatsSumOfSqOneWayR2SNegPDV": f3TwampStatsSumOfSqOneWayR2SNegPDV,
       "f3TwampStatsNumOneWayR2SNegPDV": f3TwampStatsNumOneWayR2SNegPDV,
       "f3TwampStatsMinOneWayS2RPosPDV": f3TwampStatsMinOneWayS2RPosPDV,
       "f3TwampStatsMaxOneWayS2RPosPDV": f3TwampStatsMaxOneWayS2RPosPDV,
       "f3TwampStatsAvgOneWayS2RPosPDV": f3TwampStatsAvgOneWayS2RPosPDV,
       "f3TwampStatsSumOneWayS2RPosPDV": f3TwampStatsSumOneWayS2RPosPDV,
       "f3TwampStatsSumOfSqOneWayS2RPosPDV": f3TwampStatsSumOfSqOneWayS2RPosPDV,
       "f3TwampStatsNumOneWayS2RPosPDV": f3TwampStatsNumOneWayS2RPosPDV,
       "f3TwampStatsMinOneWayR2SPosPDV": f3TwampStatsMinOneWayR2SPosPDV,
       "f3TwampStatsMaxOneWayR2SPosPDV": f3TwampStatsMaxOneWayR2SPosPDV,
       "f3TwampStatsAvgOneWayR2SPosPDV": f3TwampStatsAvgOneWayR2SPosPDV,
       "f3TwampStatsSumOneWayR2SPosPDV": f3TwampStatsSumOneWayR2SPosPDV,
       "f3TwampStatsSumOfSqOneWayR2SPosPDV": f3TwampStatsSumOfSqOneWayR2SPosPDV,
       "f3TwampStatsNumOneWayR2SPosPDV": f3TwampStatsNumOneWayR2SPosPDV,
       "f3TwampStatsNumTwoWayPD": f3TwampStatsNumTwoWayPD,
       "f3TwampStatsNumOneWayS2RPD": f3TwampStatsNumOneWayS2RPD,
       "f3TwampStatsNumOneWayR2SPD": f3TwampStatsNumOneWayR2SPD,
       "f3TwampHistoryTable": f3TwampHistoryTable,
       "f3TwampHistoryEntry": f3TwampHistoryEntry,
       "f3TwampHistoryIndex": f3TwampHistoryIndex,
       "f3TwampHistoryValid": f3TwampHistoryValid,
       "f3TwampHistoryAction": f3TwampHistoryAction,
       "f3TwampHistoryTime": f3TwampHistoryTime,
       "f3TwampHistoryS2RPkts": f3TwampHistoryS2RPkts,
       "f3TwampHistoryR2SPkts": f3TwampHistoryR2SPkts,
       "f3TwampHistoryS2RLostPkts": f3TwampHistoryS2RLostPkts,
       "f3TwampHistoryR2SLostPkts": f3TwampHistoryR2SLostPkts,
       "f3TwampHistoryS2RSyncErrs": f3TwampHistoryS2RSyncErrs,
       "f3TwampHistoryR2SSyncErrs": f3TwampHistoryR2SSyncErrs,
       "f3TwampHistoryOutOfSeqErrs": f3TwampHistoryOutOfSeqErrs,
       "f3TwampHistorySeqGaps": f3TwampHistorySeqGaps,
       "f3TwampHistoryMinTwoWayPD": f3TwampHistoryMinTwoWayPD,
       "f3TwampHistoryMaxTwoWayPD": f3TwampHistoryMaxTwoWayPD,
       "f3TwampHistoryAvgTwoWayPD": f3TwampHistoryAvgTwoWayPD,
       "f3TwampHistorySumTwoWayPD": f3TwampHistorySumTwoWayPD,
       "f3TwampHistorySumOfSqTwoWayPD": f3TwampHistorySumOfSqTwoWayPD,
       "f3TwampHistoryMinOneWayS2RPD": f3TwampHistoryMinOneWayS2RPD,
       "f3TwampHistoryMaxOneWayS2RPD": f3TwampHistoryMaxOneWayS2RPD,
       "f3TwampHistoryAvgOneWayS2RPD": f3TwampHistoryAvgOneWayS2RPD,
       "f3TwampHistorySumOneWayS2RPD": f3TwampHistorySumOneWayS2RPD,
       "f3TwampHistorySumOfSqOneWayS2RPD": f3TwampHistorySumOfSqOneWayS2RPD,
       "f3TwampHistoryMinOneWayR2SPD": f3TwampHistoryMinOneWayR2SPD,
       "f3TwampHistoryMaxOneWayR2SPD": f3TwampHistoryMaxOneWayR2SPD,
       "f3TwampHistoryAvgOneWayR2SPD": f3TwampHistoryAvgOneWayR2SPD,
       "f3TwampHistorySumOneWayR2SPD": f3TwampHistorySumOneWayR2SPD,
       "f3TwampHistorySumOfSqOneWayR2SPD": f3TwampHistorySumOfSqOneWayR2SPD,
       "f3TwampHistoryMinOneWayS2RAbsPDV": f3TwampHistoryMinOneWayS2RAbsPDV,
       "f3TwampHistoryMaxOneWayS2RAbsPDV": f3TwampHistoryMaxOneWayS2RAbsPDV,
       "f3TwampHistoryAvgOneWayS2RAbsPDV": f3TwampHistoryAvgOneWayS2RAbsPDV,
       "f3TwampHistorySumOneWayS2RAbsPDV": f3TwampHistorySumOneWayS2RAbsPDV,
       "f3TwampHistorySumOfSqOneWayS2RAbsPDV": f3TwampHistorySumOfSqOneWayS2RAbsPDV,
       "f3TwampHistoryNumOneWayS2RAbsPDV": f3TwampHistoryNumOneWayS2RAbsPDV,
       "f3TwampHistoryMinOneWayR2SAbsPDV": f3TwampHistoryMinOneWayR2SAbsPDV,
       "f3TwampHistoryMaxOneWayR2SAbsPDV": f3TwampHistoryMaxOneWayR2SAbsPDV,
       "f3TwampHistoryAvgOneWayR2SAbsPDV": f3TwampHistoryAvgOneWayR2SAbsPDV,
       "f3TwampHistorySumOneWayR2SAbsPDV": f3TwampHistorySumOneWayR2SAbsPDV,
       "f3TwampHistorySumOfSqOneWayR2SAbsPDV": f3TwampHistorySumOfSqOneWayR2SAbsPDV,
       "f3TwampHistoryNumOneWayR2SAbsPDV": f3TwampHistoryNumOneWayR2SAbsPDV,
       "f3TwampHistoryMinOneWayS2RNegPDV": f3TwampHistoryMinOneWayS2RNegPDV,
       "f3TwampHistoryMaxOneWayS2RNegPDV": f3TwampHistoryMaxOneWayS2RNegPDV,
       "f3TwampHistoryAvgOneWayS2RNegPDV": f3TwampHistoryAvgOneWayS2RNegPDV,
       "f3TwampHistorySumOneWayS2RNegPDV": f3TwampHistorySumOneWayS2RNegPDV,
       "f3TwampHistorySumOfSqOneWayS2RNegPDV": f3TwampHistorySumOfSqOneWayS2RNegPDV,
       "f3TwampHistoryNumOneWayS2RNegPDV": f3TwampHistoryNumOneWayS2RNegPDV,
       "f3TwampHistoryMinOneWayR2SNegPDV": f3TwampHistoryMinOneWayR2SNegPDV,
       "f3TwampHistoryMaxOneWayR2SNegPDV": f3TwampHistoryMaxOneWayR2SNegPDV,
       "f3TwampHistoryAvgOneWayR2SNegPDV": f3TwampHistoryAvgOneWayR2SNegPDV,
       "f3TwampHistorySumOneWayR2SNegPDV": f3TwampHistorySumOneWayR2SNegPDV,
       "f3TwampHistorySumOfSqOneWayR2SNegPDV": f3TwampHistorySumOfSqOneWayR2SNegPDV,
       "f3TwampHistoryNumOneWayR2SNegPDV": f3TwampHistoryNumOneWayR2SNegPDV,
       "f3TwampHistoryMinOneWayS2RPosPDV": f3TwampHistoryMinOneWayS2RPosPDV,
       "f3TwampHistoryMaxOneWayS2RPosPDV": f3TwampHistoryMaxOneWayS2RPosPDV,
       "f3TwampHistoryAvgOneWayS2RPosPDV": f3TwampHistoryAvgOneWayS2RPosPDV,
       "f3TwampHistorySumOneWayS2RPosPDV": f3TwampHistorySumOneWayS2RPosPDV,
       "f3TwampHistorySumOfSqOneWayS2RPosPDV": f3TwampHistorySumOfSqOneWayS2RPosPDV,
       "f3TwampHistoryNumOneWayS2RPosPDV": f3TwampHistoryNumOneWayS2RPosPDV,
       "f3TwampHistoryMinOneWayR2SPosPDV": f3TwampHistoryMinOneWayR2SPosPDV,
       "f3TwampHistoryMaxOneWayR2SPosPDV": f3TwampHistoryMaxOneWayR2SPosPDV,
       "f3TwampHistoryAvgOneWayR2SPosPDV": f3TwampHistoryAvgOneWayR2SPosPDV,
       "f3TwampHistorySumOneWayR2SPosPDV": f3TwampHistorySumOneWayR2SPosPDV,
       "f3TwampHistorySumOfSqOneWayR2SPosPDV": f3TwampHistorySumOfSqOneWayR2SPosPDV,
       "f3TwampHistoryNumOneWayR2SPosPDV": f3TwampHistoryNumOneWayR2SPosPDV,
       "f3TwampHistoryNumTwoWayPD": f3TwampHistoryNumTwoWayPD,
       "f3TwampHistoryNumOneWayS2RPD": f3TwampHistoryNumOneWayS2RPD,
       "f3TwampHistoryNumOneWayR2SPD": f3TwampHistoryNumOneWayR2SPD,
       "f3TwampDistStatsConfigTable": f3TwampDistStatsConfigTable,
       "f3TwampDistStatsConfigEntry": f3TwampDistStatsConfigEntry,
       "f3TwampDistStatsConfigIndex": f3TwampDistStatsConfigIndex,
       "f3TwampDistStatsConfigMinVal": f3TwampDistStatsConfigMinVal,
       "f3TwampDistStatsConfigMaxVal": f3TwampDistStatsConfigMaxVal,
       "f3TwampDistStatsConfigNumBins": f3TwampDistStatsConfigNumBins,
       "f3TwampDistStatsTable": f3TwampDistStatsTable,
       "f3TwampDistStatsEntry": f3TwampDistStatsEntry,
       "f3TwampDistStatsValid": f3TwampDistStatsValid,
       "f3TwampDistStatsTime": f3TwampDistStatsTime,
       "f3TwampDistStatsAction": f3TwampDistStatsAction,
       "f3TwampDistStatsNumBins": f3TwampDistStatsNumBins,
       "f3TwampDistStatsLTMin": f3TwampDistStatsLTMin,
       "f3TwampDistStatsGTMax": f3TwampDistStatsGTMax,
       "f3TwampDistStatsBinTable": f3TwampDistStatsBinTable,
       "f3TwampDistStatsBinEntry": f3TwampDistStatsBinEntry,
       "f3TwampDistStatsBinIndex": f3TwampDistStatsBinIndex,
       "f3TwampDistStatsBinLower": f3TwampDistStatsBinLower,
       "f3TwampDistStatsBinUpper": f3TwampDistStatsBinUpper,
       "f3TwampDistStatsBinNumSamples": f3TwampDistStatsBinNumSamples,
       "f3TwampDistHistoryTable": f3TwampDistHistoryTable,
       "f3TwampDistHistoryEntry": f3TwampDistHistoryEntry,
       "f3TwampDistHistoryIndex": f3TwampDistHistoryIndex,
       "f3TwampDistHistoryValid": f3TwampDistHistoryValid,
       "f3TwampDistHistoryTime": f3TwampDistHistoryTime,
       "f3TwampDistHistoryAction": f3TwampDistHistoryAction,
       "f3TwampDistHistoryNumBins": f3TwampDistHistoryNumBins,
       "f3TwampDistHistoryLTMin": f3TwampDistHistoryLTMin,
       "f3TwampDistHistoryGTMax": f3TwampDistHistoryGTMax,
       "f3TwampDistHistoryBinTable": f3TwampDistHistoryBinTable,
       "f3TwampDistHistoryBinEntry": f3TwampDistHistoryBinEntry,
       "f3TwampDistHistoryBinIndex": f3TwampDistHistoryBinIndex,
       "f3TwampDistHistoryBinLower": f3TwampDistHistoryBinLower,
       "f3TwampDistHistoryBinUpper": f3TwampDistHistoryBinUpper,
       "f3TwampDistHistoryBinNumSamples": f3TwampDistHistoryBinNumSamples,
       "f3TwampStatsThresholdTable": f3TwampStatsThresholdTable,
       "f3TwampStatsThresholdEntry": f3TwampStatsThresholdEntry,
       "f3TwampStatsThresholdIndex": f3TwampStatsThresholdIndex,
       "f3TwampStatsThresholdVariable": f3TwampStatsThresholdVariable,
       "f3TwampStatsThresholdAbsValueLo": f3TwampStatsThresholdAbsValueLo,
       "f3TwampStatsThresholdAbsValueHi": f3TwampStatsThresholdAbsValueHi,
       "f3TwampStatsThresholdMonValue": f3TwampStatsThresholdMonValue,
       "f3TwampCounterObjects": f3TwampCounterObjects,
       "f3TwampActionObjects": f3TwampActionObjects,
       "f3TwampConformance": f3TwampConformance,
       "f3TwampCompliances": f3TwampCompliances,
       "f3TwampCompliance": f3TwampCompliance,
       "f3TwampGroups": f3TwampGroups,
       "f3TwampIpInterfaceGroup": f3TwampIpInterfaceGroup,
       "f3TwampServerGroup": f3TwampServerGroup,
       "f3TwampServerSessionReflectorGroup": f3TwampServerSessionReflectorGroup,
       "f3TwampSessionReflectorGroup": f3TwampSessionReflectorGroup,
       "f3TwampSessionGroup": f3TwampSessionGroup,
       "f3TwampControlClientGroup": f3TwampControlClientGroup,
       "f3TwampControlClientSessionSenderGroup": f3TwampControlClientSessionSenderGroup,
       "f3TwampSessionSenderGroup": f3TwampSessionSenderGroup,
       "f3TwampStatisticsGroup": f3TwampStatisticsGroup,
       "f3TwampDistributionStatisticsGroup": f3TwampDistributionStatisticsGroup,
       "f3TwampThresholdGroup": f3TwampThresholdGroup,
       "f3TwampNotifications": f3TwampNotifications,
       "twampSessionSenderThresholdCrossingAlert": twampSessionSenderThresholdCrossingAlert}
)
