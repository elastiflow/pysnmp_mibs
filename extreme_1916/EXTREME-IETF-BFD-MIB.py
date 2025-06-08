# SNMP MIB module (EXTREME-IETF-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-IETF-BFD-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeBfd,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeBfd")

(ExtremeBfdCtrlDestPortNumberTC,
 ExtremeBfdCtrlSourcePortNumberTC,
 ExtremeBfdDiagTC,
 ExtremeBfdIntervalTC,
 ExtremeBfdMultiplierTC,
 ExtremeBfdSessAuthenticationTypeTC,
 ExtremeBfdSessIndexTC,
 ExtremeBfdSessOperModeTC,
 ExtremeBfdSessStateTC,
 ExtremeBfdSessTypeTC,
 ExtremeBfdSessionAuthenticationKeyTC) = mibBuilder.importSymbols(
    "EXTREME-IETF-BFD-TC-MIB",
    "ExtremeBfdCtrlDestPortNumberTC",
    "ExtremeBfdCtrlSourcePortNumberTC",
    "ExtremeBfdDiagTC",
    "ExtremeBfdIntervalTC",
    "ExtremeBfdMultiplierTC",
    "ExtremeBfdSessAuthenticationTypeTC",
    "ExtremeBfdSessIndexTC",
    "ExtremeBfdSessOperModeTC",
    "ExtremeBfdSessStateTC",
    "ExtremeBfdSessTypeTC",
    "ExtremeBfdSessionAuthenticationKeyTC")

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

extremeIetfBfdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2)
)
if mibBuilder.loadTexts:
    extremeIetfBfdMib.setRevisions(
        ("2012-12-17 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeBfdNotifications_ObjectIdentity = ObjectIdentity
extremeBfdNotifications = _ExtremeBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 0)
)
_ExtremeBfdObjects_ObjectIdentity = ObjectIdentity
extremeBfdObjects = _ExtremeBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1)
)
_ExtremeBfdScalarObjects_ObjectIdentity = ObjectIdentity
extremeBfdScalarObjects = _ExtremeBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 1)
)


class _ExtremeBfdAdminStatus_Type(Integer32):
    """Custom type extremeBfdAdminStatus based on Integer32"""
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


_ExtremeBfdAdminStatus_Type.__name__ = "Integer32"
_ExtremeBfdAdminStatus_Object = MibScalar
extremeBfdAdminStatus = _ExtremeBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 1, 1),
    _ExtremeBfdAdminStatus_Type()
)
extremeBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeBfdAdminStatus.setStatus("current")


class _ExtremeBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type extremeBfdSessNotificationsEnable based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessNotificationsEnable_Type.__name__ = "TruthValue"
_ExtremeBfdSessNotificationsEnable_Object = MibScalar
extremeBfdSessNotificationsEnable = _ExtremeBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 1, 2),
    _ExtremeBfdSessNotificationsEnable_Type()
)
extremeBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeBfdSessNotificationsEnable.setStatus("current")
_ExtremeBfdSessTable_Object = MibTable
extremeBfdSessTable = _ExtremeBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2)
)
if mibBuilder.loadTexts:
    extremeBfdSessTable.setStatus("current")
_ExtremeBfdSessEntry_Object = MibTableRow
extremeBfdSessEntry = _ExtremeBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1)
)
extremeBfdSessEntry.setIndexNames(
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessIndex"),
)
if mibBuilder.loadTexts:
    extremeBfdSessEntry.setStatus("current")
_ExtremeBfdSessIndex_Type = ExtremeBfdSessIndexTC
_ExtremeBfdSessIndex_Object = MibTableColumn
extremeBfdSessIndex = _ExtremeBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 1),
    _ExtremeBfdSessIndex_Type()
)
extremeBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBfdSessIndex.setStatus("current")


class _ExtremeBfdSessVersionNumber_Type(Unsigned32):
    """Custom type extremeBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ExtremeBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_ExtremeBfdSessVersionNumber_Object = MibTableColumn
extremeBfdSessVersionNumber = _ExtremeBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 2),
    _ExtremeBfdSessVersionNumber_Type()
)
extremeBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessVersionNumber.setStatus("current")
_ExtremeBfdSessType_Type = ExtremeBfdSessTypeTC
_ExtremeBfdSessType_Object = MibTableColumn
extremeBfdSessType = _ExtremeBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 3),
    _ExtremeBfdSessType_Type()
)
extremeBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessType.setStatus("current")


class _ExtremeBfdSessDiscriminator_Type(Unsigned32):
    """Custom type extremeBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_ExtremeBfdSessDiscriminator_Object = MibTableColumn
extremeBfdSessDiscriminator = _ExtremeBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 4),
    _ExtremeBfdSessDiscriminator_Type()
)
extremeBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessDiscriminator.setStatus("current")


class _ExtremeBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type extremeBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_ExtremeBfdSessRemoteDiscr_Object = MibTableColumn
extremeBfdSessRemoteDiscr = _ExtremeBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 5),
    _ExtremeBfdSessRemoteDiscr_Type()
)
extremeBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessRemoteDiscr.setStatus("current")


