# SNMP MIB module (CISCO-ACCESS-REGISTRAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ACCESS-REGISTRAR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:28:31 2025
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

(cdbpPeerIpAddress,) = mibBuilder.importSymbols(
    "CISCO-DIAMETER-BASE-PROTOCOL-MIB",
    "cdbpPeerIpAddress")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(radiusAccServerExtEntry,) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccServerExtEntry")

(radiusAuthServerExtEntry,) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthServerExtEntry")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoAccessRegistrarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70)
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarMIB.setRevisions(
        ("2014-12-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CarServerState(TextualConvention, Integer32):
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
          ("up", 2),
          ("down", 3))
    )



class CarServerType(TextualConvention, Integer32):
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("ldap", 2),
          ("odbc", 3),
          ("local", 4),
          ("dns", 5),
          ("domainauth", 6),
          ("dynamicauth", 7),
          ("notify", 8),
          ("other", 9),
          ("sigtran", 10),
          ("oci", 11),
          ("sigtranm3ua", 12),
          ("diameter", 13))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAccessRegistrarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAccessRegistrarMIBObjects = _CiscoAccessRegistrarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1)
)
_CarRADIUS_ObjectIdentity = ObjectIdentity
carRADIUS = _CarRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1)
)
_CarAuthServerExtTable_Object = MibTable
carAuthServerExtTable = _CarAuthServerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 1)
)
if mibBuilder.loadTexts:
    carAuthServerExtTable.setStatus("current")
_CarAuthServerExtEntry_Object = MibTableRow
carAuthServerExtEntry = _CarAuthServerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    carAuthServerExtEntry.setStatus("current")
_CarAuthServerRunningState_Type = CarServerState
_CarAuthServerRunningState_Object = MibTableColumn
carAuthServerRunningState = _CarAuthServerRunningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 1, 1, 1),
    _CarAuthServerRunningState_Type()
)
carAuthServerRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carAuthServerRunningState.setStatus("current")


class _CarAuthServerType_Type(CarServerType):
    """Custom type carAuthServerType based on CarServerType"""
    subtypeSpec = CarServerType.subtypeSpec
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("ldap", 2),
          ("odbc", 3),
          ("local", 4),
          ("dns", 5),
          ("domainauth", 6),
          ("dynamicauth", 7),
          ("notify", 8),
          ("other", 9),
          ("sigtran", 10),
          ("oci", 11),
          ("sigtranm3ua", 12),
          ("diameter", 13))
    )


_CarAuthServerType_Type.__name__ = "CarServerType"
_CarAuthServerType_Object = MibTableColumn
carAuthServerType = _CarAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 1, 1, 2),
    _CarAuthServerType_Type()
)
carAuthServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carAuthServerType.setStatus("current")
_CarAccServerExtTable_Object = MibTable
carAccServerExtTable = _CarAccServerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    carAccServerExtTable.setStatus("current")
_CarAccServerExtEntry_Object = MibTableRow
carAccServerExtEntry = _CarAccServerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    carAccServerExtEntry.setStatus("current")
_CarAccServerRunningState_Type = CarServerState
_CarAccServerRunningState_Object = MibTableColumn
carAccServerRunningState = _CarAccServerRunningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 2, 1, 1),
    _CarAccServerRunningState_Type()
)
carAccServerRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carAccServerRunningState.setStatus("current")


class _CarAccServerType_Type(CarServerType):
    """Custom type carAccServerType based on CarServerType"""
    subtypeSpec = CarServerType.subtypeSpec
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("ldap", 2),
          ("odbc", 3),
          ("local", 4),
          ("dns", 5),
          ("domainauth", 6),
          ("dynamicauth", 7),
          ("notify", 8),
          ("other", 9),
          ("sigtran", 10),
          ("oci", 11),
          ("sigtranm3ua", 12),
          ("diameter", 13))
    )


_CarAccServerType_Type.__name__ = "CarServerType"
_CarAccServerType_Object = MibTableColumn
carAccServerType = _CarAccServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 2, 1, 2),
    _CarAccServerType_Type()
)
carAccServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carAccServerType.setStatus("current")


class _CarServerInputQueueMaxSize_Type(Integer32):
    """Custom type carServerInputQueueMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CarServerInputQueueMaxSize_Type.__name__ = "Integer32"
_CarServerInputQueueMaxSize_Object = MibScalar
carServerInputQueueMaxSize = _CarServerInputQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 3),
    _CarServerInputQueueMaxSize_Type()
)
carServerInputQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carServerInputQueueMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    carServerInputQueueMaxSize.setUnits("packets")


class _CarServerInputQueueSize_Type(Integer32):
    """Custom type carServerInputQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CarServerInputQueueSize_Type.__name__ = "Integer32"
_CarServerInputQueueSize_Object = MibScalar
carServerInputQueueSize = _CarServerInputQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 4),
    _CarServerInputQueueSize_Type()
)
carServerInputQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carServerInputQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    carServerInputQueueSize.setUnits("packets")
_CarServerAccLogInError_Type = TruthValue
_CarServerAccLogInError_Object = MibScalar
carServerAccLogInError = _CarServerAccLogInError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 5),
    _CarServerAccLogInError_Type()
)
carServerAccLogInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carServerAccLogInError.setStatus("current")


class _CarServerLicenseUsage_Type(Integer32):
    """Custom type carServerLicenseUsage based on Integer32"""
    defaultValue = 100


_CarServerLicenseUsage_Type.__name__ = "Integer32"
_CarServerLicenseUsage_Object = MibScalar
carServerLicenseUsage = _CarServerLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 6),
    _CarServerLicenseUsage_Type()
)
carServerLicenseUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carServerLicenseUsage.setStatus("current")
if mibBuilder.loadTexts:
    carServerLicenseUsage.setUnits("TPS")
_CarRadRemSvrStatsTable_Object = MibTable
carRadRemSvrStatsTable = _CarRadRemSvrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7)
)
if mibBuilder.loadTexts:
    carRadRemSvrStatsTable.setStatus("current")
_CarRadRemSvrStatsEntry_Object = MibTableRow
carRadRemSvrStatsEntry = _CarRadRemSvrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1)
)
carRadRemSvrStatsEntry.setIndexNames(
    (0, "CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsIndex"),
)
if mibBuilder.loadTexts:
    carRadRemSvrStatsEntry.setStatus("current")


class _CarRadRemSvrStatsIndex_Type(Integer32):
    """Custom type carRadRemSvrStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CarRadRemSvrStatsIndex_Type.__name__ = "Integer32"
_CarRadRemSvrStatsIndex_Object = MibTableColumn
carRadRemSvrStatsIndex = _CarRadRemSvrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 1),
    _CarRadRemSvrStatsIndex_Type()
)
carRadRemSvrStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carRadRemSvrStatsIndex.setStatus("current")
_CarRadRemSvrStatsServerName_Type = SnmpAdminString
_CarRadRemSvrStatsServerName_Object = MibTableColumn
carRadRemSvrStatsServerName = _CarRadRemSvrStatsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 2),
    _CarRadRemSvrStatsServerName_Type()
)
carRadRemSvrStatsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsServerName.setStatus("current")


class _CarRadRemSvrStatsType_Type(CarServerType):
    """Custom type carRadRemSvrStatsType based on CarServerType"""
    subtypeSpec = CarServerType.subtypeSpec
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("ldap", 2),
          ("odbc", 3),
          ("local", 4),
          ("dns", 5),
          ("domainauth", 6),
          ("dynamicauth", 7),
          ("notify", 8),
          ("other", 9),
          ("sigtran", 10),
          ("oci", 11),
          ("sigtranm3ua", 12),
          ("diameter", 13))
    )


_CarRadRemSvrStatsType_Type.__name__ = "CarServerType"
_CarRadRemSvrStatsType_Object = MibTableColumn
carRadRemSvrStatsType = _CarRadRemSvrStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 3),
    _CarRadRemSvrStatsType_Type()
)
carRadRemSvrStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsType.setStatus("current")
_CarRadRemSvrStatsInetAddrType_Type = InetAddressType
_CarRadRemSvrStatsInetAddrType_Object = MibTableColumn
carRadRemSvrStatsInetAddrType = _CarRadRemSvrStatsInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 4),
    _CarRadRemSvrStatsInetAddrType_Type()
)
carRadRemSvrStatsInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsInetAddrType.setStatus("current")
_CarRadRemSvrStatsInetAddress_Type = InetAddress
_CarRadRemSvrStatsInetAddress_Object = MibTableColumn
carRadRemSvrStatsInetAddress = _CarRadRemSvrStatsInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 5),
    _CarRadRemSvrStatsInetAddress_Type()
)
carRadRemSvrStatsInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carRadRemSvrStatsInetAddress.setStatus("current")


class _CarRadRemSvrStatsPortNumber_Type(InetPortNumber):
    """Custom type carRadRemSvrStatsPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CarRadRemSvrStatsPortNumber_Type.__name__ = "InetPortNumber"
