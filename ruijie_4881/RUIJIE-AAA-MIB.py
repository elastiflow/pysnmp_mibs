# SNMP MIB module (RUIJIE-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AAA-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:22 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(radiusAccClientServerPortNumber,
 radiusAccServerAddress) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19)
)
if mibBuilder.loadTexts:
    ruijieAAAMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRadiusServerTrap_ObjectIdentity = ObjectIdentity
ruijieRadiusServerTrap = _RuijieRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 0)
)
_RuijieAAAMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAAAMIBObjects = _RuijieAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1)
)
_RuijieDot1xAuthObjects_ObjectIdentity = ObjectIdentity
ruijieDot1xAuthObjects = _RuijieDot1xAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1)
)


class _RuijieDot1xAuthStatus_Type(EnabledStatus):
    """Custom type ruijieDot1xAuthStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieDot1xAuthStatus_Type.__name__ = "EnabledStatus"
_RuijieDot1xAuthStatus_Object = MibScalar
ruijieDot1xAuthStatus = _RuijieDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 1),
    _RuijieDot1xAuthStatus_Type()
)
ruijieDot1xAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthStatus.setStatus("current")


class _RuijieDot1xAuthObjectsQuietPeriod_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsQuietPeriod based on Unsigned32"""
    defaultValue = 60


_RuijieDot1xAuthObjectsQuietPeriod_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsQuietPeriod_Object = MibScalar
ruijieDot1xAuthObjectsQuietPeriod = _RuijieDot1xAuthObjectsQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 2),
    _RuijieDot1xAuthObjectsQuietPeriod_Type()
)
ruijieDot1xAuthObjectsQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsQuietPeriod.setStatus("current")


class _RuijieDot1xAuthObjectsTxPeriod_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsTxPeriod based on Unsigned32"""
    defaultValue = 30


_RuijieDot1xAuthObjectsTxPeriod_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsTxPeriod_Object = MibScalar
ruijieDot1xAuthObjectsTxPeriod = _RuijieDot1xAuthObjectsTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 3),
    _RuijieDot1xAuthObjectsTxPeriod_Type()
)
ruijieDot1xAuthObjectsTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsTxPeriod.setStatus("current")


class _RuijieDot1xAuthObjectsSuppTimeout_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsSuppTimeout based on Unsigned32"""
    defaultValue = 30


_RuijieDot1xAuthObjectsSuppTimeout_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsSuppTimeout_Object = MibScalar
ruijieDot1xAuthObjectsSuppTimeout = _RuijieDot1xAuthObjectsSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 4),
    _RuijieDot1xAuthObjectsSuppTimeout_Type()
)
ruijieDot1xAuthObjectsSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsSuppTimeout.setStatus("current")


class _RuijieDot1xAuthObjectsServerTimeout_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsServerTimeout based on Unsigned32"""
    defaultValue = 30


_RuijieDot1xAuthObjectsServerTimeout_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsServerTimeout_Object = MibScalar
ruijieDot1xAuthObjectsServerTimeout = _RuijieDot1xAuthObjectsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 5),
    _RuijieDot1xAuthObjectsServerTimeout_Type()
)
ruijieDot1xAuthObjectsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsServerTimeout.setStatus("current")


class _RuijieDot1xAuthObjectsMaxReq_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsMaxReq based on Unsigned32"""
    defaultValue = 2


_RuijieDot1xAuthObjectsMaxReq_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsMaxReq_Object = MibScalar
ruijieDot1xAuthObjectsMaxReq = _RuijieDot1xAuthObjectsMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 6),
    _RuijieDot1xAuthObjectsMaxReq_Type()
)
ruijieDot1xAuthObjectsMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsMaxReq.setStatus("current")


class _RuijieDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_RuijieDot1xAuthObjectsReAuthPeriod_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsReAuthPeriod_Object = MibScalar
ruijieDot1xAuthObjectsReAuthPeriod = _RuijieDot1xAuthObjectsReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 7),
    _RuijieDot1xAuthObjectsReAuthPeriod_Type()
)
ruijieDot1xAuthObjectsReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsReAuthPeriod.setStatus("current")


class _RuijieDot1xAuthObjectsMaxReauth_Type(Unsigned32):
    """Custom type ruijieDot1xAuthObjectsMaxReauth based on Unsigned32"""
    defaultValue = 2


_RuijieDot1xAuthObjectsMaxReauth_Type.__name__ = "Unsigned32"
_RuijieDot1xAuthObjectsMaxReauth_Object = MibScalar
ruijieDot1xAuthObjectsMaxReauth = _RuijieDot1xAuthObjectsMaxReauth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 8),
    _RuijieDot1xAuthObjectsMaxReauth_Type()
)
ruijieDot1xAuthObjectsMaxReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsMaxReauth.setStatus("current")


class _RuijieDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):
    """Custom type ruijieDot1xAuthObjectsReAuthEnable based on EnabledStatus"""
    defaultValue = 2


_RuijieDot1xAuthObjectsReAuthEnable_Type.__name__ = "EnabledStatus"
_RuijieDot1xAuthObjectsReAuthEnable_Object = MibScalar
ruijieDot1xAuthObjectsReAuthEnable = _RuijieDot1xAuthObjectsReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 9),
    _RuijieDot1xAuthObjectsReAuthEnable_Type()
)
ruijieDot1xAuthObjectsReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsReAuthEnable.setStatus("current")
_RuijieDot1xAuthObjectsConfigTable_Object = MibTable
ruijieDot1xAuthObjectsConfigTable = _RuijieDot1xAuthObjectsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsConfigTable.setStatus("current")
_RuijieDot1xAuthObjectsConfigEntry_Object = MibTableRow
ruijieDot1xAuthObjectsConfigEntry = _RuijieDot1xAuthObjectsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1)
)
ruijieDot1xAuthObjectsConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsConfigFdbId"),
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsConfigAddr"),
)
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsConfigEntry.setStatus("current")
_RuijieDot1xAuthObjectsConfigFdbId_Type = Unsigned32
_RuijieDot1xAuthObjectsConfigFdbId_Object = MibTableColumn
ruijieDot1xAuthObjectsConfigFdbId = _RuijieDot1xAuthObjectsConfigFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 1),
    _RuijieDot1xAuthObjectsConfigFdbId_Type()
)
ruijieDot1xAuthObjectsConfigFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsConfigFdbId.setStatus("current")
_RuijieDot1xAuthObjectsConfigAddr_Type = MacAddress
_RuijieDot1xAuthObjectsConfigAddr_Object = MibTableColumn
ruijieDot1xAuthObjectsConfigAddr = _RuijieDot1xAuthObjectsConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 2),
    _RuijieDot1xAuthObjectsConfigAddr_Type()
)
ruijieDot1xAuthObjectsConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsConfigAddr.setStatus("current")


class _RuijieDot1xAuthObjectsPaeState_Type(Integer32):
    """Custom type ruijieDot1xAuthObjectsPaeState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_RuijieDot1xAuthObjectsPaeState_Type.__name__ = "Integer32"
_RuijieDot1xAuthObjectsPaeState_Object = MibTableColumn
ruijieDot1xAuthObjectsPaeState = _RuijieDot1xAuthObjectsPaeState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 3),
    _RuijieDot1xAuthObjectsPaeState_Type()
)
ruijieDot1xAuthObjectsPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsPaeState.setStatus("current")


class _RuijieDot1xAuthObjectsBackendAuthState_Type(Integer32):
    """Custom type ruijieDot1xAuthObjectsBackendAuthState based on Integer32"""
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
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_RuijieDot1xAuthObjectsBackendAuthState_Type.__name__ = "Integer32"
_RuijieDot1xAuthObjectsBackendAuthState_Object = MibTableColumn
ruijieDot1xAuthObjectsBackendAuthState = _RuijieDot1xAuthObjectsBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 4),
    _RuijieDot1xAuthObjectsBackendAuthState_Type()
)
ruijieDot1xAuthObjectsBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsBackendAuthState.setStatus("current")


class _RuijieDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):
    """Custom type ruijieDot1xAuthObjectsAuthControlledPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_RuijieDot1xAuthObjectsAuthControlledPortStatus_Type.__name__ = "Integer32"
_RuijieDot1xAuthObjectsAuthControlledPortStatus_Object = MibTableColumn
ruijieDot1xAuthObjectsAuthControlledPortStatus = _RuijieDot1xAuthObjectsAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 5),
    _RuijieDot1xAuthObjectsAuthControlledPortStatus_Type()
)
ruijieDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsAuthControlledPortStatus.setStatus("current")
_RuijieDot1xAuthObjectsKeyTxEnabled_Type = TruthValue
_RuijieDot1xAuthObjectsKeyTxEnabled_Object = MibTableColumn
ruijieDot1xAuthObjectsKeyTxEnabled = _RuijieDot1xAuthObjectsKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 6),
    _RuijieDot1xAuthObjectsKeyTxEnabled_Type()
)
ruijieDot1xAuthObjectsKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsKeyTxEnabled.setStatus("current")
_RuijieDot1xAuthObjectsIfIndex_Type = IfIndex
_RuijieDot1xAuthObjectsIfIndex_Object = MibTableColumn
ruijieDot1xAuthObjectsIfIndex = _RuijieDot1xAuthObjectsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 10, 1, 7),
    _RuijieDot1xAuthObjectsIfIndex_Type()
)
ruijieDot1xAuthObjectsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsIfIndex.setStatus("current")
_RuijieDot1xAuthObjectsStatsTable_Object = MibTable
ruijieDot1xAuthObjectsStatsTable = _RuijieDot1xAuthObjectsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsStatsTable.setStatus("current")
_RuijieDot1xAuthStatsEntry_Object = MibTableRow
ruijieDot1xAuthStatsEntry = _RuijieDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1)
)
ruijieDot1xAuthStatsEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsStatsFdbId"),
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsStatsAddr"),
)
if mibBuilder.loadTexts:
    ruijieDot1xAuthStatsEntry.setStatus("current")
_RuijieDot1xAuthObjectsStatsFdbId_Type = Unsigned32
_RuijieDot1xAuthObjectsStatsFdbId_Object = MibTableColumn
ruijieDot1xAuthObjectsStatsFdbId = _RuijieDot1xAuthObjectsStatsFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 1),
    _RuijieDot1xAuthObjectsStatsFdbId_Type()
)
ruijieDot1xAuthObjectsStatsFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsStatsFdbId.setStatus("current")
_RuijieDot1xAuthObjectsStatsAddr_Type = MacAddress
_RuijieDot1xAuthObjectsStatsAddr_Object = MibTableColumn
ruijieDot1xAuthObjectsStatsAddr = _RuijieDot1xAuthObjectsStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 2),
    _RuijieDot1xAuthObjectsStatsAddr_Type()
)
ruijieDot1xAuthObjectsStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsStatsAddr.setStatus("current")
_RuijieDot1xAuthObjectsEapolFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapolFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolFramesRx = _RuijieDot1xAuthObjectsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 3),
    _RuijieDot1xAuthObjectsEapolFramesRx_Type()
)
ruijieDot1xAuthObjectsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapolFramesTx_Type = Counter32
_RuijieDot1xAuthObjectsEapolFramesTx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolFramesTx = _RuijieDot1xAuthObjectsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 4),
    _RuijieDot1xAuthObjectsEapolFramesTx_Type()
)
ruijieDot1xAuthObjectsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolFramesTx.setStatus("current")
_RuijieDot1xAuthObjectsEapolRuijieFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapolRuijieFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolRuijieFramesRx = _RuijieDot1xAuthObjectsEapolRuijieFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 5),
    _RuijieDot1xAuthObjectsEapolRuijieFramesRx_Type()
)
ruijieDot1xAuthObjectsEapolRuijieFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolRuijieFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapolLogoffFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapolLogoffFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolLogoffFramesRx = _RuijieDot1xAuthObjectsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 6),
    _RuijieDot1xAuthObjectsEapolLogoffFramesRx_Type()
)
ruijieDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolLogoffFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapolRespIdFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapolRespIdFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolRespIdFramesRx = _RuijieDot1xAuthObjectsEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 7),
    _RuijieDot1xAuthObjectsEapolRespIdFramesRx_Type()
)
ruijieDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolRespIdFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapolRespFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapolRespFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolRespFramesRx = _RuijieDot1xAuthObjectsEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 8),
    _RuijieDot1xAuthObjectsEapolRespFramesRx_Type()
)
ruijieDot1xAuthObjectsEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolRespFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapolReqIdFramesTx_Type = Counter32
_RuijieDot1xAuthObjectsEapolReqIdFramesTx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolReqIdFramesTx = _RuijieDot1xAuthObjectsEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 9),
    _RuijieDot1xAuthObjectsEapolReqIdFramesTx_Type()
)
ruijieDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolReqIdFramesTx.setStatus("current")
_RuijieDot1xAuthObjectsEapolReqFramesTx_Type = Counter32
_RuijieDot1xAuthObjectsEapolReqFramesTx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapolReqFramesTx = _RuijieDot1xAuthObjectsEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 10),
    _RuijieDot1xAuthObjectsEapolReqFramesTx_Type()
)
ruijieDot1xAuthObjectsEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapolReqFramesTx.setStatus("current")
_RuijieDot1xAuthObjectsInvalidEapolFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsInvalidEapolFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsInvalidEapolFramesRx = _RuijieDot1xAuthObjectsInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 11),
    _RuijieDot1xAuthObjectsInvalidEapolFramesRx_Type()
)
ruijieDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsInvalidEapolFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsEapLengthErrorFramesRx_Type = Counter32
_RuijieDot1xAuthObjectsEapLengthErrorFramesRx_Object = MibTableColumn
ruijieDot1xAuthObjectsEapLengthErrorFramesRx = _RuijieDot1xAuthObjectsEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 12),
    _RuijieDot1xAuthObjectsEapLengthErrorFramesRx_Type()
)
ruijieDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsEapLengthErrorFramesRx.setStatus("current")
_RuijieDot1xAuthObjectsLastEapolFrameVersion_Type = Unsigned32
_RuijieDot1xAuthObjectsLastEapolFrameVersion_Object = MibTableColumn
ruijieDot1xAuthObjectsLastEapolFrameVersion = _RuijieDot1xAuthObjectsLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 13),
    _RuijieDot1xAuthObjectsLastEapolFrameVersion_Type()
)
ruijieDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsLastEapolFrameVersion.setStatus("current")
_RuijieDot1xAuthObjectsLastEapolFrameSource_Type = MacAddress
_RuijieDot1xAuthObjectsLastEapolFrameSource_Object = MibTableColumn
ruijieDot1xAuthObjectsLastEapolFrameSource = _RuijieDot1xAuthObjectsLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 11, 1, 14),
    _RuijieDot1xAuthObjectsLastEapolFrameSource_Type()
)
ruijieDot1xAuthObjectsLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthObjectsLastEapolFrameSource.setStatus("current")
_RuijieDot1xCurrentUserNumber_Type = Counter32
_RuijieDot1xCurrentUserNumber_Object = MibScalar
ruijieDot1xCurrentUserNumber = _RuijieDot1xCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 12),
    _RuijieDot1xCurrentUserNumber_Type()
)
ruijieDot1xCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xCurrentUserNumber.setStatus("current")
_RuijieDot1xCurrentAuthenticatedUserNumber_Type = Counter32
_RuijieDot1xCurrentAuthenticatedUserNumber_Object = MibScalar
ruijieDot1xCurrentAuthenticatedUserNumber = _RuijieDot1xCurrentAuthenticatedUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 13),
    _RuijieDot1xCurrentAuthenticatedUserNumber_Type()
)
ruijieDot1xCurrentAuthenticatedUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xCurrentAuthenticatedUserNumber.setStatus("current")


