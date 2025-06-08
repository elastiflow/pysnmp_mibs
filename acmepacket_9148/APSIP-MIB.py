# SNMP MIB module (APSIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APSIP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:26 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApPhyPortType,
 ApPresence,
 ApRedundancyState,
 ApServerStatus,
 ApSipMethod) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApPhyPortType",
    "ApPresence",
    "ApRedundancyState",
    "ApServerStatus",
    "ApSipMethod")

(apSigRealmStatsEntry,
 apSipSessionAgentStatsEntry,
 apSysMgmtSipInterfaceIP,
 apSysMgmtSipInterfaceRealmName) = mibBuilder.importSymbols(
    "APSYSMGMT-MIB",
    "apSigRealmStatsEntry",
    "apSipSessionAgentStatsEntry",
    "apSysMgmtSipInterfaceIP",
    "apSysMgmtSipInterfaceRealmName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apSipModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15)
)
if mibBuilder.loadTexts:
    apSipModule.setRevisions(
        ("2012-07-13 00:00",
         "2012-03-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSipMIBObjects_ObjectIdentity = ObjectIdentity
apSipMIBObjects = _ApSipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1)
)
_ApSipMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apSipMIBGeneralObjects = _ApSipMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1)
)
_ApSipSecInterfaceObjects_ObjectIdentity = ObjectIdentity
apSipSecInterfaceObjects = _ApSipSecInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1)
)
_ApSipSecInterfaceTotalRegistrations_Type = Unsigned32
_ApSipSecInterfaceTotalRegistrations_Object = MibScalar
apSipSecInterfaceTotalRegistrations = _ApSipSecInterfaceTotalRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 1),
    _ApSipSecInterfaceTotalRegistrations_Type()
)
apSipSecInterfaceTotalRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceTotalRegistrations.setStatus("current")
_ApSipSecInterfaceRegThreshold_Type = Unsigned32
_ApSipSecInterfaceRegThreshold_Object = MibScalar
apSipSecInterfaceRegThreshold = _ApSipSecInterfaceRegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 2),
    _ApSipSecInterfaceRegThreshold_Type()
)
apSipSecInterfaceRegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThreshold.setStatus("current")
_ApSipSecInterfaceClearThreshold_Type = Unsigned32
_ApSipSecInterfaceClearThreshold_Object = MibScalar
apSipSecInterfaceClearThreshold = _ApSipSecInterfaceClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 1, 1, 3),
    _ApSipSecInterfaceClearThreshold_Type()
)
apSipSecInterfaceClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSecInterfaceClearThreshold.setStatus("current")
_ApSipMIBTabularObjects_ObjectIdentity = ObjectIdentity
apSipMIBTabularObjects = _ApSipMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2)
)
_ApSipInterfaceTable_Object = MibTable
apSipInterfaceTable = _ApSipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apSipInterfaceTable.setStatus("current")
_ApSipInterfaceEntry_Object = MibTableRow
apSipInterfaceEntry = _ApSipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 1, 1)
)
apSipInterfaceEntry.setIndexNames(
    (0, "APSIP-MIB", "apSipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    apSipInterfaceEntry.setStatus("current")


class _ApSipInterfaceIndex_Type(Integer32):
    """Custom type apSipInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSipInterfaceIndex_Type.__name__ = "Integer32"
_ApSipInterfaceIndex_Object = MibTableColumn
apSipInterfaceIndex = _ApSipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 1, 1, 1),
    _ApSipInterfaceIndex_Type()
)
apSipInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSipInterfaceIndex.setStatus("current")


class _ApSipInterfaceRealm_Type(DisplayString):
    """Custom type apSipInterfaceRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipInterfaceRealm_Type.__name__ = "DisplayString"
_ApSipInterfaceRealm_Object = MibTableColumn
apSipInterfaceRealm = _ApSipInterfaceRealm_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 1, 1, 2),
    _ApSipInterfaceRealm_Type()
)
apSipInterfaceRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipInterfaceRealm.setStatus("current")
_ApSipRateIntfStatsTable_Object = MibTable
apSipRateIntfStatsTable = _ApSipRateIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apSipRateIntfStatsTable.setStatus("current")
_ApSipRateIntfStatsEntry_Object = MibTableRow
apSipRateIntfStatsEntry = _ApSipRateIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1)
)
apSipRateIntfStatsEntry.setIndexNames(
    (0, "APSIP-MIB", "apSipInterfaceIndex"),
    (0, "APSIP-MIB", "apSipRateIntfMethod"),
)
if mibBuilder.loadTexts:
    apSipRateIntfStatsEntry.setStatus("current")
