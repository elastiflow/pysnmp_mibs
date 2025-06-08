# SNMP MIB module (RUIJIE-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-BFD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ruijieBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48)
)
if mibBuilder.loadTexts:
    ruijieBfdMIB.setRevisions(
        ("2012-04-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieBfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RuijieBfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class RuijieBfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class RuijieBfdDiagTC(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 0),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("neighborSignaledSessionDown", 3),
          ("forwardingPlaneReset", 4),
          ("pathDown", 5),
          ("concatenatedPathDown", 6),
          ("administrativelyDown", 7),
          ("reverseConcatenatedPathDown", 8))
    )



class RuijieBfdSessTypeTC(TextualConvention, Integer32):
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
        *(("singleHop", 1),
          ("multiHopTotallyArbitraryPaths", 2),
          ("multiHopOutOfBandSignaling", 3),
          ("multiHopUnidirectionalLinks", 4),
          ("multiPointHead", 5),
          ("multiPointTail", 6))
    )



class RuijieBfdSessOperModeTC(TextualConvention, Integer32):
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
        *(("asyncModeWEchoFunction", 1),
          ("asynchModeWOEchoFunction", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4))
    )



class RuijieBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class RuijieBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class RuijieBfdSessStateTC(TextualConvention, Integer32):
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4),
          ("failing", 5))
    )



class RuijieBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", -1),
          ("reserved", 0),
          ("simplePassword", 1),
          ("keyedMD5", 2),
          ("meticulousKeyedMD5", 3),
          ("keyedSHA1", 4),
          ("meticulousKeyedSHA1", 5))
    )



class RuijieBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs

_RuijieBfdNotifications_ObjectIdentity = ObjectIdentity
ruijieBfdNotifications = _RuijieBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 0)
)
_RuijieBfdObjects_ObjectIdentity = ObjectIdentity
ruijieBfdObjects = _RuijieBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1)
)
_RuijieBfdScalarObjects_ObjectIdentity = ObjectIdentity
ruijieBfdScalarObjects = _RuijieBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 1)
)


class _RuijieBfdAdminStatus_Type(Integer32):
    """Custom type ruijieBfdAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RuijieBfdAdminStatus_Type.__name__ = "Integer32"
_RuijieBfdAdminStatus_Object = MibScalar
ruijieBfdAdminStatus = _RuijieBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 1, 1),
    _RuijieBfdAdminStatus_Type()
)
ruijieBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieBfdAdminStatus.setStatus("current")


class _RuijieBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type ruijieBfdSessNotificationsEnable based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessNotificationsEnable_Type.__name__ = "TruthValue"
_RuijieBfdSessNotificationsEnable_Object = MibScalar
ruijieBfdSessNotificationsEnable = _RuijieBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 1, 2),
    _RuijieBfdSessNotificationsEnable_Type()
)
ruijieBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieBfdSessNotificationsEnable.setStatus("current")
_RuijieBfdSessTable_Object = MibTable
ruijieBfdSessTable = _RuijieBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieBfdSessTable.setStatus("current")
_RuijieBfdSessEntry_Object = MibTableRow
ruijieBfdSessEntry = _RuijieBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1)
)
ruijieBfdSessEntry.setIndexNames(
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessIndex"),
)
if mibBuilder.loadTexts:
    ruijieBfdSessEntry.setStatus("current")
_RuijieBfdSessIndex_Type = RuijieBfdSessIndexTC
_RuijieBfdSessIndex_Object = MibTableColumn
ruijieBfdSessIndex = _RuijieBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 1),
    _RuijieBfdSessIndex_Type()
)
ruijieBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieBfdSessIndex.setStatus("current")


class _RuijieBfdSessVersionNumber_Type(Unsigned32):
    """Custom type ruijieBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_RuijieBfdSessVersionNumber_Object = MibTableColumn
ruijieBfdSessVersionNumber = _RuijieBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 2),
    _RuijieBfdSessVersionNumber_Type()
)
ruijieBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessVersionNumber.setStatus("current")
_RuijieBfdSessType_Type = RuijieBfdSessTypeTC
_RuijieBfdSessType_Object = MibTableColumn
ruijieBfdSessType = _RuijieBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 3),
    _RuijieBfdSessType_Type()
)
ruijieBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessType.setStatus("current")


class _RuijieBfdSessDiscriminator_Type(Unsigned32):
    """Custom type ruijieBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_RuijieBfdSessDiscriminator_Object = MibTableColumn
ruijieBfdSessDiscriminator = _RuijieBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 4),
    _RuijieBfdSessDiscriminator_Type()
)
ruijieBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessDiscriminator.setStatus("current")


class _RuijieBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type ruijieBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_RuijieBfdSessRemoteDiscr_Object = MibTableColumn
ruijieBfdSessRemoteDiscr = _RuijieBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 5),
    _RuijieBfdSessRemoteDiscr_Type()
)
ruijieBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessRemoteDiscr.setStatus("current")


class _RuijieBfdSessDestinationUdpPort_Type(RuijieBfdCtrlDestPortNumberTC):
    """Custom type ruijieBfdSessDestinationUdpPort based on RuijieBfdCtrlDestPortNumberTC"""
    defaultValue = 0


_RuijieBfdSessDestinationUdpPort_Type.__name__ = "RuijieBfdCtrlDestPortNumberTC"
_RuijieBfdSessDestinationUdpPort_Object = MibTableColumn
ruijieBfdSessDestinationUdpPort = _RuijieBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 6),
    _RuijieBfdSessDestinationUdpPort_Type()
)
ruijieBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDestinationUdpPort.setStatus("current")


class _RuijieBfdSessSourceUdpPort_Type(RuijieBfdCtrlSourcePortNumberTC):
    """Custom type ruijieBfdSessSourceUdpPort based on RuijieBfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_RuijieBfdSessSourceUdpPort_Type.__name__ = "RuijieBfdCtrlSourcePortNumberTC"