class _RuijieDot1xAccountStatus_Type(EnabledStatus):
    """Custom type ruijieDot1xAccountStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieDot1xAccountStatus_Type.__name__ = "EnabledStatus"
_RuijieDot1xAccountStatus_Object = MibScalar
ruijieDot1xAccountStatus = _RuijieDot1xAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 14),
    _RuijieDot1xAccountStatus_Type()
)
ruijieDot1xAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAccountStatus.setStatus("current")
_RuijieAuthIfTable_Object = MibTable
ruijieAuthIfTable = _RuijieAuthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ruijieAuthIfTable.setStatus("current")
_RuijieAuthIfEntry_Object = MibTableRow
ruijieAuthIfEntry = _RuijieAuthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1)
)
ruijieAuthIfEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAuthIf"),
)
if mibBuilder.loadTexts:
    ruijieAuthIfEntry.setStatus("current")
_RuijieAuthIf_Type = IfIndex
_RuijieAuthIf_Object = MibTableColumn
ruijieAuthIf = _RuijieAuthIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1, 1),
    _RuijieAuthIf_Type()
)
ruijieAuthIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthIf.setStatus("current")


class _RuijieAuthIfStatus_Type(EnabledStatus):
    """Custom type ruijieAuthIfStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieAuthIfStatus_Type.__name__ = "EnabledStatus"
_RuijieAuthIfStatus_Object = MibTableColumn
ruijieAuthIfStatus = _RuijieAuthIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 15, 1, 2),
    _RuijieAuthIfStatus_Type()
)
ruijieAuthIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAuthIfStatus.setStatus("current")


class _RuijieAuthenticationMode_Type(Integer32):
    """Custom type ruijieAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eap", 1),
          ("chap", 2),
          ("pap", 3))
    )


_RuijieAuthenticationMode_Type.__name__ = "Integer32"
_RuijieAuthenticationMode_Object = MibScalar
ruijieAuthenticationMode = _RuijieAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 16),
    _RuijieAuthenticationMode_Type()
)
ruijieAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAuthenticationMode.setStatus("current")
_RuijieDot1xAccountUpdateStatus_Type = EnabledStatus
_RuijieDot1xAccountUpdateStatus_Object = MibScalar
ruijieDot1xAccountUpdateStatus = _RuijieDot1xAccountUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 17),
    _RuijieDot1xAccountUpdateStatus_Type()
)
ruijieDot1xAccountUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAccountUpdateStatus.setStatus("current")


class _RuijieDot1xAcctInterimInterval_Type(Unsigned32):
    """Custom type ruijieDot1xAcctInterimInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 31536000),
    )


_RuijieDot1xAcctInterimInterval_Type.__name__ = "Unsigned32"
_RuijieDot1xAcctInterimInterval_Object = MibScalar
ruijieDot1xAcctInterimInterval = _RuijieDot1xAcctInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 18),
    _RuijieDot1xAcctInterimInterval_Type()
)
ruijieDot1xAcctInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAcctInterimInterval.setStatus("current")
_RuijieDot1xEapolTagEnabled_Type = EnabledStatus
_RuijieDot1xEapolTagEnabled_Object = MibScalar
ruijieDot1xEapolTagEnabled = _RuijieDot1xEapolTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 19),
    _RuijieDot1xEapolTagEnabled_Type()
)
ruijieDot1xEapolTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xEapolTagEnabled.setStatus("current")
_RuijieDot1xIfUserMaxTable_Object = MibTable
ruijieDot1xIfUserMaxTable = _RuijieDot1xIfUserMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 20)
)
if mibBuilder.loadTexts:
    ruijieDot1xIfUserMaxTable.setStatus("current")
_RuijieDot1xIfUserMaxEntry_Object = MibTableRow
ruijieDot1xIfUserMaxEntry = _RuijieDot1xIfUserMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 20, 1)
)
ruijieDot1xIfUserMaxEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xIfUserMaxIndex"),
)
if mibBuilder.loadTexts:
    ruijieDot1xIfUserMaxEntry.setStatus("current")
_RuijieDot1xIfUserMaxIndex_Type = IfIndex
_RuijieDot1xIfUserMaxIndex_Object = MibTableColumn
ruijieDot1xIfUserMaxIndex = _RuijieDot1xIfUserMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 20, 1, 1),
    _RuijieDot1xIfUserMaxIndex_Type()
)
ruijieDot1xIfUserMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xIfUserMaxIndex.setStatus("current")


class _RuijieDot1xIfUserMaxNum_Type(Unsigned32):
    """Custom type ruijieDot1xIfUserMaxNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_RuijieDot1xIfUserMaxNum_Type.__name__ = "Unsigned32"
_RuijieDot1xIfUserMaxNum_Object = MibTableColumn
ruijieDot1xIfUserMaxNum = _RuijieDot1xIfUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 20, 1, 2),
    _RuijieDot1xIfUserMaxNum_Type()
)
ruijieDot1xIfUserMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xIfUserMaxNum.setStatus("current")


class _RuijieDot1xPseudoSrcmac_Type(EnabledStatus):
    """Custom type ruijieDot1xPseudoSrcmac based on EnabledStatus"""
    defaultValue = 1


_RuijieDot1xPseudoSrcmac_Type.__name__ = "EnabledStatus"
_RuijieDot1xPseudoSrcmac_Object = MibScalar
ruijieDot1xPseudoSrcmac = _RuijieDot1xPseudoSrcmac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 21),
    _RuijieDot1xPseudoSrcmac_Type()
)
ruijieDot1xPseudoSrcmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xPseudoSrcmac.setStatus("current")
_RuijieDot1xUserMIB_ObjectIdentity = ObjectIdentity
ruijieDot1xUserMIB = _RuijieDot1xUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22)
)
_RuijieDot1xUserTrapsObjects_ObjectIdentity = ObjectIdentity
ruijieDot1xUserTrapsObjects = _RuijieDot1xUserTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1)
)
_RuijieDot1xUserMac_Type = MacAddress
_RuijieDot1xUserMac_Object = MibScalar
ruijieDot1xUserMac = _RuijieDot1xUserMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 1),
    _RuijieDot1xUserMac_Type()
)
ruijieDot1xUserMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserMac.setStatus("current")
_RuijieDot1xUserName_Type = DisplayString
_RuijieDot1xUserName_Object = MibScalar
ruijieDot1xUserName = _RuijieDot1xUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 2),
    _RuijieDot1xUserName_Type()
)
ruijieDot1xUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserName.setStatus("current")
_RuijieDot1xUserIp_Type = IpAddress
_RuijieDot1xUserIp_Object = MibScalar
ruijieDot1xUserIp = _RuijieDot1xUserIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 3),
    _RuijieDot1xUserIp_Type()
)
ruijieDot1xUserIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserIp.setStatus("current")
_RuijieDot1xUserIpv6_Type = InetAddress
_RuijieDot1xUserIpv6_Object = MibScalar
ruijieDot1xUserIpv6 = _RuijieDot1xUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 4),
    _RuijieDot1xUserIpv6_Type()
)
ruijieDot1xUserIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserIpv6.setStatus("current")


class _RuijieDot1xUserWlanId_Type(Integer32):
    """Custom type ruijieDot1xUserWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieDot1xUserWlanId_Type.__name__ = "Integer32"
_RuijieDot1xUserWlanId_Object = MibScalar
ruijieDot1xUserWlanId = _RuijieDot1xUserWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 5),
    _RuijieDot1xUserWlanId_Type()
)
ruijieDot1xUserWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserWlanId.setStatus("current")


class _RuijieDot1xUserVlanId_Type(Integer32):
    """Custom type ruijieDot1xUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieDot1xUserVlanId_Type.__name__ = "Integer32"
_RuijieDot1xUserVlanId_Object = MibScalar
ruijieDot1xUserVlanId = _RuijieDot1xUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 6),
    _RuijieDot1xUserVlanId_Type()
)
ruijieDot1xUserVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserVlanId.setStatus("current")
_RuijieDot1xUserSsid_Type = DisplayString
_RuijieDot1xUserSsid_Object = MibScalar
ruijieDot1xUserSsid = _RuijieDot1xUserSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 7),
    _RuijieDot1xUserSsid_Type()
)
ruijieDot1xUserSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserSsid.setStatus("current")
_RuijieDot1xUserApMac_Type = MacAddress
_RuijieDot1xUserApMac_Object = MibScalar
ruijieDot1xUserApMac = _RuijieDot1xUserApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 8),
    _RuijieDot1xUserApMac_Type()
)
ruijieDot1xUserApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserApMac.setStatus("current")
_RuijieDot1xUserTerminalType_Type = DisplayString
_RuijieDot1xUserTerminalType_Object = MibScalar
ruijieDot1xUserTerminalType = _RuijieDot1xUserTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 9),
    _RuijieDot1xUserTerminalType_Type()
)
ruijieDot1xUserTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserTerminalType.setStatus("current")


class _RuijieDot1xUserOperType_Type(Integer32):
    """Custom type ruijieDot1xUserOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("authenfail", 3))
    )


_RuijieDot1xUserOperType_Type.__name__ = "Integer32"
_RuijieDot1xUserOperType_Object = MibScalar
ruijieDot1xUserOperType = _RuijieDot1xUserOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 10),
    _RuijieDot1xUserOperType_Type()
)
ruijieDot1xUserOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserOperType.setStatus("current")
_RuijieDot1xUserTerminateCause_Type = Integer32
_RuijieDot1xUserTerminateCause_Object = MibScalar
ruijieDot1xUserTerminateCause = _RuijieDot1xUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 11),
    _RuijieDot1xUserTerminateCause_Type()
)
ruijieDot1xUserTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserTerminateCause.setStatus("current")
_RuijieDot1xUserReplyMessage_Type = DisplayString
_RuijieDot1xUserReplyMessage_Object = MibScalar
ruijieDot1xUserReplyMessage = _RuijieDot1xUserReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 12),
    _RuijieDot1xUserReplyMessage_Type()
)
ruijieDot1xUserReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserReplyMessage.setStatus("current")


class _RuijieDot1xUserIfIndex_Type(Integer32):
    """Custom type ruijieDot1xUserIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieDot1xUserIfIndex_Type.__name__ = "Integer32"
_RuijieDot1xUserIfIndex_Object = MibScalar
ruijieDot1xUserIfIndex = _RuijieDot1xUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 1, 13),
    _RuijieDot1xUserIfIndex_Type()
)
ruijieDot1xUserIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDot1xUserIfIndex.setStatus("current")
_RuijieDot1xUserTraps_ObjectIdentity = ObjectIdentity
ruijieDot1xUserTraps = _RuijieDot1xUserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 2)
)
_RuijieDot1xOnlineUserTable_Object = MibTable
ruijieDot1xOnlineUserTable = _RuijieDot1xOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserTable.setStatus("current")
_RuijieDot1xOnlineUserEntry_Object = MibTableRow
ruijieDot1xOnlineUserEntry = _RuijieDot1xOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1)
)
ruijieDot1xOnlineUserEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieDot1xOnlineUserID"),
)
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserEntry.setStatus("current")
_RuijieDot1xOnlineUserID_Type = Integer32
_RuijieDot1xOnlineUserID_Object = MibTableColumn
ruijieDot1xOnlineUserID = _RuijieDot1xOnlineUserID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 1),
    _RuijieDot1xOnlineUserID_Type()
)
ruijieDot1xOnlineUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserID.setStatus("current")
_RuijieDot1xOnlineUserName_Type = DisplayString
_RuijieDot1xOnlineUserName_Object = MibTableColumn
ruijieDot1xOnlineUserName = _RuijieDot1xOnlineUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 2),
    _RuijieDot1xOnlineUserName_Type()
)
ruijieDot1xOnlineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserName.setStatus("current")
_RuijieDot1xOnlineUserMacAddr_Type = MacAddress
_RuijieDot1xOnlineUserMacAddr_Object = MibTableColumn
ruijieDot1xOnlineUserMacAddr = _RuijieDot1xOnlineUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 3),
    _RuijieDot1xOnlineUserMacAddr_Type()
)
ruijieDot1xOnlineUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserMacAddr.setStatus("current")
_RuijieDot1xOnlineUserIfIndex_Type = Integer32
_RuijieDot1xOnlineUserIfIndex_Object = MibTableColumn
ruijieDot1xOnlineUserIfIndex = _RuijieDot1xOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 4),
    _RuijieDot1xOnlineUserIfIndex_Type()
)
ruijieDot1xOnlineUserIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserIfIndex.setStatus("current")
_RuijieDot1xOnlineUserVlanId_Type = Integer32
_RuijieDot1xOnlineUserVlanId_Object = MibTableColumn
ruijieDot1xOnlineUserVlanId = _RuijieDot1xOnlineUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 5),
    _RuijieDot1xOnlineUserVlanId_Type()
)
ruijieDot1xOnlineUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserVlanId.setStatus("current")
_RuijieDot1xOnlineUserIp_Type = IpAddress
_RuijieDot1xOnlineUserIp_Object = MibTableColumn
ruijieDot1xOnlineUserIp = _RuijieDot1xOnlineUserIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 6),
    _RuijieDot1xOnlineUserIp_Type()
)
ruijieDot1xOnlineUserIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserIp.setStatus("current")
_RuijieDot1xOnlineUserIpv6_Type = InetAddress
_RuijieDot1xOnlineUserIpv6_Object = MibTableColumn
ruijieDot1xOnlineUserIpv6 = _RuijieDot1xOnlineUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 7),
    _RuijieDot1xOnlineUserIpv6_Type()
)
ruijieDot1xOnlineUserIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xOnlineUserIpv6.setStatus("current")
_RuijieDot1xAbnormalOfflineUserCount_Type = Counter64
_RuijieDot1xAbnormalOfflineUserCount_Object = MibScalar
ruijieDot1xAbnormalOfflineUserCount = _RuijieDot1xAbnormalOfflineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 23),
    _RuijieDot1xAbnormalOfflineUserCount_Type()
)
ruijieDot1xAbnormalOfflineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAbnormalOfflineUserCount.setStatus("current")
_RuijieDot1xTotalAuthUserCount_Type = Counter64
_RuijieDot1xTotalAuthUserCount_Object = MibScalar
ruijieDot1xTotalAuthUserCount = _RuijieDot1xTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 24),
    _RuijieDot1xTotalAuthUserCount_Type()
)
ruijieDot1xTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xTotalAuthUserCount.setStatus("current")
_RuijieDot1xAuthSuccUserCount_Type = Counter64
_RuijieDot1xAuthSuccUserCount_Object = MibScalar
ruijieDot1xAuthSuccUserCount = _RuijieDot1xAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 25),
    _RuijieDot1xAuthSuccUserCount_Type()
)
ruijieDot1xAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthSuccUserCount.setStatus("current")
_RuijieDot1xAuthFailUserCount_Type = Counter64
_RuijieDot1xAuthFailUserCount_Object = MibScalar
ruijieDot1xAuthFailUserCount = _RuijieDot1xAuthFailUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 26),
    _RuijieDot1xAuthFailUserCount_Type()
)
ruijieDot1xAuthFailUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot1xAuthFailUserCount.setStatus("current")
_RuijieAAAServerObjects_ObjectIdentity = ObjectIdentity
ruijieAAAServerObjects = _RuijieAAAServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2)
)


class _RuijieAAAServerAuthPort_Type(Integer32):
    """Custom type ruijieAAAServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAServerAuthPort_Type.__name__ = "Integer32"