class _ExtremeBfdSessDestinationUdpPort_Type(ExtremeBfdCtrlDestPortNumberTC):
    """Custom type extremeBfdSessDestinationUdpPort based on ExtremeBfdCtrlDestPortNumberTC"""
    defaultValue = 0


_ExtremeBfdSessDestinationUdpPort_Type.__name__ = "ExtremeBfdCtrlDestPortNumberTC"
_ExtremeBfdSessDestinationUdpPort_Object = MibTableColumn
extremeBfdSessDestinationUdpPort = _ExtremeBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 6),
    _ExtremeBfdSessDestinationUdpPort_Type()
)
extremeBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDestinationUdpPort.setStatus("current")


class _ExtremeBfdSessSourceUdpPort_Type(ExtremeBfdCtrlSourcePortNumberTC):
    """Custom type extremeBfdSessSourceUdpPort based on ExtremeBfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_ExtremeBfdSessSourceUdpPort_Type.__name__ = "ExtremeBfdCtrlSourcePortNumberTC"
_ExtremeBfdSessSourceUdpPort_Object = MibTableColumn
extremeBfdSessSourceUdpPort = _ExtremeBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 7),
    _ExtremeBfdSessSourceUdpPort_Type()
)
extremeBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessSourceUdpPort.setStatus("current")


class _ExtremeBfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type extremeBfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_ExtremeBfdSessEchoSourceUdpPort_Type.__name__ = "InetPortNumber"
_ExtremeBfdSessEchoSourceUdpPort_Object = MibTableColumn
extremeBfdSessEchoSourceUdpPort = _ExtremeBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 8),
    _ExtremeBfdSessEchoSourceUdpPort_Type()
)
extremeBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessEchoSourceUdpPort.setStatus("current")


class _ExtremeBfdSessAdminStatus_Type(Integer32):
    """Custom type extremeBfdSessAdminStatus based on Integer32"""
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


_ExtremeBfdSessAdminStatus_Type.__name__ = "Integer32"
_ExtremeBfdSessAdminStatus_Object = MibTableColumn
extremeBfdSessAdminStatus = _ExtremeBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 9),
    _ExtremeBfdSessAdminStatus_Type()
)
extremeBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessAdminStatus.setStatus("current")


class _ExtremeBfdSessState_Type(ExtremeBfdSessStateTC):
    """Custom type extremeBfdSessState based on ExtremeBfdSessStateTC"""
    defaultValue = 2


_ExtremeBfdSessState_Type.__name__ = "ExtremeBfdSessStateTC"
_ExtremeBfdSessState_Object = MibTableColumn
extremeBfdSessState = _ExtremeBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 10),
    _ExtremeBfdSessState_Type()
)
extremeBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessState.setStatus("current")


class _ExtremeBfdSessRemoteHeardFlag_Type(TruthValue):
    """Custom type extremeBfdSessRemoteHeardFlag based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessRemoteHeardFlag_Type.__name__ = "TruthValue"
_ExtremeBfdSessRemoteHeardFlag_Object = MibTableColumn
extremeBfdSessRemoteHeardFlag = _ExtremeBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 11),
    _ExtremeBfdSessRemoteHeardFlag_Type()
)
extremeBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessRemoteHeardFlag.setStatus("current")
_ExtremeBfdSessDiag_Type = ExtremeBfdDiagTC
_ExtremeBfdSessDiag_Object = MibTableColumn
extremeBfdSessDiag = _ExtremeBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 12),
    _ExtremeBfdSessDiag_Type()
)
extremeBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessDiag.setStatus("current")
_ExtremeBfdSessOperMode_Type = ExtremeBfdSessOperModeTC
_ExtremeBfdSessOperMode_Object = MibTableColumn
extremeBfdSessOperMode = _ExtremeBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 13),
    _ExtremeBfdSessOperMode_Type()
)
extremeBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessOperMode.setStatus("current")


class _ExtremeBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type extremeBfdSessDemandModeDesiredFlag based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessDemandModeDesiredFlag_Type.__name__ = "TruthValue"
_ExtremeBfdSessDemandModeDesiredFlag_Object = MibTableColumn
extremeBfdSessDemandModeDesiredFlag = _ExtremeBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 14),
    _ExtremeBfdSessDemandModeDesiredFlag_Type()
)
extremeBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDemandModeDesiredFlag.setStatus("current")


class _ExtremeBfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type extremeBfdSessControlPlaneIndepFlag based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessControlPlaneIndepFlag_Type.__name__ = "TruthValue"
_ExtremeBfdSessControlPlaneIndepFlag_Object = MibTableColumn
extremeBfdSessControlPlaneIndepFlag = _ExtremeBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 15),
    _ExtremeBfdSessControlPlaneIndepFlag_Type()
)
extremeBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessControlPlaneIndepFlag.setStatus("current")