_CarRadRemSvrStatsPortNumber_Object = MibTableColumn
carRadRemSvrStatsPortNumber = _CarRadRemSvrStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 6),
    _CarRadRemSvrStatsPortNumber_Type()
)
carRadRemSvrStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsPortNumber.setStatus("current")
_CarRadRemSvrStatsActive_Type = TruthValue
_CarRadRemSvrStatsActive_Object = MibTableColumn
carRadRemSvrStatsActive = _CarRadRemSvrStatsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 7),
    _CarRadRemSvrStatsActive_Type()
)
carRadRemSvrStatsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsActive.setStatus("current")
_CarRadRemSvrStatsMaxTries_Type = Counter32
_CarRadRemSvrStatsMaxTries_Object = MibTableColumn
carRadRemSvrStatsMaxTries = _CarRadRemSvrStatsMaxTries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 8),
    _CarRadRemSvrStatsMaxTries_Type()
)
carRadRemSvrStatsMaxTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsMaxTries.setStatus("current")
_CarRadRemSvrStatsRTTAverage_Type = TimeInterval
_CarRadRemSvrStatsRTTAverage_Object = MibTableColumn
carRadRemSvrStatsRTTAverage = _CarRadRemSvrStatsRTTAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 9),
    _CarRadRemSvrStatsRTTAverage_Type()
)
carRadRemSvrStatsRTTAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsRTTAverage.setStatus("current")
_CarRadRemSvrStatsRTTDeviation_Type = TimeInterval
_CarRadRemSvrStatsRTTDeviation_Object = MibTableColumn
carRadRemSvrStatsRTTDeviation = _CarRadRemSvrStatsRTTDeviation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 10),
    _CarRadRemSvrStatsRTTDeviation_Type()
)
carRadRemSvrStatsRTTDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsRTTDeviation.setStatus("current")
_CarRadRemSvrStatsTimeoutPenalty_Type = TimeInterval
_CarRadRemSvrStatsTimeoutPenalty_Object = MibTableColumn
carRadRemSvrStatsTimeoutPenalty = _CarRadRemSvrStatsTimeoutPenalty_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 11),
    _CarRadRemSvrStatsTimeoutPenalty_Type()
)
carRadRemSvrStatsTimeoutPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTimeoutPenalty.setStatus("current")
_CarRadRemSvrStatsTotalReqPending_Type = Gauge32
_CarRadRemSvrStatsTotalReqPending_Object = MibTableColumn
carRadRemSvrStatsTotalReqPending = _CarRadRemSvrStatsTotalReqPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 12),
    _CarRadRemSvrStatsTotalReqPending_Type()
)
carRadRemSvrStatsTotalReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqPending.setStatus("current")
_CarRadRemSvrStatsTotalReqSent_Type = Counter32
_CarRadRemSvrStatsTotalReqSent_Object = MibTableColumn
carRadRemSvrStatsTotalReqSent = _CarRadRemSvrStatsTotalReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 13),
    _CarRadRemSvrStatsTotalReqSent_Type()
)
carRadRemSvrStatsTotalReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqSent.setStatus("current")
_CarRadRemSvrStatsTotalReqOutstanding_Type = Gauge32
_CarRadRemSvrStatsTotalReqOutstanding_Object = MibTableColumn
carRadRemSvrStatsTotalReqOutstanding = _CarRadRemSvrStatsTotalReqOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 14),
    _CarRadRemSvrStatsTotalReqOutstanding_Type()
)
carRadRemSvrStatsTotalReqOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqOutstanding.setStatus("current")
_CarRadRemSvrStatsTotalReqAcknowledged_Type = Counter32
_CarRadRemSvrStatsTotalReqAcknowledged_Object = MibTableColumn
carRadRemSvrStatsTotalReqAcknowledged = _CarRadRemSvrStatsTotalReqAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 15),
    _CarRadRemSvrStatsTotalReqAcknowledged_Type()
)
carRadRemSvrStatsTotalReqAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqAcknowledged.setStatus("current")
_CarRadRemSvrStatsTotalReqTimedOut_Type = Counter32
_CarRadRemSvrStatsTotalReqTimedOut_Object = MibTableColumn
carRadRemSvrStatsTotalReqTimedOut = _CarRadRemSvrStatsTotalReqTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 16),
    _CarRadRemSvrStatsTotalReqTimedOut_Type()
)
carRadRemSvrStatsTotalReqTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqTimedOut.setStatus("current")
_CarRadRemSvrStatsTotalRespDropForNotInCache_Type = Counter32
_CarRadRemSvrStatsTotalRespDropForNotInCache_Object = MibTableColumn
carRadRemSvrStatsTotalRespDropForNotInCache = _CarRadRemSvrStatsTotalRespDropForNotInCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 17),
    _CarRadRemSvrStatsTotalRespDropForNotInCache_Type()
)
carRadRemSvrStatsTotalRespDropForNotInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalRespDropForNotInCache.setStatus("current")
_CarRadRemSvrStatsTotalRespDropForSignMismatch_Type = Counter32
_CarRadRemSvrStatsTotalRespDropForSignMismatch_Object = MibTableColumn
carRadRemSvrStatsTotalRespDropForSignMismatch = _CarRadRemSvrStatsTotalRespDropForSignMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 18),
    _CarRadRemSvrStatsTotalRespDropForSignMismatch_Type()
)
carRadRemSvrStatsTotalRespDropForSignMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalRespDropForSignMismatch.setStatus("current")
_CarRadRemSvrStatsTotalReqDropAfterMaxTries_Type = Counter32
_CarRadRemSvrStatsTotalReqDropAfterMaxTries_Object = MibTableColumn
carRadRemSvrStatsTotalReqDropAfterMaxTries = _CarRadRemSvrStatsTotalReqDropAfterMaxTries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 19),
    _CarRadRemSvrStatsTotalReqDropAfterMaxTries_Type()
)
carRadRemSvrStatsTotalReqDropAfterMaxTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsTotalReqDropAfterMaxTries.setStatus("current")
_CarRadRemSvrStatsLastReqTime_Type = SnmpAdminString
_CarRadRemSvrStatsLastReqTime_Object = MibTableColumn
carRadRemSvrStatsLastReqTime = _CarRadRemSvrStatsLastReqTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 20),
    _CarRadRemSvrStatsLastReqTime_Type()
)
carRadRemSvrStatsLastReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsLastReqTime.setStatus("current")
_CarRadRemSvrStatsLastAcceptTime_Type = SnmpAdminString
_CarRadRemSvrStatsLastAcceptTime_Object = MibTableColumn
carRadRemSvrStatsLastAcceptTime = _CarRadRemSvrStatsLastAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 7, 1, 21),
    _CarRadRemSvrStatsLastAcceptTime_Type()
)
carRadRemSvrStatsLastAcceptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadRemSvrStatsLastAcceptTime.setStatus("current")
_CarDiaRemSvrStatsTable_Object = MibTable
carDiaRemSvrStatsTable = _CarDiaRemSvrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8)
)
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTable.setStatus("current")
_CarDiaRemSvrStatsEntry_Object = MibTableRow
carDiaRemSvrStatsEntry = _CarDiaRemSvrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1)
)
carDiaRemSvrStatsEntry.setIndexNames(
    (0, "CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsIndex"),
)
if mibBuilder.loadTexts:
    carDiaRemSvrStatsEntry.setStatus("current")


class _CarDiaRemSvrStatsIndex_Type(Integer32):
    """Custom type carDiaRemSvrStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CarDiaRemSvrStatsIndex_Type.__name__ = "Integer32"
_CarDiaRemSvrStatsIndex_Object = MibTableColumn
carDiaRemSvrStatsIndex = _CarDiaRemSvrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 1),
    _CarDiaRemSvrStatsIndex_Type()
)
carDiaRemSvrStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsIndex.setStatus("current")
_CarDiaRemSvrStatsServerName_Type = SnmpAdminString
_CarDiaRemSvrStatsServerName_Object = MibTableColumn
carDiaRemSvrStatsServerName = _CarDiaRemSvrStatsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 2),
    _CarDiaRemSvrStatsServerName_Type()
)
carDiaRemSvrStatsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsServerName.setStatus("current")


class _CarDiaRemSvrStatsType_Type(CarServerType):
    """Custom type carDiaRemSvrStatsType based on CarServerType"""
    subtypeSpec = CarServerType.subtypeSpec
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("ldap", 2),
          ("odbc", 3),
          ("local", 4),
          ("dns", 5),
          ("domainauth", 6),
          ("dynamicauth", 7),
          ("notify", 8),
          ("other", 9),
          ("sigtran", 10),
          ("oci", 11),
          ("sigtranm3ua", 12),
          ("diameter", 13))
    )


_CarDiaRemSvrStatsType_Type.__name__ = "CarServerType"
_CarDiaRemSvrStatsType_Object = MibTableColumn
carDiaRemSvrStatsType = _CarDiaRemSvrStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 3),
    _CarDiaRemSvrStatsType_Type()
)
carDiaRemSvrStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsType.setStatus("current")
_CarDiaRemSvrStatsInetAddrType_Type = InetAddressType
_CarDiaRemSvrStatsInetAddrType_Object = MibTableColumn
carDiaRemSvrStatsInetAddrType = _CarDiaRemSvrStatsInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 4),
    _CarDiaRemSvrStatsInetAddrType_Type()
)
carDiaRemSvrStatsInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsInetAddrType.setStatus("current")
_CarDiaRemSvrStatsInetAddress_Type = InetAddress
_CarDiaRemSvrStatsInetAddress_Object = MibTableColumn
carDiaRemSvrStatsInetAddress = _CarDiaRemSvrStatsInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 5),
    _CarDiaRemSvrStatsInetAddress_Type()
)
carDiaRemSvrStatsInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsInetAddress.setStatus("current")


class _CarDiaRemSvrStatsPortNumber_Type(InetPortNumber):
    """Custom type carDiaRemSvrStatsPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CarDiaRemSvrStatsPortNumber_Type.__name__ = "InetPortNumber"
_CarDiaRemSvrStatsPortNumber_Object = MibTableColumn
carDiaRemSvrStatsPortNumber = _CarDiaRemSvrStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 6),
    _CarDiaRemSvrStatsPortNumber_Type()
)
carDiaRemSvrStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsPortNumber.setStatus("current")
_CarDiaRemSvrStatsActive_Type = TruthValue
_CarDiaRemSvrStatsActive_Object = MibTableColumn
carDiaRemSvrStatsActive = _CarDiaRemSvrStatsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 7),
    _CarDiaRemSvrStatsActive_Type()
)
carDiaRemSvrStatsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsActive.setStatus("current")
_CarDiaRemSvrStatsRTTAverage_Type = TimeInterval
_CarDiaRemSvrStatsRTTAverage_Object = MibTableColumn
carDiaRemSvrStatsRTTAverage = _CarDiaRemSvrStatsRTTAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 8),
    _CarDiaRemSvrStatsRTTAverage_Type()
)
carDiaRemSvrStatsRTTAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRTTAverage.setStatus("current")
_CarDiaRemSvrStatsRTTDeviation_Type = TimeInterval
_CarDiaRemSvrStatsRTTDeviation_Object = MibTableColumn
carDiaRemSvrStatsRTTDeviation = _CarDiaRemSvrStatsRTTDeviation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 9),
    _CarDiaRemSvrStatsRTTDeviation_Type()
)
carDiaRemSvrStatsRTTDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRTTDeviation.setStatus("current")
_CarDiaRemSvrStatsTotalReqPending_Type = Gauge32
_CarDiaRemSvrStatsTotalReqPending_Object = MibTableColumn
carDiaRemSvrStatsTotalReqPending = _CarDiaRemSvrStatsTotalReqPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 10),
    _CarDiaRemSvrStatsTotalReqPending_Type()
)
carDiaRemSvrStatsTotalReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalReqPending.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalReqPending.setUnits("messages")
_CarDiaRemSvrStatsTotalReqOutstanding_Type = Gauge32
_CarDiaRemSvrStatsTotalReqOutstanding_Object = MibTableColumn
carDiaRemSvrStatsTotalReqOutstanding = _CarDiaRemSvrStatsTotalReqOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 11),
    _CarDiaRemSvrStatsTotalReqOutstanding_Type()
)
carDiaRemSvrStatsTotalReqOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalReqOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalReqOutstanding.setUnits("messages")