_RuijieBfdSessSourceUdpPort_Object = MibTableColumn
ruijieBfdSessSourceUdpPort = _RuijieBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 7),
    _RuijieBfdSessSourceUdpPort_Type()
)
ruijieBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessSourceUdpPort.setStatus("current")


class _RuijieBfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type ruijieBfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_RuijieBfdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_RuijieBfdSessEchoSourceUdpPort_Object = MibTableColumn
ruijieBfdSessEchoSourceUdpPort = _RuijieBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 8),
    _RuijieBfdSessEchoSourceUdpPort_Type()
)
ruijieBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessEchoSourceUdpPort.setStatus("current")


class _RuijieBfdSessAdminStatus_Type(Integer32):
    """Custom type ruijieBfdSessAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_RuijieBfdSessAdminStatus_Type.__name__ = "Integer32"
_RuijieBfdSessAdminStatus_Object = MibTableColumn
ruijieBfdSessAdminStatus = _RuijieBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 9),
    _RuijieBfdSessAdminStatus_Type()
)
ruijieBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessAdminStatus.setStatus("current")


class _RuijieBfdSessState_Type(RuijieBfdSessStateTC):
    """Custom type ruijieBfdSessState based on RuijieBfdSessStateTC"""
    defaultValue = 2


_RuijieBfdSessState_Type.__name__ = "RuijieBfdSessStateTC"
_RuijieBfdSessState_Object = MibTableColumn
ruijieBfdSessState = _RuijieBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 10),
    _RuijieBfdSessState_Type()
)
ruijieBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessState.setStatus("current")


class _RuijieBfdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type ruijieBfdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_RuijieBfdSessRemoteHeardFlag_Object = MibTableColumn
ruijieBfdSessRemoteHeardFlag = _RuijieBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 11),
    _RuijieBfdSessRemoteHeardFlag_Type()
)
ruijieBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessRemoteHeardFlag.setStatus("current")
_RuijieBfdSessDiag_Type = RuijieBfdDiagTC
_RuijieBfdSessDiag_Object = MibTableColumn
ruijieBfdSessDiag = _RuijieBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 12),
    _RuijieBfdSessDiag_Type()
)
ruijieBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessDiag.setStatus("current")
_RuijieBfdSessOperMode_Type = RuijieBfdSessOperModeTC
_RuijieBfdSessOperMode_Object = MibTableColumn
ruijieBfdSessOperMode = _RuijieBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 13),
    _RuijieBfdSessOperMode_Type()
)
ruijieBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessOperMode.setStatus("current")


class _RuijieBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type ruijieBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_RuijieBfdSessDemandModeDesiredFlag_Object = MibTableColumn
ruijieBfdSessDemandModeDesiredFlag = _RuijieBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 14),
    _RuijieBfdSessDemandModeDesiredFlag_Type()
)
ruijieBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDemandModeDesiredFlag.setStatus("current")


class _RuijieBfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type ruijieBfdSessControlPlaneIndepFlag based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessControlPlaneIndepFlag_Type.__name__ = "TruthValue"
_RuijieBfdSessControlPlaneIndepFlag_Object = MibTableColumn
ruijieBfdSessControlPlaneIndepFlag = _RuijieBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 15),
    _RuijieBfdSessControlPlaneIndepFlag_Type()
)
ruijieBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessControlPlaneIndepFlag.setStatus("current")


class _RuijieBfdSessMultipointFlag_Type(TruthValue):
    """Custom type ruijieBfdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessMultipointFlag_Type.__name__ = "TruthValue"