_RuijieAAAServerAuthPort_Object = MibScalar
ruijieAAAServerAuthPort = _RuijieAAAServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 2),
    _RuijieAAAServerAuthPort_Type()
)
ruijieAAAServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAAAServerAuthPort.setStatus("current")


class _RuijieAAAServerAcctPort_Type(Integer32):
    """Custom type ruijieAAAServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAServerAcctPort_Type.__name__ = "Integer32"
_RuijieAAAServerAcctPort_Object = MibScalar
ruijieAAAServerAcctPort = _RuijieAAAServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 3),
    _RuijieAAAServerAcctPort_Type()
)
ruijieAAAServerAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAAAServerAcctPort.setStatus("current")


class _RuijieAAAServerRadiusKeyStr_Type(DisplayString):
    """Custom type ruijieAAAServerRadiusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAAServerRadiusKeyStr_Type.__name__ = "DisplayString"
_RuijieAAAServerRadiusKeyStr_Object = MibScalar
ruijieAAAServerRadiusKeyStr = _RuijieAAAServerRadiusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 4),
    _RuijieAAAServerRadiusKeyStr_Type()
)
ruijieAAAServerRadiusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAAAServerRadiusKeyStr.setStatus("current")


class _RuijieAAAServerTacplusKeyStr_Type(DisplayString):
    """Custom type ruijieAAAServerTacplusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAAServerTacplusKeyStr_Type.__name__ = "DisplayString"
_RuijieAAAServerTacplusKeyStr_Object = MibScalar
ruijieAAAServerTacplusKeyStr = _RuijieAAAServerTacplusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 8),
    _RuijieAAAServerTacplusKeyStr_Type()
)
ruijieAAAServerTacplusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAAAServerTacplusKeyStr.setStatus("current")
_RuijieAAAServerConfigTable_Object = MibTable
ruijieAAAServerConfigTable = _RuijieAAAServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ruijieAAAServerConfigTable.setStatus("current")
_RuijieAAAServerConfigEntry_Object = MibTableRow
ruijieAAAServerConfigEntry = _RuijieAAAServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1)
)
ruijieAAAServerConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAAServerConfigProtocol"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAAServerConfigIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAAServerConfigEntry.setStatus("current")


class _RuijieAAAServerConfigProtocol_Type(Integer32):
    """Custom type ruijieAAAServerConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacplus", 2))
    )


_RuijieAAAServerConfigProtocol_Type.__name__ = "Integer32"
_RuijieAAAServerConfigProtocol_Object = MibTableColumn
ruijieAAAServerConfigProtocol = _RuijieAAAServerConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 1),
    _RuijieAAAServerConfigProtocol_Type()
)
ruijieAAAServerConfigProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigProtocol.setStatus("current")


class _RuijieAAAServerConfigIndex_Type(Unsigned32):
    """Custom type ruijieAAAServerConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerConfigIndex_Type.__name__ = "Unsigned32"
_RuijieAAAServerConfigIndex_Object = MibTableColumn
ruijieAAAServerConfigIndex = _RuijieAAAServerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 2),
    _RuijieAAAServerConfigIndex_Type()
)
ruijieAAAServerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigIndex.setStatus("current")
_RuijieAAAServerConfigAddressType_Type = InetAddressType
_RuijieAAAServerConfigAddressType_Object = MibTableColumn
ruijieAAAServerConfigAddressType = _RuijieAAAServerConfigAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 3),
    _RuijieAAAServerConfigAddressType_Type()
)
ruijieAAAServerConfigAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigAddressType.setStatus("current")
_RuijieAAAServerConfigAddress_Type = InetAddress
_RuijieAAAServerConfigAddress_Object = MibTableColumn
ruijieAAAServerConfigAddress = _RuijieAAAServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 4),
    _RuijieAAAServerConfigAddress_Type()
)
ruijieAAAServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigAddress.setStatus("current")


class _RuijieAAAServerConfigAuthPort_Type(Integer32):
    """Custom type ruijieAAAServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAServerConfigAuthPort_Type.__name__ = "Integer32"
_RuijieAAAServerConfigAuthPort_Object = MibTableColumn
ruijieAAAServerConfigAuthPort = _RuijieAAAServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 5),
    _RuijieAAAServerConfigAuthPort_Type()
)
ruijieAAAServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigAuthPort.setStatus("current")


class _RuijieAAAServerConfigAcctPort_Type(Integer32):
    """Custom type ruijieAAAServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAServerConfigAcctPort_Type.__name__ = "Integer32"
_RuijieAAAServerConfigAcctPort_Object = MibTableColumn
ruijieAAAServerConfigAcctPort = _RuijieAAAServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 6),
    _RuijieAAAServerConfigAcctPort_Type()
)
ruijieAAAServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigAcctPort.setStatus("current")


class _RuijieAAAServerConfigKeyStr_Type(DisplayString):
    """Custom type ruijieAAAServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAAServerConfigKeyStr_Type.__name__ = "DisplayString"
_RuijieAAAServerConfigKeyStr_Object = MibTableColumn
ruijieAAAServerConfigKeyStr = _RuijieAAAServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 7),
    _RuijieAAAServerConfigKeyStr_Type()
)
ruijieAAAServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigKeyStr.setStatus("current")
_RuijieAAAServerConfigRowStatus_Type = RowStatus
_RuijieAAAServerConfigRowStatus_Object = MibTableColumn
ruijieAAAServerConfigRowStatus = _RuijieAAAServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 9, 1, 8),
    _RuijieAAAServerConfigRowStatus_Type()
)
ruijieAAAServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAServerConfigRowStatus.setStatus("current")
_RuijieAAARadiusGroupTable_Object = MibTable
ruijieAAARadiusGroupTable = _RuijieAAARadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 10)
)
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupTable.setStatus("current")
_RuijieAAARadiusGroupEntry_Object = MibTableRow
ruijieAAARadiusGroupEntry = _RuijieAAARadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 10, 1)
)
ruijieAAARadiusGroupEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAARadiusGroupName"),
)
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupEntry.setStatus("current")


class _RuijieAAARadiusGroupName_Type(DisplayString):
    """Custom type ruijieAAARadiusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAAARadiusGroupName_Type.__name__ = "DisplayString"
_RuijieAAARadiusGroupName_Object = MibTableColumn
ruijieAAARadiusGroupName = _RuijieAAARadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 10, 1, 1),
    _RuijieAAARadiusGroupName_Type()
)
ruijieAAARadiusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupName.setStatus("current")


class _RuijieAAARadiusGroupVrf_Type(DisplayString):
    """Custom type ruijieAAARadiusGroupVrf based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RuijieAAARadiusGroupVrf_Type.__name__ = "DisplayString"
_RuijieAAARadiusGroupVrf_Object = MibTableColumn
ruijieAAARadiusGroupVrf = _RuijieAAARadiusGroupVrf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 10, 1, 2),
    _RuijieAAARadiusGroupVrf_Type()
)
ruijieAAARadiusGroupVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupVrf.setStatus("current")
_RuijieAAARadiusGroupRowStatus_Type = RowStatus
_RuijieAAARadiusGroupRowStatus_Object = MibTableColumn
ruijieAAARadiusGroupRowStatus = _RuijieAAARadiusGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 10, 1, 3),
    _RuijieAAARadiusGroupRowStatus_Type()
)
ruijieAAARadiusGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupRowStatus.setStatus("current")
_RuijieAAARadiusGroupServerTable_Object = MibTable
ruijieAAARadiusGroupServerTable = _RuijieAAARadiusGroupServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11)
)
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerTable.setStatus("current")
_RuijieAAARadiusGroupServerEntry_Object = MibTableRow
ruijieAAARadiusGroupServerEntry = _RuijieAAARadiusGroupServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1)
)
ruijieAAARadiusGroupServerEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAARadiusGroupName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerEntry.setStatus("current")


class _RuijieAAARadiusGroupServerIndex_Type(Unsigned32):
    """Custom type ruijieAAARadiusGroupServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAARadiusGroupServerIndex_Type.__name__ = "Unsigned32"
_RuijieAAARadiusGroupServerIndex_Object = MibTableColumn
ruijieAAARadiusGroupServerIndex = _RuijieAAARadiusGroupServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 1),
    _RuijieAAARadiusGroupServerIndex_Type()
)
ruijieAAARadiusGroupServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerIndex.setStatus("current")
_RuijieAAARadiusGroupServerAddressType_Type = InetAddressType
_RuijieAAARadiusGroupServerAddressType_Object = MibTableColumn
ruijieAAARadiusGroupServerAddressType = _RuijieAAARadiusGroupServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 2),
    _RuijieAAARadiusGroupServerAddressType_Type()
)
ruijieAAARadiusGroupServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerAddressType.setStatus("current")
_RuijieAAARadiusGroupServerAddress_Type = InetAddress
_RuijieAAARadiusGroupServerAddress_Object = MibTableColumn
ruijieAAARadiusGroupServerAddress = _RuijieAAARadiusGroupServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 3),
    _RuijieAAARadiusGroupServerAddress_Type()
)
ruijieAAARadiusGroupServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerAddress.setStatus("current")


class _RuijieAAARadiusGroupServerAuthPort_Type(Integer32):
    """Custom type ruijieAAARadiusGroupServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAARadiusGroupServerAuthPort_Type.__name__ = "Integer32"
_RuijieAAARadiusGroupServerAuthPort_Object = MibTableColumn
ruijieAAARadiusGroupServerAuthPort = _RuijieAAARadiusGroupServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 4),
    _RuijieAAARadiusGroupServerAuthPort_Type()
)
ruijieAAARadiusGroupServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerAuthPort.setStatus("current")


class _RuijieAAARadiusGroupServerAcctPort_Type(Integer32):
    """Custom type ruijieAAARadiusGroupServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAARadiusGroupServerAcctPort_Type.__name__ = "Integer32"
_RuijieAAARadiusGroupServerAcctPort_Object = MibTableColumn
ruijieAAARadiusGroupServerAcctPort = _RuijieAAARadiusGroupServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 5),
    _RuijieAAARadiusGroupServerAcctPort_Type()
)
ruijieAAARadiusGroupServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerAcctPort.setStatus("current")
_RuijieAAARadiusGroupServerRowStatus_Type = RowStatus
_RuijieAAARadiusGroupServerRowStatus_Object = MibTableColumn
ruijieAAARadiusGroupServerRowStatus = _RuijieAAARadiusGroupServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 11, 1, 6),
    _RuijieAAARadiusGroupServerRowStatus_Type()
)
ruijieAAARadiusGroupServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAARadiusGroupServerRowStatus.setStatus("current")


class _RuijieAAAServerTotalOnlineCount_Type(Integer32):
    """Custom type ruijieAAAServerTotalOnlineCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerTotalOnlineCount_Type.__name__ = "Integer32"
_RuijieAAAServerTotalOnlineCount_Object = MibScalar
ruijieAAAServerTotalOnlineCount = _RuijieAAAServerTotalOnlineCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 12),
    _RuijieAAAServerTotalOnlineCount_Type()
)
ruijieAAAServerTotalOnlineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerTotalOnlineCount.setStatus("current")


class _RuijieAAAServerAbnormalOffline_Type(Counter32):
    """Custom type ruijieAAAServerAbnormalOffline based on Counter32"""
    defaultValue = 0


_RuijieAAAServerAbnormalOffline_Type.__name__ = "Counter32"
_RuijieAAAServerAbnormalOffline_Object = MibScalar
ruijieAAAServerAbnormalOffline = _RuijieAAAServerAbnormalOffline_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 13),
    _RuijieAAAServerAbnormalOffline_Type()
)
ruijieAAAServerAbnormalOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerAbnormalOffline.setStatus("current")


class _RuijieAAAServerRadiusAuthReqCount_Type(Counter32):
    """Custom type ruijieAAAServerRadiusAuthReqCount based on Counter32"""
    defaultValue = 0


_RuijieAAAServerRadiusAuthReqCount_Type.__name__ = "Counter32"
_RuijieAAAServerRadiusAuthReqCount_Object = MibScalar
ruijieAAAServerRadiusAuthReqCount = _RuijieAAAServerRadiusAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 14),
    _RuijieAAAServerRadiusAuthReqCount_Type()
)
ruijieAAAServerRadiusAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerRadiusAuthReqCount.setStatus("current")


class _RuijieAAAServerRadiusAuthRespCount_Type(Counter32):
    """Custom type ruijieAAAServerRadiusAuthRespCount based on Counter32"""
    defaultValue = 0


_RuijieAAAServerRadiusAuthRespCount_Type.__name__ = "Counter32"
_RuijieAAAServerRadiusAuthRespCount_Object = MibScalar
ruijieAAAServerRadiusAuthRespCount = _RuijieAAAServerRadiusAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 15),
    _RuijieAAAServerRadiusAuthRespCount_Type()
)
ruijieAAAServerRadiusAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerRadiusAuthRespCount.setStatus("current")