_ApSipRateIntfMethod_Type = ApSipMethod
_ApSipRateIntfMethod_Object = MibTableColumn
apSipRateIntfMethod = _ApSipRateIntfMethod_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 1),
    _ApSipRateIntfMethod_Type()
)
apSipRateIntfMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSipRateIntfMethod.setStatus("current")
_ApSipRateIntfMsgRcvd_Type = Gauge32
_ApSipRateIntfMsgRcvd_Object = MibTableColumn
apSipRateIntfMsgRcvd = _ApSipRateIntfMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 5),
    _ApSipRateIntfMsgRcvd_Type()
)
apSipRateIntfMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfMsgRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfMsgRcvd.setUnits("messages per 10 seconds")
_ApSipRateIntfMsgSent_Type = Gauge32
_ApSipRateIntfMsgSent_Object = MibTableColumn
apSipRateIntfMsgSent = _ApSipRateIntfMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 6),
    _ApSipRateIntfMsgSent_Type()
)
apSipRateIntfMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfMsgSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfMsgSent.setUnits("messages per 10 seconds")
_ApSipRateIntfReqRcvd_Type = Gauge32
_ApSipRateIntfReqRcvd_Object = MibTableColumn
apSipRateIntfReqRcvd = _ApSipRateIntfReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 7),
    _ApSipRateIntfReqRcvd_Type()
)
apSipRateIntfReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfReqRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfReqRcvd.setUnits("messages per 10 seconds")
_ApSipRateIntfReqSent_Type = Gauge32
_ApSipRateIntfReqSent_Object = MibTableColumn
apSipRateIntfReqSent = _ApSipRateIntfReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 8),
    _ApSipRateIntfReqSent_Type()
)
apSipRateIntfReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfReqSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfReqSent.setUnits("messages per 10 seconds")
_ApSipRateIntfRspRcvd_Type = Gauge32
_ApSipRateIntfRspRcvd_Object = MibTableColumn
apSipRateIntfRspRcvd = _ApSipRateIntfRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 9),
    _ApSipRateIntfRspRcvd_Type()
)
apSipRateIntfRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfRspRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfRspRcvd.setUnits("messages per 10 seconds")
_ApSipRateIntfRspSent_Type = Gauge32
_ApSipRateIntfRspSent_Object = MibTableColumn
apSipRateIntfRspSent = _ApSipRateIntfRspSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 2, 1, 10),
    _ApSipRateIntfRspSent_Type()
)
apSipRateIntfRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateIntfRspSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateIntfRspSent.setUnits("messages per 10 seconds")
_ApSipAgentTable_Object = MibTable
apSipAgentTable = _ApSipAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apSipAgentTable.setStatus("current")
_ApSipAgentEntry_Object = MibTableRow
apSipAgentEntry = _ApSipAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 3, 1)
)
apSipAgentEntry.setIndexNames(
    (0, "APSIP-MIB", "apSipAgentIndex"),
    (0, "APSIP-MIB", "apSipAgentStatsMethod"),
)
if mibBuilder.loadTexts:
    apSipAgentEntry.setStatus("current")


class _ApSipAgentIndex_Type(Integer32):
    """Custom type apSipAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSipAgentIndex_Type.__name__ = "Integer32"
_ApSipAgentIndex_Object = MibTableColumn
apSipAgentIndex = _ApSipAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 3, 1, 1),
    _ApSipAgentIndex_Type()
)
apSipAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSipAgentIndex.setStatus("current")


class _ApSipAgentName_Type(DisplayString):
    """Custom type apSipAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipAgentName_Type.__name__ = "DisplayString"
_ApSipAgentName_Object = MibTableColumn
apSipAgentName = _ApSipAgentName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 3, 1, 2),
    _ApSipAgentName_Type()
)
apSipAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipAgentName.setStatus("current")
_ApSipRateAgentStatsTable_Object = MibTable
apSipRateAgentStatsTable = _ApSipRateAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4)
)
if mibBuilder.loadTexts:
    apSipRateAgentStatsTable.setStatus("current")
_ApSipRateAgentStatsEntry_Object = MibTableRow
apSipRateAgentStatsEntry = _ApSipRateAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1)
)
apSipRateAgentStatsEntry.setIndexNames(
    (0, "APSIP-MIB", "apSipAgentIndex"),
    (0, "APSIP-MIB", "apSipAgentStatsMethod"),
)
if mibBuilder.loadTexts:
    apSipRateAgentStatsEntry.setStatus("current")