_RuijieBfdSessMultipointFlag_Object = MibTableColumn
ruijieBfdSessMultipointFlag = _RuijieBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 16),
    _RuijieBfdSessMultipointFlag_Type()
)
ruijieBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessMultipointFlag.setStatus("current")
_RuijieBfdSessInterface_Type = InterfaceIndexOrZero
_RuijieBfdSessInterface_Object = MibTableColumn
ruijieBfdSessInterface = _RuijieBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 17),
    _RuijieBfdSessInterface_Type()
)
ruijieBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessInterface.setStatus("current")
_RuijieBfdSessSrcAddrType_Type = InetAddressType
_RuijieBfdSessSrcAddrType_Object = MibTableColumn
ruijieBfdSessSrcAddrType = _RuijieBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 18),
    _RuijieBfdSessSrcAddrType_Type()
)
ruijieBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessSrcAddrType.setStatus("current")
_RuijieBfdSessSrcAddr_Type = InetAddress
_RuijieBfdSessSrcAddr_Object = MibTableColumn
ruijieBfdSessSrcAddr = _RuijieBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 19),
    _RuijieBfdSessSrcAddr_Type()
)
ruijieBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessSrcAddr.setStatus("current")
_RuijieBfdSessDstAddrType_Type = InetAddressType
_RuijieBfdSessDstAddrType_Object = MibTableColumn
ruijieBfdSessDstAddrType = _RuijieBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 20),
    _RuijieBfdSessDstAddrType_Type()
)
ruijieBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDstAddrType.setStatus("current")
_RuijieBfdSessDstAddr_Type = InetAddress
_RuijieBfdSessDstAddr_Object = MibTableColumn
ruijieBfdSessDstAddr = _RuijieBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 21),
    _RuijieBfdSessDstAddr_Type()
)
ruijieBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDstAddr.setStatus("current")


class _RuijieBfdSessGTSM_Type(TruthValue):
    """Custom type ruijieBfdSessGTSM based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessGTSM_Type.__name__ = "TruthValue"
_RuijieBfdSessGTSM_Object = MibTableColumn
ruijieBfdSessGTSM = _RuijieBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 22),
    _RuijieBfdSessGTSM_Type()
)
ruijieBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessGTSM.setStatus("current")


class _RuijieBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type ruijieBfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_RuijieBfdSessGTSMTTL_Object = MibTableColumn
ruijieBfdSessGTSMTTL = _RuijieBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 23),
    _RuijieBfdSessGTSMTTL_Type()
)
ruijieBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessGTSMTTL.setStatus("current")
_RuijieBfdSessDesiredMinTxInterval_Type = RuijieBfdIntervalTC
_RuijieBfdSessDesiredMinTxInterval_Object = MibTableColumn
ruijieBfdSessDesiredMinTxInterval = _RuijieBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 24),
    _RuijieBfdSessDesiredMinTxInterval_Type()
)
ruijieBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDesiredMinTxInterval.setStatus("current")
_RuijieBfdSessReqMinRxInterval_Type = RuijieBfdIntervalTC
_RuijieBfdSessReqMinRxInterval_Object = MibTableColumn
ruijieBfdSessReqMinRxInterval = _RuijieBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 25),
    _RuijieBfdSessReqMinRxInterval_Type()
)
ruijieBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessReqMinRxInterval.setStatus("current")
_RuijieBfdSessReqMinEchoRxInterval_Type = RuijieBfdIntervalTC
_RuijieBfdSessReqMinEchoRxInterval_Object = MibTableColumn
ruijieBfdSessReqMinEchoRxInterval = _RuijieBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 26),
    _RuijieBfdSessReqMinEchoRxInterval_Type()
)
ruijieBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessReqMinEchoRxInterval.setStatus("current")
_RuijieBfdSessDetectMult_Type = RuijieBfdMultiplierTC
_RuijieBfdSessDetectMult_Object = MibTableColumn
ruijieBfdSessDetectMult = _RuijieBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 27),
    _RuijieBfdSessDetectMult_Type()
)
ruijieBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDetectMult.setStatus("current")
_RuijieBfdSessNegotiatedInterval_Type = RuijieBfdIntervalTC
_RuijieBfdSessNegotiatedInterval_Object = MibTableColumn
ruijieBfdSessNegotiatedInterval = _RuijieBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 28),
    _RuijieBfdSessNegotiatedInterval_Type()
)
ruijieBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessNegotiatedInterval.setStatus("current")
_RuijieBfdSessNegotiatedEchoInterval_Type = RuijieBfdIntervalTC
_RuijieBfdSessNegotiatedEchoInterval_Object = MibTableColumn
ruijieBfdSessNegotiatedEchoInterval = _RuijieBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 29),
    _RuijieBfdSessNegotiatedEchoInterval_Type()
)
ruijieBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessNegotiatedEchoInterval.setStatus("current")
_RuijieBfdSessNegotiatedDetectMult_Type = RuijieBfdMultiplierTC
_RuijieBfdSessNegotiatedDetectMult_Object = MibTableColumn
ruijieBfdSessNegotiatedDetectMult = _RuijieBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 30),
    _RuijieBfdSessNegotiatedDetectMult_Type()
)
ruijieBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessNegotiatedDetectMult.setStatus("current")


class _RuijieBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type ruijieBfdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_RuijieBfdSessAuthPresFlag_Type.__name__ = "TruthValue"
_RuijieBfdSessAuthPresFlag_Object = MibTableColumn
ruijieBfdSessAuthPresFlag = _RuijieBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 31),
    _RuijieBfdSessAuthPresFlag_Type()
)
ruijieBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessAuthPresFlag.setStatus("current")


class _RuijieBfdSessAuthenticationType_Type(RuijieBfdSessAuthenticationTypeTC):
    """Custom type ruijieBfdSessAuthenticationType based on RuijieBfdSessAuthenticationTypeTC"""
    defaultValue = -1


_RuijieBfdSessAuthenticationType_Type.__name__ = "RuijieBfdSessAuthenticationTypeTC"
_RuijieBfdSessAuthenticationType_Object = MibTableColumn
ruijieBfdSessAuthenticationType = _RuijieBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 32),
    _RuijieBfdSessAuthenticationType_Type()
)
ruijieBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessAuthenticationType.setStatus("current")


class _RuijieBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type ruijieBfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RuijieBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_RuijieBfdSessAuthenticationKeyID_Object = MibTableColumn
ruijieBfdSessAuthenticationKeyID = _RuijieBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 33),
    _RuijieBfdSessAuthenticationKeyID_Type()
)
ruijieBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessAuthenticationKeyID.setStatus("current")
_RuijieBfdSessAuthenticationKey_Type = RuijieBfdSessionAuthenticationKeyTC
_RuijieBfdSessAuthenticationKey_Object = MibTableColumn
ruijieBfdSessAuthenticationKey = _RuijieBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 34),
    _RuijieBfdSessAuthenticationKey_Type()
)
ruijieBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessAuthenticationKey.setStatus("current")
_RuijieBfdSessStorageType_Type = StorageType
_RuijieBfdSessStorageType_Object = MibTableColumn
ruijieBfdSessStorageType = _RuijieBfdSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 35),
    _RuijieBfdSessStorageType_Type()
)
ruijieBfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessStorageType.setStatus("current")
_RuijieBfdSessRowStatus_Type = RowStatus
_RuijieBfdSessRowStatus_Object = MibTableColumn
ruijieBfdSessRowStatus = _RuijieBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 36),
    _RuijieBfdSessRowStatus_Type()
)
ruijieBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessRowStatus.setStatus("current")


class _RuijieBfdSessIfName_Type(DisplayString):
    """Custom type ruijieBfdSessIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieBfdSessIfName_Type.__name__ = "DisplayString"
