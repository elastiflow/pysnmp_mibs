# SNMP MIB module (CISCO-SSH-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/CISCO-SSH-INFO-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

(ciscoMibs,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMibs")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ssh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SshBoardState(TextualConvention, Integer32):
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
        *(("fail", 1),
          ("active", 2),
          ("inactive", 3),
          ("reset", 4))
    )



class SshChipState(TextualConvention, Integer32):
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
        *(("fail", 1),
          ("active", 2),
          ("unknown", 3),
          ("missing", 4))
    )



class SshServerState(TextualConvention, Integer32):
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
        *(("fail", 1),
          ("active", 2),
          ("inactive", 3),
          ("noBoards", 4))
    )



# MIB Managed Objects in the order of their OIDs

_SshServer_ObjectIdentity = ObjectIdentity
sshServer = _SshServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1)
)
_SshBoardCount_Type = Integer32
_SshBoardCount_Object = MibScalar
sshBoardCount = _SshBoardCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 1),
    _SshBoardCount_Type()
)
sshBoardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardCount.setStatus("current")
_SshChipCount_Type = Integer32
_SshChipCount_Object = MibScalar
sshChipCount = _SshChipCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 2),
    _SshChipCount_Type()
)
sshChipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipCount.setStatus("current")
_SshRequestCount_Type = Gauge32
_SshRequestCount_Object = MibScalar
sshRequestCount = _SshRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 3),
    _SshRequestCount_Type()
)
sshRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRequestCount.setStatus("current")
_SshFailureCount_Type = Counter32
_SshFailureCount_Object = MibScalar
sshFailureCount = _SshFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 4),
    _SshFailureCount_Type()
)
sshFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshFailureCount.setStatus("current")
_SshState_Type = SshServerState
_SshState_Object = MibScalar
sshState = _SshState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 5),
    _SshState_Type()
)
sshState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshState.setStatus("current")
_SshUpTime_Type = Gauge32
_SshUpTime_Object = MibScalar
sshUpTime = _SshUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 6),
    _SshUpTime_Type()
)
sshUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sshUpTime.setUnits("centi-seconds")
_SshClearStatistics_Type = Integer32
_SshClearStatistics_Object = MibScalar
sshClearStatistics = _SshClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 7),
    _SshClearStatistics_Type()
)
sshClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClearStatistics.setStatus("current")
_SshStatsUpTime_Type = Gauge32
_SshStatsUpTime_Object = MibScalar
sshStatsUpTime = _SshStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 8),
    _SshStatsUpTime_Type()
)
sshStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshStatsUpTime.setStatus("current")
_SshResponseFailurePacketCount_Type = Counter32
_SshResponseFailurePacketCount_Object = MibScalar
sshResponseFailurePacketCount = _SshResponseFailurePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 9),
    _SshResponseFailurePacketCount_Type()
)
sshResponseFailurePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshResponseFailurePacketCount.setStatus("current")
_SshUdpPort_Type = Integer32
_SshUdpPort_Object = MibScalar
sshUdpPort = _SshUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 10),
    _SshUdpPort_Type()
)
sshUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUdpPort.setStatus("current")
_SshTftpServer_Type = DisplayString
_SshTftpServer_Object = MibScalar
sshTftpServer = _SshTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 11),
    _SshTftpServer_Type()
)
sshTftpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshTftpServer.setStatus("current")
_SshNumChipTypes_Type = Integer32
_SshNumChipTypes_Object = MibScalar
sshNumChipTypes = _SshNumChipTypes_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 12),
    _SshNumChipTypes_Type()
)
sshNumChipTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshNumChipTypes.setStatus("current")
_SshSWQLoad_Type = Gauge32
_SshSWQLoad_Object = MibScalar
sshSWQLoad = _SshSWQLoad_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 1, 13),
    _SshSWQLoad_Type()
)
sshSWQLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSWQLoad.setStatus("current")
_SshBoard_ObjectIdentity = ObjectIdentity
sshBoard = _SshBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2)
)
_SshBoardTable_Object = MibTable
sshBoardTable = _SshBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1)
)
if mibBuilder.loadTexts:
    sshBoardTable.setStatus("current")
