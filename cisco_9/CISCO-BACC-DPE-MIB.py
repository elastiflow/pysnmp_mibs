# SNMP MIB module (CISCO-BACC-DPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-BACC-DPE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:08:31 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBaccDpeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345)
)
if mibBuilder.loadTexts:
    ciscoBaccDpeMIB.setRevisions(
        ("2005-09-02 00:00",
         "2004-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoBaccProvGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBaccDpeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBaccDpeMIBObjects = _CiscoBaccDpeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1)
)
_CiscoBaccDpeSystem_ObjectIdentity = ObjectIdentity
ciscoBaccDpeSystem = _CiscoBaccDpeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 1)
)
_CbdRduName_Type = SnmpAdminString
_CbdRduName_Object = MibScalar
cbdRduName = _CbdRduName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 1, 1),
    _CbdRduName_Type()
)
cbdRduName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduName.setStatus("current")
_CbdRduPort_Type = InetPortNumber
_CbdRduPort_Object = MibScalar
cbdRduPort = _CbdRduPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 1, 2),
    _CbdRduPort_Type()
)
cbdRduPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduPort.setStatus("current")
_CbdPacketCableEnabled_Type = TruthValue
_CbdPacketCableEnabled_Object = MibScalar
cbdPacketCableEnabled = _CbdPacketCableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 1, 3),
    _CbdPacketCableEnabled_Type()
)
cbdPacketCableEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdPacketCableEnabled.setStatus("current")
_CiscoBaccDpeResource_ObjectIdentity = ObjectIdentity
ciscoBaccDpeResource = _CiscoBaccDpeResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2)
)
_CbdProvGroupTable_Object = MibTable
cbdProvGroupTable = _CbdProvGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbdProvGroupTable.setStatus("current")
_CbdProvGroupEntry_Object = MibTableRow
cbdProvGroupEntry = _CbdProvGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1, 1)
)
cbdProvGroupEntry.setIndexNames(
    (0, "CISCO-BACC-DPE-MIB", "cbdProvGroupIndex"),
)
if mibBuilder.loadTexts:
    cbdProvGroupEntry.setStatus("current")
_CbdProvGroupIndex_Type = Unsigned32
_CbdProvGroupIndex_Object = MibTableColumn
cbdProvGroupIndex = _CbdProvGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1, 1, 1),
    _CbdProvGroupIndex_Type()
)
cbdProvGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbdProvGroupIndex.setStatus("current")
_CbdProvGroupType_Type = CiscoBaccProvGroupType
_CbdProvGroupType_Object = MibTableColumn
cbdProvGroupType = _CbdProvGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1, 1, 2),
    _CbdProvGroupType_Type()
)
cbdProvGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProvGroupType.setStatus("current")
_CbdProvGroupName_Type = SnmpAdminString
_CbdProvGroupName_Object = MibTableColumn
cbdProvGroupName = _CbdProvGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1, 1, 3),
    _CbdProvGroupName_Type()
)
cbdProvGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProvGroupName.setStatus("current")
_CbdProvGroupNumDeviceConfig_Type = Gauge32
_CbdProvGroupNumDeviceConfig_Object = MibTableColumn
cbdProvGroupNumDeviceConfig = _CbdProvGroupNumDeviceConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 1, 1, 4),
    _CbdProvGroupNumDeviceConfig_Type()
)
cbdProvGroupNumDeviceConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProvGroupNumDeviceConfig.setStatus("current")
_CbdProtocolServerTable_Object = MibTable
cbdProtocolServerTable = _CbdProtocolServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cbdProtocolServerTable.setStatus("current")
_CbdProtocolServerEntry_Object = MibTableRow
cbdProtocolServerEntry = _CbdProtocolServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1)
)
cbdProtocolServerEntry.setIndexNames(
    (0, "CISCO-BACC-DPE-MIB", "cbdProtocolServerIndex"),
)
if mibBuilder.loadTexts:
    cbdProtocolServerEntry.setStatus("current")