class _RuijieAAAServerRadiusAuthSuccessCount_Type(Counter32):
    """Custom type ruijieAAAServerRadiusAuthSuccessCount based on Counter32"""
    defaultValue = 0


_RuijieAAAServerRadiusAuthSuccessCount_Type.__name__ = "Counter32"
_RuijieAAAServerRadiusAuthSuccessCount_Object = MibScalar
ruijieAAAServerRadiusAuthSuccessCount = _RuijieAAAServerRadiusAuthSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 16),
    _RuijieAAAServerRadiusAuthSuccessCount_Type()
)
ruijieAAAServerRadiusAuthSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerRadiusAuthSuccessCount.setStatus("current")


class _RuijieAAAServerCurrOnlineUserCount_Type(Integer32):
    """Custom type ruijieAAAServerCurrOnlineUserCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerCurrOnlineUserCount_Type.__name__ = "Integer32"
_RuijieAAAServerCurrOnlineUserCount_Object = MibScalar
ruijieAAAServerCurrOnlineUserCount = _RuijieAAAServerCurrOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 17),
    _RuijieAAAServerCurrOnlineUserCount_Type()
)
ruijieAAAServerCurrOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerCurrOnlineUserCount.setStatus("current")
_RuijieAAAMasterAuthenServerConfigTable_Object = MibTable
ruijieAAAMasterAuthenServerConfigTable = _RuijieAAAMasterAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18)
)
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigTable.setStatus("current")
_RuijieAAAMasterAuthenServerConfigEntry_Object = MibTableRow
ruijieAAAMasterAuthenServerConfigEntry = _RuijieAAAMasterAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1)
)
ruijieAAAMasterAuthenServerConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAAMasterAuthenServerConfigGrpName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAAMasterAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigEntry.setStatus("current")


class _RuijieAAAMasterAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type ruijieAAAMasterAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAAAMasterAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_RuijieAAAMasterAuthenServerConfigGrpName_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigGrpName = _RuijieAAAMasterAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 1),
    _RuijieAAAMasterAuthenServerConfigGrpName_Type()
)
ruijieAAAMasterAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigGrpName.setStatus("current")


class _RuijieAAAMasterAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type ruijieAAAMasterAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAMasterAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_RuijieAAAMasterAuthenServerConfigSrvIndex_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigSrvIndex = _RuijieAAAMasterAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 2),
    _RuijieAAAMasterAuthenServerConfigSrvIndex_Type()
)
ruijieAAAMasterAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigSrvIndex.setStatus("current")
_RuijieAAAMasterAuthenServerConfigAddress_Type = IpAddress
_RuijieAAAMasterAuthenServerConfigAddress_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigAddress = _RuijieAAAMasterAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 3),
    _RuijieAAAMasterAuthenServerConfigAddress_Type()
)
ruijieAAAMasterAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigAddress.setStatus("current")


class _RuijieAAAMasterAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type ruijieAAAMasterAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAMasterAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_RuijieAAAMasterAuthenServerConfigAuthPort_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigAuthPort = _RuijieAAAMasterAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 4),
    _RuijieAAAMasterAuthenServerConfigAuthPort_Type()
)
ruijieAAAMasterAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigAuthPort.setStatus("current")


class _RuijieAAAMasterAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type ruijieAAAMasterAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAMasterAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_RuijieAAAMasterAuthenServerConfigAcctPort_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigAcctPort = _RuijieAAAMasterAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 5),
    _RuijieAAAMasterAuthenServerConfigAcctPort_Type()
)
ruijieAAAMasterAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigAcctPort.setStatus("current")


class _RuijieAAAMasterAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type ruijieAAAMasterAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAAMasterAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_RuijieAAAMasterAuthenServerConfigKeyStr_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigKeyStr = _RuijieAAAMasterAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 6),
    _RuijieAAAMasterAuthenServerConfigKeyStr_Type()
)
ruijieAAAMasterAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigKeyStr.setStatus("current")
_RuijieAAAMasterAuthenServerConfigRowStatus_Type = RowStatus
_RuijieAAAMasterAuthenServerConfigRowStatus_Object = MibTableColumn
ruijieAAAMasterAuthenServerConfigRowStatus = _RuijieAAAMasterAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 18, 1, 7),
    _RuijieAAAMasterAuthenServerConfigRowStatus_Type()
)
ruijieAAAMasterAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAuthenServerConfigRowStatus.setStatus("current")
_RuijieAAABackAuthenServerConfigTable_Object = MibTable
ruijieAAABackAuthenServerConfigTable = _RuijieAAABackAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19)
)
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigTable.setStatus("current")
_RuijieAAABackAuthenServerConfigEntry_Object = MibTableRow
ruijieAAABackAuthenServerConfigEntry = _RuijieAAABackAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1)
)
ruijieAAABackAuthenServerConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAABackAuthenServerConfigGrpName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAABackAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigEntry.setStatus("current")


class _RuijieAAABackAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type ruijieAAABackAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAAABackAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_RuijieAAABackAuthenServerConfigGrpName_Object = MibTableColumn
ruijieAAABackAuthenServerConfigGrpName = _RuijieAAABackAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 1),
    _RuijieAAABackAuthenServerConfigGrpName_Type()
)
ruijieAAABackAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigGrpName.setStatus("current")


class _RuijieAAABackAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type ruijieAAABackAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAABackAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_RuijieAAABackAuthenServerConfigSrvIndex_Object = MibTableColumn
ruijieAAABackAuthenServerConfigSrvIndex = _RuijieAAABackAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 2),
    _RuijieAAABackAuthenServerConfigSrvIndex_Type()
)
ruijieAAABackAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigSrvIndex.setStatus("current")
_RuijieAAABackAuthenServerConfigAddress_Type = IpAddress
_RuijieAAABackAuthenServerConfigAddress_Object = MibTableColumn
ruijieAAABackAuthenServerConfigAddress = _RuijieAAABackAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 3),
    _RuijieAAABackAuthenServerConfigAddress_Type()
)
ruijieAAABackAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigAddress.setStatus("current")


class _RuijieAAABackAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type ruijieAAABackAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAABackAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_RuijieAAABackAuthenServerConfigAuthPort_Object = MibTableColumn
ruijieAAABackAuthenServerConfigAuthPort = _RuijieAAABackAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 4),
    _RuijieAAABackAuthenServerConfigAuthPort_Type()
)
ruijieAAABackAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigAuthPort.setStatus("current")


class _RuijieAAABackAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type ruijieAAABackAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAABackAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_RuijieAAABackAuthenServerConfigAcctPort_Object = MibTableColumn
ruijieAAABackAuthenServerConfigAcctPort = _RuijieAAABackAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 5),
    _RuijieAAABackAuthenServerConfigAcctPort_Type()
)
ruijieAAABackAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigAcctPort.setStatus("current")


class _RuijieAAABackAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type ruijieAAABackAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAABackAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_RuijieAAABackAuthenServerConfigKeyStr_Object = MibTableColumn
ruijieAAABackAuthenServerConfigKeyStr = _RuijieAAABackAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 6),
    _RuijieAAABackAuthenServerConfigKeyStr_Type()
)
ruijieAAABackAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigKeyStr.setStatus("current")
_RuijieAAABackAuthenServerConfigRowStatus_Type = RowStatus
_RuijieAAABackAuthenServerConfigRowStatus_Object = MibTableColumn
ruijieAAABackAuthenServerConfigRowStatus = _RuijieAAABackAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 19, 1, 7),
    _RuijieAAABackAuthenServerConfigRowStatus_Type()
)
ruijieAAABackAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAuthenServerConfigRowStatus.setStatus("current")
_RuijieAAAMasterAcctServerConfigTable_Object = MibTable
ruijieAAAMasterAcctServerConfigTable = _RuijieAAAMasterAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20)
)
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigTable.setStatus("current")
_RuijieAAAMasterAcctServerConfigEntry_Object = MibTableRow
ruijieAAAMasterAcctServerConfigEntry = _RuijieAAAMasterAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1)
)
ruijieAAAMasterAcctServerConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAAMasterAcctServerConfigGrpName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAAMasterAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigEntry.setStatus("current")


class _RuijieAAAMasterAcctServerConfigGrpName_Type(DisplayString):
    """Custom type ruijieAAAMasterAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAAAMasterAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_RuijieAAAMasterAcctServerConfigGrpName_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigGrpName = _RuijieAAAMasterAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 1),
    _RuijieAAAMasterAcctServerConfigGrpName_Type()
)
ruijieAAAMasterAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigGrpName.setStatus("current")


class _RuijieAAAMasterAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type ruijieAAAMasterAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAMasterAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_RuijieAAAMasterAcctServerConfigSrvIndex_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigSrvIndex = _RuijieAAAMasterAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 2),
    _RuijieAAAMasterAcctServerConfigSrvIndex_Type()
)
ruijieAAAMasterAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigSrvIndex.setStatus("current")
_RuijieAAAMasterAcctServerConfigAddress_Type = IpAddress
_RuijieAAAMasterAcctServerConfigAddress_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigAddress = _RuijieAAAMasterAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 3),
    _RuijieAAAMasterAcctServerConfigAddress_Type()
)
ruijieAAAMasterAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigAddress.setStatus("current")


class _RuijieAAAMasterAcctServerConfigAuthPort_Type(Integer32):
    """Custom type ruijieAAAMasterAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAMasterAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_RuijieAAAMasterAcctServerConfigAuthPort_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigAuthPort = _RuijieAAAMasterAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 4),
    _RuijieAAAMasterAcctServerConfigAuthPort_Type()
)
ruijieAAAMasterAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigAuthPort.setStatus("current")


class _RuijieAAAMasterAcctServerConfigAcctPort_Type(Integer32):
    """Custom type ruijieAAAMasterAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAAMasterAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_RuijieAAAMasterAcctServerConfigAcctPort_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigAcctPort = _RuijieAAAMasterAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 5),
    _RuijieAAAMasterAcctServerConfigAcctPort_Type()
)
ruijieAAAMasterAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigAcctPort.setStatus("current")


class _RuijieAAAMasterAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type ruijieAAAMasterAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAAMasterAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_RuijieAAAMasterAcctServerConfigKeyStr_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigKeyStr = _RuijieAAAMasterAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 6),
    _RuijieAAAMasterAcctServerConfigKeyStr_Type()
)
ruijieAAAMasterAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigKeyStr.setStatus("current")
_RuijieAAAMasterAcctServerConfigRowStatus_Type = RowStatus
_RuijieAAAMasterAcctServerConfigRowStatus_Object = MibTableColumn
ruijieAAAMasterAcctServerConfigRowStatus = _RuijieAAAMasterAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 20, 1, 7),
    _RuijieAAAMasterAcctServerConfigRowStatus_Type()
)
ruijieAAAMasterAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAAMasterAcctServerConfigRowStatus.setStatus("current")
_RuijieAAABackAcctServerConfigTable_Object = MibTable
ruijieAAABackAcctServerConfigTable = _RuijieAAABackAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21)
)
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigTable.setStatus("current")
_RuijieAAABackAcctServerConfigEntry_Object = MibTableRow
ruijieAAABackAcctServerConfigEntry = _RuijieAAABackAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1)
)
ruijieAAABackAcctServerConfigEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAABackAcctServerConfigGrpName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAAABackAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigEntry.setStatus("current")


class _RuijieAAABackAcctServerConfigGrpName_Type(DisplayString):
    """Custom type ruijieAAABackAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAAABackAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_RuijieAAABackAcctServerConfigGrpName_Object = MibTableColumn
ruijieAAABackAcctServerConfigGrpName = _RuijieAAABackAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 1),
    _RuijieAAABackAcctServerConfigGrpName_Type()
)
ruijieAAABackAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigGrpName.setStatus("current")


class _RuijieAAABackAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type ruijieAAABackAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAABackAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_RuijieAAABackAcctServerConfigSrvIndex_Object = MibTableColumn
ruijieAAABackAcctServerConfigSrvIndex = _RuijieAAABackAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 2),
    _RuijieAAABackAcctServerConfigSrvIndex_Type()
)
ruijieAAABackAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigSrvIndex.setStatus("current")
_RuijieAAABackAcctServerConfigAddress_Type = IpAddress
_RuijieAAABackAcctServerConfigAddress_Object = MibTableColumn
ruijieAAABackAcctServerConfigAddress = _RuijieAAABackAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 3),
    _RuijieAAABackAcctServerConfigAddress_Type()
)
ruijieAAABackAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigAddress.setStatus("current")


class _RuijieAAABackAcctServerConfigAuthPort_Type(Integer32):
    """Custom type ruijieAAABackAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAABackAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_RuijieAAABackAcctServerConfigAuthPort_Object = MibTableColumn
ruijieAAABackAcctServerConfigAuthPort = _RuijieAAABackAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 4),
    _RuijieAAABackAcctServerConfigAuthPort_Type()
)
ruijieAAABackAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigAuthPort.setStatus("current")


class _RuijieAAABackAcctServerConfigAcctPort_Type(Integer32):
    """Custom type ruijieAAABackAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieAAABackAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_RuijieAAABackAcctServerConfigAcctPort_Object = MibTableColumn
ruijieAAABackAcctServerConfigAcctPort = _RuijieAAABackAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 5),
    _RuijieAAABackAcctServerConfigAcctPort_Type()
)
ruijieAAABackAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigAcctPort.setStatus("current")


class _RuijieAAABackAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type ruijieAAABackAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAAABackAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_RuijieAAABackAcctServerConfigKeyStr_Object = MibTableColumn
ruijieAAABackAcctServerConfigKeyStr = _RuijieAAABackAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 6),
    _RuijieAAABackAcctServerConfigKeyStr_Type()
)
ruijieAAABackAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigKeyStr.setStatus("current")
_RuijieAAABackAcctServerConfigRowStatus_Type = RowStatus
_RuijieAAABackAcctServerConfigRowStatus_Object = MibTableColumn
ruijieAAABackAcctServerConfigRowStatus = _RuijieAAABackAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 21, 1, 7),
    _RuijieAAABackAcctServerConfigRowStatus_Type()
)
ruijieAAABackAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAAABackAcctServerConfigRowStatus.setStatus("current")


class _RuijieAAAServerTotalAuthUserCount_Type(Unsigned32):
    """Custom type ruijieAAAServerTotalAuthUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuijieAAAServerTotalAuthUserCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerTotalAuthUserCount_Object = MibScalar