_SshBoardEntry_Object = MibTableRow
sshBoardEntry = _SshBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1)
)
sshBoardEntry.setIndexNames(
    (0, "CISCO-SSH-INFO-MIB", "sshBoardIndex"),
)
if mibBuilder.loadTexts:
    sshBoardEntry.setStatus("current")
_SshBoardIndex_Type = Integer32
_SshBoardIndex_Object = MibTableColumn
sshBoardIndex = _SshBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 1),
    _SshBoardIndex_Type()
)
sshBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshBoardIndex.setStatus("current")
_SshBoardSerialNumber_Type = Integer32
_SshBoardSerialNumber_Object = MibTableColumn
sshBoardSerialNumber = _SshBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 2),
    _SshBoardSerialNumber_Type()
)
sshBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardSerialNumber.setStatus("current")
_SshBoardState_Type = SshBoardState
_SshBoardState_Object = MibTableColumn
sshBoardState = _SshBoardState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 3),
    _SshBoardState_Type()
)
sshBoardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardState.setStatus("current")
_SshBoardVersion_Type = DisplayString
_SshBoardVersion_Object = MibTableColumn
sshBoardVersion = _SshBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 4),
    _SshBoardVersion_Type()
)
sshBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardVersion.setStatus("current")


class _SshBoardMode_Type(Integer32):
    """Custom type sshBoardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_SshBoardMode_Type.__name__ = "Integer32"
_SshBoardMode_Object = MibTableColumn
sshBoardMode = _SshBoardMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 5),
    _SshBoardMode_Type()
)
sshBoardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardMode.setStatus("current")
_SshBoardRequestCount_Type = Gauge32
_SshBoardRequestCount_Object = MibTableColumn
sshBoardRequestCount = _SshBoardRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 6),
    _SshBoardRequestCount_Type()
)
sshBoardRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardRequestCount.setStatus("current")
_SshBoardFailureCount_Type = Counter32
_SshBoardFailureCount_Object = MibTableColumn
sshBoardFailureCount = _SshBoardFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 7),
    _SshBoardFailureCount_Type()
)
sshBoardFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardFailureCount.setStatus("current")
_SshBoardUpTime_Type = Gauge32
_SshBoardUpTime_Object = MibTableColumn
sshBoardUpTime = _SshBoardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 8),
    _SshBoardUpTime_Type()
)
sshBoardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardUpTime.setStatus("current")
_SshBoardChipNum_Type = Integer32
_SshBoardChipNum_Object = MibTableColumn
sshBoardChipNum = _SshBoardChipNum_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 9),
    _SshBoardChipNum_Type()
)
sshBoardChipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardChipNum.setStatus("current")
_SshBoardCpu2SccVersion_Type = OctetString
_SshBoardCpu2SccVersion_Object = MibTableColumn
sshBoardCpu2SccVersion = _SshBoardCpu2SccVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 10),
    _SshBoardCpu2SccVersion_Type()
)
sshBoardCpu2SccVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardCpu2SccVersion.setStatus("current")
_SshBoardUptimeSec_Type = Gauge32
_SshBoardUptimeSec_Object = MibTableColumn
sshBoardUptimeSec = _SshBoardUptimeSec_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 11),
    _SshBoardUptimeSec_Type()
)
sshBoardUptimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardUptimeSec.setStatus("current")
_SshBoardRequestCountMSW_Type = Gauge32
_SshBoardRequestCountMSW_Object = MibTableColumn
sshBoardRequestCountMSW = _SshBoardRequestCountMSW_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 2, 1, 1, 12),
    _SshBoardRequestCountMSW_Type()
)
sshBoardRequestCountMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshBoardRequestCountMSW.setStatus("current")
_SshChip_ObjectIdentity = ObjectIdentity
sshChip = _SshChip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3)
)
_SshChipTable_Object = MibTable
sshChipTable = _SshChipTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1)
)
if mibBuilder.loadTexts:
    sshChipTable.setStatus("current")
_SshChipEntry_Object = MibTableRow
sshChipEntry = _SshChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1)
)
sshChipEntry.setIndexNames(
    (0, "CISCO-SSH-INFO-MIB", "sshBoardIndex"),
    (0, "CISCO-SSH-INFO-MIB", "sshChipIndex"),
)
if mibBuilder.loadTexts:
    sshChipEntry.setStatus("current")
_SshChipIndex_Type = Integer32
_SshChipIndex_Object = MibTableColumn
sshChipIndex = _SshChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 1),
    _SshChipIndex_Type()
)
sshChipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshChipIndex.setStatus("current")
_SshChipTypeVal_Type = Integer32
_SshChipTypeVal_Object = MibTableColumn
sshChipTypeVal = _SshChipTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 2),
    _SshChipTypeVal_Type()
)
sshChipTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipTypeVal.setStatus("current")
_SshChipState_Type = SshChipState
_SshChipState_Object = MibTableColumn
sshChipState = _SshChipState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 3),
    _SshChipState_Type()
)
sshChipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipState.setStatus("current")
_SshChipUtilizationRatio_Type = Integer32
_SshChipUtilizationRatio_Object = MibTableColumn
sshChipUtilizationRatio = _SshChipUtilizationRatio_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 4),
    _SshChipUtilizationRatio_Type()
)
sshChipUtilizationRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipUtilizationRatio.setStatus("current")
_SshChipResetResponse_Type = DisplayString
_SshChipResetResponse_Object = MibTableColumn
sshChipResetResponse = _SshChipResetResponse_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 5),
    _SshChipResetResponse_Type()
)
sshChipResetResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipResetResponse.setStatus("current")
_SshChipSignatureCount_Type = Gauge32
_SshChipSignatureCount_Object = MibTableColumn
sshChipSignatureCount = _SshChipSignatureCount_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 6),
    _SshChipSignatureCount_Type()
)
sshChipSignatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipSignatureCount.setStatus("current")
_SshChipRequestCountMSW_Type = Gauge32
_SshChipRequestCountMSW_Object = MibTableColumn
sshChipRequestCountMSW = _SshChipRequestCountMSW_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 7),
    _SshChipRequestCountMSW_Type()
)
sshChipRequestCountMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipRequestCountMSW.setStatus("current")
_SshChipLatency_Type = Integer32
_SshChipLatency_Object = MibTableColumn
sshChipLatency = _SshChipLatency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 3, 1, 1, 8),
    _SshChipLatency_Type()
)
sshChipLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshChipLatency.setStatus("current")
_SshNotifications_ObjectIdentity = ObjectIdentity
sshNotifications = _SshNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4)
)
_SshNotificationsV2_ObjectIdentity = ObjectIdentity
sshNotificationsV2 = _SshNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0)
)
_SshChipType_ObjectIdentity = ObjectIdentity
sshChipType = _SshChipType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 5)
)
_SshChipTypeInfoTable_Object = MibTable
sshChipTypeInfoTable = _SshChipTypeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 5, 1)
)
if mibBuilder.loadTexts:
    sshChipTypeInfoTable.setStatus("current")
_SshConformance_ObjectIdentity = ObjectIdentity
sshConformance = _SshConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 6)
)

# Managed Objects groups

sshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 6, 1)
)
sshGroup.setObjects(
      *(("CISCO-SSH-INFO-MIB", "sshBoardCount"),
        ("CISCO-SSH-INFO-MIB", "sshChipCount"),
        ("CISCO-SSH-INFO-MIB", "sshFailureCount"),
        ("CISCO-SSH-INFO-MIB", "sshRequestCount"),
        ("CISCO-SSH-INFO-MIB", "sshState"),
        ("CISCO-SSH-INFO-MIB", "sshClearStatistics"),
        ("CISCO-SSH-INFO-MIB", "sshStatsUpTime"),
        ("CISCO-SSH-INFO-MIB", "sshResponseFailurePacketCount"),
        ("CISCO-SSH-INFO-MIB", "sshUdpPort"),
        ("CISCO-SSH-INFO-MIB", "sshBoardIndex"),
        ("CISCO-SSH-INFO-MIB", "sshBoardSerialNumber"),
        ("CISCO-SSH-INFO-MIB", "sshBoardState"),
        ("CISCO-SSH-INFO-MIB", "sshBoardVersion"),
        ("CISCO-SSH-INFO-MIB", "sshBoardMode"),
        ("CISCO-SSH-INFO-MIB", "sshBoardRequestCount"),
        ("CISCO-SSH-INFO-MIB", "sshBoardFailureCount"),
        ("CISCO-SSH-INFO-MIB", "sshBoardUpTime"),
        ("CISCO-SSH-INFO-MIB", "sshBoardChipNum"),
        ("CISCO-SSH-INFO-MIB", "sshBoardCpu2SccVersion"),
        ("CISCO-SSH-INFO-MIB", "sshChipIndex"),
        ("CISCO-SSH-INFO-MIB", "sshChipType"),
        ("CISCO-SSH-INFO-MIB", "sshChipState"),
        ("CISCO-SSH-INFO-MIB", "sshChipUtilizationRatio"),
        ("CISCO-SSH-INFO-MIB", "sshChipResetResponse"))
)
if mibBuilder.loadTexts:
    sshGroup.setStatus("current")


# Notification objects

sshBoardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 1)
)
sshBoardUp.setObjects(
    ("CISCO-SSH-INFO-MIB", "sshBoardIndex")
)
if mibBuilder.loadTexts:
    sshBoardUp.setStatus(
        "current"
    )

sshBoardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 2)
)
sshBoardFail.setObjects(
    ("CISCO-SSH-INFO-MIB", "sshBoardIndex")
)
if mibBuilder.loadTexts:
    sshBoardFail.setStatus(
        "current"
    )

sshBoardInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 3)
)
sshBoardInactive.setObjects(
    ("CISCO-SSH-INFO-MIB", "sshBoardIndex")
)
if mibBuilder.loadTexts:
    sshBoardInactive.setStatus(
        "current"
    )

sshBoardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 4)
)
sshBoardReset.setObjects(
    ("CISCO-SSH-INFO-MIB", "sshBoardIndex")
)
if mibBuilder.loadTexts:
    sshBoardReset.setStatus(
        "current"
    )

sshChipUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 5)
)
sshChipUp.setObjects(
      *(("CISCO-SSH-INFO-MIB", "sshBoardIndex"),
        ("CISCO-SSH-INFO-MIB", "sshChipIndex"))
)
if mibBuilder.loadTexts:
    sshChipUp.setStatus(
        "current"
    )

sshChipFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 6)
)
sshChipFail.setObjects(
      *(("CISCO-SSH-INFO-MIB", "sshBoardIndex"),
        ("CISCO-SSH-INFO-MIB", "sshChipIndex"))
)
if mibBuilder.loadTexts:
    sshChipFail.setStatus(
        "current"
    )

sshServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 7)
)
if mibBuilder.loadTexts:
    sshServerUp.setStatus(
        "current"
    )

sshServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 8)
)
if mibBuilder.loadTexts:
    sshServerFail.setStatus(
        "current"
    )

sshServerInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 9)
)
if mibBuilder.loadTexts:
    sshServerInactive.setStatus(
        "current"
    )

sshServerNoChips = NotificationType(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 4, 0, 10)
)
if mibBuilder.loadTexts:
    sshServerNoChips.setStatus(
        "current"
    )


# Notifications groups

sshNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1855, 2, 31, 6, 2)
)
sshNotificationsGroup.setObjects(
      *(("CISCO-SSH-INFO-MIB", "sshBoardUp"),
        ("CISCO-SSH-INFO-MIB", "sshBoardFail"),
        ("CISCO-SSH-INFO-MIB", "sshBoardInactive"),
        ("CISCO-SSH-INFO-MIB", "sshBoardReset"),
        ("CISCO-SSH-INFO-MIB", "sshChipUp"),
        ("CISCO-SSH-INFO-MIB", "sshChipFail"),
        ("CISCO-SSH-INFO-MIB", "sshServerUp"),
        ("CISCO-SSH-INFO-MIB", "sshServerFail"),
        ("CISCO-SSH-INFO-MIB", "sshServerInactive"),
        ("CISCO-SSH-INFO-MIB", "sshServerNoChips"))
)
if mibBuilder.loadTexts:
    sshNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSH-INFO-MIB",
    **{"SshBoardState": SshBoardState,
       "SshChipState": SshChipState,
       "SshServerState": SshServerState,
       "ssh": ssh,
       "sshServer": sshServer,
       "sshBoardCount": sshBoardCount,
       "sshChipCount": sshChipCount,
       "sshRequestCount": sshRequestCount,
       "sshFailureCount": sshFailureCount,
       "sshState": sshState,
       "sshUpTime": sshUpTime,
       "sshClearStatistics": sshClearStatistics,
       "sshStatsUpTime": sshStatsUpTime,
       "sshResponseFailurePacketCount": sshResponseFailurePacketCount,
       "sshUdpPort": sshUdpPort,
       "sshTftpServer": sshTftpServer,
       "sshNumChipTypes": sshNumChipTypes,
       "sshSWQLoad": sshSWQLoad,
       "sshBoard": sshBoard,
       "sshBoardTable": sshBoardTable,
       "sshBoardEntry": sshBoardEntry,
       "sshBoardIndex": sshBoardIndex,
       "sshBoardSerialNumber": sshBoardSerialNumber,
       "sshBoardState": sshBoardState,
       "sshBoardVersion": sshBoardVersion,
       "sshBoardMode": sshBoardMode,
       "sshBoardRequestCount": sshBoardRequestCount,
       "sshBoardFailureCount": sshBoardFailureCount,
       "sshBoardUpTime": sshBoardUpTime,
       "sshBoardChipNum": sshBoardChipNum,
       "sshBoardCpu2SccVersion": sshBoardCpu2SccVersion,
       "sshBoardUptimeSec": sshBoardUptimeSec,
       "sshBoardRequestCountMSW": sshBoardRequestCountMSW,
       "sshChip": sshChip,
       "sshChipTable": sshChipTable,
       "sshChipEntry": sshChipEntry,
       "sshChipIndex": sshChipIndex,
       "sshChipTypeVal": sshChipTypeVal,
       "sshChipState": sshChipState,
       "sshChipUtilizationRatio": sshChipUtilizationRatio,
       "sshChipResetResponse": sshChipResetResponse,
       "sshChipSignatureCount": sshChipSignatureCount,
       "sshChipRequestCountMSW": sshChipRequestCountMSW,
       "sshChipLatency": sshChipLatency,
       "sshNotifications": sshNotifications,
       "sshNotificationsV2": sshNotificationsV2,
       "sshBoardUp": sshBoardUp,
       "sshBoardFail": sshBoardFail,
       "sshBoardInactive": sshBoardInactive,
       "sshBoardReset": sshBoardReset,
       "sshChipUp": sshChipUp,
       "sshChipFail": sshChipFail,
       "sshServerUp": sshServerUp,
       "sshServerFail": sshServerFail,
       "sshServerInactive": sshServerInactive,
       "sshServerNoChips": sshServerNoChips,
       "sshChipType": sshChipType,
       "sshChipTypeInfoTable": sshChipTypeInfoTable,
       "sshConformance": sshConformance,
       "sshGroup": sshGroup,
       "sshNotificationsGroup": sshNotificationsGroup}
)