class _CarDiaRemSvrStatsState_Type(Integer32):
    """Custom type carDiaRemSvrStatsState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("waitConnAck", 2),
          ("waitICEA", 3),
          ("elect", 4),
          ("waitReturns", 5),
          ("rOpen", 6),
          ("iOpen", 7),
          ("closing", 8))
    )


_CarDiaRemSvrStatsState_Type.__name__ = "Integer32"
_CarDiaRemSvrStatsState_Object = MibTableColumn
carDiaRemSvrStatsState = _CarDiaRemSvrStatsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 12),
    _CarDiaRemSvrStatsState_Type()
)
carDiaRemSvrStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsState.setStatus("current")
_CarDiaRemSvrStatsASRsIn_Type = Counter32
_CarDiaRemSvrStatsASRsIn_Object = MibTableColumn
carDiaRemSvrStatsASRsIn = _CarDiaRemSvrStatsASRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 13),
    _CarDiaRemSvrStatsASRsIn_Type()
)
carDiaRemSvrStatsASRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASRsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASRsIn.setUnits("messages")
_CarDiaRemSvrStatsASRsOut_Type = Counter32
_CarDiaRemSvrStatsASRsOut_Object = MibTableColumn
carDiaRemSvrStatsASRsOut = _CarDiaRemSvrStatsASRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 14),
    _CarDiaRemSvrStatsASRsOut_Type()
)
carDiaRemSvrStatsASRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASRsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASRsOut.setUnits("messages")
_CarDiaRemSvrStatsASAsIn_Type = Counter32
_CarDiaRemSvrStatsASAsIn_Object = MibTableColumn
carDiaRemSvrStatsASAsIn = _CarDiaRemSvrStatsASAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 15),
    _CarDiaRemSvrStatsASAsIn_Type()
)
carDiaRemSvrStatsASAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASAsIn.setUnits("messages")
_CarDiaRemSvrStatsASAsOut_Type = Counter32
_CarDiaRemSvrStatsASAsOut_Object = MibTableColumn
carDiaRemSvrStatsASAsOut = _CarDiaRemSvrStatsASAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 16),
    _CarDiaRemSvrStatsASAsOut_Type()
)
carDiaRemSvrStatsASAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsASAsOut.setUnits("messages")
_CarDiaRemSvrStatsACRsIn_Type = Counter32
_CarDiaRemSvrStatsACRsIn_Object = MibTableColumn
carDiaRemSvrStatsACRsIn = _CarDiaRemSvrStatsACRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 17),
    _CarDiaRemSvrStatsACRsIn_Type()
)
carDiaRemSvrStatsACRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACRsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACRsIn.setUnits("messages")
_CarDiaRemSvrStatsACRsOut_Type = Counter32
_CarDiaRemSvrStatsACRsOut_Object = MibTableColumn
carDiaRemSvrStatsACRsOut = _CarDiaRemSvrStatsACRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 18),
    _CarDiaRemSvrStatsACRsOut_Type()
)
carDiaRemSvrStatsACRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACRsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACRsOut.setUnits("messages")
_CarDiaRemSvrStatsACAsIn_Type = Counter32
_CarDiaRemSvrStatsACAsIn_Object = MibTableColumn
carDiaRemSvrStatsACAsIn = _CarDiaRemSvrStatsACAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 19),
    _CarDiaRemSvrStatsACAsIn_Type()
)
carDiaRemSvrStatsACAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACAsIn.setUnits("messages")
_CarDiaRemSvrStatsACAsOut_Type = Counter32
_CarDiaRemSvrStatsACAsOut_Object = MibTableColumn
carDiaRemSvrStatsACAsOut = _CarDiaRemSvrStatsACAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 20),
    _CarDiaRemSvrStatsACAsOut_Type()
)
carDiaRemSvrStatsACAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsACAsOut.setUnits("messages")
_CarDiaRemSvrStatsCERsIn_Type = Counter32
_CarDiaRemSvrStatsCERsIn_Object = MibTableColumn
carDiaRemSvrStatsCERsIn = _CarDiaRemSvrStatsCERsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 21),
    _CarDiaRemSvrStatsCERsIn_Type()
)
carDiaRemSvrStatsCERsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCERsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCERsIn.setUnits("messages")
_CarDiaRemSvrStatsCERsOut_Type = Counter32
_CarDiaRemSvrStatsCERsOut_Object = MibTableColumn
carDiaRemSvrStatsCERsOut = _CarDiaRemSvrStatsCERsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 22),
    _CarDiaRemSvrStatsCERsOut_Type()
)
carDiaRemSvrStatsCERsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCERsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCERsOut.setUnits("messages")
_CarDiaRemSvrStatsCEAsIn_Type = Counter32
_CarDiaRemSvrStatsCEAsIn_Object = MibTableColumn
carDiaRemSvrStatsCEAsIn = _CarDiaRemSvrStatsCEAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 23),
    _CarDiaRemSvrStatsCEAsIn_Type()
)
carDiaRemSvrStatsCEAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCEAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCEAsIn.setUnits("messages")
_CarDiaRemSvrStatsCEAsOut_Type = Counter32
_CarDiaRemSvrStatsCEAsOut_Object = MibTableColumn
carDiaRemSvrStatsCEAsOut = _CarDiaRemSvrStatsCEAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 24),
    _CarDiaRemSvrStatsCEAsOut_Type()
)
carDiaRemSvrStatsCEAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCEAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsCEAsOut.setUnits("messages")
_CarDiaRemSvrStatsDWRsIn_Type = Counter32
_CarDiaRemSvrStatsDWRsIn_Object = MibTableColumn
carDiaRemSvrStatsDWRsIn = _CarDiaRemSvrStatsDWRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 25),
    _CarDiaRemSvrStatsDWRsIn_Type()
)
carDiaRemSvrStatsDWRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWRsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWRsIn.setUnits("messages")
_CarDiaRemSvrStatsDWRsOut_Type = Counter32
_CarDiaRemSvrStatsDWRsOut_Object = MibTableColumn
carDiaRemSvrStatsDWRsOut = _CarDiaRemSvrStatsDWRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 26),
    _CarDiaRemSvrStatsDWRsOut_Type()
)
carDiaRemSvrStatsDWRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWRsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWRsOut.setUnits("messages")
_CarDiaRemSvrStatsDWAsIn_Type = Counter32
_CarDiaRemSvrStatsDWAsIn_Object = MibTableColumn
carDiaRemSvrStatsDWAsIn = _CarDiaRemSvrStatsDWAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 27),
    _CarDiaRemSvrStatsDWAsIn_Type()
)
carDiaRemSvrStatsDWAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWAsIn.setUnits("messages")
_CarDiaRemSvrStatsDWAsOut_Type = Counter32
_CarDiaRemSvrStatsDWAsOut_Object = MibTableColumn
carDiaRemSvrStatsDWAsOut = _CarDiaRemSvrStatsDWAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 28),
    _CarDiaRemSvrStatsDWAsOut_Type()
)
carDiaRemSvrStatsDWAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWAsOut.setUnits("messages")
_CarDiaRemSvrStatsDPRsIn_Type = Counter32
_CarDiaRemSvrStatsDPRsIn_Object = MibTableColumn
carDiaRemSvrStatsDPRsIn = _CarDiaRemSvrStatsDPRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 29),
    _CarDiaRemSvrStatsDPRsIn_Type()
)
carDiaRemSvrStatsDPRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPRsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPRsIn.setUnits("messages")
_CarDiaRemSvrStatsDPRsOut_Type = Counter32
_CarDiaRemSvrStatsDPRsOut_Object = MibTableColumn
carDiaRemSvrStatsDPRsOut = _CarDiaRemSvrStatsDPRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 30),
    _CarDiaRemSvrStatsDPRsOut_Type()
)
carDiaRemSvrStatsDPRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPRsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPRsOut.setUnits("messages")
_CarDiaRemSvrStatsDPAsIn_Type = Counter32
_CarDiaRemSvrStatsDPAsIn_Object = MibTableColumn
carDiaRemSvrStatsDPAsIn = _CarDiaRemSvrStatsDPAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 31),
    _CarDiaRemSvrStatsDPAsIn_Type()
)
carDiaRemSvrStatsDPAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPAsIn.setUnits("messages")
_CarDiaRemSvrStatsDPAsOut_Type = Counter32
_CarDiaRemSvrStatsDPAsOut_Object = MibTableColumn
carDiaRemSvrStatsDPAsOut = _CarDiaRemSvrStatsDPAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 32),
    _CarDiaRemSvrStatsDPAsOut_Type()
)
carDiaRemSvrStatsDPAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDPAsOut.setUnits("messages")
_CarDiaRemSvrStatsRARsIn_Type = Counter32
_CarDiaRemSvrStatsRARsIn_Object = MibTableColumn
carDiaRemSvrStatsRARsIn = _CarDiaRemSvrStatsRARsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 33),
    _CarDiaRemSvrStatsRARsIn_Type()
)
carDiaRemSvrStatsRARsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRARsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRARsIn.setUnits("messages")
_CarDiaRemSvrStatsRARsOut_Type = Counter32
_CarDiaRemSvrStatsRARsOut_Object = MibTableColumn
carDiaRemSvrStatsRARsOut = _CarDiaRemSvrStatsRARsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 34),
    _CarDiaRemSvrStatsRARsOut_Type()
)
carDiaRemSvrStatsRARsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRARsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRARsOut.setUnits("messages")
_CarDiaRemSvrStatsRAAsIn_Type = Counter32
_CarDiaRemSvrStatsRAAsIn_Object = MibTableColumn
carDiaRemSvrStatsRAAsIn = _CarDiaRemSvrStatsRAAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 35),
    _CarDiaRemSvrStatsRAAsIn_Type()
)
carDiaRemSvrStatsRAAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRAAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRAAsIn.setUnits("messages")
_CarDiaRemSvrStatsRAAsOut_Type = Counter32
_CarDiaRemSvrStatsRAAsOut_Object = MibTableColumn
carDiaRemSvrStatsRAAsOut = _CarDiaRemSvrStatsRAAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 36),
    _CarDiaRemSvrStatsRAAsOut_Type()
)
carDiaRemSvrStatsRAAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRAAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRAAsOut.setUnits("messages")
_CarDiaRemSvrStatsSTRsIn_Type = Counter32
_CarDiaRemSvrStatsSTRsIn_Object = MibTableColumn
carDiaRemSvrStatsSTRsIn = _CarDiaRemSvrStatsSTRsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 37),
    _CarDiaRemSvrStatsSTRsIn_Type()
)
carDiaRemSvrStatsSTRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTRsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTRsIn.setUnits("messages")
_CarDiaRemSvrStatsSTRsOut_Type = Counter32
_CarDiaRemSvrStatsSTRsOut_Object = MibTableColumn
carDiaRemSvrStatsSTRsOut = _CarDiaRemSvrStatsSTRsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 38),
    _CarDiaRemSvrStatsSTRsOut_Type()
)
carDiaRemSvrStatsSTRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTRsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTRsOut.setUnits("messages")
_CarDiaRemSvrStatsSTAsIn_Type = Counter32
_CarDiaRemSvrStatsSTAsIn_Object = MibTableColumn
carDiaRemSvrStatsSTAsIn = _CarDiaRemSvrStatsSTAsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 39),
    _CarDiaRemSvrStatsSTAsIn_Type()
)
carDiaRemSvrStatsSTAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTAsIn.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTAsIn.setUnits("messages")
_CarDiaRemSvrStatsSTAsOut_Type = Counter32
_CarDiaRemSvrStatsSTAsOut_Object = MibTableColumn
carDiaRemSvrStatsSTAsOut = _CarDiaRemSvrStatsSTAsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 40),
    _CarDiaRemSvrStatsSTAsOut_Type()
)
carDiaRemSvrStatsSTAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTAsOut.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsSTAsOut.setUnits("messages")
_CarDiaRemSvrStatsRedirectEvents_Type = Counter32
_CarDiaRemSvrStatsRedirectEvents_Object = MibTableColumn
carDiaRemSvrStatsRedirectEvents = _CarDiaRemSvrStatsRedirectEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 41),
    _CarDiaRemSvrStatsRedirectEvents_Type()
)
carDiaRemSvrStatsRedirectEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsRedirectEvents.setStatus("current")
_CarDiaRemSvrStatsAccDupReq_Type = Counter32
_CarDiaRemSvrStatsAccDupReq_Object = MibTableColumn
carDiaRemSvrStatsAccDupReq = _CarDiaRemSvrStatsAccDupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 42),
    _CarDiaRemSvrStatsAccDupReq_Type()
)
carDiaRemSvrStatsAccDupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsAccDupReq.setStatus("current")
_CarDiaRemSvrStatsMalformedReq_Type = Counter32
_CarDiaRemSvrStatsMalformedReq_Object = MibTableColumn
carDiaRemSvrStatsMalformedReq = _CarDiaRemSvrStatsMalformedReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 43),
    _CarDiaRemSvrStatsMalformedReq_Type()
)
carDiaRemSvrStatsMalformedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsMalformedReq.setStatus("current")
_CarDiaRemSvrStatsAccsNotRecorded_Type = Counter32
_CarDiaRemSvrStatsAccsNotRecorded_Object = MibTableColumn
carDiaRemSvrStatsAccsNotRecorded = _CarDiaRemSvrStatsAccsNotRecorded_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 44),
    _CarDiaRemSvrStatsAccsNotRecorded_Type()
)
carDiaRemSvrStatsAccsNotRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsAccsNotRecorded.setStatus("current")


class _CarDiaRemSvrStatsWhoInitDisconnect_Type(Integer32):
    """Custom type carDiaRemSvrStatsWhoInitDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("remoteserver", 2))
    )