ruijieAAAServerTotalAuthUserCount = _RuijieAAAServerTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 22),
    _RuijieAAAServerTotalAuthUserCount_Type()
)
ruijieAAAServerTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerTotalAuthUserCount.setStatus("current")


class _RuijieAAAServerAuthSuccUserCount_Type(Unsigned32):
    """Custom type ruijieAAAServerAuthSuccUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuijieAAAServerAuthSuccUserCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerAuthSuccUserCount_Object = MibScalar
ruijieAAAServerAuthSuccUserCount = _RuijieAAAServerAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 23),
    _RuijieAAAServerAuthSuccUserCount_Type()
)
ruijieAAAServerAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerAuthSuccUserCount.setStatus("current")


class _RuijieAAAServerDot1xOnlineUserCount_Type(Integer32):
    """Custom type ruijieAAAServerDot1xOnlineUserCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerDot1xOnlineUserCount_Type.__name__ = "Integer32"
_RuijieAAAServerDot1xOnlineUserCount_Object = MibScalar
ruijieAAAServerDot1xOnlineUserCount = _RuijieAAAServerDot1xOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 24),
    _RuijieAAAServerDot1xOnlineUserCount_Type()
)
ruijieAAAServerDot1xOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerDot1xOnlineUserCount.setStatus("current")


class _RuijieAAAServerMacOnlineUserCount_Type(Integer32):
    """Custom type ruijieAAAServerMacOnlineUserCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerMacOnlineUserCount_Type.__name__ = "Integer32"
_RuijieAAAServerMacOnlineUserCount_Object = MibScalar
ruijieAAAServerMacOnlineUserCount = _RuijieAAAServerMacOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 25),
    _RuijieAAAServerMacOnlineUserCount_Type()
)
ruijieAAAServerMacOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerMacOnlineUserCount.setStatus("current")


class _RuijieAAAServerWebOnlineUserCount_Type(Integer32):
    """Custom type ruijieAAAServerWebOnlineUserCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerWebOnlineUserCount_Type.__name__ = "Integer32"
_RuijieAAAServerWebOnlineUserCount_Object = MibScalar
ruijieAAAServerWebOnlineUserCount = _RuijieAAAServerWebOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 26),
    _RuijieAAAServerWebOnlineUserCount_Type()
)
ruijieAAAServerWebOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerWebOnlineUserCount.setStatus("current")


class _RuijieAAAServerTatalOnlineUserCount_Type(Integer32):
    """Custom type ruijieAAAServerTatalOnlineUserCount based on Integer32"""
    defaultValue = 0


_RuijieAAAServerTatalOnlineUserCount_Type.__name__ = "Integer32"
_RuijieAAAServerTatalOnlineUserCount_Object = MibScalar
ruijieAAAServerTatalOnlineUserCount = _RuijieAAAServerTatalOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 27),
    _RuijieAAAServerTatalOnlineUserCount_Type()
)
ruijieAAAServerTatalOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerTatalOnlineUserCount.setStatus("current")
_RuijieAAAServerIfOnlineUserTable_Object = MibTable
ruijieAAAServerIfOnlineUserTable = _RuijieAAAServerIfOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28)
)
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserTable.setStatus("current")
_RuijieAAAServerIfOnlineUserEntry_Object = MibTableRow
ruijieAAAServerIfOnlineUserEntry = _RuijieAAAServerIfOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1)
)
ruijieAAAServerIfOnlineUserEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAAAServerIfOnlineUserIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserEntry.setStatus("current")


class _RuijieAAAServerIfOnlineUserIfIndex_Type(Unsigned32):
    """Custom type ruijieAAAServerIfOnlineUserIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerIfOnlineUserIfIndex_Type.__name__ = "Unsigned32"
_RuijieAAAServerIfOnlineUserIfIndex_Object = MibTableColumn
ruijieAAAServerIfOnlineUserIfIndex = _RuijieAAAServerIfOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1, 1),
    _RuijieAAAServerIfOnlineUserIfIndex_Type()
)
ruijieAAAServerIfOnlineUserIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserIfIndex.setStatus("current")


class _RuijieAAAServerIfOnlineUserDot1xCount_Type(Unsigned32):
    """Custom type ruijieAAAServerIfOnlineUserDot1xCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerIfOnlineUserDot1xCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerIfOnlineUserDot1xCount_Object = MibTableColumn
ruijieAAAServerIfOnlineUserDot1xCount = _RuijieAAAServerIfOnlineUserDot1xCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1, 2),
    _RuijieAAAServerIfOnlineUserDot1xCount_Type()
)
ruijieAAAServerIfOnlineUserDot1xCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserDot1xCount.setStatus("current")


class _RuijieAAAServerIfOnlineUserWebCount_Type(Unsigned32):
    """Custom type ruijieAAAServerIfOnlineUserWebCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerIfOnlineUserWebCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerIfOnlineUserWebCount_Object = MibTableColumn
ruijieAAAServerIfOnlineUserWebCount = _RuijieAAAServerIfOnlineUserWebCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1, 3),
    _RuijieAAAServerIfOnlineUserWebCount_Type()
)
ruijieAAAServerIfOnlineUserWebCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserWebCount.setStatus("current")


class _RuijieAAAServerIfOnlineUserMacCount_Type(Unsigned32):
    """Custom type ruijieAAAServerIfOnlineUserMacCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerIfOnlineUserMacCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerIfOnlineUserMacCount_Object = MibTableColumn
ruijieAAAServerIfOnlineUserMacCount = _RuijieAAAServerIfOnlineUserMacCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1, 4),
    _RuijieAAAServerIfOnlineUserMacCount_Type()
)
ruijieAAAServerIfOnlineUserMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserMacCount.setStatus("current")


class _RuijieAAAServerIfOnlineUserTotalCount_Type(Unsigned32):
    """Custom type ruijieAAAServerIfOnlineUserTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieAAAServerIfOnlineUserTotalCount_Type.__name__ = "Unsigned32"
_RuijieAAAServerIfOnlineUserTotalCount_Object = MibTableColumn
ruijieAAAServerIfOnlineUserTotalCount = _RuijieAAAServerIfOnlineUserTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 2, 28, 1, 5),
    _RuijieAAAServerIfOnlineUserTotalCount_Type()
)
ruijieAAAServerIfOnlineUserTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAAAServerIfOnlineUserTotalCount.setStatus("current")
_RuijieAuthUserObjects_ObjectIdentity = ObjectIdentity
ruijieAuthUserObjects = _RuijieAuthUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3)
)
_RuijieAuthAddrTable_Object = MibTable
ruijieAuthAddrTable = _RuijieAuthAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieAuthAddrTable.setStatus("current")
_RuijieAuthAddrEntry_Object = MibTableRow
ruijieAuthAddrEntry = _RuijieAuthAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1)
)
ruijieAuthAddrEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAuthPort"),
    (0, "RUIJIE-AAA-MIB", "ruijieAuthMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieAuthAddrEntry.setStatus("current")
_RuijieAuthPort_Type = IfIndex
_RuijieAuthPort_Object = MibTableColumn
ruijieAuthPort = _RuijieAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 1),
    _RuijieAuthPort_Type()
)
ruijieAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthPort.setStatus("current")
_RuijieAuthMacAddress_Type = MacAddress
_RuijieAuthMacAddress_Object = MibTableColumn
ruijieAuthMacAddress = _RuijieAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 2),
    _RuijieAuthMacAddress_Type()
)
ruijieAuthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthMacAddress.setStatus("current")


class _RuijieAuthAddrStatus_Type(Integer32):
    """Custom type ruijieAuthAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RuijieAuthAddrStatus_Type.__name__ = "Integer32"
_RuijieAuthAddrStatus_Object = MibTableColumn
ruijieAuthAddrStatus = _RuijieAuthAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 1, 1, 3),
    _RuijieAuthAddrStatus_Type()
)
ruijieAuthAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAuthAddrStatus.setStatus("current")
_RuijieAuthUserTable_Object = MibTable
ruijieAuthUserTable = _RuijieAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieAuthUserTable.setStatus("current")
_RuijieAuthUserEntry_Object = MibTableRow
ruijieAuthUserEntry = _RuijieAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1)
)
ruijieAuthUserEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAuthUserFdbId"),
    (0, "RUIJIE-AAA-MIB", "ruijieAuthUserMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieAuthUserEntry.setStatus("current")
_RuijieAuthUserFdbId_Type = Unsigned32
_RuijieAuthUserFdbId_Object = MibTableColumn
ruijieAuthUserFdbId = _RuijieAuthUserFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 1),
    _RuijieAuthUserFdbId_Type()
)
ruijieAuthUserFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserFdbId.setStatus("current")
_RuijieAuthUserMacAddress_Type = MacAddress
_RuijieAuthUserMacAddress_Object = MibTableColumn
ruijieAuthUserMacAddress = _RuijieAuthUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 2),
    _RuijieAuthUserMacAddress_Type()
)
ruijieAuthUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMacAddress.setStatus("current")
_RuijieAuthUserName_Type = DisplayString
_RuijieAuthUserName_Object = MibTableColumn
ruijieAuthUserName = _RuijieAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 3),
    _RuijieAuthUserName_Type()
)
ruijieAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserName.setStatus("current")
_RuijieAuthUserSessionId_Type = DisplayString
_RuijieAuthUserSessionId_Object = MibTableColumn
ruijieAuthUserSessionId = _RuijieAuthUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 4),
    _RuijieAuthUserSessionId_Type()
)
ruijieAuthUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserSessionId.setStatus("current")
_RuijieAuthUserIpAddr_Type = IpAddress
_RuijieAuthUserIpAddr_Object = MibTableColumn
ruijieAuthUserIpAddr = _RuijieAuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 5),
    _RuijieAuthUserIpAddr_Type()
)
ruijieAuthUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserIpAddr.setStatus("current")
_RuijieAuthUserPort_Type = Integer32
_RuijieAuthUserPort_Object = MibTableColumn
ruijieAuthUserPort = _RuijieAuthUserPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 6),
    _RuijieAuthUserPort_Type()
)
ruijieAuthUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserPort.setStatus("current")
_RuijieAuthUserStatus_Type = ConfigStatus
_RuijieAuthUserStatus_Object = MibTableColumn
ruijieAuthUserStatus = _RuijieAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 2, 1, 7),
    _RuijieAuthUserStatus_Type()
)
ruijieAuthUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAuthUserStatus.setStatus("current")


class _RuijieAuthUserForVPNDel_Type(DisplayString):
    """Custom type ruijieAuthUserForVPNDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAuthUserForVPNDel_Type.__name__ = "DisplayString"
_RuijieAuthUserForVPNDel_Object = MibScalar
ruijieAuthUserForVPNDel = _RuijieAuthUserForVPNDel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 3),
    _RuijieAuthUserForVPNDel_Type()
)
ruijieAuthUserForVPNDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAuthUserForVPNDel.setStatus("current")
_RuijieOnlineUserTable_Object = MibTable
ruijieOnlineUserTable = _RuijieOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ruijieOnlineUserTable.setStatus("current")
_RuijieOnlineUserEntry_Object = MibTableRow
ruijieOnlineUserEntry = _RuijieOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1)
)
ruijieOnlineUserEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieOnlineUserSessionId"),
)
if mibBuilder.loadTexts:
    ruijieOnlineUserEntry.setStatus("current")
_RuijieOnlineUserSessionId_Type = DisplayString
_RuijieOnlineUserSessionId_Object = MibTableColumn
ruijieOnlineUserSessionId = _RuijieOnlineUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 1),
    _RuijieOnlineUserSessionId_Type()
)
ruijieOnlineUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserSessionId.setStatus("current")
_RuijieOnlineUserVid_Type = Unsigned32
_RuijieOnlineUserVid_Object = MibTableColumn
ruijieOnlineUserVid = _RuijieOnlineUserVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 2),
    _RuijieOnlineUserVid_Type()
)
ruijieOnlineUserVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserVid.setStatus("current")
_RuijieOnlineUserMacAddress_Type = MacAddress
_RuijieOnlineUserMacAddress_Object = MibTableColumn
ruijieOnlineUserMacAddress = _RuijieOnlineUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 3),
    _RuijieOnlineUserMacAddress_Type()
)
ruijieOnlineUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserMacAddress.setStatus("current")
_RuijieOnlineUserPort_Type = Integer32
_RuijieOnlineUserPort_Object = MibTableColumn
ruijieOnlineUserPort = _RuijieOnlineUserPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 4),
    _RuijieOnlineUserPort_Type()
)
ruijieOnlineUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserPort.setStatus("current")
_RuijieOnlineUserName_Type = DisplayString
_RuijieOnlineUserName_Object = MibTableColumn
ruijieOnlineUserName = _RuijieOnlineUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 5),
    _RuijieOnlineUserName_Type()
)
ruijieOnlineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserName.setStatus("current")
_RuijieOnlineUserIpAddr_Type = IpAddress
_RuijieOnlineUserIpAddr_Object = MibTableColumn
ruijieOnlineUserIpAddr = _RuijieOnlineUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 6),
    _RuijieOnlineUserIpAddr_Type()
)
ruijieOnlineUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOnlineUserIpAddr.setStatus("current")
_RuijieOnlineUserStatus_Type = ConfigStatus
_RuijieOnlineUserStatus_Object = MibTableColumn
ruijieOnlineUserStatus = _RuijieOnlineUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 4, 1, 7),
    _RuijieOnlineUserStatus_Type()
)
ruijieOnlineUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOnlineUserStatus.setStatus("current")
_RuijieAaaVersion_Type = Integer32
_RuijieAaaVersion_Object = MibScalar
ruijieAaaVersion = _RuijieAaaVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 3, 5),
    _RuijieAaaVersion_Type()
)
ruijieAaaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAaaVersion.setStatus("current")
_RuijieAuthModeObjects_ObjectIdentity = ObjectIdentity
ruijieAuthModeObjects = _RuijieAuthModeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 4)
)


class _RuijieIpAuthorizationMode_Type(Integer32):
    """Custom type ruijieIpAuthorizationMode based on Integer32"""
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
        *(("disable", 1),
          ("dhcpServer", 2),
          ("radiusServer", 3),
          ("supplicant", 4),
          ("mixed", 5))
    )


_RuijieIpAuthorizationMode_Type.__name__ = "Integer32"
_RuijieIpAuthorizationMode_Object = MibScalar
ruijieIpAuthorizationMode = _RuijieIpAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 4, 1),
    _RuijieIpAuthorizationMode_Type()
)
ruijieIpAuthorizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpAuthorizationMode.setStatus("current")
_RuijieClientProbeObjects_ObjectIdentity = ObjectIdentity
ruijieClientProbeObjects = _RuijieClientProbeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5)
)
_RuijieClientProbeEnabledStatus_Type = EnabledStatus
_RuijieClientProbeEnabledStatus_Object = MibScalar
ruijieClientProbeEnabledStatus = _RuijieClientProbeEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 1),
    _RuijieClientProbeEnabledStatus_Type()
)
ruijieClientProbeEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClientProbeEnabledStatus.setStatus("current")
_RuijieClientProbeHelloInterval_Type = Unsigned32
_RuijieClientProbeHelloInterval_Object = MibScalar
ruijieClientProbeHelloInterval = _RuijieClientProbeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 2),
    _RuijieClientProbeHelloInterval_Type()
)
ruijieClientProbeHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClientProbeHelloInterval.setStatus("current")
_RuijieClientProbeAliveInteval_Type = Unsigned32
_RuijieClientProbeAliveInteval_Object = MibScalar
ruijieClientProbeAliveInteval = _RuijieClientProbeAliveInteval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 5, 3),
    _RuijieClientProbeAliveInteval_Type()
)
ruijieClientProbeAliveInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClientProbeAliveInteval.setStatus("current")
_RuijieAAAConfigObjects_ObjectIdentity = ObjectIdentity
ruijieAAAConfigObjects = _RuijieAAAConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6)
)
_RuijieAuthenConfigObjects_ObjectIdentity = ObjectIdentity
ruijieAuthenConfigObjects = _RuijieAuthenConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1)
)
_RuijieAuthenMethodListTable_Object = MibTable
ruijieAuthenMethodListTable = _RuijieAuthenMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieAuthenMethodListTable.setStatus("current")
_RuijieAuthenMethodListEntry_Object = MibTableRow
ruijieAuthenMethodListEntry = _RuijieAuthenMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1)
)
ruijieAuthenMethodListEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAuthenMethodListType"),
    (0, "RUIJIE-AAA-MIB", "ruijieAuthenMethodListName"),
)
if mibBuilder.loadTexts:
    ruijieAuthenMethodListEntry.setStatus("current")


class _RuijieAuthenMethodListType_Type(Integer32):
    """Custom type ruijieAuthenMethodListType based on Integer32"""
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
        *(("login", 1),
          ("ppp", 2),
          ("dot1x", 3),
          ("enable", 4),
          ("web", 5),
          ("cmweb", 6),
          ("mt", 7),
          ("general", 8))
    )


_RuijieAuthenMethodListType_Type.__name__ = "Integer32"
_RuijieAuthenMethodListType_Object = MibTableColumn
ruijieAuthenMethodListType = _RuijieAuthenMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 1),
    _RuijieAuthenMethodListType_Type()
)
ruijieAuthenMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenMethodListType.setStatus("current")


class _RuijieAuthenMethodListName_Type(DisplayString):
    """Custom type ruijieAuthenMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAuthenMethodListName_Type.__name__ = "DisplayString"