_ApSipAgentStatsMethod_Type = ApSipMethod
_ApSipAgentStatsMethod_Object = MibTableColumn
apSipAgentStatsMethod = _ApSipAgentStatsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 1),
    _ApSipAgentStatsMethod_Type()
)
apSipAgentStatsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSipAgentStatsMethod.setStatus("current")
_ApSipRateAgentMsgRcvd_Type = Gauge32
_ApSipRateAgentMsgRcvd_Object = MibTableColumn
apSipRateAgentMsgRcvd = _ApSipRateAgentMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 5),
    _ApSipRateAgentMsgRcvd_Type()
)
apSipRateAgentMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentMsgRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentMsgRcvd.setUnits("messages per 10 seconds")
_ApSipRateAgentMsgSent_Type = Gauge32
_ApSipRateAgentMsgSent_Object = MibTableColumn
apSipRateAgentMsgSent = _ApSipRateAgentMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 6),
    _ApSipRateAgentMsgSent_Type()
)
apSipRateAgentMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentMsgSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentMsgSent.setUnits("messages per 10 seconds")
_ApSipRateAgentReqRcvd_Type = Gauge32
_ApSipRateAgentReqRcvd_Object = MibTableColumn
apSipRateAgentReqRcvd = _ApSipRateAgentReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 7),
    _ApSipRateAgentReqRcvd_Type()
)
apSipRateAgentReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentReqRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentReqRcvd.setUnits("messages per 10 seconds")
_ApSipRateAgentReqSent_Type = Gauge32
_ApSipRateAgentReqSent_Object = MibTableColumn
apSipRateAgentReqSent = _ApSipRateAgentReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 8),
    _ApSipRateAgentReqSent_Type()
)
apSipRateAgentReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentReqSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentReqSent.setUnits("messages per 10 seconds")
_ApSipRateAgentRspRcvd_Type = Gauge32
_ApSipRateAgentRspRcvd_Object = MibTableColumn
apSipRateAgentRspRcvd = _ApSipRateAgentRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 9),
    _ApSipRateAgentRspRcvd_Type()
)
apSipRateAgentRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentRspRcvd.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentRspRcvd.setUnits("messages per 10 seconds")
_ApSipRateAgentRspSent_Type = Gauge32
_ApSipRateAgentRspSent_Object = MibTableColumn
apSipRateAgentRspSent = _ApSipRateAgentRspSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 4, 1, 10),
    _ApSipRateAgentRspSent_Type()
)
apSipRateAgentRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipRateAgentRspSent.setStatus("current")
if mibBuilder.loadTexts:
    apSipRateAgentRspSent.setUnits("messages per 10 seconds")
_ApSipSaCacStatsTable_Object = MibTable
apSipSaCacStatsTable = _ApSipSaCacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 5)
)
if mibBuilder.loadTexts:
    apSipSaCacStatsTable.setStatus("current")
_ApSipSaCacStatsEntry_Object = MibTableRow
apSipSaCacStatsEntry = _ApSipSaCacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    apSipSaCacStatsEntry.setStatus("current")
_ApSipSaCacSessionUtilLevel_Type = Gauge32
_ApSipSaCacSessionUtilLevel_Object = MibTableColumn
apSipSaCacSessionUtilLevel = _ApSipSaCacSessionUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 5, 1, 1),
    _ApSipSaCacSessionUtilLevel_Type()
)
apSipSaCacSessionUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSaCacSessionUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSipSaCacSessionUtilLevel.setUnits("percentage")
_ApSipSaCacBurstRateUtilLevel_Type = Gauge32
_ApSipSaCacBurstRateUtilLevel_Object = MibTableColumn
apSipSaCacBurstRateUtilLevel = _ApSipSaCacBurstRateUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 5, 1, 2),
    _ApSipSaCacBurstRateUtilLevel_Type()
)
apSipSaCacBurstRateUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSaCacBurstRateUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSipSaCacBurstRateUtilLevel.setUnits("percentage")
_ApSigRealmCacStatsTable_Object = MibTable
apSigRealmCacStatsTable = _ApSigRealmCacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 6)
)
if mibBuilder.loadTexts:
    apSigRealmCacStatsTable.setStatus("current")
_ApSigRealmCacStatsEntry_Object = MibTableRow
apSigRealmCacStatsEntry = _ApSigRealmCacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    apSigRealmCacStatsEntry.setStatus("current")
_ApSigRealmCacSessionUtilLevel_Type = Gauge32
_ApSigRealmCacSessionUtilLevel_Object = MibTableColumn
apSigRealmCacSessionUtilLevel = _ApSigRealmCacSessionUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 6, 1, 1),
    _ApSigRealmCacSessionUtilLevel_Type()
)
apSigRealmCacSessionUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmCacSessionUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSigRealmCacSessionUtilLevel.setUnits("percentage")
_ApSigRealmCacBurstRateUtilLevel_Type = Gauge32
_ApSigRealmCacBurstRateUtilLevel_Object = MibTableColumn
apSigRealmCacBurstRateUtilLevel = _ApSigRealmCacBurstRateUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 6, 1, 2),
    _ApSigRealmCacBurstRateUtilLevel_Type()
)
apSigRealmCacBurstRateUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmCacBurstRateUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSigRealmCacBurstRateUtilLevel.setUnits("percentage")
_ApSipInterfaceCacStatsTable_Object = MibTable
apSipInterfaceCacStatsTable = _ApSipInterfaceCacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 7)
)
if mibBuilder.loadTexts:
    apSipInterfaceCacStatsTable.setStatus("current")