_CarDiaRemSvrStatsWhoInitDisconnect_Type.__name__ = "Integer32"
_CarDiaRemSvrStatsWhoInitDisconnect_Object = MibTableColumn
carDiaRemSvrStatsWhoInitDisconnect = _CarDiaRemSvrStatsWhoInitDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 45),
    _CarDiaRemSvrStatsWhoInitDisconnect_Type()
)
carDiaRemSvrStatsWhoInitDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsWhoInitDisconnect.setStatus("current")
_CarDiaRemSvrStatsAccRetrans_Type = Counter32
_CarDiaRemSvrStatsAccRetrans_Object = MibTableColumn
carDiaRemSvrStatsAccRetrans = _CarDiaRemSvrStatsAccRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 46),
    _CarDiaRemSvrStatsAccRetrans_Type()
)
carDiaRemSvrStatsAccRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsAccRetrans.setStatus("current")
_CarDiaRemSvrStatsTotalRetrans_Type = Counter32
_CarDiaRemSvrStatsTotalRetrans_Object = MibTableColumn
carDiaRemSvrStatsTotalRetrans = _CarDiaRemSvrStatsTotalRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 47),
    _CarDiaRemSvrStatsTotalRetrans_Type()
)
carDiaRemSvrStatsTotalRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalRetrans.setStatus("current")
_CarDiaRemSvrStatsAccPendReqOut_Type = Gauge32
_CarDiaRemSvrStatsAccPendReqOut_Object = MibTableColumn
carDiaRemSvrStatsAccPendReqOut = _CarDiaRemSvrStatsAccPendReqOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 48),
    _CarDiaRemSvrStatsAccPendReqOut_Type()
)
carDiaRemSvrStatsAccPendReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsAccPendReqOut.setStatus("current")
_CarDiaRemSvrStatsAccReqDropped_Type = Counter32
_CarDiaRemSvrStatsAccReqDropped_Object = MibTableColumn
carDiaRemSvrStatsAccReqDropped = _CarDiaRemSvrStatsAccReqDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 49),
    _CarDiaRemSvrStatsAccReqDropped_Type()
)
carDiaRemSvrStatsAccReqDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsAccReqDropped.setStatus("current")
_CarDiaRemSvrStatsHByHDropMessages_Type = Counter32
_CarDiaRemSvrStatsHByHDropMessages_Object = MibTableColumn
carDiaRemSvrStatsHByHDropMessages = _CarDiaRemSvrStatsHByHDropMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 50),
    _CarDiaRemSvrStatsHByHDropMessages_Type()
)
carDiaRemSvrStatsHByHDropMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsHByHDropMessages.setStatus("current")
_CarDiaRemSvrStatsEToEDupMessages_Type = Counter32
_CarDiaRemSvrStatsEToEDupMessages_Object = MibTableColumn
carDiaRemSvrStatsEToEDupMessages = _CarDiaRemSvrStatsEToEDupMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 51),
    _CarDiaRemSvrStatsEToEDupMessages_Type()
)
carDiaRemSvrStatsEToEDupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsEToEDupMessages.setStatus("current")
_CarDiaRemSvrStatsUnknownTypes_Type = Counter32
_CarDiaRemSvrStatsUnknownTypes_Object = MibTableColumn
carDiaRemSvrStatsUnknownTypes = _CarDiaRemSvrStatsUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 52),
    _CarDiaRemSvrStatsUnknownTypes_Type()
)
carDiaRemSvrStatsUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsUnknownTypes.setStatus("current")
_CarDiaRemSvrStatsProtocolErrors_Type = Counter32
_CarDiaRemSvrStatsProtocolErrors_Object = MibTableColumn
carDiaRemSvrStatsProtocolErrors = _CarDiaRemSvrStatsProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 53),
    _CarDiaRemSvrStatsProtocolErrors_Type()
)
carDiaRemSvrStatsProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsProtocolErrors.setStatus("current")
_CarDiaRemSvrStatsTransientFailures_Type = Counter32
_CarDiaRemSvrStatsTransientFailures_Object = MibTableColumn
carDiaRemSvrStatsTransientFailures = _CarDiaRemSvrStatsTransientFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 54),
    _CarDiaRemSvrStatsTransientFailures_Type()
)
carDiaRemSvrStatsTransientFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTransientFailures.setStatus("current")
_CarDiaRemSvrStatsPermanentFailures_Type = Counter32
_CarDiaRemSvrStatsPermanentFailures_Object = MibTableColumn
carDiaRemSvrStatsPermanentFailures = _CarDiaRemSvrStatsPermanentFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 55),
    _CarDiaRemSvrStatsPermanentFailures_Type()
)
carDiaRemSvrStatsPermanentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsPermanentFailures.setStatus("current")
_CarDiaRemSvrStatsTransportDown_Type = Counter32
_CarDiaRemSvrStatsTransportDown_Object = MibTableColumn
carDiaRemSvrStatsTransportDown = _CarDiaRemSvrStatsTransportDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 56),
    _CarDiaRemSvrStatsTransportDown_Type()
)
carDiaRemSvrStatsTransportDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTransportDown.setStatus("current")


class _CarDiaRemSvrStatsDWCurrentStatus_Type(Integer32):
    """Custom type carDiaRemSvrStatsDWCurrentStatus based on Integer32"""
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
        *(("okay", 1),
          ("suspect", 2),
          ("down", 3),
          ("reopen", 4))
    )


_CarDiaRemSvrStatsDWCurrentStatus_Type.__name__ = "Integer32"
_CarDiaRemSvrStatsDWCurrentStatus_Object = MibTableColumn
carDiaRemSvrStatsDWCurrentStatus = _CarDiaRemSvrStatsDWCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 57),
    _CarDiaRemSvrStatsDWCurrentStatus_Type()
)
carDiaRemSvrStatsDWCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsDWCurrentStatus.setStatus("current")
_CarDiaRemSvrStatsTimeoutConnAtmpts_Type = Counter32
_CarDiaRemSvrStatsTimeoutConnAtmpts_Object = MibTableColumn
carDiaRemSvrStatsTimeoutConnAtmpts = _CarDiaRemSvrStatsTimeoutConnAtmpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 58),
    _CarDiaRemSvrStatsTimeoutConnAtmpts_Type()
)
carDiaRemSvrStatsTimeoutConnAtmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTimeoutConnAtmpts.setStatus("current")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTimeoutConnAtmpts.setUnits("attempts")
_CarDiaRemSvrStatsTotalReqAcknowledged_Type = Counter32
_CarDiaRemSvrStatsTotalReqAcknowledged_Object = MibTableColumn
carDiaRemSvrStatsTotalReqAcknowledged = _CarDiaRemSvrStatsTotalReqAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 8, 1, 59),
    _CarDiaRemSvrStatsTotalReqAcknowledged_Type()
)
carDiaRemSvrStatsTotalReqAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaRemSvrStatsTotalReqAcknowledged.setStatus("current")
_CarRadSvrStats_ObjectIdentity = ObjectIdentity
carRadSvrStats = _CarRadSvrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9)
)
_CarRadSvrStatsServerStartTime_Type = SnmpAdminString
_CarRadSvrStatsServerStartTime_Object = MibScalar
carRadSvrStatsServerStartTime = _CarRadSvrStatsServerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 1),
    _CarRadSvrStatsServerStartTime_Type()
)
carRadSvrStatsServerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsServerStartTime.setStatus("current")
_CarRadSvrStatsServerResetTime_Type = SnmpAdminString
_CarRadSvrStatsServerResetTime_Object = MibScalar
carRadSvrStatsServerResetTime = _CarRadSvrStatsServerResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 2),
    _CarRadSvrStatsServerResetTime_Type()
)
carRadSvrStatsServerResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsServerResetTime.setStatus("current")