_CbdProtocolServerIndex_Type = Unsigned32
_CbdProtocolServerIndex_Object = MibTableColumn
cbdProtocolServerIndex = _CbdProtocolServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 1),
    _CbdProtocolServerIndex_Type()
)
cbdProtocolServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbdProtocolServerIndex.setStatus("current")
_CbdProtocolServerEnabled_Type = TruthValue
_CbdProtocolServerEnabled_Object = MibTableColumn
cbdProtocolServerEnabled = _CbdProtocolServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 2),
    _CbdProtocolServerEnabled_Type()
)
cbdProtocolServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerEnabled.setStatus("current")
_CbdProtocolServerProtocol_Type = SnmpAdminString
_CbdProtocolServerProtocol_Object = MibTableColumn
cbdProtocolServerProtocol = _CbdProtocolServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 3),
    _CbdProtocolServerProtocol_Type()
)
cbdProtocolServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerProtocol.setStatus("current")
_CbdProtocolServerPktsReceived_Type = Counter32
_CbdProtocolServerPktsReceived_Object = MibTableColumn
cbdProtocolServerPktsReceived = _CbdProtocolServerPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 4),
    _CbdProtocolServerPktsReceived_Type()
)
cbdProtocolServerPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerPktsReceived.setStatus("current")
_CbdProtocolServerPktsDropped_Type = Counter32
_CbdProtocolServerPktsDropped_Object = MibTableColumn
cbdProtocolServerPktsDropped = _CbdProtocolServerPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 5),
    _CbdProtocolServerPktsDropped_Type()
)
cbdProtocolServerPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerPktsDropped.setStatus("current")
_CbdProtocolServerSuccesses_Type = Counter32
_CbdProtocolServerSuccesses_Object = MibTableColumn
cbdProtocolServerSuccesses = _CbdProtocolServerSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 6),
    _CbdProtocolServerSuccesses_Type()
)
cbdProtocolServerSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerSuccesses.setStatus("current")
_CbdProtocolServerFailures_Type = Counter32
_CbdProtocolServerFailures_Object = MibTableColumn
cbdProtocolServerFailures = _CbdProtocolServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 2, 2, 1, 7),
    _CbdProtocolServerFailures_Type()
)
cbdProtocolServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdProtocolServerFailures.setStatus("current")
_CiscoBaccDpeStatistics_ObjectIdentity = ObjectIdentity
ciscoBaccDpeStatistics = _CiscoBaccDpeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3)
)
_CiscoBaccDpeCfgCache_ObjectIdentity = ObjectIdentity
ciscoBaccDpeCfgCache = _CiscoBaccDpeCfgCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 1)
)
_CbdConfigs_Type = Gauge32
_CbdConfigs_Object = MibScalar
cbdConfigs = _CbdConfigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 1, 1),
    _CbdConfigs_Type()
)
cbdConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdConfigs.setStatus("current")
_CbdCacheHits_Type = Counter32
_CbdCacheHits_Object = MibScalar
cbdCacheHits = _CbdCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 1, 2),
    _CbdCacheHits_Type()
)
cbdCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCacheHits.setStatus("current")
_CbdCacheMisses_Type = Counter32
_CbdCacheMisses_Object = MibScalar
cbdCacheMisses = _CbdCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 1, 3),
    _CbdCacheMisses_Type()
)
cbdCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCacheMisses.setStatus("current")
_CbdFiles_Type = Unsigned32
_CbdFiles_Object = MibScalar
cbdFiles = _CbdFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 1, 4),
    _CbdFiles_Type()
)
cbdFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdFiles.setStatus("current")
_CiscoBaccDpePacketCable_ObjectIdentity = ObjectIdentity
ciscoBaccDpePacketCable = _CiscoBaccDpePacketCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2)
)
_CbdInformSuccesses_Type = Counter32
_CbdInformSuccesses_Object = MibScalar
cbdInformSuccesses = _CbdInformSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 1),
    _CbdInformSuccesses_Type()
)
cbdInformSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdInformSuccesses.setStatus("current")
_CbdSNMPSetSuccesses_Type = Counter32
_CbdSNMPSetSuccesses_Object = MibScalar
cbdSNMPSetSuccesses = _CbdSNMPSetSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 2),
    _CbdSNMPSetSuccesses_Type()
)
cbdSNMPSetSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdSNMPSetSuccesses.setStatus("current")
_CbdCfgInformSuccesses_Type = Counter32
_CbdCfgInformSuccesses_Object = MibScalar
cbdCfgInformSuccesses = _CbdCfgInformSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 3),
    _CbdCfgInformSuccesses_Type()
)
cbdCfgInformSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgInformSuccesses.setStatus("current")
_CbdCfgInformFailures_Type = Counter32
_CbdCfgInformFailures_Object = MibScalar
cbdCfgInformFailures = _CbdCfgInformFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 4),
    _CbdCfgInformFailures_Type()
)
cbdCfgInformFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgInformFailures.setStatus("current")
_CbdCfgApReqMessages_Type = Counter32
_CbdCfgApReqMessages_Object = MibScalar
cbdCfgApReqMessages = _CbdCfgApReqMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 5),
    _CbdCfgApReqMessages_Type()
)
cbdCfgApReqMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgApReqMessages.setStatus("current")
_CbdCfgApRepMessages_Type = Counter32
_CbdCfgApRepMessages_Object = MibScalar
cbdCfgApRepMessages = _CbdCfgApRepMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 6),
    _CbdCfgApRepMessages_Type()
)
cbdCfgApRepMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgApRepMessages.setStatus("current")
_CbdCfgFqdnReqMessages_Type = Counter32
_CbdCfgFqdnReqMessages_Object = MibScalar
cbdCfgFqdnReqMessages = _CbdCfgFqdnReqMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 7),
    _CbdCfgFqdnReqMessages_Type()
)
cbdCfgFqdnReqMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgFqdnReqMessages.setStatus("current")
_CbdCfgFqdnRepMessages_Type = Counter32
_CbdCfgFqdnRepMessages_Object = MibScalar
cbdCfgFqdnRepMessages = _CbdCfgFqdnRepMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 2, 8),
    _CbdCfgFqdnRepMessages_Type()
)
cbdCfgFqdnRepMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdCfgFqdnRepMessages.setStatus("current")
_CiscoBaccDpeRdu_ObjectIdentity = ObjectIdentity
ciscoBaccDpeRdu = _CiscoBaccDpeRdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3)
)
_CbdRduInMessages_Type = Counter32
_CbdRduInMessages_Object = MibScalar
cbdRduInMessages = _CbdRduInMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 1),
    _CbdRduInMessages_Type()
)
cbdRduInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduInMessages.setStatus("current")
_CbdRduOutMessages_Type = Counter32
_CbdRduOutMessages_Object = MibScalar
cbdRduOutMessages = _CbdRduOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 2),
    _CbdRduOutMessages_Type()
)
cbdRduOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduOutMessages.setStatus("current")
_CbdRduInMsgAvgSize_Type = Gauge32
_CbdRduInMsgAvgSize_Object = MibScalar
cbdRduInMsgAvgSize = _CbdRduInMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 3),
    _CbdRduInMsgAvgSize_Type()
)
cbdRduInMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduInMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduInMsgAvgSize.setUnits("bytes")
_CbdRduOutMsgAvgSize_Type = Gauge32
_CbdRduOutMsgAvgSize_Object = MibScalar
cbdRduOutMsgAvgSize = _CbdRduOutMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 4),
    _CbdRduOutMsgAvgSize_Type()
)
cbdRduOutMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduOutMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduOutMsgAvgSize.setUnits("bytes")
_CbdRduInMsgMaxSize_Type = Unsigned32
_CbdRduInMsgMaxSize_Object = MibScalar
cbdRduInMsgMaxSize = _CbdRduInMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 5),
    _CbdRduInMsgMaxSize_Type()
)
cbdRduInMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduInMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduInMsgMaxSize.setUnits("bytes")
_CbdRduInMsgMinSize_Type = Unsigned32
_CbdRduInMsgMinSize_Object = MibScalar
cbdRduInMsgMinSize = _CbdRduInMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 6),
    _CbdRduInMsgMinSize_Type()
)
cbdRduInMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduInMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduInMsgMinSize.setUnits("bytes")
_CbdRduOutMsgMaxSize_Type = Unsigned32
_CbdRduOutMsgMaxSize_Object = MibScalar
cbdRduOutMsgMaxSize = _CbdRduOutMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 7),
    _CbdRduOutMsgMaxSize_Type()
)
cbdRduOutMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduOutMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduOutMsgMaxSize.setUnits("bytes")
_CbdRduOutMsgMinSize_Type = Unsigned32
_CbdRduOutMsgMinSize_Object = MibScalar
cbdRduOutMsgMinSize = _CbdRduOutMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 8),
    _CbdRduOutMsgMinSize_Type()
)
cbdRduOutMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduOutMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduOutMsgMinSize.setUnits("bytes")
_CbdRduAvgTimeToRecv_Type = Gauge32
_CbdRduAvgTimeToRecv_Object = MibScalar
cbdRduAvgTimeToRecv = _CbdRduAvgTimeToRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 9),
    _CbdRduAvgTimeToRecv_Type()
)
cbdRduAvgTimeToRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduAvgTimeToRecv.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduAvgTimeToRecv.setUnits("milli-seconds")
_CbdRduAvgTimeToSend_Type = Gauge32
_CbdRduAvgTimeToSend_Object = MibScalar
cbdRduAvgTimeToSend = _CbdRduAvgTimeToSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 1, 3, 3, 10),
    _CbdRduAvgTimeToSend_Type()
)
cbdRduAvgTimeToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdRduAvgTimeToSend.setStatus("current")
if mibBuilder.loadTexts:
    cbdRduAvgTimeToSend.setUnits("milli-seconds")
_CiscoBaccDpeMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBaccDpeMIBConformance = _CiscoBaccDpeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2)
)
_CiscoBaccDpeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBaccDpeMIBCompliances = _CiscoBaccDpeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 1)
)
_CiscoBaccDpeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBaccDpeMIBGroups = _CiscoBaccDpeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 2)
)

# Managed Objects groups

ciscoBaccDpeBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 2, 1)
)
ciscoBaccDpeBasicGroup.setObjects(
      *(("CISCO-BACC-DPE-MIB", "cbdPacketCableEnabled"),
        ("CISCO-BACC-DPE-MIB", "cbdRduName"),
        ("CISCO-BACC-DPE-MIB", "cbdRduPort"))
)
if mibBuilder.loadTexts:
    ciscoBaccDpeBasicGroup.setStatus("current")

ciscoBaccDpeProvGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 2, 2)
)
ciscoBaccDpeProvGroupGroup.setObjects(
      *(("CISCO-BACC-DPE-MIB", "cbdProvGroupName"),
        ("CISCO-BACC-DPE-MIB", "cbdProvGroupType"),
        ("CISCO-BACC-DPE-MIB", "cbdProvGroupNumDeviceConfig"))
)
if mibBuilder.loadTexts:
    ciscoBaccDpeProvGroupGroup.setStatus("current")

ciscoBaccDpeStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 2, 3)
)
ciscoBaccDpeStatisticsGroup.setObjects(
      *(("CISCO-BACC-DPE-MIB", "cbdCfgInformFailures"),
        ("CISCO-BACC-DPE-MIB", "cbdCfgInformSuccesses"),
        ("CISCO-BACC-DPE-MIB", "cbdConfigs"),
        ("CISCO-BACC-DPE-MIB", "cbdFiles"),
        ("CISCO-BACC-DPE-MIB", "cbdCacheHits"),
        ("CISCO-BACC-DPE-MIB", "cbdInformSuccesses"),
        ("CISCO-BACC-DPE-MIB", "cbdCacheMisses"),
        ("CISCO-BACC-DPE-MIB", "cbdSNMPSetSuccesses"),
        ("CISCO-BACC-DPE-MIB", "cbdCfgApReqMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdCfgApRepMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdCfgFqdnReqMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdCfgFqdnRepMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerEnabled"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerProtocol"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerPktsReceived"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerPktsDropped"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerSuccesses"),
        ("CISCO-BACC-DPE-MIB", "cbdProtocolServerFailures"))
)
if mibBuilder.loadTexts:
    ciscoBaccDpeStatisticsGroup.setStatus("current")

ciscoBaccDpeRduStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 2, 4)
)
ciscoBaccDpeRduStatisticsGroup.setObjects(
      *(("CISCO-BACC-DPE-MIB", "cbdRduInMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdRduOutMessages"),
        ("CISCO-BACC-DPE-MIB", "cbdRduInMsgAvgSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduOutMsgAvgSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduInMsgMaxSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduInMsgMinSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduOutMsgMaxSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduOutMsgMinSize"),
        ("CISCO-BACC-DPE-MIB", "cbdRduAvgTimeToRecv"),
        ("CISCO-BACC-DPE-MIB", "cbdRduAvgTimeToSend"))
)
if mibBuilder.loadTexts:
    ciscoBaccDpeRduStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBaccDpeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 345, 2, 1, 1)
)
ciscoBaccDpeMIBCompliance.setObjects(
      *(("CISCO-BACC-DPE-MIB", "ciscoBaccDpeBasicGroup"),
        ("CISCO-BACC-DPE-MIB", "ciscoBaccDpeStatisticsGroup"),
        ("CISCO-BACC-DPE-MIB", "ciscoBaccDpeProvGroupGroup"),
        ("CISCO-BACC-DPE-MIB", "ciscoBaccDpeRduStatisticsGroup"))
)
if mibBuilder.loadTexts:
    ciscoBaccDpeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BACC-DPE-MIB",
    **{"CiscoBaccProvGroupType": CiscoBaccProvGroupType,
       "ciscoBaccDpeMIB": ciscoBaccDpeMIB,
       "ciscoBaccDpeMIBObjects": ciscoBaccDpeMIBObjects,
       "ciscoBaccDpeSystem": ciscoBaccDpeSystem,
       "cbdRduName": cbdRduName,
       "cbdRduPort": cbdRduPort,
       "cbdPacketCableEnabled": cbdPacketCableEnabled,
       "ciscoBaccDpeResource": ciscoBaccDpeResource,
       "cbdProvGroupTable": cbdProvGroupTable,
       "cbdProvGroupEntry": cbdProvGroupEntry,
       "cbdProvGroupIndex": cbdProvGroupIndex,
       "cbdProvGroupType": cbdProvGroupType,
       "cbdProvGroupName": cbdProvGroupName,
       "cbdProvGroupNumDeviceConfig": cbdProvGroupNumDeviceConfig,
       "cbdProtocolServerTable": cbdProtocolServerTable,
       "cbdProtocolServerEntry": cbdProtocolServerEntry,
       "cbdProtocolServerIndex": cbdProtocolServerIndex,
       "cbdProtocolServerEnabled": cbdProtocolServerEnabled,
       "cbdProtocolServerProtocol": cbdProtocolServerProtocol,
       "cbdProtocolServerPktsReceived": cbdProtocolServerPktsReceived,
       "cbdProtocolServerPktsDropped": cbdProtocolServerPktsDropped,
       "cbdProtocolServerSuccesses": cbdProtocolServerSuccesses,
       "cbdProtocolServerFailures": cbdProtocolServerFailures,
       "ciscoBaccDpeStatistics": ciscoBaccDpeStatistics,
       "ciscoBaccDpeCfgCache": ciscoBaccDpeCfgCache,
       "cbdConfigs": cbdConfigs,
       "cbdCacheHits": cbdCacheHits,
       "cbdCacheMisses": cbdCacheMisses,
       "cbdFiles": cbdFiles,
       "ciscoBaccDpePacketCable": ciscoBaccDpePacketCable,
       "cbdInformSuccesses": cbdInformSuccesses,
       "cbdSNMPSetSuccesses": cbdSNMPSetSuccesses,
       "cbdCfgInformSuccesses": cbdCfgInformSuccesses,
       "cbdCfgInformFailures": cbdCfgInformFailures,
       "cbdCfgApReqMessages": cbdCfgApReqMessages,
       "cbdCfgApRepMessages": cbdCfgApRepMessages,
       "cbdCfgFqdnReqMessages": cbdCfgFqdnReqMessages,
       "cbdCfgFqdnRepMessages": cbdCfgFqdnRepMessages,
       "ciscoBaccDpeRdu": ciscoBaccDpeRdu,
       "cbdRduInMessages": cbdRduInMessages,
       "cbdRduOutMessages": cbdRduOutMessages,
       "cbdRduInMsgAvgSize": cbdRduInMsgAvgSize,
       "cbdRduOutMsgAvgSize": cbdRduOutMsgAvgSize,
       "cbdRduInMsgMaxSize": cbdRduInMsgMaxSize,
       "cbdRduInMsgMinSize": cbdRduInMsgMinSize,
       "cbdRduOutMsgMaxSize": cbdRduOutMsgMaxSize,
       "cbdRduOutMsgMinSize": cbdRduOutMsgMinSize,
       "cbdRduAvgTimeToRecv": cbdRduAvgTimeToRecv,
       "cbdRduAvgTimeToSend": cbdRduAvgTimeToSend,
       "ciscoBaccDpeMIBConformance": ciscoBaccDpeMIBConformance,
       "ciscoBaccDpeMIBCompliances": ciscoBaccDpeMIBCompliances,
       "ciscoBaccDpeMIBCompliance": ciscoBaccDpeMIBCompliance,
       "ciscoBaccDpeMIBGroups": ciscoBaccDpeMIBGroups,
       "ciscoBaccDpeBasicGroup": ciscoBaccDpeBasicGroup,
       "ciscoBaccDpeProvGroupGroup": ciscoBaccDpeProvGroupGroup,
       "ciscoBaccDpeStatisticsGroup": ciscoBaccDpeStatisticsGroup,
       "ciscoBaccDpeRduStatisticsGroup": ciscoBaccDpeRduStatisticsGroup}
)