_ApSipInterfaceCacStatsEntry_Object = MibTableRow
apSipInterfaceCacStatsEntry = _ApSipInterfaceCacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    apSipInterfaceCacStatsEntry.setStatus("current")
_ApSipInterfaceCacSessionUtilLevel_Type = Gauge32
_ApSipInterfaceCacSessionUtilLevel_Object = MibTableColumn
apSipInterfaceCacSessionUtilLevel = _ApSipInterfaceCacSessionUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 7, 1, 1),
    _ApSipInterfaceCacSessionUtilLevel_Type()
)
apSipInterfaceCacSessionUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipInterfaceCacSessionUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSipInterfaceCacSessionUtilLevel.setUnits("percentage")
_ApSipInterfaceCacBurstRateUtilLevel_Type = Gauge32
_ApSipInterfaceCacBurstRateUtilLevel_Object = MibTableColumn
apSipInterfaceCacBurstRateUtilLevel = _ApSipInterfaceCacBurstRateUtilLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 1, 2, 7, 1, 2),
    _ApSipInterfaceCacBurstRateUtilLevel_Type()
)
apSipInterfaceCacBurstRateUtilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipInterfaceCacBurstRateUtilLevel.setStatus("current")
if mibBuilder.loadTexts:
    apSipInterfaceCacBurstRateUtilLevel.setUnits("percentage")
_ApSipNotificationObjects_ObjectIdentity = ObjectIdentity
apSipNotificationObjects = _ApSipNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2)
)
_ApSipSecInterfaceNotifications_ObjectIdentity = ObjectIdentity
apSipSecInterfaceNotifications = _ApSipSecInterfaceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1)
)
_ApSipSecIntfNotifObjects_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifObjects = _ApSipSecIntfNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 1)
)
_ApSipSecIntfNotifPrefix_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifPrefix = _ApSipSecIntfNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2)
)
_ApSipSecIntfNotifications_ObjectIdentity = ObjectIdentity
apSipSecIntfNotifications = _ApSipSecIntfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0)
)
_ApSipSurvivabilityNotif_ObjectIdentity = ObjectIdentity
apSipSurvivabilityNotif = _ApSipSurvivabilityNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2)
)
_ApSipSurvivabilityNotifObjects_ObjectIdentity = ObjectIdentity
apSipSurvivabilityNotifObjects = _ApSipSurvivabilityNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2, 1)
)
_ApSipSurvivabilityNotifPrefix_ObjectIdentity = ObjectIdentity
apSipSurvivabilityNotifPrefix = _ApSipSurvivabilityNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2, 2)
)
_ApSipSurvivabilityNotifications_ObjectIdentity = ObjectIdentity
apSipSurvivabilityNotifications = _ApSipSurvivabilityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2, 2, 0)
)
_ApSipCACUtilNotif_ObjectIdentity = ObjectIdentity
apSipCACUtilNotif = _ApSipCACUtilNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3)
)
_ApSipCACUtilNotifObjects_ObjectIdentity = ObjectIdentity
apSipCACUtilNotifObjects = _ApSipCACUtilNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 1)
)
_ApSipCACUtilTrapType_Type = ObjectIdentifier
_ApSipCACUtilTrapType_Object = MibScalar
apSipCACUtilTrapType = _ApSipCACUtilTrapType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 1, 1),
    _ApSipCACUtilTrapType_Type()
)
apSipCACUtilTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipCACUtilTrapType.setStatus("current")
_ApSipCACUtilTrapValue_Type = Gauge32
_ApSipCACUtilTrapValue_Object = MibScalar
apSipCACUtilTrapValue = _ApSipCACUtilTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 1, 2),
    _ApSipCACUtilTrapValue_Type()
)
apSipCACUtilTrapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipCACUtilTrapValue.setStatus("current")
_ApSipCACUtilNotifPrefix_ObjectIdentity = ObjectIdentity
apSipCACUtilNotifPrefix = _ApSipCACUtilNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 2)
)
_ApSipCACUtilNotifications_ObjectIdentity = ObjectIdentity
apSipCACUtilNotifications = _ApSipCACUtilNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 2, 0)
)
_ApSipConformance_ObjectIdentity = ObjectIdentity
apSipConformance = _ApSipConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3)
)
_ApSipObjectGroups_ObjectIdentity = ObjectIdentity
apSipObjectGroups = _ApSipObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1)
)
_ApSipNotificationGroups_ObjectIdentity = ObjectIdentity
apSipNotificationGroups = _ApSipNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2)
)
_ApSipRecModule_ObjectIdentity = ObjectIdentity
apSipRecModule = _ApSipRecModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4)
)
_ApSipRecNotifications_ObjectIdentity = ObjectIdentity
apSipRecNotifications = _ApSipRecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1)
)
_ApSipRecNotificationPrefix_ObjectIdentity = ObjectIdentity
apSipRecNotificationPrefix = _ApSipRecNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 0)
)
_ApSipRecNotifyObjects_ObjectIdentity = ObjectIdentity
apSipRecNotifyObjects = _ApSipRecNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1)
)