class _CarRadSvrStatsServerState_Type(Integer32):
    """Custom type carRadSvrStatsServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 1),
          ("running", 2))
    )


_CarRadSvrStatsServerState_Type.__name__ = "Integer32"
_CarRadSvrStatsServerState_Object = MibScalar
carRadSvrStatsServerState = _CarRadSvrStatsServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 3),
    _CarRadSvrStatsServerState_Type()
)
carRadSvrStatsServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsServerState.setStatus("current")
_CarRadSvrStatsTotalPacketsInPool_Type = Counter32
_CarRadSvrStatsTotalPacketsInPool_Object = MibScalar
carRadSvrStatsTotalPacketsInPool = _CarRadSvrStatsTotalPacketsInPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 4),
    _CarRadSvrStatsTotalPacketsInPool_Type()
)
carRadSvrStatsTotalPacketsInPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsInPool.setStatus("current")
_CarRadSvrStatsTotalPacketsReceived_Type = Counter32
_CarRadSvrStatsTotalPacketsReceived_Object = MibScalar
carRadSvrStatsTotalPacketsReceived = _CarRadSvrStatsTotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 5),
    _CarRadSvrStatsTotalPacketsReceived_Type()
)
carRadSvrStatsTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsReceived.setStatus("current")
_CarRadSvrStatsTotalPacketsSent_Type = Counter32
_CarRadSvrStatsTotalPacketsSent_Object = MibScalar
carRadSvrStatsTotalPacketsSent = _CarRadSvrStatsTotalPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 6),
    _CarRadSvrStatsTotalPacketsSent_Type()
)
carRadSvrStatsTotalPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsSent.setStatus("current")
_CarRadSvrStatsTotalReq_Type = Counter32
_CarRadSvrStatsTotalReq_Object = MibScalar
carRadSvrStatsTotalReq = _CarRadSvrStatsTotalReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 7),
    _CarRadSvrStatsTotalReq_Type()
)
carRadSvrStatsTotalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalReq.setStatus("current")
_CarRadSvrStatsTotalResp_Type = Counter32
_CarRadSvrStatsTotalResp_Object = MibScalar
carRadSvrStatsTotalResp = _CarRadSvrStatsTotalResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 8),
    _CarRadSvrStatsTotalResp_Type()
)
carRadSvrStatsTotalResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalResp.setStatus("current")
_CarRadSvrStatsTotalAccessReq_Type = Counter32
_CarRadSvrStatsTotalAccessReq_Object = MibScalar
carRadSvrStatsTotalAccessReq = _CarRadSvrStatsTotalAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 9),
    _CarRadSvrStatsTotalAccessReq_Type()
)
carRadSvrStatsTotalAccessReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccessReq.setStatus("current")
_CarRadSvrStatsTotalAccessAccepts_Type = Counter32
_CarRadSvrStatsTotalAccessAccepts_Object = MibScalar
carRadSvrStatsTotalAccessAccepts = _CarRadSvrStatsTotalAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 10),
    _CarRadSvrStatsTotalAccessAccepts_Type()
)
carRadSvrStatsTotalAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccessAccepts.setStatus("current")
_CarRadSvrStatsTotalAccessChallenges_Type = Counter32
_CarRadSvrStatsTotalAccessChallenges_Object = MibScalar
carRadSvrStatsTotalAccessChallenges = _CarRadSvrStatsTotalAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 11),
    _CarRadSvrStatsTotalAccessChallenges_Type()
)
carRadSvrStatsTotalAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccessChallenges.setStatus("current")
_CarRadSvrStatsTotalAccessRejects_Type = Counter32
_CarRadSvrStatsTotalAccessRejects_Object = MibScalar
carRadSvrStatsTotalAccessRejects = _CarRadSvrStatsTotalAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 12),
    _CarRadSvrStatsTotalAccessRejects_Type()
)
carRadSvrStatsTotalAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccessRejects.setStatus("current")
_CarRadSvrStatsTotalAccessResp_Type = Counter32
_CarRadSvrStatsTotalAccessResp_Object = MibScalar
carRadSvrStatsTotalAccessResp = _CarRadSvrStatsTotalAccessResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 13),
    _CarRadSvrStatsTotalAccessResp_Type()
)
carRadSvrStatsTotalAccessResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccessResp.setStatus("current")
_CarRadSvrStatsTotalAccountingReq_Type = Counter32
_CarRadSvrStatsTotalAccountingReq_Object = MibScalar
carRadSvrStatsTotalAccountingReq = _CarRadSvrStatsTotalAccountingReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 14),
    _CarRadSvrStatsTotalAccountingReq_Type()
)
carRadSvrStatsTotalAccountingReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccountingReq.setStatus("current")
_CarRadSvrStatsTotalAccountingResp_Type = Counter32
_CarRadSvrStatsTotalAccountingResp_Object = MibScalar
carRadSvrStatsTotalAccountingResp = _CarRadSvrStatsTotalAccountingResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 15),
    _CarRadSvrStatsTotalAccountingResp_Type()
)
carRadSvrStatsTotalAccountingResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAccountingResp.setStatus("current")
_CarRadSvrStatsTotalStatusServerReq_Type = Counter32
_CarRadSvrStatsTotalStatusServerReq_Object = MibScalar
carRadSvrStatsTotalStatusServerReq = _CarRadSvrStatsTotalStatusServerReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 16),
    _CarRadSvrStatsTotalStatusServerReq_Type()
)
carRadSvrStatsTotalStatusServerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalStatusServerReq.setStatus("current")
_CarRadSvrStatsTotalAscendIPAAllocateReq_Type = Counter32
_CarRadSvrStatsTotalAscendIPAAllocateReq_Object = MibScalar
carRadSvrStatsTotalAscendIPAAllocateReq = _CarRadSvrStatsTotalAscendIPAAllocateReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 17),
    _CarRadSvrStatsTotalAscendIPAAllocateReq_Type()
)
carRadSvrStatsTotalAscendIPAAllocateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAscendIPAAllocateReq.setStatus("current")
_CarRadSvrStatsTotalAscendIPAAllocateResp_Type = Counter32
_CarRadSvrStatsTotalAscendIPAAllocateResp_Object = MibScalar
carRadSvrStatsTotalAscendIPAAllocateResp = _CarRadSvrStatsTotalAscendIPAAllocateResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 18),
    _CarRadSvrStatsTotalAscendIPAAllocateResp_Type()
)
carRadSvrStatsTotalAscendIPAAllocateResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAscendIPAAllocateResp.setStatus("current")
_CarRadSvrStatsTotalAscendIPAReleaseReq_Type = Counter32
_CarRadSvrStatsTotalAscendIPAReleaseReq_Object = MibScalar
carRadSvrStatsTotalAscendIPAReleaseReq = _CarRadSvrStatsTotalAscendIPAReleaseReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 19),
    _CarRadSvrStatsTotalAscendIPAReleaseReq_Type()
)
carRadSvrStatsTotalAscendIPAReleaseReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAscendIPAReleaseReq.setStatus("current")
_CarRadSvrStatsTotalAscendIPAReleaseResp_Type = Counter32
_CarRadSvrStatsTotalAscendIPAReleaseResp_Object = MibScalar
carRadSvrStatsTotalAscendIPAReleaseResp = _CarRadSvrStatsTotalAscendIPAReleaseResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 20),
    _CarRadSvrStatsTotalAscendIPAReleaseResp_Type()
)
carRadSvrStatsTotalAscendIPAReleaseResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalAscendIPAReleaseResp.setStatus("current")
_CarRadSvrStatsTotalUSRNASRebootReq_Type = Counter32
_CarRadSvrStatsTotalUSRNASRebootReq_Object = MibScalar
carRadSvrStatsTotalUSRNASRebootReq = _CarRadSvrStatsTotalUSRNASRebootReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 21),
    _CarRadSvrStatsTotalUSRNASRebootReq_Type()
)
carRadSvrStatsTotalUSRNASRebootReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRNASRebootReq.setStatus("current")
_CarRadSvrStatsTotalUSRNASRebootResp_Type = Counter32
_CarRadSvrStatsTotalUSRNASRebootResp_Object = MibScalar
carRadSvrStatsTotalUSRNASRebootResp = _CarRadSvrStatsTotalUSRNASRebootResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 22),
    _CarRadSvrStatsTotalUSRNASRebootResp_Type()
)
carRadSvrStatsTotalUSRNASRebootResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRNASRebootResp.setStatus("current")
_CarRadSvrStatsTotalUSRResourceFreeReq_Type = Counter32
_CarRadSvrStatsTotalUSRResourceFreeReq_Object = MibScalar
carRadSvrStatsTotalUSRResourceFreeReq = _CarRadSvrStatsTotalUSRResourceFreeReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 23),
    _CarRadSvrStatsTotalUSRResourceFreeReq_Type()
)
carRadSvrStatsTotalUSRResourceFreeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRResourceFreeReq.setStatus("current")
_CarRadSvrStatsTotalUSRResourceFreeResp_Type = Counter32
_CarRadSvrStatsTotalUSRResourceFreeResp_Object = MibScalar
carRadSvrStatsTotalUSRResourceFreeResp = _CarRadSvrStatsTotalUSRResourceFreeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 24),
    _CarRadSvrStatsTotalUSRResourceFreeResp_Type()
)
carRadSvrStatsTotalUSRResourceFreeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRResourceFreeResp.setStatus("current")
_CarRadSvrStatsTotalUSRQueryResourceReq_Type = Counter32
_CarRadSvrStatsTotalUSRQueryResourceReq_Object = MibScalar
carRadSvrStatsTotalUSRQueryResourceReq = _CarRadSvrStatsTotalUSRQueryResourceReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 25),
    _CarRadSvrStatsTotalUSRQueryResourceReq_Type()
)
carRadSvrStatsTotalUSRQueryResourceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRQueryResourceReq.setStatus("current")
_CarRadSvrStatsTotalUSRQueryResourceResp_Type = Counter32
_CarRadSvrStatsTotalUSRQueryResourceResp_Object = MibScalar
carRadSvrStatsTotalUSRQueryResourceResp = _CarRadSvrStatsTotalUSRQueryResourceResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 26),
    _CarRadSvrStatsTotalUSRQueryResourceResp_Type()
)
carRadSvrStatsTotalUSRQueryResourceResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRQueryResourceResp.setStatus("current")
_CarRadSvrStatsTotalUSRQueryReclaimReq_Type = Counter32
_CarRadSvrStatsTotalUSRQueryReclaimReq_Object = MibScalar
carRadSvrStatsTotalUSRQueryReclaimReq = _CarRadSvrStatsTotalUSRQueryReclaimReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 27),
    _CarRadSvrStatsTotalUSRQueryReclaimReq_Type()
)
carRadSvrStatsTotalUSRQueryReclaimReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRQueryReclaimReq.setStatus("current")
_CarRadSvrStatsTotalUSRQueryReclaimResp_Type = Counter32
_CarRadSvrStatsTotalUSRQueryReclaimResp_Object = MibScalar
carRadSvrStatsTotalUSRQueryReclaimResp = _CarRadSvrStatsTotalUSRQueryReclaimResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 28),
    _CarRadSvrStatsTotalUSRQueryReclaimResp_Type()
)
carRadSvrStatsTotalUSRQueryReclaimResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalUSRQueryReclaimResp.setStatus("current")
_CarRadSvrStatsTotalPacketsInUse_Type = Gauge32
_CarRadSvrStatsTotalPacketsInUse_Object = MibScalar
carRadSvrStatsTotalPacketsInUse = _CarRadSvrStatsTotalPacketsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 29),
    _CarRadSvrStatsTotalPacketsInUse_Type()
)
carRadSvrStatsTotalPacketsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsInUse.setStatus("current")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsInUse.setUnits("messages")
_CarRadSvrStatsTotalPacketsDrained_Type = Counter32
_CarRadSvrStatsTotalPacketsDrained_Object = MibScalar
carRadSvrStatsTotalPacketsDrained = _CarRadSvrStatsTotalPacketsDrained_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 30),
    _CarRadSvrStatsTotalPacketsDrained_Type()
)
carRadSvrStatsTotalPacketsDrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsDrained.setStatus("current")
_CarRadSvrStatsTotalPacketsDropped_Type = Counter32
_CarRadSvrStatsTotalPacketsDropped_Object = MibScalar
carRadSvrStatsTotalPacketsDropped = _CarRadSvrStatsTotalPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 31),
    _CarRadSvrStatsTotalPacketsDropped_Type()
)
carRadSvrStatsTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPacketsDropped.setStatus("current")
_CarRadSvrStatsTotalPayloadDecryptionFailures_Type = Counter32
_CarRadSvrStatsTotalPayloadDecryptionFailures_Object = MibScalar
carRadSvrStatsTotalPayloadDecryptionFailures = _CarRadSvrStatsTotalPayloadDecryptionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 9, 32),
    _CarRadSvrStatsTotalPayloadDecryptionFailures_Type()
)
carRadSvrStatsTotalPayloadDecryptionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrStatsTotalPayloadDecryptionFailures.setStatus("current")
_CarRadSvrXMLStats_ObjectIdentity = ObjectIdentity
carRadSvrXMLStats = _CarRadSvrXMLStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10)
)
_CarRadSvrXMLStatsTotalXMLPacketsInPool_Type = Counter32
_CarRadSvrXMLStatsTotalXMLPacketsInPool_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketsInPool = _CarRadSvrXMLStatsTotalXMLPacketsInPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 1),
    _CarRadSvrXMLStatsTotalXMLPacketsInPool_Type()
)
carRadSvrXMLStatsTotalXMLPacketsInPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsInPool.setStatus("current")
_CarRadSvrXMLStatsTotalXMLPacketsReceived_Type = Counter32
_CarRadSvrXMLStatsTotalXMLPacketsReceived_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketsReceived = _CarRadSvrXMLStatsTotalXMLPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 2),
    _CarRadSvrXMLStatsTotalXMLPacketsReceived_Type()
)
carRadSvrXMLStatsTotalXMLPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsReceived.setStatus("current")
_CarRadSvrXMLStatsTotalXMLReq_Type = Counter32
_CarRadSvrXMLStatsTotalXMLReq_Object = MibScalar
carRadSvrXMLStatsTotalXMLReq = _CarRadSvrXMLStatsTotalXMLReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 3),
    _CarRadSvrXMLStatsTotalXMLReq_Type()
)
carRadSvrXMLStatsTotalXMLReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLReq.setStatus("current")
_CarRadSvrXMLStatsTotalXMLResp_Type = Counter32
_CarRadSvrXMLStatsTotalXMLResp_Object = MibScalar
carRadSvrXMLStatsTotalXMLResp = _CarRadSvrXMLStatsTotalXMLResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 4),
    _CarRadSvrXMLStatsTotalXMLResp_Type()
)
carRadSvrXMLStatsTotalXMLResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLResp.setStatus("current")
_CarRadSvrXMLStatsTotalXMLPacketsInUse_Type = Gauge32
_CarRadSvrXMLStatsTotalXMLPacketsInUse_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketsInUse = _CarRadSvrXMLStatsTotalXMLPacketsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 5),
    _CarRadSvrXMLStatsTotalXMLPacketsInUse_Type()
)
carRadSvrXMLStatsTotalXMLPacketsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsInUse.setStatus("current")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsInUse.setUnits("messages")
_CarRadSvrXMLStatsTotalXMLPacketsDrained_Type = Counter32
_CarRadSvrXMLStatsTotalXMLPacketsDrained_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketsDrained = _CarRadSvrXMLStatsTotalXMLPacketsDrained_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 6),
    _CarRadSvrXMLStatsTotalXMLPacketsDrained_Type()
)
carRadSvrXMLStatsTotalXMLPacketsDrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsDrained.setStatus("current")
_CarRadSvrXMLStatsTotalXMLPacketsDropped_Type = Counter32
_CarRadSvrXMLStatsTotalXMLPacketsDropped_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketsDropped = _CarRadSvrXMLStatsTotalXMLPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 7),
    _CarRadSvrXMLStatsTotalXMLPacketsDropped_Type()
)
carRadSvrXMLStatsTotalXMLPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketsDropped.setStatus("current")
_CarRadSvrXMLStatsTotalXMLPacketParseFailures_Type = Counter32
_CarRadSvrXMLStatsTotalXMLPacketParseFailures_Object = MibScalar
carRadSvrXMLStatsTotalXMLPacketParseFailures = _CarRadSvrXMLStatsTotalXMLPacketParseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 10, 8),
    _CarRadSvrXMLStatsTotalXMLPacketParseFailures_Type()
)
carRadSvrXMLStatsTotalXMLPacketParseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRadSvrXMLStatsTotalXMLPacketParseFailures.setStatus("current")
_CarDiaSvrStats_ObjectIdentity = ObjectIdentity
carDiaSvrStats = _CarDiaSvrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11)
)
_CarDiaSvrStatsServerStartTime_Type = SnmpAdminString
_CarDiaSvrStatsServerStartTime_Object = MibScalar
carDiaSvrStatsServerStartTime = _CarDiaSvrStatsServerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 1),
    _CarDiaSvrStatsServerStartTime_Type()
)
carDiaSvrStatsServerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsServerStartTime.setStatus("current")
_CarDiaSvrStatsServerResetTime_Type = SnmpAdminString
_CarDiaSvrStatsServerResetTime_Object = MibScalar
carDiaSvrStatsServerResetTime = _CarDiaSvrStatsServerResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 2),
    _CarDiaSvrStatsServerResetTime_Type()
)
carDiaSvrStatsServerResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsServerResetTime.setStatus("current")


class _CarDiaSvrStatsServerState_Type(Integer32):
    """Custom type carDiaSvrStatsServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 1),
          ("running", 2),
          ("unknown", 3))
    )