_RuijieAuthenMethodListName_Object = MibTableColumn
ruijieAuthenMethodListName = _RuijieAuthenMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 2),
    _RuijieAuthenMethodListName_Type()
)
ruijieAuthenMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenMethodListName.setStatus("current")


class _RuijieAuthenMethodListString_Type(DisplayString):
    """Custom type ruijieAuthenMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAuthenMethodListString_Type.__name__ = "DisplayString"
_RuijieAuthenMethodListString_Object = MibTableColumn
ruijieAuthenMethodListString = _RuijieAuthenMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 3),
    _RuijieAuthenMethodListString_Type()
)
ruijieAuthenMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenMethodListString.setStatus("current")
_RuijieAuthenMethodListRowStatus_Type = RowStatus
_RuijieAuthenMethodListRowStatus_Object = MibTableColumn
ruijieAuthenMethodListRowStatus = _RuijieAuthenMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 4),
    _RuijieAuthenMethodListRowStatus_Type()
)
ruijieAuthenMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenMethodListRowStatus.setStatus("current")
_RuijieAuthorConfigObjects_ObjectIdentity = ObjectIdentity
ruijieAuthorConfigObjects = _RuijieAuthorConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2)
)
_RuijieAuthorMethodListTable_Object = MibTable
ruijieAuthorMethodListTable = _RuijieAuthorMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieAuthorMethodListTable.setStatus("current")
_RuijieAuthorMethodListEntry_Object = MibTableRow
ruijieAuthorMethodListEntry = _RuijieAuthorMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1)
)
ruijieAuthorMethodListEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAuthorMethodListType"),
    (0, "RUIJIE-AAA-MIB", "ruijieAuthorMethodListName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAuthorMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    ruijieAuthorMethodListEntry.setStatus("current")


class _RuijieAuthorMethodListType_Type(Integer32):
    """Custom type ruijieAuthorMethodListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("command", 2),
          ("network", 3))
    )


_RuijieAuthorMethodListType_Type.__name__ = "Integer32"
_RuijieAuthorMethodListType_Object = MibTableColumn
ruijieAuthorMethodListType = _RuijieAuthorMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 1),
    _RuijieAuthorMethodListType_Type()
)
ruijieAuthorMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthorMethodListType.setStatus("current")


class _RuijieAuthorMethodListName_Type(DisplayString):
    """Custom type ruijieAuthorMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAuthorMethodListName_Type.__name__ = "DisplayString"
_RuijieAuthorMethodListName_Object = MibTableColumn
ruijieAuthorMethodListName = _RuijieAuthorMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 2),
    _RuijieAuthorMethodListName_Type()
)
ruijieAuthorMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthorMethodListName.setStatus("current")


class _RuijieAuthorMethodListCmdLevel_Type(Integer32):
    """Custom type ruijieAuthorMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieAuthorMethodListCmdLevel_Type.__name__ = "Integer32"
_RuijieAuthorMethodListCmdLevel_Object = MibTableColumn
ruijieAuthorMethodListCmdLevel = _RuijieAuthorMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 3),
    _RuijieAuthorMethodListCmdLevel_Type()
)
ruijieAuthorMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthorMethodListCmdLevel.setStatus("current")


class _RuijieAuthorMethodListString_Type(DisplayString):
    """Custom type ruijieAuthorMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAuthorMethodListString_Type.__name__ = "DisplayString"
_RuijieAuthorMethodListString_Object = MibTableColumn
ruijieAuthorMethodListString = _RuijieAuthorMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 4),
    _RuijieAuthorMethodListString_Type()
)
ruijieAuthorMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthorMethodListString.setStatus("current")
_RuijieAuthorMethodListRowStatus_Type = RowStatus
_RuijieAuthorMethodListRowStatus_Object = MibTableColumn
ruijieAuthorMethodListRowStatus = _RuijieAuthorMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 5),
    _RuijieAuthorMethodListRowStatus_Type()
)
ruijieAuthorMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthorMethodListRowStatus.setStatus("current")
_RuijieAcctConfigObjects_ObjectIdentity = ObjectIdentity
ruijieAcctConfigObjects = _RuijieAcctConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3)
)
_RuijieAcctMethodListTable_Object = MibTable
ruijieAcctMethodListTable = _RuijieAcctMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieAcctMethodListTable.setStatus("current")
_RuijieAcctMethodListEntry_Object = MibTableRow
ruijieAcctMethodListEntry = _RuijieAcctMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1)
)
ruijieAcctMethodListEntry.setIndexNames(
    (0, "RUIJIE-AAA-MIB", "ruijieAcctMethodListType"),
    (0, "RUIJIE-AAA-MIB", "ruijieAcctMethodListName"),
    (0, "RUIJIE-AAA-MIB", "ruijieAcctMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    ruijieAcctMethodListEntry.setStatus("current")


class _RuijieAcctMethodListType_Type(Integer32):
    """Custom type ruijieAcctMethodListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("command", 2),
          ("network", 3))
    )


_RuijieAcctMethodListType_Type.__name__ = "Integer32"
_RuijieAcctMethodListType_Object = MibTableColumn
ruijieAcctMethodListType = _RuijieAcctMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 1),
    _RuijieAcctMethodListType_Type()
)
ruijieAcctMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcctMethodListType.setStatus("current")


class _RuijieAcctMethodListName_Type(DisplayString):
    """Custom type ruijieAcctMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieAcctMethodListName_Type.__name__ = "DisplayString"
_RuijieAcctMethodListName_Object = MibTableColumn
ruijieAcctMethodListName = _RuijieAcctMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 2),
    _RuijieAcctMethodListName_Type()
)
ruijieAcctMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcctMethodListName.setStatus("current")


class _RuijieAcctMethodListMode_Type(Integer32):
    """Custom type ruijieAcctMethodListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-stop", 1),
          ("stop-only", 2))
    )


_RuijieAcctMethodListMode_Type.__name__ = "Integer32"
_RuijieAcctMethodListMode_Object = MibTableColumn
ruijieAcctMethodListMode = _RuijieAcctMethodListMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 3),
    _RuijieAcctMethodListMode_Type()
)
ruijieAcctMethodListMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAcctMethodListMode.setStatus("current")


class _RuijieAcctMethodListCmdLevel_Type(Integer32):
    """Custom type ruijieAcctMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieAcctMethodListCmdLevel_Type.__name__ = "Integer32"
_RuijieAcctMethodListCmdLevel_Object = MibTableColumn
ruijieAcctMethodListCmdLevel = _RuijieAcctMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 4),
    _RuijieAcctMethodListCmdLevel_Type()
)
ruijieAcctMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcctMethodListCmdLevel.setStatus("current")


class _RuijieAcctMethodListString_Type(DisplayString):
    """Custom type ruijieAcctMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcctMethodListString_Type.__name__ = "DisplayString"
_RuijieAcctMethodListString_Object = MibTableColumn
ruijieAcctMethodListString = _RuijieAcctMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 5),
    _RuijieAcctMethodListString_Type()
)
ruijieAcctMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAcctMethodListString.setStatus("current")
_RuijieAcctMethodListRowStatus_Type = RowStatus
_RuijieAcctMethodListRowStatus_Object = MibTableColumn
ruijieAcctMethodListRowStatus = _RuijieAcctMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 6),
    _RuijieAcctMethodListRowStatus_Type()
)
ruijieAcctMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAcctMethodListRowStatus.setStatus("current")
_RuijieAAAUserApplyObjects_ObjectIdentity = ObjectIdentity
ruijieAAAUserApplyObjects = _RuijieAAAUserApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 7)
)
_RuijieAAADo1xApplyObjects_ObjectIdentity = ObjectIdentity
ruijieAAADo1xApplyObjects = _RuijieAAADo1xApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 7, 1)
)


class _RuijieDot1xAuthenMethodList_Type(DisplayString):
    """Custom type ruijieDot1xAuthenMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieDot1xAuthenMethodList_Type.__name__ = "DisplayString"
_RuijieDot1xAuthenMethodList_Object = MibScalar
ruijieDot1xAuthenMethodList = _RuijieDot1xAuthenMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 7, 1, 1),
    _RuijieDot1xAuthenMethodList_Type()
)
ruijieDot1xAuthenMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthenMethodList.setStatus("current")


class _RuijieDot1xAuthorMethodList_Type(DisplayString):
    """Custom type ruijieDot1xAuthorMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieDot1xAuthorMethodList_Type.__name__ = "DisplayString"
_RuijieDot1xAuthorMethodList_Object = MibScalar
ruijieDot1xAuthorMethodList = _RuijieDot1xAuthorMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 7, 1, 2),
    _RuijieDot1xAuthorMethodList_Type()
)
ruijieDot1xAuthorMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAuthorMethodList.setStatus("current")