_RuijieBfdSessIfName_Object = MibTableColumn
ruijieBfdSessIfName = _RuijieBfdSessIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 37),
    _RuijieBfdSessIfName_Type()
)
ruijieBfdSessIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessIfName.setStatus("current")


class _RuijieBfdSessIfDes_Type(DisplayString):
    """Custom type ruijieBfdSessIfDes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieBfdSessIfDes_Type.__name__ = "DisplayString"
_RuijieBfdSessIfDes_Object = MibTableColumn
ruijieBfdSessIfDes = _RuijieBfdSessIfDes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 2, 1, 38),
    _RuijieBfdSessIfDes_Type()
)
ruijieBfdSessIfDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessIfDes.setStatus("current")
_RuijieBfdSessPerfTable_Object = MibTable
ruijieBfdSessPerfTable = _RuijieBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieBfdSessPerfTable.setStatus("current")
_RuijieBfdSessPerfEntry_Object = MibTableRow
ruijieBfdSessPerfEntry = _RuijieBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEntry.setStatus("current")
_RuijieBfdSessPerfCtrlPktIn_Type = Counter32
_RuijieBfdSessPerfCtrlPktIn_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktIn = _RuijieBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 1),
    _RuijieBfdSessPerfCtrlPktIn_Type()
)
ruijieBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktIn.setStatus("current")
_RuijieBfdSessPerfCtrlPktOut_Type = Counter32
_RuijieBfdSessPerfCtrlPktOut_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktOut = _RuijieBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 2),
    _RuijieBfdSessPerfCtrlPktOut_Type()
)
ruijieBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktOut.setStatus("current")
_RuijieBfdSessPerfCtrlPktDrop_Type = Counter32
_RuijieBfdSessPerfCtrlPktDrop_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktDrop = _RuijieBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 3),
    _RuijieBfdSessPerfCtrlPktDrop_Type()
)
ruijieBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktDrop.setStatus("current")
_RuijieBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_RuijieBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktDropLastTime = _RuijieBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 4),
    _RuijieBfdSessPerfCtrlPktDropLastTime_Type()
)
ruijieBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_RuijieBfdSessPerfEchoPktIn_Type = Counter32
_RuijieBfdSessPerfEchoPktIn_Object = MibTableColumn
ruijieBfdSessPerfEchoPktIn = _RuijieBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 5),
    _RuijieBfdSessPerfEchoPktIn_Type()
)
ruijieBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktIn.setStatus("current")
_RuijieBfdSessPerfEchoPktOut_Type = Counter32
_RuijieBfdSessPerfEchoPktOut_Object = MibTableColumn
ruijieBfdSessPerfEchoPktOut = _RuijieBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 6),
    _RuijieBfdSessPerfEchoPktOut_Type()
)
ruijieBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktOut.setStatus("current")
_RuijieBfdSessPerfEchoPktDrop_Type = Counter32
_RuijieBfdSessPerfEchoPktDrop_Object = MibTableColumn
ruijieBfdSessPerfEchoPktDrop = _RuijieBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 7),
    _RuijieBfdSessPerfEchoPktDrop_Type()
)
ruijieBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktDrop.setStatus("current")
_RuijieBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_RuijieBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
ruijieBfdSessPerfEchoPktDropLastTime = _RuijieBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 8),
    _RuijieBfdSessPerfEchoPktDropLastTime_Type()
)
ruijieBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktDropLastTime.setStatus("current")
_RuijieBfdSessUpTime_Type = TimeStamp
_RuijieBfdSessUpTime_Object = MibTableColumn
ruijieBfdSessUpTime = _RuijieBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 9),
    _RuijieBfdSessUpTime_Type()
)
ruijieBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessUpTime.setStatus("current")
_RuijieBfdSessPerfLastSessDownTime_Type = TimeStamp
_RuijieBfdSessPerfLastSessDownTime_Object = MibTableColumn
ruijieBfdSessPerfLastSessDownTime = _RuijieBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 10),
    _RuijieBfdSessPerfLastSessDownTime_Type()
)
ruijieBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfLastSessDownTime.setStatus("current")
_RuijieBfdSessPerfLastCommLostDiag_Type = RuijieBfdDiagTC
_RuijieBfdSessPerfLastCommLostDiag_Object = MibTableColumn
ruijieBfdSessPerfLastCommLostDiag = _RuijieBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 11),
    _RuijieBfdSessPerfLastCommLostDiag_Type()
)
ruijieBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfLastCommLostDiag.setStatus("current")
_RuijieBfdSessPerfSessUpCount_Type = Counter32
_RuijieBfdSessPerfSessUpCount_Object = MibTableColumn
ruijieBfdSessPerfSessUpCount = _RuijieBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 12),
    _RuijieBfdSessPerfSessUpCount_Type()
)
ruijieBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfSessUpCount.setStatus("current")
_RuijieBfdSessPerfDiscTime_Type = TimeStamp
_RuijieBfdSessPerfDiscTime_Object = MibTableColumn
ruijieBfdSessPerfDiscTime = _RuijieBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 13),
    _RuijieBfdSessPerfDiscTime_Type()
)
ruijieBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfDiscTime.setStatus("current")
_RuijieBfdSessPerfCtrlPktInHC_Type = Counter64
_RuijieBfdSessPerfCtrlPktInHC_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktInHC = _RuijieBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 14),
    _RuijieBfdSessPerfCtrlPktInHC_Type()
)
ruijieBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktInHC.setStatus("current")
_RuijieBfdSessPerfCtrlPktOutHC_Type = Counter64
_RuijieBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktOutHC = _RuijieBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 15),
    _RuijieBfdSessPerfCtrlPktOutHC_Type()
)
ruijieBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktOutHC.setStatus("current")
_RuijieBfdSessPerfCtrlPktDropHC_Type = Counter64
_RuijieBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
ruijieBfdSessPerfCtrlPktDropHC = _RuijieBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 16),
    _RuijieBfdSessPerfCtrlPktDropHC_Type()
)
ruijieBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfCtrlPktDropHC.setStatus("current")
_RuijieBfdSessPerfEchoPktInHC_Type = Counter64
_RuijieBfdSessPerfEchoPktInHC_Object = MibTableColumn
ruijieBfdSessPerfEchoPktInHC = _RuijieBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 17),
    _RuijieBfdSessPerfEchoPktInHC_Type()
)
ruijieBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktInHC.setStatus("current")
_RuijieBfdSessPerfEchoPktOutHC_Type = Counter64
_RuijieBfdSessPerfEchoPktOutHC_Object = MibTableColumn
ruijieBfdSessPerfEchoPktOutHC = _RuijieBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 18),
    _RuijieBfdSessPerfEchoPktOutHC_Type()
)
ruijieBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktOutHC.setStatus("current")
_RuijieBfdSessPerfEchoPktDropHC_Type = Counter64
_RuijieBfdSessPerfEchoPktDropHC_Object = MibTableColumn
ruijieBfdSessPerfEchoPktDropHC = _RuijieBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 3, 1, 19),
    _RuijieBfdSessPerfEchoPktDropHC_Type()
)
ruijieBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessPerfEchoPktDropHC.setStatus("current")
_RuijieBfdSessDiscMapTable_Object = MibTable
ruijieBfdSessDiscMapTable = _RuijieBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieBfdSessDiscMapTable.setStatus("current")
_RuijieBfdSessDiscMapEntry_Object = MibTableRow
ruijieBfdSessDiscMapEntry = _RuijieBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 4, 1)
)
ruijieBfdSessDiscMapEntry.setIndexNames(
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    ruijieBfdSessDiscMapEntry.setStatus("current")
_RuijieBfdSessDiscMapIndex_Type = RuijieBfdSessIndexTC
_RuijieBfdSessDiscMapIndex_Object = MibTableColumn
ruijieBfdSessDiscMapIndex = _RuijieBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 4, 1, 1),
    _RuijieBfdSessDiscMapIndex_Type()
)
ruijieBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessDiscMapIndex.setStatus("current")
_RuijieBfdSessDiscMapStorageType_Type = StorageType
_RuijieBfdSessDiscMapStorageType_Object = MibTableColumn
ruijieBfdSessDiscMapStorageType = _RuijieBfdSessDiscMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 4, 1, 2),
    _RuijieBfdSessDiscMapStorageType_Type()
)
ruijieBfdSessDiscMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDiscMapStorageType.setStatus("current")
_RuijieBfdSessDiscMapRowStatus_Type = RowStatus
_RuijieBfdSessDiscMapRowStatus_Object = MibTableColumn
ruijieBfdSessDiscMapRowStatus = _RuijieBfdSessDiscMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 4, 1, 3),
    _RuijieBfdSessDiscMapRowStatus_Type()
)
ruijieBfdSessDiscMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessDiscMapRowStatus.setStatus("current")
_RuijieBfdSessIpMapTable_Object = MibTable
ruijieBfdSessIpMapTable = _RuijieBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieBfdSessIpMapTable.setStatus("current")
_RuijieBfdSessIpMapEntry_Object = MibTableRow
ruijieBfdSessIpMapEntry = _RuijieBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 5, 1)
)
ruijieBfdSessIpMapEntry.setIndexNames(
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessInterface"),
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessSrcAddrType"),
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessSrcAddr"),
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessDstAddrType"),
    (0, "RUIJIE-BFD-MIB", "ruijieBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    ruijieBfdSessIpMapEntry.setStatus("current")
_RuijieBfdSessIpMapIndex_Type = RuijieBfdSessIndexTC
_RuijieBfdSessIpMapIndex_Object = MibTableColumn
ruijieBfdSessIpMapIndex = _RuijieBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 5, 1, 1),
    _RuijieBfdSessIpMapIndex_Type()
)
ruijieBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBfdSessIpMapIndex.setStatus("current")
_RuijieBfdSessIpMapStorageType_Type = StorageType
_RuijieBfdSessIpMapStorageType_Object = MibTableColumn
ruijieBfdSessIpMapStorageType = _RuijieBfdSessIpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 5, 1, 2),
    _RuijieBfdSessIpMapStorageType_Type()
)
ruijieBfdSessIpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessIpMapStorageType.setStatus("current")
_RuijieBfdSessIpMapRowStatus_Type = RowStatus
_RuijieBfdSessIpMapRowStatus_Object = MibTableColumn
ruijieBfdSessIpMapRowStatus = _RuijieBfdSessIpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 1, 5, 1, 3),
    _RuijieBfdSessIpMapRowStatus_Type()
)
ruijieBfdSessIpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBfdSessIpMapRowStatus.setStatus("current")
_RuijieBfdConformance_ObjectIdentity = ObjectIdentity
ruijieBfdConformance = _RuijieBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2)
)
_RuijieBfdGroups_ObjectIdentity = ObjectIdentity
ruijieBfdGroups = _RuijieBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1)
)
_RuijieBfdCompliances_ObjectIdentity = ObjectIdentity
ruijieBfdCompliances = _RuijieBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 2)
)
ruijieBfdSessEntry.registerAugmentions(
    ("RUIJIE-BFD-MIB",
     "ruijieBfdSessPerfEntry")
)
ruijieBfdSessPerfEntry.setIndexNames(*ruijieBfdSessEntry.getIndexNames())

# Managed Objects groups

ruijieBfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1, 1)
)
ruijieBfdSessionGroup.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdAdminStatus"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessNotificationsEnable"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessVersionNumber"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDestinationUdpPort"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessSourceUdpPort"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessEchoSourceUdpPort"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessAdminStatus"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessOperMode"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDemandModeDesiredFlag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessControlPlaneIndepFlag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessMultipointFlag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessInterface"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessSrcAddrType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessSrcAddr"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDstAddrType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDstAddr"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessGTSM"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessGTSMTTL"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDesiredMinTxInterval"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessReqMinRxInterval"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessReqMinEchoRxInterval"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDetectMult"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessAuthPresFlag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessAuthenticationType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessAuthenticationKeyID"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessAuthenticationKey"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessStorageType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessRowStatus"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiscMapStorageType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiscMapRowStatus"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIpMapStorageType"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIpMapRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessionGroup.setStatus("current")

ruijieBfdSessionReadOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1, 2)
)
ruijieBfdSessionReadOnlyGroup.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessDiscriminator"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessRemoteDiscr"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessState"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessRemoteHeardFlag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessNegotiatedInterval"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessNegotiatedEchoInterval"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessNegotiatedDetectMult"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiscMapIndex"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessionReadOnlyGroup.setStatus("current")

ruijieBfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1, 3)
)
ruijieBfdSessionPerfGroup.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktIn"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktOut"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktDrop"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktDropLastTime"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktIn"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktOut"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktDrop"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktDropLastTime"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessUpTime"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfLastSessDownTime"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfLastCommLostDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfSessUpCount"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessionPerfGroup.setStatus("current")

ruijieBfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1, 4)
)
ruijieBfdSessionPerfHCGroup.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktInHC"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktOutHC"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfCtrlPktDropHC"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktInHC"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktOutHC"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessPerfEchoPktDropHC"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessionPerfHCGroup.setStatus("current")


# Notification objects

ruijieBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 0, 1)
)
ruijieBfdSessUp.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessInterface"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIfName"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIfDes"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessUp.setStatus(
        "current"
    )

ruijieBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 0, 2)
)
ruijieBfdSessDown.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDiag"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessInterface"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIfName"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessIfDes"))
)
if mibBuilder.loadTexts:
    ruijieBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

ruijieBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 1, 5)
)
ruijieBfdNotificationGroup.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessUp"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessDown"))
)
if mibBuilder.loadTexts:
    ruijieBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieBfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 2, 1)
)
ruijieBfdModuleFullCompliance.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessionGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionReadOnlyGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionPerfGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdNotificationGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    ruijieBfdModuleFullCompliance.setStatus(
        "current"
    )

ruijieBfdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 48, 2, 2, 2)
)
ruijieBfdModuleReadOnlyCompliance.setObjects(
      *(("RUIJIE-BFD-MIB", "ruijieBfdSessionGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionReadOnlyGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionPerfGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdNotificationGroup"),
        ("RUIJIE-BFD-MIB", "ruijieBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    ruijieBfdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-BFD-MIB",
    **{"RuijieBfdSessIndexTC": RuijieBfdSessIndexTC,
       "RuijieBfdIntervalTC": RuijieBfdIntervalTC,
       "RuijieBfdMultiplierTC": RuijieBfdMultiplierTC,
       "RuijieBfdDiagTC": RuijieBfdDiagTC,
       "RuijieBfdSessTypeTC": RuijieBfdSessTypeTC,
       "RuijieBfdSessOperModeTC": RuijieBfdSessOperModeTC,
       "RuijieBfdCtrlDestPortNumberTC": RuijieBfdCtrlDestPortNumberTC,
       "RuijieBfdCtrlSourcePortNumberTC": RuijieBfdCtrlSourcePortNumberTC,
       "RuijieBfdSessStateTC": RuijieBfdSessStateTC,
       "RuijieBfdSessAuthenticationTypeTC": RuijieBfdSessAuthenticationTypeTC,
       "RuijieBfdSessionAuthenticationKeyTC": RuijieBfdSessionAuthenticationKeyTC,
       "ruijieBfdMIB": ruijieBfdMIB,
       "ruijieBfdNotifications": ruijieBfdNotifications,
       "ruijieBfdSessUp": ruijieBfdSessUp,
       "ruijieBfdSessDown": ruijieBfdSessDown,
       "ruijieBfdObjects": ruijieBfdObjects,
       "ruijieBfdScalarObjects": ruijieBfdScalarObjects,
       "ruijieBfdAdminStatus": ruijieBfdAdminStatus,
       "ruijieBfdSessNotificationsEnable": ruijieBfdSessNotificationsEnable,
       "ruijieBfdSessTable": ruijieBfdSessTable,
       "ruijieBfdSessEntry": ruijieBfdSessEntry,
       "ruijieBfdSessIndex": ruijieBfdSessIndex,
       "ruijieBfdSessVersionNumber": ruijieBfdSessVersionNumber,
       "ruijieBfdSessType": ruijieBfdSessType,
       "ruijieBfdSessDiscriminator": ruijieBfdSessDiscriminator,
       "ruijieBfdSessRemoteDiscr": ruijieBfdSessRemoteDiscr,
       "ruijieBfdSessDestinationUdpPort": ruijieBfdSessDestinationUdpPort,
       "ruijieBfdSessSourceUdpPort": ruijieBfdSessSourceUdpPort,
       "ruijieBfdSessEchoSourceUdpPort": ruijieBfdSessEchoSourceUdpPort,
       "ruijieBfdSessAdminStatus": ruijieBfdSessAdminStatus,
       "ruijieBfdSessState": ruijieBfdSessState,
       "ruijieBfdSessRemoteHeardFlag": ruijieBfdSessRemoteHeardFlag,
       "ruijieBfdSessDiag": ruijieBfdSessDiag,
       "ruijieBfdSessOperMode": ruijieBfdSessOperMode,
       "ruijieBfdSessDemandModeDesiredFlag": ruijieBfdSessDemandModeDesiredFlag,
       "ruijieBfdSessControlPlaneIndepFlag": ruijieBfdSessControlPlaneIndepFlag,
       "ruijieBfdSessMultipointFlag": ruijieBfdSessMultipointFlag,
       "ruijieBfdSessInterface": ruijieBfdSessInterface,
       "ruijieBfdSessSrcAddrType": ruijieBfdSessSrcAddrType,
       "ruijieBfdSessSrcAddr": ruijieBfdSessSrcAddr,
       "ruijieBfdSessDstAddrType": ruijieBfdSessDstAddrType,
       "ruijieBfdSessDstAddr": ruijieBfdSessDstAddr,
       "ruijieBfdSessGTSM": ruijieBfdSessGTSM,
       "ruijieBfdSessGTSMTTL": ruijieBfdSessGTSMTTL,
       "ruijieBfdSessDesiredMinTxInterval": ruijieBfdSessDesiredMinTxInterval,
       "ruijieBfdSessReqMinRxInterval": ruijieBfdSessReqMinRxInterval,
       "ruijieBfdSessReqMinEchoRxInterval": ruijieBfdSessReqMinEchoRxInterval,
       "ruijieBfdSessDetectMult": ruijieBfdSessDetectMult,
       "ruijieBfdSessNegotiatedInterval": ruijieBfdSessNegotiatedInterval,
       "ruijieBfdSessNegotiatedEchoInterval": ruijieBfdSessNegotiatedEchoInterval,
       "ruijieBfdSessNegotiatedDetectMult": ruijieBfdSessNegotiatedDetectMult,
       "ruijieBfdSessAuthPresFlag": ruijieBfdSessAuthPresFlag,
       "ruijieBfdSessAuthenticationType": ruijieBfdSessAuthenticationType,
       "ruijieBfdSessAuthenticationKeyID": ruijieBfdSessAuthenticationKeyID,
       "ruijieBfdSessAuthenticationKey": ruijieBfdSessAuthenticationKey,
       "ruijieBfdSessStorageType": ruijieBfdSessStorageType,
       "ruijieBfdSessRowStatus": ruijieBfdSessRowStatus,
       "ruijieBfdSessIfName": ruijieBfdSessIfName,
       "ruijieBfdSessIfDes": ruijieBfdSessIfDes,
       "ruijieBfdSessPerfTable": ruijieBfdSessPerfTable,
       "ruijieBfdSessPerfEntry": ruijieBfdSessPerfEntry,
       "ruijieBfdSessPerfCtrlPktIn": ruijieBfdSessPerfCtrlPktIn,
       "ruijieBfdSessPerfCtrlPktOut": ruijieBfdSessPerfCtrlPktOut,
       "ruijieBfdSessPerfCtrlPktDrop": ruijieBfdSessPerfCtrlPktDrop,
       "ruijieBfdSessPerfCtrlPktDropLastTime": ruijieBfdSessPerfCtrlPktDropLastTime,
       "ruijieBfdSessPerfEchoPktIn": ruijieBfdSessPerfEchoPktIn,
       "ruijieBfdSessPerfEchoPktOut": ruijieBfdSessPerfEchoPktOut,
       "ruijieBfdSessPerfEchoPktDrop": ruijieBfdSessPerfEchoPktDrop,
       "ruijieBfdSessPerfEchoPktDropLastTime": ruijieBfdSessPerfEchoPktDropLastTime,
       "ruijieBfdSessUpTime": ruijieBfdSessUpTime,
       "ruijieBfdSessPerfLastSessDownTime": ruijieBfdSessPerfLastSessDownTime,
       "ruijieBfdSessPerfLastCommLostDiag": ruijieBfdSessPerfLastCommLostDiag,
       "ruijieBfdSessPerfSessUpCount": ruijieBfdSessPerfSessUpCount,
       "ruijieBfdSessPerfDiscTime": ruijieBfdSessPerfDiscTime,
       "ruijieBfdSessPerfCtrlPktInHC": ruijieBfdSessPerfCtrlPktInHC,
       "ruijieBfdSessPerfCtrlPktOutHC": ruijieBfdSessPerfCtrlPktOutHC,
       "ruijieBfdSessPerfCtrlPktDropHC": ruijieBfdSessPerfCtrlPktDropHC,
       "ruijieBfdSessPerfEchoPktInHC": ruijieBfdSessPerfEchoPktInHC,
       "ruijieBfdSessPerfEchoPktOutHC": ruijieBfdSessPerfEchoPktOutHC,
       "ruijieBfdSessPerfEchoPktDropHC": ruijieBfdSessPerfEchoPktDropHC,
       "ruijieBfdSessDiscMapTable": ruijieBfdSessDiscMapTable,
       "ruijieBfdSessDiscMapEntry": ruijieBfdSessDiscMapEntry,
       "ruijieBfdSessDiscMapIndex": ruijieBfdSessDiscMapIndex,
       "ruijieBfdSessDiscMapStorageType": ruijieBfdSessDiscMapStorageType,
       "ruijieBfdSessDiscMapRowStatus": ruijieBfdSessDiscMapRowStatus,
       "ruijieBfdSessIpMapTable": ruijieBfdSessIpMapTable,
       "ruijieBfdSessIpMapEntry": ruijieBfdSessIpMapEntry,
       "ruijieBfdSessIpMapIndex": ruijieBfdSessIpMapIndex,
       "ruijieBfdSessIpMapStorageType": ruijieBfdSessIpMapStorageType,
       "ruijieBfdSessIpMapRowStatus": ruijieBfdSessIpMapRowStatus,
       "ruijieBfdConformance": ruijieBfdConformance,
       "ruijieBfdGroups": ruijieBfdGroups,
       "ruijieBfdSessionGroup": ruijieBfdSessionGroup,
       "ruijieBfdSessionReadOnlyGroup": ruijieBfdSessionReadOnlyGroup,
       "ruijieBfdSessionPerfGroup": ruijieBfdSessionPerfGroup,
       "ruijieBfdSessionPerfHCGroup": ruijieBfdSessionPerfHCGroup,
       "ruijieBfdNotificationGroup": ruijieBfdNotificationGroup,
       "ruijieBfdCompliances": ruijieBfdCompliances,
       "ruijieBfdModuleFullCompliance": ruijieBfdModuleFullCompliance,
       "ruijieBfdModuleReadOnlyCompliance": ruijieBfdModuleReadOnlyCompliance}
)