_CarDiaSvrStatsServerState_Type.__name__ = "Integer32"
_CarDiaSvrStatsServerState_Object = MibScalar
carDiaSvrStatsServerState = _CarDiaSvrStatsServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 3),
    _CarDiaSvrStatsServerState_Type()
)
carDiaSvrStatsServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsServerState.setStatus("current")
_CarDiaSvrStatsTotalUpTime_Type = TimeInterval
_CarDiaSvrStatsTotalUpTime_Object = MibScalar
carDiaSvrStatsTotalUpTime = _CarDiaSvrStatsTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 4),
    _CarDiaSvrStatsTotalUpTime_Type()
)
carDiaSvrStatsTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalUpTime.setStatus("current")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalUpTime.setUnits("secs")
_CarDiaSvrStatsElapsedResetTime_Type = TimeInterval
_CarDiaSvrStatsElapsedResetTime_Object = MibScalar
carDiaSvrStatsElapsedResetTime = _CarDiaSvrStatsElapsedResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 5),
    _CarDiaSvrStatsElapsedResetTime_Type()
)
carDiaSvrStatsElapsedResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsElapsedResetTime.setStatus("current")
if mibBuilder.loadTexts:
    carDiaSvrStatsElapsedResetTime.setUnits("secs")
_CarDiaSvrStatsTotalPacketsIn_Type = Counter32
_CarDiaSvrStatsTotalPacketsIn_Object = MibScalar
carDiaSvrStatsTotalPacketsIn = _CarDiaSvrStatsTotalPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 6),
    _CarDiaSvrStatsTotalPacketsIn_Type()
)
carDiaSvrStatsTotalPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalPacketsIn.setStatus("current")
_CarDiaSvrStatsTotalPacketsOut_Type = Counter32
_CarDiaSvrStatsTotalPacketsOut_Object = MibScalar
carDiaSvrStatsTotalPacketsOut = _CarDiaSvrStatsTotalPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 7),
    _CarDiaSvrStatsTotalPacketsOut_Type()
)
carDiaSvrStatsTotalPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalPacketsOut.setStatus("current")
_CarDiaSvrStatsTotalPacketsInUse_Type = Gauge32
_CarDiaSvrStatsTotalPacketsInUse_Object = MibScalar
carDiaSvrStatsTotalPacketsInUse = _CarDiaSvrStatsTotalPacketsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 11, 8),
    _CarDiaSvrStatsTotalPacketsInUse_Type()
)
carDiaSvrStatsTotalPacketsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalPacketsInUse.setStatus("current")
if mibBuilder.loadTexts:
    carDiaSvrStatsTotalPacketsInUse.setUnits("messages")
_CarServerSigtranLicenseUsage_Type = Integer32
_CarServerSigtranLicenseUsage_Object = MibScalar
carServerSigtranLicenseUsage = _CarServerSigtranLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 1, 12),
    _CarServerSigtranLicenseUsage_Type()
)
carServerSigtranLicenseUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carServerSigtranLicenseUsage.setStatus("current")
_CarNotifObjects_ObjectIdentity = ObjectIdentity
carNotifObjects = _CarNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2)
)


class _CarNotifStartType_Type(Integer32):
    """Custom type carNotifStartType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstStart", 1),
          ("reload", 2))
    )


_CarNotifStartType_Type.__name__ = "Integer32"
_CarNotifStartType_Object = MibScalar
carNotifStartType = _CarNotifStartType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 1),
    _CarNotifStartType_Type()
)
carNotifStartType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carNotifStartType.setStatus("current")


class _CarNotifInputQueueHighThreshold_Type(Integer32):
    """Custom type carNotifInputQueueHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CarNotifInputQueueHighThreshold_Type.__name__ = "Integer32"
_CarNotifInputQueueHighThreshold_Object = MibScalar
carNotifInputQueueHighThreshold = _CarNotifInputQueueHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 2),
    _CarNotifInputQueueHighThreshold_Type()
)
carNotifInputQueueHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carNotifInputQueueHighThreshold.setStatus("current")


class _CarNotifInputQueueLowThreshold_Type(Integer32):
    """Custom type carNotifInputQueueLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CarNotifInputQueueLowThreshold_Type.__name__ = "Integer32"
_CarNotifInputQueueLowThreshold_Object = MibScalar
carNotifInputQueueLowThreshold = _CarNotifInputQueueLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 3),
    _CarNotifInputQueueLowThreshold_Type()
)
carNotifInputQueueLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carNotifInputQueueLowThreshold.setStatus("current")
_CarNotifAcctLogErrorInterval_Type = TimeTicks
_CarNotifAcctLogErrorInterval_Object = MibScalar
carNotifAcctLogErrorInterval = _CarNotifAcctLogErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 4),
    _CarNotifAcctLogErrorInterval_Type()
)
carNotifAcctLogErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carNotifAcctLogErrorInterval.setStatus("current")
_CarNotifAcctLogErrorReason_Type = SnmpAdminString
_CarNotifAcctLogErrorReason_Object = MibScalar
carNotifAcctLogErrorReason = _CarNotifAcctLogErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 5),
    _CarNotifAcctLogErrorReason_Type()
)
carNotifAcctLogErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carNotifAcctLogErrorReason.setStatus("current")


class _CarNotifLicenseUsage_Type(Integer32):
    """Custom type carNotifLicenseUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_CarNotifLicenseUsage_Type.__name__ = "Integer32"
_CarNotifLicenseUsage_Object = MibScalar
carNotifLicenseUsage = _CarNotifLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 6),
    _CarNotifLicenseUsage_Type()
)
carNotifLicenseUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carNotifLicenseUsage.setStatus("current")
_CarNotifSigtranLicenseUsage_Type = Integer32
_CarNotifSigtranLicenseUsage_Object = MibScalar
carNotifSigtranLicenseUsage = _CarNotifSigtranLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 1, 2, 7),
    _CarNotifSigtranLicenseUsage_Type()
)
carNotifSigtranLicenseUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    carNotifSigtranLicenseUsage.setStatus("current")
_CarMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
carMIBNotificationPrefix = _CarMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2)
)
_CarMIBNotifications_ObjectIdentity = ObjectIdentity
carMIBNotifications = _CarMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0)
)
_CiscoAccessRegistrarMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAccessRegistrarMIBConformance = _CiscoAccessRegistrarMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3)
)
_CiscoAccessRegistrarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAccessRegistrarMIBCompliances = _CiscoAccessRegistrarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 1)
)
_CiscoAccessRegistrarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAccessRegistrarMIBGroups = _CiscoAccessRegistrarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2)
)
radiusAuthServerExtEntry.registerAugmentions(
    ("CISCO-ACCESS-REGISTRAR-MIB",
     "carAuthServerExtEntry")
)
carAuthServerExtEntry.setIndexNames(*radiusAuthServerExtEntry.getIndexNames())
radiusAccServerExtEntry.registerAugmentions(
    ("CISCO-ACCESS-REGISTRAR-MIB",
     "carAccServerExtEntry")
)
carAccServerExtEntry.setIndexNames(*radiusAccServerExtEntry.getIndexNames())

# Managed Objects groups

ciscoAccessRegistrarNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 1)
)
ciscoAccessRegistrarNotifObjectsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carNotifStartType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifAcctLogErrorInterval"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifAcctLogErrorReason"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueHighThreshold"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueLowThreshold"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifLicenseUsage"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifSigtranLicenseUsage"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarNotifObjectsGroup.setStatus("current")

ciscoAccessRegistrarMibObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 2)
)
ciscoAccessRegistrarMibObjectsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carAuthServerRunningState"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carAuthServerType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carAccServerRunningState"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carAccServerType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerInputQueueMaxSize"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerInputQueueSize"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerAccLogInError"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerLicenseUsage"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerSigtranLicenseUsage"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarMibObjectsGroup.setStatus("current")

ciscoAccessRegistrarDiaRemSvrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 4)
)
ciscoAccessRegistrarDiaRemSvrStatsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsPortNumber"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsActive"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRTTAverage"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRTTDeviation"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTotalReqPending"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTotalReqOutstanding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsState"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsASRsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsASRsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsASAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsASAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsACRsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsACRsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsACAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsACAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsCERsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsCERsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsCEAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsCEAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDWRsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDWRsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDWAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDWAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDPRsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDPRsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDPAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDPAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRARsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRARsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRAAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRAAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsSTRsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsSTRsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsSTAsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsSTAsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsRedirectEvents"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsAccDupReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsMalformedReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsAccsNotRecorded"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsWhoInitDisconnect"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsAccRetrans"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTotalRetrans"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsAccPendReqOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsAccReqDropped"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsHByHDropMessages"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsEToEDupMessages"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsUnknownTypes"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsProtocolErrors"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTransientFailures"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsPermanentFailures"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTransportDown"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsDWCurrentStatus"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTimeoutConnAtmpts"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsTotalReqAcknowledged"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarDiaRemSvrStatsGroup.setStatus("current")

ciscoAccessRegistrarRadRemSvrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 5)
)
ciscoAccessRegistrarRadRemSvrStatsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsPortNumber"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsActive"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsMaxTries"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsRTTAverage"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsRTTDeviation"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTimeoutPenalty"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqPending"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqSent"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqOutstanding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqAcknowledged"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqTimedOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalRespDropForNotInCache"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalRespDropForSignMismatch"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsTotalReqDropAfterMaxTries"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsLastReqTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsLastAcceptTime"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarRadRemSvrStatsGroup.setStatus("current")

ciscoAccessRegistrarRadSvrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 6)
)
ciscoAccessRegistrarRadSvrStatsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsServerStartTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsServerResetTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsServerState"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsInPool"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsReceived"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsSent"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccessReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccessAccepts"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccessChallenges"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccessRejects"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccessResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccountingReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAccountingResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalStatusServerReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAscendIPAAllocateReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAscendIPAAllocateResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAscendIPAReleaseReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalAscendIPAReleaseResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRNASRebootReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRNASRebootResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRResourceFreeReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRResourceFreeResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRQueryResourceReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRQueryResourceResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRQueryReclaimReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalUSRQueryReclaimResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsInUse"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsDrained"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPacketsDropped"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrStatsTotalPayloadDecryptionFailures"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarRadSvrStatsGroup.setStatus("current")

ciscoAccessRegistrarDiaSvrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 7)
)
ciscoAccessRegistrarDiaSvrStatsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsServerStartTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsServerResetTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsServerState"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsTotalUpTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsElapsedResetTime"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsTotalPacketsIn"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsTotalPacketsOut"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaSvrStatsTotalPacketsInUse"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarDiaSvrStatsGroup.setStatus("current")

ciscoAccessRegistrarRadSvrXMLStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 8)
)
ciscoAccessRegistrarRadSvrXMLStatsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketsInPool"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketsReceived"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLReq"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLResp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketsInUse"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketsDrained"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketsDropped"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadSvrXMLStatsTotalXMLPacketParseFailures"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarRadSvrXMLStatsGroup.setStatus("current")


# Notification objects

carServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 1)
)
carServerStart.setObjects(
    ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifStartType")
)
if mibBuilder.loadTexts:
    carServerStart.setStatus(
        "current"
    )

carServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 2)
)
if mibBuilder.loadTexts:
    carServerStop.setStatus(
        "current"
    )

carInputQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 3)
)
carInputQueueFull.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueHighThreshold"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueLowThreshold"))
)
if mibBuilder.loadTexts:
    carInputQueueFull.setStatus(
        "current"
    )

carInputQueueNotVeryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 4)
)
carInputQueueNotVeryFull.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueHighThreshold"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifInputQueueLowThreshold"))
)
if mibBuilder.loadTexts:
    carInputQueueNotVeryFull.setStatus(
        "current"
    )

carOtherAuthServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 5)
)
carOtherAuthServerNotResponding.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carOtherAuthServerNotResponding.setStatus(
        "current"
    )

carOtherAuthServerResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 6)
)
carOtherAuthServerResponding.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carOtherAuthServerResponding.setStatus(
        "current"
    )

carOtherAccServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 7)
)
carOtherAccServerNotResponding.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carOtherAccServerNotResponding.setStatus(
        "current"
    )

carOtherAccServerResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 8)
)
carOtherAccServerResponding.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carOtherAccServerResponding.setStatus(
        "current"
    )

carAccoutingLoggingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 9)
)
carAccoutingLoggingFailure.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carNotifAcctLogErrorReason"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carNotifAcctLogErrorInterval"))
)
if mibBuilder.loadTexts:
    carAccoutingLoggingFailure.setStatus(
        "current"
    )

carLicenseUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 10)
)
carLicenseUsage.setObjects(
    ("CISCO-ACCESS-REGISTRAR-MIB", "carServerLicenseUsage")
)
if mibBuilder.loadTexts:
    carLicenseUsage.setStatus(
        "current"
    )

carDiameterPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 11)
)
carDiameterPeerDown.setObjects(
    ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIpAddress")
)
if mibBuilder.loadTexts:
    carDiameterPeerDown.setStatus(
        "current"
    )

carDiameterPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 12)
)
carDiameterPeerUp.setObjects(
    ("CISCO-DIAMETER-BASE-PROTOCOL-MIB", "cdbpPeerIpAddress")
)
if mibBuilder.loadTexts:
    carDiameterPeerUp.setStatus(
        "current"
    )

carDiaRemSvrConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 13)
)
carDiaRemSvrConnectionUp.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carDiaRemSvrConnectionUp.setStatus(
        "current"
    )

carDiaRemSvrConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 14)
)
carDiaRemSvrConnectionDown.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddrType"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsInetAddress"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsPortNumber"))
)
if mibBuilder.loadTexts:
    carDiaRemSvrConnectionDown.setStatus(
        "current"
    )

carDiaRemSvrTransientFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 15)
)
carDiaRemSvrTransientFailure.setObjects(
    ("CISCO-ACCESS-REGISTRAR-MIB", "carRadRemSvrStatsServerName")
)
if mibBuilder.loadTexts:
    carDiaRemSvrTransientFailure.setStatus(
        "current"
    )

carDiaRemSvrPermanentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 16)
)
carDiaRemSvrPermanentFailure.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsServerName"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrStatsPermanentFailures"))
)
if mibBuilder.loadTexts:
    carDiaRemSvrPermanentFailure.setStatus(
        "current"
    )

carSigtranLicenseUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 2, 0, 17)
)
carSigtranLicenseUsage.setObjects(
    ("CISCO-ACCESS-REGISTRAR-MIB", "carServerSigtranLicenseUsage")
)
if mibBuilder.loadTexts:
    carSigtranLicenseUsage.setStatus(
        "current"
    )


# Notifications groups

ciscoAccessRegistrarNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 2, 3)
)
ciscoAccessRegistrarNotificationsGroup.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "carServerStart"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carServerStop"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carInputQueueFull"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carInputQueueNotVeryFull"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carOtherAuthServerNotResponding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carOtherAuthServerResponding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carOtherAccServerNotResponding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carOtherAccServerResponding"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carAccoutingLoggingFailure"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carLicenseUsage"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiameterPeerDown"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiameterPeerUp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrConnectionUp"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrConnectionDown"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrTransientFailure"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carDiaRemSvrPermanentFailure"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "carSigtranLicenseUsage"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAccessRegistrarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 70, 3, 1, 1)
)
ciscoAccessRegistrarMIBCompliance.setObjects(
      *(("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarNotifObjectsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarNotificationsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarMibObjectsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarDiaRemSvrStatsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarRadRemSvrStatsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarRadSvrStatsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarDiaSvrStatsGroup"),
        ("CISCO-ACCESS-REGISTRAR-MIB", "ciscoAccessRegistrarRadSvrXMLStatsGroup"))
)
if mibBuilder.loadTexts:
    ciscoAccessRegistrarMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ACCESS-REGISTRAR-MIB",
    **{"CarServerState": CarServerState,
       "CarServerType": CarServerType,
       "ciscoAccessRegistrarMIB": ciscoAccessRegistrarMIB,
       "ciscoAccessRegistrarMIBObjects": ciscoAccessRegistrarMIBObjects,
       "carRADIUS": carRADIUS,
       "carAuthServerExtTable": carAuthServerExtTable,
       "carAuthServerExtEntry": carAuthServerExtEntry,
       "carAuthServerRunningState": carAuthServerRunningState,
       "carAuthServerType": carAuthServerType,
       "carAccServerExtTable": carAccServerExtTable,
       "carAccServerExtEntry": carAccServerExtEntry,
       "carAccServerRunningState": carAccServerRunningState,
       "carAccServerType": carAccServerType,
       "carServerInputQueueMaxSize": carServerInputQueueMaxSize,
       "carServerInputQueueSize": carServerInputQueueSize,
       "carServerAccLogInError": carServerAccLogInError,
       "carServerLicenseUsage": carServerLicenseUsage,
       "carRadRemSvrStatsTable": carRadRemSvrStatsTable,
       "carRadRemSvrStatsEntry": carRadRemSvrStatsEntry,
       "carRadRemSvrStatsIndex": carRadRemSvrStatsIndex,
       "carRadRemSvrStatsServerName": carRadRemSvrStatsServerName,
       "carRadRemSvrStatsType": carRadRemSvrStatsType,
       "carRadRemSvrStatsInetAddrType": carRadRemSvrStatsInetAddrType,
       "carRadRemSvrStatsInetAddress": carRadRemSvrStatsInetAddress,
       "carRadRemSvrStatsPortNumber": carRadRemSvrStatsPortNumber,
       "carRadRemSvrStatsActive": carRadRemSvrStatsActive,
       "carRadRemSvrStatsMaxTries": carRadRemSvrStatsMaxTries,
       "carRadRemSvrStatsRTTAverage": carRadRemSvrStatsRTTAverage,
       "carRadRemSvrStatsRTTDeviation": carRadRemSvrStatsRTTDeviation,
       "carRadRemSvrStatsTimeoutPenalty": carRadRemSvrStatsTimeoutPenalty,
       "carRadRemSvrStatsTotalReqPending": carRadRemSvrStatsTotalReqPending,
       "carRadRemSvrStatsTotalReqSent": carRadRemSvrStatsTotalReqSent,
       "carRadRemSvrStatsTotalReqOutstanding": carRadRemSvrStatsTotalReqOutstanding,
       "carRadRemSvrStatsTotalReqAcknowledged": carRadRemSvrStatsTotalReqAcknowledged,
       "carRadRemSvrStatsTotalReqTimedOut": carRadRemSvrStatsTotalReqTimedOut,
       "carRadRemSvrStatsTotalRespDropForNotInCache": carRadRemSvrStatsTotalRespDropForNotInCache,
       "carRadRemSvrStatsTotalRespDropForSignMismatch": carRadRemSvrStatsTotalRespDropForSignMismatch,
       "carRadRemSvrStatsTotalReqDropAfterMaxTries": carRadRemSvrStatsTotalReqDropAfterMaxTries,
       "carRadRemSvrStatsLastReqTime": carRadRemSvrStatsLastReqTime,
       "carRadRemSvrStatsLastAcceptTime": carRadRemSvrStatsLastAcceptTime,
       "carDiaRemSvrStatsTable": carDiaRemSvrStatsTable,
       "carDiaRemSvrStatsEntry": carDiaRemSvrStatsEntry,
       "carDiaRemSvrStatsIndex": carDiaRemSvrStatsIndex,
       "carDiaRemSvrStatsServerName": carDiaRemSvrStatsServerName,
       "carDiaRemSvrStatsType": carDiaRemSvrStatsType,
       "carDiaRemSvrStatsInetAddrType": carDiaRemSvrStatsInetAddrType,
       "carDiaRemSvrStatsInetAddress": carDiaRemSvrStatsInetAddress,
       "carDiaRemSvrStatsPortNumber": carDiaRemSvrStatsPortNumber,
       "carDiaRemSvrStatsActive": carDiaRemSvrStatsActive,
       "carDiaRemSvrStatsRTTAverage": carDiaRemSvrStatsRTTAverage,
       "carDiaRemSvrStatsRTTDeviation": carDiaRemSvrStatsRTTDeviation,
       "carDiaRemSvrStatsTotalReqPending": carDiaRemSvrStatsTotalReqPending,
       "carDiaRemSvrStatsTotalReqOutstanding": carDiaRemSvrStatsTotalReqOutstanding,
       "carDiaRemSvrStatsState": carDiaRemSvrStatsState,
       "carDiaRemSvrStatsASRsIn": carDiaRemSvrStatsASRsIn,
       "carDiaRemSvrStatsASRsOut": carDiaRemSvrStatsASRsOut,
       "carDiaRemSvrStatsASAsIn": carDiaRemSvrStatsASAsIn,
       "carDiaRemSvrStatsASAsOut": carDiaRemSvrStatsASAsOut,
       "carDiaRemSvrStatsACRsIn": carDiaRemSvrStatsACRsIn,
       "carDiaRemSvrStatsACRsOut": carDiaRemSvrStatsACRsOut,
       "carDiaRemSvrStatsACAsIn": carDiaRemSvrStatsACAsIn,
       "carDiaRemSvrStatsACAsOut": carDiaRemSvrStatsACAsOut,
       "carDiaRemSvrStatsCERsIn": carDiaRemSvrStatsCERsIn,
       "carDiaRemSvrStatsCERsOut": carDiaRemSvrStatsCERsOut,
       "carDiaRemSvrStatsCEAsIn": carDiaRemSvrStatsCEAsIn,
       "carDiaRemSvrStatsCEAsOut": carDiaRemSvrStatsCEAsOut,
       "carDiaRemSvrStatsDWRsIn": carDiaRemSvrStatsDWRsIn,
       "carDiaRemSvrStatsDWRsOut": carDiaRemSvrStatsDWRsOut,
       "carDiaRemSvrStatsDWAsIn": carDiaRemSvrStatsDWAsIn,
       "carDiaRemSvrStatsDWAsOut": carDiaRemSvrStatsDWAsOut,
       "carDiaRemSvrStatsDPRsIn": carDiaRemSvrStatsDPRsIn,
       "carDiaRemSvrStatsDPRsOut": carDiaRemSvrStatsDPRsOut,
       "carDiaRemSvrStatsDPAsIn": carDiaRemSvrStatsDPAsIn,
       "carDiaRemSvrStatsDPAsOut": carDiaRemSvrStatsDPAsOut,
       "carDiaRemSvrStatsRARsIn": carDiaRemSvrStatsRARsIn,
       "carDiaRemSvrStatsRARsOut": carDiaRemSvrStatsRARsOut,
       "carDiaRemSvrStatsRAAsIn": carDiaRemSvrStatsRAAsIn,
       "carDiaRemSvrStatsRAAsOut": carDiaRemSvrStatsRAAsOut,
       "carDiaRemSvrStatsSTRsIn": carDiaRemSvrStatsSTRsIn,
       "carDiaRemSvrStatsSTRsOut": carDiaRemSvrStatsSTRsOut,
       "carDiaRemSvrStatsSTAsIn": carDiaRemSvrStatsSTAsIn,
       "carDiaRemSvrStatsSTAsOut": carDiaRemSvrStatsSTAsOut,
       "carDiaRemSvrStatsRedirectEvents": carDiaRemSvrStatsRedirectEvents,
       "carDiaRemSvrStatsAccDupReq": carDiaRemSvrStatsAccDupReq,
       "carDiaRemSvrStatsMalformedReq": carDiaRemSvrStatsMalformedReq,
       "carDiaRemSvrStatsAccsNotRecorded": carDiaRemSvrStatsAccsNotRecorded,
       "carDiaRemSvrStatsWhoInitDisconnect": carDiaRemSvrStatsWhoInitDisconnect,
       "carDiaRemSvrStatsAccRetrans": carDiaRemSvrStatsAccRetrans,
       "carDiaRemSvrStatsTotalRetrans": carDiaRemSvrStatsTotalRetrans,
       "carDiaRemSvrStatsAccPendReqOut": carDiaRemSvrStatsAccPendReqOut,
       "carDiaRemSvrStatsAccReqDropped": carDiaRemSvrStatsAccReqDropped,
       "carDiaRemSvrStatsHByHDropMessages": carDiaRemSvrStatsHByHDropMessages,
       "carDiaRemSvrStatsEToEDupMessages": carDiaRemSvrStatsEToEDupMessages,
       "carDiaRemSvrStatsUnknownTypes": carDiaRemSvrStatsUnknownTypes,
       "carDiaRemSvrStatsProtocolErrors": carDiaRemSvrStatsProtocolErrors,
       "carDiaRemSvrStatsTransientFailures": carDiaRemSvrStatsTransientFailures,
       "carDiaRemSvrStatsPermanentFailures": carDiaRemSvrStatsPermanentFailures,
       "carDiaRemSvrStatsTransportDown": carDiaRemSvrStatsTransportDown,
       "carDiaRemSvrStatsDWCurrentStatus": carDiaRemSvrStatsDWCurrentStatus,
       "carDiaRemSvrStatsTimeoutConnAtmpts": carDiaRemSvrStatsTimeoutConnAtmpts,
       "carDiaRemSvrStatsTotalReqAcknowledged": carDiaRemSvrStatsTotalReqAcknowledged,
       "carRadSvrStats": carRadSvrStats,
       "carRadSvrStatsServerStartTime": carRadSvrStatsServerStartTime,
       "carRadSvrStatsServerResetTime": carRadSvrStatsServerResetTime,
       "carRadSvrStatsServerState": carRadSvrStatsServerState,
       "carRadSvrStatsTotalPacketsInPool": carRadSvrStatsTotalPacketsInPool,
       "carRadSvrStatsTotalPacketsReceived": carRadSvrStatsTotalPacketsReceived,
       "carRadSvrStatsTotalPacketsSent": carRadSvrStatsTotalPacketsSent,
       "carRadSvrStatsTotalReq": carRadSvrStatsTotalReq,
       "carRadSvrStatsTotalResp": carRadSvrStatsTotalResp,
       "carRadSvrStatsTotalAccessReq": carRadSvrStatsTotalAccessReq,
       "carRadSvrStatsTotalAccessAccepts": carRadSvrStatsTotalAccessAccepts,
       "carRadSvrStatsTotalAccessChallenges": carRadSvrStatsTotalAccessChallenges,
       "carRadSvrStatsTotalAccessRejects": carRadSvrStatsTotalAccessRejects,
       "carRadSvrStatsTotalAccessResp": carRadSvrStatsTotalAccessResp,
       "carRadSvrStatsTotalAccountingReq": carRadSvrStatsTotalAccountingReq,
       "carRadSvrStatsTotalAccountingResp": carRadSvrStatsTotalAccountingResp,
       "carRadSvrStatsTotalStatusServerReq": carRadSvrStatsTotalStatusServerReq,
       "carRadSvrStatsTotalAscendIPAAllocateReq": carRadSvrStatsTotalAscendIPAAllocateReq,
       "carRadSvrStatsTotalAscendIPAAllocateResp": carRadSvrStatsTotalAscendIPAAllocateResp,
       "carRadSvrStatsTotalAscendIPAReleaseReq": carRadSvrStatsTotalAscendIPAReleaseReq,
       "carRadSvrStatsTotalAscendIPAReleaseResp": carRadSvrStatsTotalAscendIPAReleaseResp,
       "carRadSvrStatsTotalUSRNASRebootReq": carRadSvrStatsTotalUSRNASRebootReq,
       "carRadSvrStatsTotalUSRNASRebootResp": carRadSvrStatsTotalUSRNASRebootResp,
       "carRadSvrStatsTotalUSRResourceFreeReq": carRadSvrStatsTotalUSRResourceFreeReq,
       "carRadSvrStatsTotalUSRResourceFreeResp": carRadSvrStatsTotalUSRResourceFreeResp,
       "carRadSvrStatsTotalUSRQueryResourceReq": carRadSvrStatsTotalUSRQueryResourceReq,
       "carRadSvrStatsTotalUSRQueryResourceResp": carRadSvrStatsTotalUSRQueryResourceResp,
       "carRadSvrStatsTotalUSRQueryReclaimReq": carRadSvrStatsTotalUSRQueryReclaimReq,
       "carRadSvrStatsTotalUSRQueryReclaimResp": carRadSvrStatsTotalUSRQueryReclaimResp,
       "carRadSvrStatsTotalPacketsInUse": carRadSvrStatsTotalPacketsInUse,
       "carRadSvrStatsTotalPacketsDrained": carRadSvrStatsTotalPacketsDrained,
       "carRadSvrStatsTotalPacketsDropped": carRadSvrStatsTotalPacketsDropped,
       "carRadSvrStatsTotalPayloadDecryptionFailures": carRadSvrStatsTotalPayloadDecryptionFailures,
       "carRadSvrXMLStats": carRadSvrXMLStats,
       "carRadSvrXMLStatsTotalXMLPacketsInPool": carRadSvrXMLStatsTotalXMLPacketsInPool,
       "carRadSvrXMLStatsTotalXMLPacketsReceived": carRadSvrXMLStatsTotalXMLPacketsReceived,
       "carRadSvrXMLStatsTotalXMLReq": carRadSvrXMLStatsTotalXMLReq,
       "carRadSvrXMLStatsTotalXMLResp": carRadSvrXMLStatsTotalXMLResp,
       "carRadSvrXMLStatsTotalXMLPacketsInUse": carRadSvrXMLStatsTotalXMLPacketsInUse,
       "carRadSvrXMLStatsTotalXMLPacketsDrained": carRadSvrXMLStatsTotalXMLPacketsDrained,
       "carRadSvrXMLStatsTotalXMLPacketsDropped": carRadSvrXMLStatsTotalXMLPacketsDropped,
       "carRadSvrXMLStatsTotalXMLPacketParseFailures": carRadSvrXMLStatsTotalXMLPacketParseFailures,
       "carDiaSvrStats": carDiaSvrStats,
       "carDiaSvrStatsServerStartTime": carDiaSvrStatsServerStartTime,
       "carDiaSvrStatsServerResetTime": carDiaSvrStatsServerResetTime,
       "carDiaSvrStatsServerState": carDiaSvrStatsServerState,
       "carDiaSvrStatsTotalUpTime": carDiaSvrStatsTotalUpTime,
       "carDiaSvrStatsElapsedResetTime": carDiaSvrStatsElapsedResetTime,
       "carDiaSvrStatsTotalPacketsIn": carDiaSvrStatsTotalPacketsIn,
       "carDiaSvrStatsTotalPacketsOut": carDiaSvrStatsTotalPacketsOut,
       "carDiaSvrStatsTotalPacketsInUse": carDiaSvrStatsTotalPacketsInUse,
       "carServerSigtranLicenseUsage": carServerSigtranLicenseUsage,
       "carNotifObjects": carNotifObjects,
       "carNotifStartType": carNotifStartType,
       "carNotifInputQueueHighThreshold": carNotifInputQueueHighThreshold,
       "carNotifInputQueueLowThreshold": carNotifInputQueueLowThreshold,
       "carNotifAcctLogErrorInterval": carNotifAcctLogErrorInterval,
       "carNotifAcctLogErrorReason": carNotifAcctLogErrorReason,
       "carNotifLicenseUsage": carNotifLicenseUsage,
       "carNotifSigtranLicenseUsage": carNotifSigtranLicenseUsage,
       "carMIBNotificationPrefix": carMIBNotificationPrefix,
       "carMIBNotifications": carMIBNotifications,
       "carServerStart": carServerStart,
       "carServerStop": carServerStop,
       "carInputQueueFull": carInputQueueFull,
       "carInputQueueNotVeryFull": carInputQueueNotVeryFull,
       "carOtherAuthServerNotResponding": carOtherAuthServerNotResponding,
       "carOtherAuthServerResponding": carOtherAuthServerResponding,
       "carOtherAccServerNotResponding": carOtherAccServerNotResponding,
       "carOtherAccServerResponding": carOtherAccServerResponding,
       "carAccoutingLoggingFailure": carAccoutingLoggingFailure,
       "carLicenseUsage": carLicenseUsage,
       "carDiameterPeerDown": carDiameterPeerDown,
       "carDiameterPeerUp": carDiameterPeerUp,
       "carDiaRemSvrConnectionUp": carDiaRemSvrConnectionUp,
       "carDiaRemSvrConnectionDown": carDiaRemSvrConnectionDown,
       "carDiaRemSvrTransientFailure": carDiaRemSvrTransientFailure,
       "carDiaRemSvrPermanentFailure": carDiaRemSvrPermanentFailure,
       "carSigtranLicenseUsage": carSigtranLicenseUsage,
       "ciscoAccessRegistrarMIBConformance": ciscoAccessRegistrarMIBConformance,
       "ciscoAccessRegistrarMIBCompliances": ciscoAccessRegistrarMIBCompliances,
       "ciscoAccessRegistrarMIBCompliance": ciscoAccessRegistrarMIBCompliance,
       "ciscoAccessRegistrarMIBGroups": ciscoAccessRegistrarMIBGroups,
       "ciscoAccessRegistrarNotifObjectsGroup": ciscoAccessRegistrarNotifObjectsGroup,
       "ciscoAccessRegistrarMibObjectsGroup": ciscoAccessRegistrarMibObjectsGroup,
       "ciscoAccessRegistrarNotificationsGroup": ciscoAccessRegistrarNotificationsGroup,
       "ciscoAccessRegistrarDiaRemSvrStatsGroup": ciscoAccessRegistrarDiaRemSvrStatsGroup,
       "ciscoAccessRegistrarRadRemSvrStatsGroup": ciscoAccessRegistrarRadRemSvrStatsGroup,
       "ciscoAccessRegistrarRadSvrStatsGroup": ciscoAccessRegistrarRadSvrStatsGroup,
       "ciscoAccessRegistrarDiaSvrStatsGroup": ciscoAccessRegistrarDiaSvrStatsGroup,
       "ciscoAccessRegistrarRadSvrXMLStatsGroup": ciscoAccessRegistrarRadSvrXMLStatsGroup}
)