class _RuijieDot1xAcctMethodList_Type(DisplayString):
    """Custom type ruijieDot1xAcctMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieDot1xAcctMethodList_Type.__name__ = "DisplayString"
_RuijieDot1xAcctMethodList_Object = MibScalar
ruijieDot1xAcctMethodList = _RuijieDot1xAcctMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 7, 1, 3),
    _RuijieDot1xAcctMethodList_Type()
)
ruijieDot1xAcctMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot1xAcctMethodList.setStatus("current")
_RuijieRdASObjects_ObjectIdentity = ObjectIdentity
ruijieRdASObjects = _RuijieRdASObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 8)
)
_RuijieRdASipInetAddreType_Type = InetAddressType
_RuijieRdASipInetAddreType_Object = MibScalar
ruijieRdASipInetAddreType = _RuijieRdASipInetAddreType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 8, 1),
    _RuijieRdASipInetAddreType_Type()
)
ruijieRdASipInetAddreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRdASipInetAddreType.setStatus("current")
_RuijieRdASipInsetAddres_Type = InetAddress
_RuijieRdASipInsetAddres_Object = MibScalar
ruijieRdASipInsetAddres = _RuijieRdASipInsetAddres_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 8, 2),
    _RuijieRdASipInsetAddres_Type()
)
ruijieRdASipInsetAddres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRdASipInsetAddres.setStatus("current")
_RuijieAAAMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAAAMIBConformance = _RuijieAAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2)
)
_RuijieAAAMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAAAMIBCompliances = _RuijieAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 1)
)
_RuijieAAAMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAAAMIBGroups = _RuijieAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2)
)

# Managed Objects groups

ruijieDot1xAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 1)
)
ruijieDot1xAuthMIBGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieDot1xAuthStatus"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsQuietPeriod"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsTxPeriod"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsSuppTimeout"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsServerTimeout"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsMaxReq"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsReAuthPeriod"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsReAuthEnable"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsConfigFdbId"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsConfigAddr"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsPaeState"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsBackendAuthState"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsAuthControlledPortStatus"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsKeyTxEnabled"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsIfIndex"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsStatsFdbId"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsStatsAddr"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolFramesTx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolRuijieFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolLogoffFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolRespIdFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolRespFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolReqIdFramesTx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapolReqFramesTx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsInvalidEapolFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsEapLengthErrorFramesRx"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsLastEapolFrameVersion"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsLastEapolFrameSource"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xCurrentUserNumber"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xCurrentAuthenticatedUserNumber"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthObjectsMaxReauth"),
        ("RUIJIE-AAA-MIB", "ruijieAuthIf"),
        ("RUIJIE-AAA-MIB", "ruijieAuthIfStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAuthenticationMode"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xPseudoSrcmac"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAbnormalOfflineUserCount"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xTotalAuthUserCount"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthSuccUserCount"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthFailUserCount"))
)
if mibBuilder.loadTexts:
    ruijieDot1xAuthMIBGroup.setStatus("current")

ruijieAAAServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 2)
)
ruijieAAAServerMIBGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieAAAServerAuthPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerAcctPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerRadiusKeyStr"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerTacplusKeyStr"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigAddressType"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigAddress"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigAuthPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigAcctPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigKeyStr"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieAAAServerMIBGroup.setStatus("current")

ruijieAuthAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 3)
)
ruijieAuthAddrMIBGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieAuthMacAddress"),
        ("RUIJIE-AAA-MIB", "ruijieAuthPort"),
        ("RUIJIE-AAA-MIB", "ruijieAuthAddrStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserFdbId"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserMacAddress"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserName"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserSessionId"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserIpAddr"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserPort"),
        ("RUIJIE-AAA-MIB", "ruijieAuthUserStatus"))
)
if mibBuilder.loadTexts:
    ruijieAuthAddrMIBGroup.setStatus("current")

ruijieAuthModeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 4)
)
ruijieAuthModeMIBGroup.setObjects(
    ("RUIJIE-AAA-MIB", "ruijieIpAuthorizationMode")
)
if mibBuilder.loadTexts:
    ruijieAuthModeMIBGroup.setStatus("current")

ruijieClientProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 5)
)
ruijieClientProbeGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieClientProbeEnabledStatus"),
        ("RUIJIE-AAA-MIB", "ruijieClientProbeHelloInterval"),
        ("RUIJIE-AAA-MIB", "ruijieClientProbeAliveInteval"))
)
if mibBuilder.loadTexts:
    ruijieClientProbeGroup.setStatus("current")

ruijieAAAConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 6)
)
ruijieAAAConfigMIBGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieAuthenMethodListType"),
        ("RUIJIE-AAA-MIB", "ruijieAuthenMethodListName"),
        ("RUIJIE-AAA-MIB", "ruijieAuthenMethodListString"),
        ("RUIJIE-AAA-MIB", "ruijieAuthenMethodListRowStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAuthorMethodListType"),
        ("RUIJIE-AAA-MIB", "ruijieAuthorMethodListName"),
        ("RUIJIE-AAA-MIB", "ruijieAuthorMethodListCmdLevel"),
        ("RUIJIE-AAA-MIB", "ruijieAuthorMethodListString"),
        ("RUIJIE-AAA-MIB", "ruijieAuthorMethodListRowStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListType"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListName"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListMode"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListCmdLevel"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListString"),
        ("RUIJIE-AAA-MIB", "ruijieAcctMethodListRowStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupName"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupVrf"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupRowStatus"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerAddressType"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerAddress"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerAuthPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerAcctPort"),
        ("RUIJIE-AAA-MIB", "ruijieAAARadiusGroupServerRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieAAAConfigMIBGroup.setStatus("current")

ruijieAAAUserApplyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 7)
)
ruijieAAAUserApplyMIBGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieDot1xAuthenMethodList"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAuthorMethodList"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xAcctMethodList"))
)
if mibBuilder.loadTexts:
    ruijieAAAUserApplyMIBGroup.setStatus("current")

ruijieRdASGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 2, 8)
)
ruijieRdASGroup.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieRdASipInetAddreType"),
        ("RUIJIE-AAA-MIB", "ruijieRdASipInsetAddres"))
)
if mibBuilder.loadTexts:
    ruijieRdASGroup.setStatus("current")


# Notification objects

ruijieRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 0, 1)
)
ruijieRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    ruijieRadiusAuthServerDownTrap.setStatus(
        "current"
    )

ruijieRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 0, 2)
)
ruijieRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    ruijieRadiusAccServerDownTrap.setStatus(
        "current"
    )

ruijieRadiusAuthServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 0, 3)
)
ruijieRadiusAuthServerRecoverTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    ruijieRadiusAuthServerRecoverTrap.setStatus(
        "current"
    )

ruijieRadiusAccServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 0, 4)
)
ruijieRadiusAccServerRecoverTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    ruijieRadiusAccServerRecoverTrap.setStatus(
        "current"
    )

ruijieDot1xUserMgmtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 2, 1)
)
ruijieDot1xUserMgmtTrap.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieDot1xUserMac"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserName"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIp"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIpv6"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserWlanId"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserVlanId"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserSsid"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserApMac"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserTerminalType"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserOperType"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserTerminateCause"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserReplyMessage"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIfIndex"))
)
if mibBuilder.loadTexts:
    ruijieDot1xUserMgmtTrap.setStatus(
        "current"
    )

ruijieDot1xWiredUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 1, 1, 22, 2, 2)
)
ruijieDot1xWiredUserTrap.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieDot1xUserMac"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserName"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIfIndex"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserVlanId"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIp"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserIpv6"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserOperType"),
        ("RUIJIE-AAA-MIB", "ruijieDot1xUserTerminateCause"))
)
if mibBuilder.loadTexts:
    ruijieDot1xWiredUserTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 19, 2, 1, 1)
)
ruijieAAAMIBCompliance.setObjects(
      *(("RUIJIE-AAA-MIB", "ruijieDot1xAuthMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieAAAServerMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieAuthAddrMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieAuthModeMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieAAAConfigMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieAAAUserApplyMIBGroup"),
        ("RUIJIE-AAA-MIB", "ruijieRdASGroup"),
        ("RUIJIE-AAA-MIB", "ruijieClientProbeGroup"))
)
if mibBuilder.loadTexts:
    ruijieAAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AAA-MIB",
    **{"ruijieAAAMIB": ruijieAAAMIB,
       "ruijieRadiusServerTrap": ruijieRadiusServerTrap,
       "ruijieRadiusAuthServerDownTrap": ruijieRadiusAuthServerDownTrap,
       "ruijieRadiusAccServerDownTrap": ruijieRadiusAccServerDownTrap,
       "ruijieRadiusAuthServerRecoverTrap": ruijieRadiusAuthServerRecoverTrap,
       "ruijieRadiusAccServerRecoverTrap": ruijieRadiusAccServerRecoverTrap,
       "ruijieAAAMIBObjects": ruijieAAAMIBObjects,
       "ruijieDot1xAuthObjects": ruijieDot1xAuthObjects,
       "ruijieDot1xAuthStatus": ruijieDot1xAuthStatus,
       "ruijieDot1xAuthObjectsQuietPeriod": ruijieDot1xAuthObjectsQuietPeriod,
       "ruijieDot1xAuthObjectsTxPeriod": ruijieDot1xAuthObjectsTxPeriod,
       "ruijieDot1xAuthObjectsSuppTimeout": ruijieDot1xAuthObjectsSuppTimeout,
       "ruijieDot1xAuthObjectsServerTimeout": ruijieDot1xAuthObjectsServerTimeout,
       "ruijieDot1xAuthObjectsMaxReq": ruijieDot1xAuthObjectsMaxReq,
       "ruijieDot1xAuthObjectsReAuthPeriod": ruijieDot1xAuthObjectsReAuthPeriod,
       "ruijieDot1xAuthObjectsMaxReauth": ruijieDot1xAuthObjectsMaxReauth,
       "ruijieDot1xAuthObjectsReAuthEnable": ruijieDot1xAuthObjectsReAuthEnable,
       "ruijieDot1xAuthObjectsConfigTable": ruijieDot1xAuthObjectsConfigTable,
       "ruijieDot1xAuthObjectsConfigEntry": ruijieDot1xAuthObjectsConfigEntry,
       "ruijieDot1xAuthObjectsConfigFdbId": ruijieDot1xAuthObjectsConfigFdbId,
       "ruijieDot1xAuthObjectsConfigAddr": ruijieDot1xAuthObjectsConfigAddr,
       "ruijieDot1xAuthObjectsPaeState": ruijieDot1xAuthObjectsPaeState,
       "ruijieDot1xAuthObjectsBackendAuthState": ruijieDot1xAuthObjectsBackendAuthState,
       "ruijieDot1xAuthObjectsAuthControlledPortStatus": ruijieDot1xAuthObjectsAuthControlledPortStatus,
       "ruijieDot1xAuthObjectsKeyTxEnabled": ruijieDot1xAuthObjectsKeyTxEnabled,
       "ruijieDot1xAuthObjectsIfIndex": ruijieDot1xAuthObjectsIfIndex,
       "ruijieDot1xAuthObjectsStatsTable": ruijieDot1xAuthObjectsStatsTable,
       "ruijieDot1xAuthStatsEntry": ruijieDot1xAuthStatsEntry,
       "ruijieDot1xAuthObjectsStatsFdbId": ruijieDot1xAuthObjectsStatsFdbId,
       "ruijieDot1xAuthObjectsStatsAddr": ruijieDot1xAuthObjectsStatsAddr,
       "ruijieDot1xAuthObjectsEapolFramesRx": ruijieDot1xAuthObjectsEapolFramesRx,
       "ruijieDot1xAuthObjectsEapolFramesTx": ruijieDot1xAuthObjectsEapolFramesTx,
       "ruijieDot1xAuthObjectsEapolRuijieFramesRx": ruijieDot1xAuthObjectsEapolRuijieFramesRx,
       "ruijieDot1xAuthObjectsEapolLogoffFramesRx": ruijieDot1xAuthObjectsEapolLogoffFramesRx,
       "ruijieDot1xAuthObjectsEapolRespIdFramesRx": ruijieDot1xAuthObjectsEapolRespIdFramesRx,
       "ruijieDot1xAuthObjectsEapolRespFramesRx": ruijieDot1xAuthObjectsEapolRespFramesRx,
       "ruijieDot1xAuthObjectsEapolReqIdFramesTx": ruijieDot1xAuthObjectsEapolReqIdFramesTx,
       "ruijieDot1xAuthObjectsEapolReqFramesTx": ruijieDot1xAuthObjectsEapolReqFramesTx,
       "ruijieDot1xAuthObjectsInvalidEapolFramesRx": ruijieDot1xAuthObjectsInvalidEapolFramesRx,
       "ruijieDot1xAuthObjectsEapLengthErrorFramesRx": ruijieDot1xAuthObjectsEapLengthErrorFramesRx,
       "ruijieDot1xAuthObjectsLastEapolFrameVersion": ruijieDot1xAuthObjectsLastEapolFrameVersion,
       "ruijieDot1xAuthObjectsLastEapolFrameSource": ruijieDot1xAuthObjectsLastEapolFrameSource,
       "ruijieDot1xCurrentUserNumber": ruijieDot1xCurrentUserNumber,
       "ruijieDot1xCurrentAuthenticatedUserNumber": ruijieDot1xCurrentAuthenticatedUserNumber,
       "ruijieDot1xAccountStatus": ruijieDot1xAccountStatus,
       "ruijieAuthIfTable": ruijieAuthIfTable,
       "ruijieAuthIfEntry": ruijieAuthIfEntry,
       "ruijieAuthIf": ruijieAuthIf,
       "ruijieAuthIfStatus": ruijieAuthIfStatus,
       "ruijieAuthenticationMode": ruijieAuthenticationMode,
       "ruijieDot1xAccountUpdateStatus": ruijieDot1xAccountUpdateStatus,
       "ruijieDot1xAcctInterimInterval": ruijieDot1xAcctInterimInterval,
       "ruijieDot1xEapolTagEnabled": ruijieDot1xEapolTagEnabled,
       "ruijieDot1xIfUserMaxTable": ruijieDot1xIfUserMaxTable,
       "ruijieDot1xIfUserMaxEntry": ruijieDot1xIfUserMaxEntry,
       "ruijieDot1xIfUserMaxIndex": ruijieDot1xIfUserMaxIndex,
       "ruijieDot1xIfUserMaxNum": ruijieDot1xIfUserMaxNum,
       "ruijieDot1xPseudoSrcmac": ruijieDot1xPseudoSrcmac,
       "ruijieDot1xUserMIB": ruijieDot1xUserMIB,
       "ruijieDot1xUserTrapsObjects": ruijieDot1xUserTrapsObjects,
       "ruijieDot1xUserMac": ruijieDot1xUserMac,
       "ruijieDot1xUserName": ruijieDot1xUserName,
       "ruijieDot1xUserIp": ruijieDot1xUserIp,
       "ruijieDot1xUserIpv6": ruijieDot1xUserIpv6,
       "ruijieDot1xUserWlanId": ruijieDot1xUserWlanId,
       "ruijieDot1xUserVlanId": ruijieDot1xUserVlanId,
       "ruijieDot1xUserSsid": ruijieDot1xUserSsid,
       "ruijieDot1xUserApMac": ruijieDot1xUserApMac,
       "ruijieDot1xUserTerminalType": ruijieDot1xUserTerminalType,
       "ruijieDot1xUserOperType": ruijieDot1xUserOperType,
       "ruijieDot1xUserTerminateCause": ruijieDot1xUserTerminateCause,
       "ruijieDot1xUserReplyMessage": ruijieDot1xUserReplyMessage,
       "ruijieDot1xUserIfIndex": ruijieDot1xUserIfIndex,
       "ruijieDot1xUserTraps": ruijieDot1xUserTraps,
       "ruijieDot1xUserMgmtTrap": ruijieDot1xUserMgmtTrap,
       "ruijieDot1xWiredUserTrap": ruijieDot1xWiredUserTrap,
       "ruijieDot1xOnlineUserTable": ruijieDot1xOnlineUserTable,
       "ruijieDot1xOnlineUserEntry": ruijieDot1xOnlineUserEntry,
       "ruijieDot1xOnlineUserID": ruijieDot1xOnlineUserID,
       "ruijieDot1xOnlineUserName": ruijieDot1xOnlineUserName,
       "ruijieDot1xOnlineUserMacAddr": ruijieDot1xOnlineUserMacAddr,
       "ruijieDot1xOnlineUserIfIndex": ruijieDot1xOnlineUserIfIndex,
       "ruijieDot1xOnlineUserVlanId": ruijieDot1xOnlineUserVlanId,
       "ruijieDot1xOnlineUserIp": ruijieDot1xOnlineUserIp,
       "ruijieDot1xOnlineUserIpv6": ruijieDot1xOnlineUserIpv6,
       "ruijieDot1xAbnormalOfflineUserCount": ruijieDot1xAbnormalOfflineUserCount,
       "ruijieDot1xTotalAuthUserCount": ruijieDot1xTotalAuthUserCount,
       "ruijieDot1xAuthSuccUserCount": ruijieDot1xAuthSuccUserCount,
       "ruijieDot1xAuthFailUserCount": ruijieDot1xAuthFailUserCount,
       "ruijieAAAServerObjects": ruijieAAAServerObjects,
       "ruijieAAAServerAuthPort": ruijieAAAServerAuthPort,
       "ruijieAAAServerAcctPort": ruijieAAAServerAcctPort,
       "ruijieAAAServerRadiusKeyStr": ruijieAAAServerRadiusKeyStr,
       "ruijieAAAServerTacplusKeyStr": ruijieAAAServerTacplusKeyStr,
       "ruijieAAAServerConfigTable": ruijieAAAServerConfigTable,
       "ruijieAAAServerConfigEntry": ruijieAAAServerConfigEntry,
       "ruijieAAAServerConfigProtocol": ruijieAAAServerConfigProtocol,
       "ruijieAAAServerConfigIndex": ruijieAAAServerConfigIndex,
       "ruijieAAAServerConfigAddressType": ruijieAAAServerConfigAddressType,
       "ruijieAAAServerConfigAddress": ruijieAAAServerConfigAddress,
       "ruijieAAAServerConfigAuthPort": ruijieAAAServerConfigAuthPort,
       "ruijieAAAServerConfigAcctPort": ruijieAAAServerConfigAcctPort,
       "ruijieAAAServerConfigKeyStr": ruijieAAAServerConfigKeyStr,
       "ruijieAAAServerConfigRowStatus": ruijieAAAServerConfigRowStatus,
       "ruijieAAARadiusGroupTable": ruijieAAARadiusGroupTable,
       "ruijieAAARadiusGroupEntry": ruijieAAARadiusGroupEntry,
       "ruijieAAARadiusGroupName": ruijieAAARadiusGroupName,
       "ruijieAAARadiusGroupVrf": ruijieAAARadiusGroupVrf,
       "ruijieAAARadiusGroupRowStatus": ruijieAAARadiusGroupRowStatus,
       "ruijieAAARadiusGroupServerTable": ruijieAAARadiusGroupServerTable,
       "ruijieAAARadiusGroupServerEntry": ruijieAAARadiusGroupServerEntry,
       "ruijieAAARadiusGroupServerIndex": ruijieAAARadiusGroupServerIndex,
       "ruijieAAARadiusGroupServerAddressType": ruijieAAARadiusGroupServerAddressType,
       "ruijieAAARadiusGroupServerAddress": ruijieAAARadiusGroupServerAddress,
       "ruijieAAARadiusGroupServerAuthPort": ruijieAAARadiusGroupServerAuthPort,
       "ruijieAAARadiusGroupServerAcctPort": ruijieAAARadiusGroupServerAcctPort,
       "ruijieAAARadiusGroupServerRowStatus": ruijieAAARadiusGroupServerRowStatus,
       "ruijieAAAServerTotalOnlineCount": ruijieAAAServerTotalOnlineCount,
       "ruijieAAAServerAbnormalOffline": ruijieAAAServerAbnormalOffline,
       "ruijieAAAServerRadiusAuthReqCount": ruijieAAAServerRadiusAuthReqCount,
       "ruijieAAAServerRadiusAuthRespCount": ruijieAAAServerRadiusAuthRespCount,
       "ruijieAAAServerRadiusAuthSuccessCount": ruijieAAAServerRadiusAuthSuccessCount,
       "ruijieAAAServerCurrOnlineUserCount": ruijieAAAServerCurrOnlineUserCount,
       "ruijieAAAMasterAuthenServerConfigTable": ruijieAAAMasterAuthenServerConfigTable,
       "ruijieAAAMasterAuthenServerConfigEntry": ruijieAAAMasterAuthenServerConfigEntry,
       "ruijieAAAMasterAuthenServerConfigGrpName": ruijieAAAMasterAuthenServerConfigGrpName,
       "ruijieAAAMasterAuthenServerConfigSrvIndex": ruijieAAAMasterAuthenServerConfigSrvIndex,
       "ruijieAAAMasterAuthenServerConfigAddress": ruijieAAAMasterAuthenServerConfigAddress,
       "ruijieAAAMasterAuthenServerConfigAuthPort": ruijieAAAMasterAuthenServerConfigAuthPort,
       "ruijieAAAMasterAuthenServerConfigAcctPort": ruijieAAAMasterAuthenServerConfigAcctPort,
       "ruijieAAAMasterAuthenServerConfigKeyStr": ruijieAAAMasterAuthenServerConfigKeyStr,
       "ruijieAAAMasterAuthenServerConfigRowStatus": ruijieAAAMasterAuthenServerConfigRowStatus,
       "ruijieAAABackAuthenServerConfigTable": ruijieAAABackAuthenServerConfigTable,
       "ruijieAAABackAuthenServerConfigEntry": ruijieAAABackAuthenServerConfigEntry,
       "ruijieAAABackAuthenServerConfigGrpName": ruijieAAABackAuthenServerConfigGrpName,
       "ruijieAAABackAuthenServerConfigSrvIndex": ruijieAAABackAuthenServerConfigSrvIndex,
       "ruijieAAABackAuthenServerConfigAddress": ruijieAAABackAuthenServerConfigAddress,
       "ruijieAAABackAuthenServerConfigAuthPort": ruijieAAABackAuthenServerConfigAuthPort,
       "ruijieAAABackAuthenServerConfigAcctPort": ruijieAAABackAuthenServerConfigAcctPort,
       "ruijieAAABackAuthenServerConfigKeyStr": ruijieAAABackAuthenServerConfigKeyStr,
       "ruijieAAABackAuthenServerConfigRowStatus": ruijieAAABackAuthenServerConfigRowStatus,
       "ruijieAAAMasterAcctServerConfigTable": ruijieAAAMasterAcctServerConfigTable,
       "ruijieAAAMasterAcctServerConfigEntry": ruijieAAAMasterAcctServerConfigEntry,
       "ruijieAAAMasterAcctServerConfigGrpName": ruijieAAAMasterAcctServerConfigGrpName,
       "ruijieAAAMasterAcctServerConfigSrvIndex": ruijieAAAMasterAcctServerConfigSrvIndex,
       "ruijieAAAMasterAcctServerConfigAddress": ruijieAAAMasterAcctServerConfigAddress,
       "ruijieAAAMasterAcctServerConfigAuthPort": ruijieAAAMasterAcctServerConfigAuthPort,
       "ruijieAAAMasterAcctServerConfigAcctPort": ruijieAAAMasterAcctServerConfigAcctPort,
       "ruijieAAAMasterAcctServerConfigKeyStr": ruijieAAAMasterAcctServerConfigKeyStr,
       "ruijieAAAMasterAcctServerConfigRowStatus": ruijieAAAMasterAcctServerConfigRowStatus,
       "ruijieAAABackAcctServerConfigTable": ruijieAAABackAcctServerConfigTable,
       "ruijieAAABackAcctServerConfigEntry": ruijieAAABackAcctServerConfigEntry,
       "ruijieAAABackAcctServerConfigGrpName": ruijieAAABackAcctServerConfigGrpName,
       "ruijieAAABackAcctServerConfigSrvIndex": ruijieAAABackAcctServerConfigSrvIndex,
       "ruijieAAABackAcctServerConfigAddress": ruijieAAABackAcctServerConfigAddress,
       "ruijieAAABackAcctServerConfigAuthPort": ruijieAAABackAcctServerConfigAuthPort,
       "ruijieAAABackAcctServerConfigAcctPort": ruijieAAABackAcctServerConfigAcctPort,
       "ruijieAAABackAcctServerConfigKeyStr": ruijieAAABackAcctServerConfigKeyStr,
       "ruijieAAABackAcctServerConfigRowStatus": ruijieAAABackAcctServerConfigRowStatus,
       "ruijieAAAServerTotalAuthUserCount": ruijieAAAServerTotalAuthUserCount,
       "ruijieAAAServerAuthSuccUserCount": ruijieAAAServerAuthSuccUserCount,
       "ruijieAAAServerDot1xOnlineUserCount": ruijieAAAServerDot1xOnlineUserCount,
       "ruijieAAAServerMacOnlineUserCount": ruijieAAAServerMacOnlineUserCount,
       "ruijieAAAServerWebOnlineUserCount": ruijieAAAServerWebOnlineUserCount,
       "ruijieAAAServerTatalOnlineUserCount": ruijieAAAServerTatalOnlineUserCount,
       "ruijieAAAServerIfOnlineUserTable": ruijieAAAServerIfOnlineUserTable,
       "ruijieAAAServerIfOnlineUserEntry": ruijieAAAServerIfOnlineUserEntry,
       "ruijieAAAServerIfOnlineUserIfIndex": ruijieAAAServerIfOnlineUserIfIndex,
       "ruijieAAAServerIfOnlineUserDot1xCount": ruijieAAAServerIfOnlineUserDot1xCount,
       "ruijieAAAServerIfOnlineUserWebCount": ruijieAAAServerIfOnlineUserWebCount,
       "ruijieAAAServerIfOnlineUserMacCount": ruijieAAAServerIfOnlineUserMacCount,
       "ruijieAAAServerIfOnlineUserTotalCount": ruijieAAAServerIfOnlineUserTotalCount,
       "ruijieAuthUserObjects": ruijieAuthUserObjects,
       "ruijieAuthAddrTable": ruijieAuthAddrTable,
       "ruijieAuthAddrEntry": ruijieAuthAddrEntry,
       "ruijieAuthPort": ruijieAuthPort,
       "ruijieAuthMacAddress": ruijieAuthMacAddress,
       "ruijieAuthAddrStatus": ruijieAuthAddrStatus,
       "ruijieAuthUserTable": ruijieAuthUserTable,
       "ruijieAuthUserEntry": ruijieAuthUserEntry,
       "ruijieAuthUserFdbId": ruijieAuthUserFdbId,
       "ruijieAuthUserMacAddress": ruijieAuthUserMacAddress,
       "ruijieAuthUserName": ruijieAuthUserName,
       "ruijieAuthUserSessionId": ruijieAuthUserSessionId,
       "ruijieAuthUserIpAddr": ruijieAuthUserIpAddr,
       "ruijieAuthUserPort": ruijieAuthUserPort,
       "ruijieAuthUserStatus": ruijieAuthUserStatus,
       "ruijieAuthUserForVPNDel": ruijieAuthUserForVPNDel,
       "ruijieOnlineUserTable": ruijieOnlineUserTable,
       "ruijieOnlineUserEntry": ruijieOnlineUserEntry,
       "ruijieOnlineUserSessionId": ruijieOnlineUserSessionId,
       "ruijieOnlineUserVid": ruijieOnlineUserVid,
       "ruijieOnlineUserMacAddress": ruijieOnlineUserMacAddress,
       "ruijieOnlineUserPort": ruijieOnlineUserPort,
       "ruijieOnlineUserName": ruijieOnlineUserName,
       "ruijieOnlineUserIpAddr": ruijieOnlineUserIpAddr,
       "ruijieOnlineUserStatus": ruijieOnlineUserStatus,
       "ruijieAaaVersion": ruijieAaaVersion,
       "ruijieAuthModeObjects": ruijieAuthModeObjects,
       "ruijieIpAuthorizationMode": ruijieIpAuthorizationMode,
       "ruijieClientProbeObjects": ruijieClientProbeObjects,
       "ruijieClientProbeEnabledStatus": ruijieClientProbeEnabledStatus,
       "ruijieClientProbeHelloInterval": ruijieClientProbeHelloInterval,
       "ruijieClientProbeAliveInteval": ruijieClientProbeAliveInteval,
       "ruijieAAAConfigObjects": ruijieAAAConfigObjects,
       "ruijieAuthenConfigObjects": ruijieAuthenConfigObjects,
       "ruijieAuthenMethodListTable": ruijieAuthenMethodListTable,
       "ruijieAuthenMethodListEntry": ruijieAuthenMethodListEntry,
       "ruijieAuthenMethodListType": ruijieAuthenMethodListType,
       "ruijieAuthenMethodListName": ruijieAuthenMethodListName,
       "ruijieAuthenMethodListString": ruijieAuthenMethodListString,
       "ruijieAuthenMethodListRowStatus": ruijieAuthenMethodListRowStatus,
       "ruijieAuthorConfigObjects": ruijieAuthorConfigObjects,
       "ruijieAuthorMethodListTable": ruijieAuthorMethodListTable,
       "ruijieAuthorMethodListEntry": ruijieAuthorMethodListEntry,
       "ruijieAuthorMethodListType": ruijieAuthorMethodListType,
       "ruijieAuthorMethodListName": ruijieAuthorMethodListName,
       "ruijieAuthorMethodListCmdLevel": ruijieAuthorMethodListCmdLevel,
       "ruijieAuthorMethodListString": ruijieAuthorMethodListString,
       "ruijieAuthorMethodListRowStatus": ruijieAuthorMethodListRowStatus,
       "ruijieAcctConfigObjects": ruijieAcctConfigObjects,
       "ruijieAcctMethodListTable": ruijieAcctMethodListTable,
       "ruijieAcctMethodListEntry": ruijieAcctMethodListEntry,
       "ruijieAcctMethodListType": ruijieAcctMethodListType,
       "ruijieAcctMethodListName": ruijieAcctMethodListName,
       "ruijieAcctMethodListMode": ruijieAcctMethodListMode,
       "ruijieAcctMethodListCmdLevel": ruijieAcctMethodListCmdLevel,
       "ruijieAcctMethodListString": ruijieAcctMethodListString,
       "ruijieAcctMethodListRowStatus": ruijieAcctMethodListRowStatus,
       "ruijieAAAUserApplyObjects": ruijieAAAUserApplyObjects,
       "ruijieAAADo1xApplyObjects": ruijieAAADo1xApplyObjects,
       "ruijieDot1xAuthenMethodList": ruijieDot1xAuthenMethodList,
       "ruijieDot1xAuthorMethodList": ruijieDot1xAuthorMethodList,
       "ruijieDot1xAcctMethodList": ruijieDot1xAcctMethodList,
       "ruijieRdASObjects": ruijieRdASObjects,
       "ruijieRdASipInetAddreType": ruijieRdASipInetAddreType,
       "ruijieRdASipInsetAddres": ruijieRdASipInsetAddres,
       "ruijieAAAMIBConformance": ruijieAAAMIBConformance,
       "ruijieAAAMIBCompliances": ruijieAAAMIBCompliances,
       "ruijieAAAMIBCompliance": ruijieAAAMIBCompliance,
       "ruijieAAAMIBGroups": ruijieAAAMIBGroups,
       "ruijieDot1xAuthMIBGroup": ruijieDot1xAuthMIBGroup,
       "ruijieAAAServerMIBGroup": ruijieAAAServerMIBGroup,
       "ruijieAuthAddrMIBGroup": ruijieAuthAddrMIBGroup,
       "ruijieAuthModeMIBGroup": ruijieAuthModeMIBGroup,
       "ruijieClientProbeGroup": ruijieClientProbeGroup,
       "ruijieAAAConfigMIBGroup": ruijieAAAConfigMIBGroup,
       "ruijieAAAUserApplyMIBGroup": ruijieAAAUserApplyMIBGroup,
       "ruijieRdASGroup": ruijieRdASGroup}
)