class _ApSipRecRecDlgCallIdHeader_Type(DisplayString):
    """Custom type apSipRecRecDlgCallIdHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecRecDlgCallIdHeader_Type.__name__ = "DisplayString"
_ApSipRecRecDlgCallIdHeader_Object = MibScalar
apSipRecRecDlgCallIdHeader = _ApSipRecRecDlgCallIdHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 1),
    _ApSipRecRecDlgCallIdHeader_Type()
)
apSipRecRecDlgCallIdHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecRecDlgCallIdHeader.setStatus("current")


class _ApSipRecRecDlgToHeader_Type(DisplayString):
    """Custom type apSipRecRecDlgToHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecRecDlgToHeader_Type.__name__ = "DisplayString"
_ApSipRecRecDlgToHeader_Object = MibScalar
apSipRecRecDlgToHeader = _ApSipRecRecDlgToHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 2),
    _ApSipRecRecDlgToHeader_Type()
)
apSipRecRecDlgToHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecRecDlgToHeader.setStatus("current")


class _ApSipRecRecDlgFromHeader_Type(DisplayString):
    """Custom type apSipRecRecDlgFromHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecRecDlgFromHeader_Type.__name__ = "DisplayString"
_ApSipRecRecDlgFromHeader_Object = MibScalar
apSipRecRecDlgFromHeader = _ApSipRecRecDlgFromHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 3),
    _ApSipRecRecDlgFromHeader_Type()
)
apSipRecRecDlgFromHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecRecDlgFromHeader.setStatus("current")


class _ApSipRecCommSessCallIdHeader_Type(DisplayString):
    """Custom type apSipRecCommSessCallIdHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecCommSessCallIdHeader_Type.__name__ = "DisplayString"
_ApSipRecCommSessCallIdHeader_Object = MibScalar
apSipRecCommSessCallIdHeader = _ApSipRecCommSessCallIdHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 4),
    _ApSipRecCommSessCallIdHeader_Type()
)
apSipRecCommSessCallIdHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecCommSessCallIdHeader.setStatus("current")


class _ApSipRecCommSessToHeader_Type(DisplayString):
    """Custom type apSipRecCommSessToHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecCommSessToHeader_Type.__name__ = "DisplayString"
_ApSipRecCommSessToHeader_Object = MibScalar
apSipRecCommSessToHeader = _ApSipRecCommSessToHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 5),
    _ApSipRecCommSessToHeader_Type()
)
apSipRecCommSessToHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecCommSessToHeader.setStatus("current")


class _ApSipRecCommSessFromHeader_Type(DisplayString):
    """Custom type apSipRecCommSessFromHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipRecCommSessFromHeader_Type.__name__ = "DisplayString"
_ApSipRecCommSessFromHeader_Object = MibScalar
apSipRecCommSessFromHeader = _ApSipRecCommSessFromHeader_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 1, 6),
    _ApSipRecCommSessFromHeader_Type()
)
apSipRecCommSessFromHeader.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSipRecCommSessFromHeader.setStatus("current")
apSipSessionAgentStatsEntry.registerAugmentions(
    ("APSIP-MIB",
     "apSipSaCacStatsEntry")
)
apSipSaCacStatsEntry.setIndexNames(*apSipSessionAgentStatsEntry.getIndexNames())
apSigRealmStatsEntry.registerAugmentions(
    ("APSIP-MIB",
     "apSigRealmCacStatsEntry")
)
apSigRealmCacStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
apSipInterfaceEntry.registerAugmentions(
    ("APSIP-MIB",
     "apSipInterfaceCacStatsEntry")
)
apSipInterfaceCacStatsEntry.setIndexNames(*apSipInterfaceEntry.getIndexNames())

# Managed Objects groups

apSipSecInterfaceRegObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1, 1)
)
apSipSecInterfaceRegObjectsGroup.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceRegThreshold"),
        ("APSIP-MIB", "apSipSecInterfaceClearThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegObjectsGroup.setStatus("current")

apSipRateStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1, 2)
)
apSipRateStatsGroup.setObjects(
      *(("APSIP-MIB", "apSipInterfaceRealm"),
        ("APSIP-MIB", "apSipRateIntfMsgRcvd"),
        ("APSIP-MIB", "apSipRateIntfMsgSent"),
        ("APSIP-MIB", "apSipRateIntfReqRcvd"),
        ("APSIP-MIB", "apSipRateIntfReqSent"),
        ("APSIP-MIB", "apSipRateIntfRspRcvd"),
        ("APSIP-MIB", "apSipRateIntfRspSent"),
        ("APSIP-MIB", "apSipAgentName"),
        ("APSIP-MIB", "apSipRateAgentMsgRcvd"),
        ("APSIP-MIB", "apSipRateAgentMsgSent"),
        ("APSIP-MIB", "apSipRateAgentReqRcvd"),
        ("APSIP-MIB", "apSipRateAgentReqSent"),
        ("APSIP-MIB", "apSipRateAgentRspRcvd"),
        ("APSIP-MIB", "apSipRateAgentRspSent"))
)
if mibBuilder.loadTexts:
    apSipRateStatsGroup.setStatus("current")

apSipCACStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1, 3)
)
apSipCACStatsGroup.setObjects(
      *(("APSIP-MIB", "apSipSaCacSessionUtilLevel"),
        ("APSIP-MIB", "apSipSaCacBurstRateUtilLevel"),
        ("APSIP-MIB", "apSigRealmCacSessionUtilLevel"),
        ("APSIP-MIB", "apSigRealmCacBurstRateUtilLevel"),
        ("APSIP-MIB", "apSipInterfaceCacSessionUtilLevel"),
        ("APSIP-MIB", "apSipInterfaceCacBurstRateUtilLevel"))
)
if mibBuilder.loadTexts:
    apSipCACStatsGroup.setStatus("current")

apSipCACStatsSubGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 1, 4)
)
apSipCACStatsSubGroup.setObjects(
      *(("APSIP-MIB", "apSipSaCacSessionUtilLevel"),
        ("APSIP-MIB", "apSipSaCacBurstRateUtilLevel"),
        ("APSIP-MIB", "apSigRealmCacSessionUtilLevel"),
        ("APSIP-MIB", "apSigRealmCacBurstRateUtilLevel"))
)
if mibBuilder.loadTexts:
    apSipCACStatsSubGroup.setStatus("current")


# Notification objects

apSipSecInterfaceRegThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0, 1)
)
apSipSecInterfaceRegThresholdExceededTrap.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceRegThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThresholdExceededTrap.setStatus(
        "current"
    )

apSipSecInterfaceRegThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 1, 2, 0, 2)
)
apSipSecInterfaceRegThresholdClearTrap.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceTotalRegistrations"),
        ("APSIP-MIB", "apSipSecInterfaceClearThreshold"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegThresholdClearTrap.setStatus(
        "current"
    )

apSipSurvivabilityModeEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2, 2, 0, 1)
)
apSipSurvivabilityModeEnter.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRealmName"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceIP"))
)
if mibBuilder.loadTexts:
    apSipSurvivabilityModeEnter.setStatus(
        "current"
    )

apSipSurvivabilityModeExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 2, 2, 0, 2)
)
apSipSurvivabilityModeExit.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRealmName"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceIP"))
)
if mibBuilder.loadTexts:
    apSipSurvivabilityModeExit.setStatus(
        "current"
    )

apSipCACUtilAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 2, 0, 1)
)
apSipCACUtilAlertTrap.setObjects(
      *(("APSIP-MIB", "apSipCACUtilTrapType"),
        ("APSIP-MIB", "apSipCACUtilTrapValue"))
)
if mibBuilder.loadTexts:
    apSipCACUtilAlertTrap.setStatus(
        "current"
    )

apSipCACUtilClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 2, 3, 2, 0, 2)
)
apSipCACUtilClearTrap.setObjects(
      *(("APSIP-MIB", "apSipCACUtilTrapType"),
        ("APSIP-MIB", "apSipCACUtilTrapValue"))
)
if mibBuilder.loadTexts:
    apSipCACUtilClearTrap.setStatus(
        "current"
    )

apSipRecRecDlgFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 0, 1)
)
apSipRecRecDlgFailNotify.setObjects(
      *(("APSIP-MIB", "apSipRecRecDlgCallIdHeader"),
        ("APSIP-MIB", "apSipRecRecDlgToHeader"),
        ("APSIP-MIB", "apSipRecRecDlgFromHeader"))
)
if mibBuilder.loadTexts:
    apSipRecRecDlgFailNotify.setStatus(
        "current"
    )

apSipRecCommSessionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 4, 1, 0, 2)
)
apSipRecCommSessionNotify.setObjects(
      *(("APSIP-MIB", "apSipRecCommSessCallIdHeader"),
        ("APSIP-MIB", "apSipRecCommSessToHeader"),
        ("APSIP-MIB", "apSipRecCommSessFromHeader"))
)
if mibBuilder.loadTexts:
    apSipRecCommSessionNotify.setStatus(
        "current"
    )


# Notifications groups

apSipSecInterfaceRegNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2, 1)
)
apSipSecInterfaceRegNotificationsGroup.setObjects(
      *(("APSIP-MIB", "apSipSecInterfaceRegThresholdExceededTrap"),
        ("APSIP-MIB", "apSipSecInterfaceRegThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegNotificationsGroup.setStatus(
        "current"
    )

apSipSurvivabilityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2, 2)
)
apSipSurvivabilityNotificationsGroup.setObjects(
      *(("APSIP-MIB", "apSipSurvivabilityModeEnter"),
        ("APSIP-MIB", "apSipSurvivabilityModeExit"))
)
if mibBuilder.loadTexts:
    apSipSurvivabilityNotificationsGroup.setStatus(
        "current"
    )

apSipCACNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2, 3)
)
apSipCACNotificationsGroup.setObjects(
      *(("APSIP-MIB", "apSipCACUtilAlertTrap"),
        ("APSIP-MIB", "apSipCACUtilClearTrap"))
)
if mibBuilder.loadTexts:
    apSipCACNotificationsGroup.setStatus(
        "current"
    )

apSipRecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 15, 3, 2, 4)
)
apSipRecNotificationGroup.setObjects(
      *(("APSIP-MIB", "apSipRecRecDlgFailNotify"),
        ("APSIP-MIB", "apSipRecCommSessionNotify"))
)
if mibBuilder.loadTexts:
    apSipRecNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSIP-MIB",
    **{"apSipModule": apSipModule,
       "apSipMIBObjects": apSipMIBObjects,
       "apSipMIBGeneralObjects": apSipMIBGeneralObjects,
       "apSipSecInterfaceObjects": apSipSecInterfaceObjects,
       "apSipSecInterfaceTotalRegistrations": apSipSecInterfaceTotalRegistrations,
       "apSipSecInterfaceRegThreshold": apSipSecInterfaceRegThreshold,
       "apSipSecInterfaceClearThreshold": apSipSecInterfaceClearThreshold,
       "apSipMIBTabularObjects": apSipMIBTabularObjects,
       "apSipInterfaceTable": apSipInterfaceTable,
       "apSipInterfaceEntry": apSipInterfaceEntry,
       "apSipInterfaceIndex": apSipInterfaceIndex,
       "apSipInterfaceRealm": apSipInterfaceRealm,
       "apSipRateIntfStatsTable": apSipRateIntfStatsTable,
       "apSipRateIntfStatsEntry": apSipRateIntfStatsEntry,
       "apSipRateIntfMethod": apSipRateIntfMethod,
       "apSipRateIntfMsgRcvd": apSipRateIntfMsgRcvd,
       "apSipRateIntfMsgSent": apSipRateIntfMsgSent,
       "apSipRateIntfReqRcvd": apSipRateIntfReqRcvd,
       "apSipRateIntfReqSent": apSipRateIntfReqSent,
       "apSipRateIntfRspRcvd": apSipRateIntfRspRcvd,
       "apSipRateIntfRspSent": apSipRateIntfRspSent,
       "apSipAgentTable": apSipAgentTable,
       "apSipAgentEntry": apSipAgentEntry,
       "apSipAgentIndex": apSipAgentIndex,
       "apSipAgentName": apSipAgentName,
       "apSipRateAgentStatsTable": apSipRateAgentStatsTable,
       "apSipRateAgentStatsEntry": apSipRateAgentStatsEntry,
       "apSipAgentStatsMethod": apSipAgentStatsMethod,
       "apSipRateAgentMsgRcvd": apSipRateAgentMsgRcvd,
       "apSipRateAgentMsgSent": apSipRateAgentMsgSent,
       "apSipRateAgentReqRcvd": apSipRateAgentReqRcvd,
       "apSipRateAgentReqSent": apSipRateAgentReqSent,
       "apSipRateAgentRspRcvd": apSipRateAgentRspRcvd,
       "apSipRateAgentRspSent": apSipRateAgentRspSent,
       "apSipSaCacStatsTable": apSipSaCacStatsTable,
       "apSipSaCacStatsEntry": apSipSaCacStatsEntry,
       "apSipSaCacSessionUtilLevel": apSipSaCacSessionUtilLevel,
       "apSipSaCacBurstRateUtilLevel": apSipSaCacBurstRateUtilLevel,
       "apSigRealmCacStatsTable": apSigRealmCacStatsTable,
       "apSigRealmCacStatsEntry": apSigRealmCacStatsEntry,
       "apSigRealmCacSessionUtilLevel": apSigRealmCacSessionUtilLevel,
       "apSigRealmCacBurstRateUtilLevel": apSigRealmCacBurstRateUtilLevel,
       "apSipInterfaceCacStatsTable": apSipInterfaceCacStatsTable,
       "apSipInterfaceCacStatsEntry": apSipInterfaceCacStatsEntry,
       "apSipInterfaceCacSessionUtilLevel": apSipInterfaceCacSessionUtilLevel,
       "apSipInterfaceCacBurstRateUtilLevel": apSipInterfaceCacBurstRateUtilLevel,
       "apSipNotificationObjects": apSipNotificationObjects,
       "apSipSecInterfaceNotifications": apSipSecInterfaceNotifications,
       "apSipSecIntfNotifObjects": apSipSecIntfNotifObjects,
       "apSipSecIntfNotifPrefix": apSipSecIntfNotifPrefix,
       "apSipSecIntfNotifications": apSipSecIntfNotifications,
       "apSipSecInterfaceRegThresholdExceededTrap": apSipSecInterfaceRegThresholdExceededTrap,
       "apSipSecInterfaceRegThresholdClearTrap": apSipSecInterfaceRegThresholdClearTrap,
       "apSipSurvivabilityNotif": apSipSurvivabilityNotif,
       "apSipSurvivabilityNotifObjects": apSipSurvivabilityNotifObjects,
       "apSipSurvivabilityNotifPrefix": apSipSurvivabilityNotifPrefix,
       "apSipSurvivabilityNotifications": apSipSurvivabilityNotifications,
       "apSipSurvivabilityModeEnter": apSipSurvivabilityModeEnter,
       "apSipSurvivabilityModeExit": apSipSurvivabilityModeExit,
       "apSipCACUtilNotif": apSipCACUtilNotif,
       "apSipCACUtilNotifObjects": apSipCACUtilNotifObjects,
       "apSipCACUtilTrapType": apSipCACUtilTrapType,
       "apSipCACUtilTrapValue": apSipCACUtilTrapValue,
       "apSipCACUtilNotifPrefix": apSipCACUtilNotifPrefix,
       "apSipCACUtilNotifications": apSipCACUtilNotifications,
       "apSipCACUtilAlertTrap": apSipCACUtilAlertTrap,
       "apSipCACUtilClearTrap": apSipCACUtilClearTrap,
       "apSipConformance": apSipConformance,
       "apSipObjectGroups": apSipObjectGroups,
       "apSipSecInterfaceRegObjectsGroup": apSipSecInterfaceRegObjectsGroup,
       "apSipRateStatsGroup": apSipRateStatsGroup,
       "apSipCACStatsGroup": apSipCACStatsGroup,
       "apSipCACStatsSubGroup": apSipCACStatsSubGroup,
       "apSipNotificationGroups": apSipNotificationGroups,
       "apSipSecInterfaceRegNotificationsGroup": apSipSecInterfaceRegNotificationsGroup,
       "apSipSurvivabilityNotificationsGroup": apSipSurvivabilityNotificationsGroup,
       "apSipCACNotificationsGroup": apSipCACNotificationsGroup,
       "apSipRecNotificationGroup": apSipRecNotificationGroup,
       "apSipRecModule": apSipRecModule,
       "apSipRecNotifications": apSipRecNotifications,
       "apSipRecNotificationPrefix": apSipRecNotificationPrefix,
       "apSipRecRecDlgFailNotify": apSipRecRecDlgFailNotify,
       "apSipRecCommSessionNotify": apSipRecCommSessionNotify,
       "apSipRecNotifyObjects": apSipRecNotifyObjects,
       "apSipRecRecDlgCallIdHeader": apSipRecRecDlgCallIdHeader,
       "apSipRecRecDlgToHeader": apSipRecRecDlgToHeader,
       "apSipRecRecDlgFromHeader": apSipRecRecDlgFromHeader,
       "apSipRecCommSessCallIdHeader": apSipRecCommSessCallIdHeader,
       "apSipRecCommSessToHeader": apSipRecCommSessToHeader,
       "apSipRecCommSessFromHeader": apSipRecCommSessFromHeader}
)