class _ExtremeBfdSessMultipointFlag_Type(TruthValue):
    """Custom type extremeBfdSessMultipointFlag based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessMultipointFlag_Type.__name__ = "TruthValue"
_ExtremeBfdSessMultipointFlag_Object = MibTableColumn
extremeBfdSessMultipointFlag = _ExtremeBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 16),
    _ExtremeBfdSessMultipointFlag_Type()
)
extremeBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessMultipointFlag.setStatus("current")
_ExtremeBfdSessInterface_Type = InterfaceIndexOrZero
_ExtremeBfdSessInterface_Object = MibTableColumn
extremeBfdSessInterface = _ExtremeBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 17),
    _ExtremeBfdSessInterface_Type()
)
extremeBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessInterface.setStatus("current")
_ExtremeBfdSessSrcAddrType_Type = InetAddressType
_ExtremeBfdSessSrcAddrType_Object = MibTableColumn
extremeBfdSessSrcAddrType = _ExtremeBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 18),
    _ExtremeBfdSessSrcAddrType_Type()
)
extremeBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessSrcAddrType.setStatus("current")
_ExtremeBfdSessSrcAddr_Type = InetAddress
_ExtremeBfdSessSrcAddr_Object = MibTableColumn
extremeBfdSessSrcAddr = _ExtremeBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 19),
    _ExtremeBfdSessSrcAddr_Type()
)
extremeBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessSrcAddr.setStatus("current")
_ExtremeBfdSessDstAddrType_Type = InetAddressType
_ExtremeBfdSessDstAddrType_Object = MibTableColumn
extremeBfdSessDstAddrType = _ExtremeBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 20),
    _ExtremeBfdSessDstAddrType_Type()
)
extremeBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDstAddrType.setStatus("current")
_ExtremeBfdSessDstAddr_Type = InetAddress
_ExtremeBfdSessDstAddr_Object = MibTableColumn
extremeBfdSessDstAddr = _ExtremeBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 21),
    _ExtremeBfdSessDstAddr_Type()
)
extremeBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDstAddr.setStatus("current")


class _ExtremeBfdSessGTSM_Type(TruthValue):
    """Custom type extremeBfdSessGTSM based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessGTSM_Type.__name__ = "TruthValue"
_ExtremeBfdSessGTSM_Object = MibTableColumn
extremeBfdSessGTSM = _ExtremeBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 22),
    _ExtremeBfdSessGTSM_Type()
)
extremeBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessGTSM.setStatus("current")


class _ExtremeBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type extremeBfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_ExtremeBfdSessGTSMTTL_Object = MibTableColumn
extremeBfdSessGTSMTTL = _ExtremeBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 23),
    _ExtremeBfdSessGTSMTTL_Type()
)
extremeBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessGTSMTTL.setStatus("current")
_ExtremeBfdSessDesiredMinTxInterval_Type = ExtremeBfdIntervalTC
_ExtremeBfdSessDesiredMinTxInterval_Object = MibTableColumn
extremeBfdSessDesiredMinTxInterval = _ExtremeBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 24),
    _ExtremeBfdSessDesiredMinTxInterval_Type()
)
extremeBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDesiredMinTxInterval.setStatus("current")
_ExtremeBfdSessReqMinRxInterval_Type = ExtremeBfdIntervalTC
_ExtremeBfdSessReqMinRxInterval_Object = MibTableColumn
extremeBfdSessReqMinRxInterval = _ExtremeBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 25),
    _ExtremeBfdSessReqMinRxInterval_Type()
)
extremeBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessReqMinRxInterval.setStatus("current")
_ExtremeBfdSessReqMinEchoRxInterval_Type = ExtremeBfdIntervalTC
_ExtremeBfdSessReqMinEchoRxInterval_Object = MibTableColumn
extremeBfdSessReqMinEchoRxInterval = _ExtremeBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 26),
    _ExtremeBfdSessReqMinEchoRxInterval_Type()
)
extremeBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessReqMinEchoRxInterval.setStatus("current")
_ExtremeBfdSessDetectMult_Type = ExtremeBfdMultiplierTC
_ExtremeBfdSessDetectMult_Object = MibTableColumn
extremeBfdSessDetectMult = _ExtremeBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 27),
    _ExtremeBfdSessDetectMult_Type()
)
extremeBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDetectMult.setStatus("current")
_ExtremeBfdSessNegotiatedInterval_Type = ExtremeBfdIntervalTC
_ExtremeBfdSessNegotiatedInterval_Object = MibTableColumn
extremeBfdSessNegotiatedInterval = _ExtremeBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 28),
    _ExtremeBfdSessNegotiatedInterval_Type()
)
extremeBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessNegotiatedInterval.setStatus("current")
_ExtremeBfdSessNegotiatedEchoInterval_Type = ExtremeBfdIntervalTC
_ExtremeBfdSessNegotiatedEchoInterval_Object = MibTableColumn
extremeBfdSessNegotiatedEchoInterval = _ExtremeBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 29),
    _ExtremeBfdSessNegotiatedEchoInterval_Type()
)
extremeBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessNegotiatedEchoInterval.setStatus("current")
_ExtremeBfdSessNegotiatedDetectMult_Type = ExtremeBfdMultiplierTC
_ExtremeBfdSessNegotiatedDetectMult_Object = MibTableColumn
extremeBfdSessNegotiatedDetectMult = _ExtremeBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 30),
    _ExtremeBfdSessNegotiatedDetectMult_Type()
)
extremeBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessNegotiatedDetectMult.setStatus("current")


class _ExtremeBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type extremeBfdSessAuthPresFlag based on TruthValue"""
    defaultValue = 2


_ExtremeBfdSessAuthPresFlag_Type.__name__ = "TruthValue"
_ExtremeBfdSessAuthPresFlag_Object = MibTableColumn
extremeBfdSessAuthPresFlag = _ExtremeBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 31),
    _ExtremeBfdSessAuthPresFlag_Type()
)
extremeBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessAuthPresFlag.setStatus("current")


class _ExtremeBfdSessAuthenticationType_Type(ExtremeBfdSessAuthenticationTypeTC):
    """Custom type extremeBfdSessAuthenticationType based on ExtremeBfdSessAuthenticationTypeTC"""
    defaultValue = -1


_ExtremeBfdSessAuthenticationType_Type.__name__ = "ExtremeBfdSessAuthenticationTypeTC"
_ExtremeBfdSessAuthenticationType_Object = MibTableColumn
extremeBfdSessAuthenticationType = _ExtremeBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 32),
    _ExtremeBfdSessAuthenticationType_Type()
)
extremeBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessAuthenticationType.setStatus("current")


class _ExtremeBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type extremeBfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_ExtremeBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_ExtremeBfdSessAuthenticationKeyID_Object = MibTableColumn
extremeBfdSessAuthenticationKeyID = _ExtremeBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 33),
    _ExtremeBfdSessAuthenticationKeyID_Type()
)
extremeBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessAuthenticationKeyID.setStatus("current")
_ExtremeBfdSessAuthenticationKey_Type = ExtremeBfdSessionAuthenticationKeyTC
_ExtremeBfdSessAuthenticationKey_Object = MibTableColumn
extremeBfdSessAuthenticationKey = _ExtremeBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 34),
    _ExtremeBfdSessAuthenticationKey_Type()
)
extremeBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessAuthenticationKey.setStatus("current")
_ExtremeBfdSessStorageType_Type = StorageType
_ExtremeBfdSessStorageType_Object = MibTableColumn
extremeBfdSessStorageType = _ExtremeBfdSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 35),
    _ExtremeBfdSessStorageType_Type()
)
extremeBfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessStorageType.setStatus("current")
_ExtremeBfdSessRowStatus_Type = RowStatus
_ExtremeBfdSessRowStatus_Object = MibTableColumn
extremeBfdSessRowStatus = _ExtremeBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 2, 1, 36),
    _ExtremeBfdSessRowStatus_Type()
)
extremeBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessRowStatus.setStatus("current")
_ExtremeBfdSessPerfTable_Object = MibTable
extremeBfdSessPerfTable = _ExtremeBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3)
)
if mibBuilder.loadTexts:
    extremeBfdSessPerfTable.setStatus("current")
_ExtremeBfdSessPerfEntry_Object = MibTableRow
extremeBfdSessPerfEntry = _ExtremeBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    extremeBfdSessPerfEntry.setStatus("current")
_ExtremeBfdSessPerfCtrlPktIn_Type = Counter32
_ExtremeBfdSessPerfCtrlPktIn_Object = MibTableColumn
extremeBfdSessPerfCtrlPktIn = _ExtremeBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 1),
    _ExtremeBfdSessPerfCtrlPktIn_Type()
)
extremeBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktIn.setStatus("current")
_ExtremeBfdSessPerfCtrlPktOut_Type = Counter32
_ExtremeBfdSessPerfCtrlPktOut_Object = MibTableColumn
extremeBfdSessPerfCtrlPktOut = _ExtremeBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 2),
    _ExtremeBfdSessPerfCtrlPktOut_Type()
)
extremeBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktOut.setStatus("current")
_ExtremeBfdSessPerfCtrlPktDrop_Type = Counter32
_ExtremeBfdSessPerfCtrlPktDrop_Object = MibTableColumn
extremeBfdSessPerfCtrlPktDrop = _ExtremeBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 3),
    _ExtremeBfdSessPerfCtrlPktDrop_Type()
)
extremeBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktDrop.setStatus("current")
_ExtremeBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_ExtremeBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
extremeBfdSessPerfCtrlPktDropLastTime = _ExtremeBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 4),
    _ExtremeBfdSessPerfCtrlPktDropLastTime_Type()
)
extremeBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_ExtremeBfdSessPerfEchoPktIn_Type = Counter32
_ExtremeBfdSessPerfEchoPktIn_Object = MibTableColumn
extremeBfdSessPerfEchoPktIn = _ExtremeBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 5),
    _ExtremeBfdSessPerfEchoPktIn_Type()
)
extremeBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktIn.setStatus("current")
_ExtremeBfdSessPerfEchoPktOut_Type = Counter32
_ExtremeBfdSessPerfEchoPktOut_Object = MibTableColumn
extremeBfdSessPerfEchoPktOut = _ExtremeBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 6),
    _ExtremeBfdSessPerfEchoPktOut_Type()
)
extremeBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktOut.setStatus("current")
_ExtremeBfdSessPerfEchoPktDrop_Type = Counter32
_ExtremeBfdSessPerfEchoPktDrop_Object = MibTableColumn
extremeBfdSessPerfEchoPktDrop = _ExtremeBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 7),
    _ExtremeBfdSessPerfEchoPktDrop_Type()
)
extremeBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktDrop.setStatus("current")
_ExtremeBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_ExtremeBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
extremeBfdSessPerfEchoPktDropLastTime = _ExtremeBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 8),
    _ExtremeBfdSessPerfEchoPktDropLastTime_Type()
)
extremeBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktDropLastTime.setStatus("current")
_ExtremeBfdSessUpTime_Type = TimeStamp
_ExtremeBfdSessUpTime_Object = MibTableColumn
extremeBfdSessUpTime = _ExtremeBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 9),
    _ExtremeBfdSessUpTime_Type()
)
extremeBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessUpTime.setStatus("current")
_ExtremeBfdSessPerfLastSessDownTime_Type = TimeStamp
_ExtremeBfdSessPerfLastSessDownTime_Object = MibTableColumn
extremeBfdSessPerfLastSessDownTime = _ExtremeBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 10),
    _ExtremeBfdSessPerfLastSessDownTime_Type()
)
extremeBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfLastSessDownTime.setStatus("current")
_ExtremeBfdSessPerfLastCommLostDiag_Type = ExtremeBfdDiagTC
_ExtremeBfdSessPerfLastCommLostDiag_Object = MibTableColumn
extremeBfdSessPerfLastCommLostDiag = _ExtremeBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 11),
    _ExtremeBfdSessPerfLastCommLostDiag_Type()
)
extremeBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfLastCommLostDiag.setStatus("current")
_ExtremeBfdSessPerfSessUpCount_Type = Counter32
_ExtremeBfdSessPerfSessUpCount_Object = MibTableColumn
extremeBfdSessPerfSessUpCount = _ExtremeBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 12),
    _ExtremeBfdSessPerfSessUpCount_Type()
)
extremeBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfSessUpCount.setStatus("current")
_ExtremeBfdSessPerfDiscTime_Type = TimeStamp
_ExtremeBfdSessPerfDiscTime_Object = MibTableColumn
extremeBfdSessPerfDiscTime = _ExtremeBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 13),
    _ExtremeBfdSessPerfDiscTime_Type()
)
extremeBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfDiscTime.setStatus("current")
_ExtremeBfdSessPerfCtrlPktInHC_Type = Counter64
_ExtremeBfdSessPerfCtrlPktInHC_Object = MibTableColumn
extremeBfdSessPerfCtrlPktInHC = _ExtremeBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 14),
    _ExtremeBfdSessPerfCtrlPktInHC_Type()
)
extremeBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktInHC.setStatus("current")
_ExtremeBfdSessPerfCtrlPktOutHC_Type = Counter64
_ExtremeBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
extremeBfdSessPerfCtrlPktOutHC = _ExtremeBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 15),
    _ExtremeBfdSessPerfCtrlPktOutHC_Type()
)
extremeBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktOutHC.setStatus("current")
_ExtremeBfdSessPerfCtrlPktDropHC_Type = Counter64
_ExtremeBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
extremeBfdSessPerfCtrlPktDropHC = _ExtremeBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 16),
    _ExtremeBfdSessPerfCtrlPktDropHC_Type()
)
extremeBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfCtrlPktDropHC.setStatus("current")
_ExtremeBfdSessPerfEchoPktInHC_Type = Counter64
_ExtremeBfdSessPerfEchoPktInHC_Object = MibTableColumn
extremeBfdSessPerfEchoPktInHC = _ExtremeBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 17),
    _ExtremeBfdSessPerfEchoPktInHC_Type()
)
extremeBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktInHC.setStatus("current")
_ExtremeBfdSessPerfEchoPktOutHC_Type = Counter64
_ExtremeBfdSessPerfEchoPktOutHC_Object = MibTableColumn
extremeBfdSessPerfEchoPktOutHC = _ExtremeBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 18),
    _ExtremeBfdSessPerfEchoPktOutHC_Type()
)
extremeBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktOutHC.setStatus("current")
_ExtremeBfdSessPerfEchoPktDropHC_Type = Counter64
_ExtremeBfdSessPerfEchoPktDropHC_Object = MibTableColumn
extremeBfdSessPerfEchoPktDropHC = _ExtremeBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 3, 1, 19),
    _ExtremeBfdSessPerfEchoPktDropHC_Type()
)
extremeBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessPerfEchoPktDropHC.setStatus("current")
_ExtremeBfdSessDiscMapTable_Object = MibTable
extremeBfdSessDiscMapTable = _ExtremeBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 4)
)
if mibBuilder.loadTexts:
    extremeBfdSessDiscMapTable.setStatus("current")
_ExtremeBfdSessDiscMapEntry_Object = MibTableRow
extremeBfdSessDiscMapEntry = _ExtremeBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 4, 1)
)
extremeBfdSessDiscMapEntry.setIndexNames(
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    extremeBfdSessDiscMapEntry.setStatus("current")
_ExtremeBfdSessDiscMapIndex_Type = ExtremeBfdSessIndexTC
_ExtremeBfdSessDiscMapIndex_Object = MibTableColumn
extremeBfdSessDiscMapIndex = _ExtremeBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 4, 1, 1),
    _ExtremeBfdSessDiscMapIndex_Type()
)
extremeBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessDiscMapIndex.setStatus("current")
_ExtremeBfdSessDiscMapStorageType_Type = StorageType
_ExtremeBfdSessDiscMapStorageType_Object = MibTableColumn
extremeBfdSessDiscMapStorageType = _ExtremeBfdSessDiscMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 4, 1, 2),
    _ExtremeBfdSessDiscMapStorageType_Type()
)
extremeBfdSessDiscMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDiscMapStorageType.setStatus("current")
_ExtremeBfdSessDiscMapRowStatus_Type = RowStatus
_ExtremeBfdSessDiscMapRowStatus_Object = MibTableColumn
extremeBfdSessDiscMapRowStatus = _ExtremeBfdSessDiscMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 4, 1, 3),
    _ExtremeBfdSessDiscMapRowStatus_Type()
)
extremeBfdSessDiscMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessDiscMapRowStatus.setStatus("current")
_ExtremeBfdSessIpMapTable_Object = MibTable
extremeBfdSessIpMapTable = _ExtremeBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 5)
)
if mibBuilder.loadTexts:
    extremeBfdSessIpMapTable.setStatus("current")
_ExtremeBfdSessIpMapEntry_Object = MibTableRow
extremeBfdSessIpMapEntry = _ExtremeBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 5, 1)
)
extremeBfdSessIpMapEntry.setIndexNames(
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessInterface"),
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessSrcAddrType"),
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessSrcAddr"),
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessDstAddrType"),
    (0, "EXTREME-IETF-BFD-MIB", "extremeBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    extremeBfdSessIpMapEntry.setStatus("current")
_ExtremeBfdSessIpMapIndex_Type = ExtremeBfdSessIndexTC
_ExtremeBfdSessIpMapIndex_Object = MibTableColumn
extremeBfdSessIpMapIndex = _ExtremeBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 5, 1, 1),
    _ExtremeBfdSessIpMapIndex_Type()
)
extremeBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBfdSessIpMapIndex.setStatus("current")
_ExtremeBfdSessIpMapStorageType_Type = StorageType
_ExtremeBfdSessIpMapStorageType_Object = MibTableColumn
extremeBfdSessIpMapStorageType = _ExtremeBfdSessIpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 5, 1, 2),
    _ExtremeBfdSessIpMapStorageType_Type()
)
extremeBfdSessIpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessIpMapStorageType.setStatus("current")
_ExtremeBfdSessIpMapRowStatus_Type = RowStatus
_ExtremeBfdSessIpMapRowStatus_Object = MibTableColumn
extremeBfdSessIpMapRowStatus = _ExtremeBfdSessIpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 1, 5, 1, 3),
    _ExtremeBfdSessIpMapRowStatus_Type()
)
extremeBfdSessIpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeBfdSessIpMapRowStatus.setStatus("current")
_ExtremeBfdConformance_ObjectIdentity = ObjectIdentity
extremeBfdConformance = _ExtremeBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2)
)
_ExtremeBfdGroups_ObjectIdentity = ObjectIdentity
extremeBfdGroups = _ExtremeBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1)
)
_ExtremeBfdCompliances_ObjectIdentity = ObjectIdentity
extremeBfdCompliances = _ExtremeBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 2)
)
extremeBfdSessEntry.registerAugmentions(
    ("EXTREME-IETF-BFD-MIB",
     "extremeBfdSessPerfEntry")
)
extremeBfdSessPerfEntry.setIndexNames(*extremeBfdSessEntry.getIndexNames())

# Managed Objects groups

extremeBfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1, 1)
)
extremeBfdSessionGroup.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdAdminStatus"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessNotificationsEnable"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessVersionNumber"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDestinationUdpPort"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessSourceUdpPort"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessEchoSourceUdpPort"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessAdminStatus"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessOperMode"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDemandModeDesiredFlag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessControlPlaneIndepFlag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessMultipointFlag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessInterface"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessSrcAddrType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessSrcAddr"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDstAddrType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDstAddr"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessGTSM"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessGTSMTTL"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDesiredMinTxInterval"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessReqMinRxInterval"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessReqMinEchoRxInterval"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDetectMult"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessAuthPresFlag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessAuthenticationType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessAuthenticationKeyID"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessAuthenticationKey"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessStorageType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessRowStatus"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiscMapStorageType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiscMapRowStatus"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessIpMapStorageType"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessIpMapRowStatus"))
)
if mibBuilder.loadTexts:
    extremeBfdSessionGroup.setStatus("current")

extremeBfdSessionReadOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1, 2)
)
extremeBfdSessionReadOnlyGroup.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiscriminator"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessRemoteDiscr"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessState"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessRemoteHeardFlag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessNegotiatedInterval"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessNegotiatedEchoInterval"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessNegotiatedDetectMult"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiscMapIndex"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    extremeBfdSessionReadOnlyGroup.setStatus("current")

extremeBfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1, 3)
)
extremeBfdSessionPerfGroup.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktIn"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktOut"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktDrop"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktDropLastTime"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktIn"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktOut"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktDrop"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktDropLastTime"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessUpTime"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfLastSessDownTime"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfLastCommLostDiag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfSessUpCount"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    extremeBfdSessionPerfGroup.setStatus("current")

extremeBfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1, 4)
)
extremeBfdSessionPerfHCGroup.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktInHC"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktOutHC"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfCtrlPktDropHC"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktInHC"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktOutHC"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessPerfEchoPktDropHC"))
)
if mibBuilder.loadTexts:
    extremeBfdSessionPerfHCGroup.setStatus("current")


# Notification objects

extremeBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 0, 1)
)
extremeBfdSessUp.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessOperMode"))
)
if mibBuilder.loadTexts:
    extremeBfdSessUp.setStatus(
        "current"
    )

extremeBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 0, 2)
)
extremeBfdSessDown.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessDiag"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessOperMode"))
)
if mibBuilder.loadTexts:
    extremeBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

extremeBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 1, 5)
)
extremeBfdNotificationGroup.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessUp"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessDown"))
)
if mibBuilder.loadTexts:
    extremeBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeBfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 2, 1)
)
extremeBfdModuleFullCompliance.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessionGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionReadOnlyGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionPerfGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdNotificationGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    extremeBfdModuleFullCompliance.setStatus(
        "current"
    )

extremeBfdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 2, 2, 2, 2)
)
extremeBfdModuleReadOnlyCompliance.setObjects(
      *(("EXTREME-IETF-BFD-MIB", "extremeBfdSessionGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionReadOnlyGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionPerfGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdNotificationGroup"),
        ("EXTREME-IETF-BFD-MIB", "extremeBfdSessionPerfHCGroup"))
)
if mibBuilder.loadTexts:
    extremeBfdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-IETF-BFD-MIB",
    **{"extremeIetfBfdMib": extremeIetfBfdMib,
       "extremeBfdNotifications": extremeBfdNotifications,
       "extremeBfdSessUp": extremeBfdSessUp,
       "extremeBfdSessDown": extremeBfdSessDown,
       "extremeBfdObjects": extremeBfdObjects,
       "extremeBfdScalarObjects": extremeBfdScalarObjects,
       "extremeBfdAdminStatus": extremeBfdAdminStatus,
       "extremeBfdSessNotificationsEnable": extremeBfdSessNotificationsEnable,
       "extremeBfdSessTable": extremeBfdSessTable,
       "extremeBfdSessEntry": extremeBfdSessEntry,
       "extremeBfdSessIndex": extremeBfdSessIndex,
       "extremeBfdSessVersionNumber": extremeBfdSessVersionNumber,
       "extremeBfdSessType": extremeBfdSessType,
       "extremeBfdSessDiscriminator": extremeBfdSessDiscriminator,
       "extremeBfdSessRemoteDiscr": extremeBfdSessRemoteDiscr,
       "extremeBfdSessDestinationUdpPort": extremeBfdSessDestinationUdpPort,
       "extremeBfdSessSourceUdpPort": extremeBfdSessSourceUdpPort,
       "extremeBfdSessEchoSourceUdpPort": extremeBfdSessEchoSourceUdpPort,
       "extremeBfdSessAdminStatus": extremeBfdSessAdminStatus,
       "extremeBfdSessState": extremeBfdSessState,
       "extremeBfdSessRemoteHeardFlag": extremeBfdSessRemoteHeardFlag,
       "extremeBfdSessDiag": extremeBfdSessDiag,
       "extremeBfdSessOperMode": extremeBfdSessOperMode,
       "extremeBfdSessDemandModeDesiredFlag": extremeBfdSessDemandModeDesiredFlag,
       "extremeBfdSessControlPlaneIndepFlag": extremeBfdSessControlPlaneIndepFlag,
       "extremeBfdSessMultipointFlag": extremeBfdSessMultipointFlag,
       "extremeBfdSessInterface": extremeBfdSessInterface,
       "extremeBfdSessSrcAddrType": extremeBfdSessSrcAddrType,
       "extremeBfdSessSrcAddr": extremeBfdSessSrcAddr,
       "extremeBfdSessDstAddrType": extremeBfdSessDstAddrType,
       "extremeBfdSessDstAddr": extremeBfdSessDstAddr,
       "extremeBfdSessGTSM": extremeBfdSessGTSM,
       "extremeBfdSessGTSMTTL": extremeBfdSessGTSMTTL,
       "extremeBfdSessDesiredMinTxInterval": extremeBfdSessDesiredMinTxInterval,
       "extremeBfdSessReqMinRxInterval": extremeBfdSessReqMinRxInterval,
       "extremeBfdSessReqMinEchoRxInterval": extremeBfdSessReqMinEchoRxInterval,
       "extremeBfdSessDetectMult": extremeBfdSessDetectMult,
       "extremeBfdSessNegotiatedInterval": extremeBfdSessNegotiatedInterval,
       "extremeBfdSessNegotiatedEchoInterval": extremeBfdSessNegotiatedEchoInterval,
       "extremeBfdSessNegotiatedDetectMult": extremeBfdSessNegotiatedDetectMult,
       "extremeBfdSessAuthPresFlag": extremeBfdSessAuthPresFlag,
       "extremeBfdSessAuthenticationType": extremeBfdSessAuthenticationType,
       "extremeBfdSessAuthenticationKeyID": extremeBfdSessAuthenticationKeyID,
       "extremeBfdSessAuthenticationKey": extremeBfdSessAuthenticationKey,
       "extremeBfdSessStorageType": extremeBfdSessStorageType,
       "extremeBfdSessRowStatus": extremeBfdSessRowStatus,
       "extremeBfdSessPerfTable": extremeBfdSessPerfTable,
       "extremeBfdSessPerfEntry": extremeBfdSessPerfEntry,
       "extremeBfdSessPerfCtrlPktIn": extremeBfdSessPerfCtrlPktIn,
       "extremeBfdSessPerfCtrlPktOut": extremeBfdSessPerfCtrlPktOut,
       "extremeBfdSessPerfCtrlPktDrop": extremeBfdSessPerfCtrlPktDrop,
       "extremeBfdSessPerfCtrlPktDropLastTime": extremeBfdSessPerfCtrlPktDropLastTime,
       "extremeBfdSessPerfEchoPktIn": extremeBfdSessPerfEchoPktIn,
       "extremeBfdSessPerfEchoPktOut": extremeBfdSessPerfEchoPktOut,
       "extremeBfdSessPerfEchoPktDrop": extremeBfdSessPerfEchoPktDrop,
       "extremeBfdSessPerfEchoPktDropLastTime": extremeBfdSessPerfEchoPktDropLastTime,
       "extremeBfdSessUpTime": extremeBfdSessUpTime,
       "extremeBfdSessPerfLastSessDownTime": extremeBfdSessPerfLastSessDownTime,
       "extremeBfdSessPerfLastCommLostDiag": extremeBfdSessPerfLastCommLostDiag,
       "extremeBfdSessPerfSessUpCount": extremeBfdSessPerfSessUpCount,
       "extremeBfdSessPerfDiscTime": extremeBfdSessPerfDiscTime,
       "extremeBfdSessPerfCtrlPktInHC": extremeBfdSessPerfCtrlPktInHC,
       "extremeBfdSessPerfCtrlPktOutHC": extremeBfdSessPerfCtrlPktOutHC,
       "extremeBfdSessPerfCtrlPktDropHC": extremeBfdSessPerfCtrlPktDropHC,
       "extremeBfdSessPerfEchoPktInHC": extremeBfdSessPerfEchoPktInHC,
       "extremeBfdSessPerfEchoPktOutHC": extremeBfdSessPerfEchoPktOutHC,
       "extremeBfdSessPerfEchoPktDropHC": extremeBfdSessPerfEchoPktDropHC,
       "extremeBfdSessDiscMapTable": extremeBfdSessDiscMapTable,
       "extremeBfdSessDiscMapEntry": extremeBfdSessDiscMapEntry,
       "extremeBfdSessDiscMapIndex": extremeBfdSessDiscMapIndex,
       "extremeBfdSessDiscMapStorageType": extremeBfdSessDiscMapStorageType,
       "extremeBfdSessDiscMapRowStatus": extremeBfdSessDiscMapRowStatus,
       "extremeBfdSessIpMapTable": extremeBfdSessIpMapTable,
       "extremeBfdSessIpMapEntry": extremeBfdSessIpMapEntry,
       "extremeBfdSessIpMapIndex": extremeBfdSessIpMapIndex,
       "extremeBfdSessIpMapStorageType": extremeBfdSessIpMapStorageType,
       "extremeBfdSessIpMapRowStatus": extremeBfdSessIpMapRowStatus,
       "extremeBfdConformance": extremeBfdConformance,
       "extremeBfdGroups": extremeBfdGroups,
       "extremeBfdSessionGroup": extremeBfdSessionGroup,
       "extremeBfdSessionReadOnlyGroup": extremeBfdSessionReadOnlyGroup,
       "extremeBfdSessionPerfGroup": extremeBfdSessionPerfGroup,
       "extremeBfdSessionPerfHCGroup": extremeBfdSessionPerfHCGroup,
       "extremeBfdNotificationGroup": extremeBfdNotificationGroup,
       "extremeBfdCompliances": extremeBfdCompliances,
       "extremeBfdModuleFullCompliance": extremeBfdModuleFullCompliance,
       "extremeBfdModuleReadOnlyCompliance": extremeBfdModuleReadOnlyCompliance}
)
