# SNMP MIB module (RUIJIE-RNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RNS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieRnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160)
)
if mibBuilder.loadTexts:
    ruijieRnsMIB.setRevisions(
        ("2019-03-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RnsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("icmpEcho", 1),
          ("dns", 2),
          ("tcpConnect", 3),
          ("udpEcho", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RnsBase_ObjectIdentity = ObjectIdentity
rnsBase = _RnsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 1)
)


class _RnsReset_Type(EnabledStatus):
    """Custom type rnsReset based on EnabledStatus"""
    defaultValue = 2


_RnsReset_Type.__name__ = "EnabledStatus"
_RnsReset_Object = MibScalar
rnsReset = _RnsReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 1, 1),
    _RnsReset_Type()
)
rnsReset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsReset.setStatus("current")


class _RnsClearStat_Type(EnabledStatus):
    """Custom type rnsClearStat based on EnabledStatus"""
    defaultValue = 2


_RnsClearStat_Type.__name__ = "EnabledStatus"
_RnsClearStat_Object = MibScalar
rnsClearStat = _RnsClearStat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 1, 2),
    _RnsClearStat_Type()
)
rnsClearStat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsClearStat.setStatus("current")
_RnsNumOfDetectEntry_Type = Integer32
_RnsNumOfDetectEntry_Object = MibScalar
rnsNumOfDetectEntry = _RnsNumOfDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 1, 3),
    _RnsNumOfDetectEntry_Type()
)
rnsNumOfDetectEntry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsNumOfDetectEntry.setStatus("current")


class _RnsSupportDetectType_Type(Bits):
    """Custom type rnsSupportDetectType based on Bits"""
    namedValues = NamedValues(
        *(("icmpEcho", 0),
          ("dns", 1),
          ("tcpConnect", 2),
          ("udpEcho", 3))
    )

_RnsSupportDetectType_Type.__name__ = "Bits"
_RnsSupportDetectType_Object = MibScalar
rnsSupportDetectType = _RnsSupportDetectType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 1, 4),
    _RnsSupportDetectType_Type()
)
rnsSupportDetectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsSupportDetectType.setStatus("current")
_RnsAdmin_ObjectIdentity = ObjectIdentity
rnsAdmin = _RnsAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2)
)
_RnsDetectTable_Object = MibTable
rnsDetectTable = _RnsDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1)
)
if mibBuilder.loadTexts:
    rnsDetectTable.setStatus("current")
_RnsDetectEntry_Object = MibTableRow
rnsDetectEntry = _RnsDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1)
)
rnsDetectEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsDetectId"),
)
if mibBuilder.loadTexts:
    rnsDetectEntry.setStatus("current")
_RnsDetectId_Type = Integer32
_RnsDetectId_Object = MibTableColumn
rnsDetectId = _RnsDetectId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 1),
    _RnsDetectId_Type()
)
rnsDetectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsDetectId.setStatus("current")


class _RnsDetectTag_Type(DisplayString):
    """Custom type rnsDetectTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_RnsDetectTag_Type.__name__ = "DisplayString"
_RnsDetectTag_Object = MibTableColumn
rnsDetectTag = _RnsDetectTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 2),
    _RnsDetectTag_Type()
)
rnsDetectTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectTag.setStatus("current")
_RnsDetectType_Type = RnsType
_RnsDetectType_Object = MibTableColumn
rnsDetectType = _RnsDetectType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 3),
    _RnsDetectType_Type()
)
rnsDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectType.setStatus("current")


class _RnsDetectFrequency_Type(Unsigned32):
    """Custom type rnsDetectFrequency based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800000),
    )


_RnsDetectFrequency_Type.__name__ = "Unsigned32"
_RnsDetectFrequency_Object = MibTableColumn
rnsDetectFrequency = _RnsDetectFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 4),
    _RnsDetectFrequency_Type()
)
rnsDetectFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rnsDetectFrequency.setUnits("millisecond")


class _RnsDetectTimeout_Type(Unsigned32):
    """Custom type rnsDetectTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800000),
    )


_RnsDetectTimeout_Type.__name__ = "Unsigned32"
_RnsDetectTimeout_Object = MibTableColumn
rnsDetectTimeout = _RnsDetectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 5),
    _RnsDetectTimeout_Type()
)
rnsDetectTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rnsDetectTimeout.setUnits("millisecond")


class _RnsDetectThreshold_Type(Unsigned32):
    """Custom type rnsDetectThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_RnsDetectThreshold_Type.__name__ = "Unsigned32"
_RnsDetectThreshold_Object = MibTableColumn
rnsDetectThreshold = _RnsDetectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 6),
    _RnsDetectThreshold_Type()
)
rnsDetectThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rnsDetectThreshold.setUnits("millisecond")
_RnsDetectTargetHost_Type = DisplayString
_RnsDetectTargetHost_Object = MibTableColumn
rnsDetectTargetHost = _RnsDetectTargetHost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 7),
    _RnsDetectTargetHost_Type()
)
rnsDetectTargetHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectTargetHost.setStatus("current")
_RnsDetectTargetPort_Type = InetPortNumber
_RnsDetectTargetPort_Object = MibTableColumn
rnsDetectTargetPort = _RnsDetectTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 8),
    _RnsDetectTargetPort_Type()
)
rnsDetectTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectTargetPort.setStatus("current")
_RnsDetectSourceAddress_Type = InetAddress
_RnsDetectSourceAddress_Object = MibTableColumn
rnsDetectSourceAddress = _RnsDetectSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 9),
    _RnsDetectSourceAddress_Type()
)
rnsDetectSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectSourceAddress.setStatus("current")
_RnsDetectOutInterface_Type = DisplayString
_RnsDetectOutInterface_Object = MibTableColumn
rnsDetectOutInterface = _RnsDetectOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 10),
    _RnsDetectOutInterface_Type()
)
rnsDetectOutInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectOutInterface.setStatus("current")
_RnsDetectIsMgmt_Type = TruthValue
_RnsDetectIsMgmt_Object = MibTableColumn
rnsDetectIsMgmt = _RnsDetectIsMgmt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 11),
    _RnsDetectIsMgmt_Type()
)
rnsDetectIsMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectIsMgmt.setStatus("current")
_RnsDetectNexthopAddressType_Type = InetAddressType
_RnsDetectNexthopAddressType_Object = MibTableColumn
rnsDetectNexthopAddressType = _RnsDetectNexthopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 12),
    _RnsDetectNexthopAddressType_Type()
)
rnsDetectNexthopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectNexthopAddressType.setStatus("current")
_RnsDetectNexthopAddress_Type = InetAddress
_RnsDetectNexthopAddress_Object = MibTableColumn
rnsDetectNexthopAddress = _RnsDetectNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 13),
    _RnsDetectNexthopAddress_Type()
)
rnsDetectNexthopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectNexthopAddress.setStatus("current")
_RnsDetectVrfName_Type = DisplayString
_RnsDetectVrfName_Object = MibTableColumn
rnsDetectVrfName = _RnsDetectVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 14),
    _RnsDetectVrfName_Type()
)
rnsDetectVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectVrfName.setStatus("current")


class _RnsDetectDataSize_Type(Unsigned32):
    """Custom type rnsDetectDataSize based on Unsigned32"""
    defaultValue = 36

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 1472),
    )


_RnsDetectDataSize_Type.__name__ = "Unsigned32"
_RnsDetectDataSize_Object = MibTableColumn
rnsDetectDataSize = _RnsDetectDataSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 15),
    _RnsDetectDataSize_Type()
)
rnsDetectDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectDataSize.setStatus("current")
if mibBuilder.loadTexts:
    rnsDetectDataSize.setUnits("octets")


class _RnsDetectDSField_Type(Unsigned32):
    """Custom type rnsDetectDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RnsDetectDSField_Type.__name__ = "Unsigned32"
_RnsDetectDSField_Object = MibTableColumn
rnsDetectDSField = _RnsDetectDSField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 16),
    _RnsDetectDSField_Type()
)
rnsDetectDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectDSField.setStatus("current")
_RnsDetectStatus_Type = RowStatus
_RnsDetectStatus_Object = MibTableColumn
rnsDetectStatus = _RnsDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 1, 1, 17),
    _RnsDetectStatus_Type()
)
rnsDetectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsDetectStatus.setStatus("current")
_RnsClearStatisTable_Object = MibTable
rnsClearStatisTable = _RnsClearStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 2)
)
if mibBuilder.loadTexts:
    rnsClearStatisTable.setStatus("current")
_RnsClearStatisEntry_Object = MibTableRow
rnsClearStatisEntry = _RnsClearStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 2, 1)
)
rnsClearStatisEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsClearStatisId"),
)
if mibBuilder.loadTexts:
    rnsClearStatisEntry.setStatus("current")
_RnsClearStatisId_Type = Integer32
_RnsClearStatisId_Object = MibTableColumn
rnsClearStatisId = _RnsClearStatisId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 2, 1, 1),
    _RnsClearStatisId_Type()
)
rnsClearStatisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsClearStatisId.setStatus("current")


class _RnsClearStatisClear_Type(Integer32):
    """Custom type rnsClearStatisClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disclear", 0),
          ("clear", 1))
    )


_RnsClearStatisClear_Type.__name__ = "Integer32"
_RnsClearStatisClear_Object = MibTableColumn
rnsClearStatisClear = _RnsClearStatisClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 2, 1, 2),
    _RnsClearStatisClear_Type()
)
rnsClearStatisClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsClearStatisClear.setStatus("current")
_RnsScheduleTable_Object = MibTable
rnsScheduleTable = _RnsScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3)
)
if mibBuilder.loadTexts:
    rnsScheduleTable.setStatus("current")
_RnsScheduleEntry_Object = MibTableRow
rnsScheduleEntry = _RnsScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1)
)
rnsScheduleEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsScheduleId"),
)
if mibBuilder.loadTexts:
    rnsScheduleEntry.setStatus("current")
_RnsScheduleId_Type = Integer32
_RnsScheduleId_Object = MibTableColumn
rnsScheduleId = _RnsScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 1),
    _RnsScheduleId_Type()
)
rnsScheduleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsScheduleId.setStatus("current")


class _RnsScheduleStartType_Type(Integer32):
    """Custom type rnsScheduleStartType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pending", 0),
          ("startNow", 1),
          ("startAt", 2),
          ("startAfter", 3))
    )


_RnsScheduleStartType_Type.__name__ = "Integer32"
_RnsScheduleStartType_Object = MibTableColumn
rnsScheduleStartType = _RnsScheduleStartType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 2),
    _RnsScheduleStartType_Type()
)
rnsScheduleStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsScheduleStartType.setStatus("current")
_RnsScheduleStartTime_Type = DisplayString
_RnsScheduleStartTime_Object = MibTableColumn
rnsScheduleStartTime = _RnsScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 3),
    _RnsScheduleStartTime_Type()
)
rnsScheduleStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsScheduleStartTime.setStatus("current")
_RnsScheduleLife_Type = DisplayString
_RnsScheduleLife_Object = MibTableColumn
rnsScheduleLife = _RnsScheduleLife_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 4),
    _RnsScheduleLife_Type()
)
rnsScheduleLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsScheduleLife.setStatus("current")


class _RnsScheduleRecurring_Type(EnabledStatus):
    """Custom type rnsScheduleRecurring based on EnabledStatus"""
    defaultValue = 2


_RnsScheduleRecurring_Type.__name__ = "EnabledStatus"
_RnsScheduleRecurring_Object = MibTableColumn
rnsScheduleRecurring = _RnsScheduleRecurring_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 5),
    _RnsScheduleRecurring_Type()
)
rnsScheduleRecurring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsScheduleRecurring.setStatus("current")
_RnsScheduleStatus_Type = RowStatus
_RnsScheduleStatus_Object = MibTableColumn
rnsScheduleStatus = _RnsScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 2, 3, 1, 6),
    _RnsScheduleStatus_Type()
)
rnsScheduleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsScheduleStatus.setStatus("current")
_RnsStats_ObjectIdentity = ObjectIdentity
rnsStats = _RnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3)
)
_RnsResultsTable_Object = MibTable
rnsResultsTable = _RnsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1)
)
if mibBuilder.loadTexts:
    rnsResultsTable.setStatus("current")
_RnsResultsEntry_Object = MibTableRow
rnsResultsEntry = _RnsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1)
)
rnsResultsEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsResultsId"),
)
if mibBuilder.loadTexts:
    rnsResultsEntry.setStatus("current")
_RnsResultsId_Type = Integer32
_RnsResultsId_Object = MibTableColumn
rnsResultsId = _RnsResultsId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 1),
    _RnsResultsId_Type()
)
rnsResultsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsId.setStatus("current")


class _RnsResultsLatestStatus_Type(Integer32):
    """Custom type rnsResultsLatestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResult", 0),
          ("success", 1),
          ("failure", 2))
    )


_RnsResultsLatestStatus_Type.__name__ = "Integer32"
_RnsResultsLatestStatus_Object = MibTableColumn
rnsResultsLatestStatus = _RnsResultsLatestStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 2),
    _RnsResultsLatestStatus_Type()
)
rnsResultsLatestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsLatestStatus.setStatus("current")
_RnsResultsSuccessfuls_Type = Counter32
_RnsResultsSuccessfuls_Object = MibTableColumn
rnsResultsSuccessfuls = _RnsResultsSuccessfuls_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 3),
    _RnsResultsSuccessfuls_Type()
)
rnsResultsSuccessfuls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsSuccessfuls.setStatus("current")
_RnsResultsFailures_Type = Counter32
_RnsResultsFailures_Object = MibTableColumn
rnsResultsFailures = _RnsResultsFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 4),
    _RnsResultsFailures_Type()
)
rnsResultsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsFailures.setStatus("current")
_RnsResultsAttempts_Type = Counter32
_RnsResultsAttempts_Object = MibTableColumn
rnsResultsAttempts = _RnsResultsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 5),
    _RnsResultsAttempts_Type()
)
rnsResultsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsAttempts.setStatus("current")
_RnsResultsRttAvg_Type = Gauge32
_RnsResultsRttAvg_Object = MibTableColumn
rnsResultsRttAvg = _RnsResultsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 6),
    _RnsResultsRttAvg_Type()
)
rnsResultsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsRttAvg.setStatus("current")
_RnsResultsRttMin_Type = Gauge32
_RnsResultsRttMin_Object = MibTableColumn
rnsResultsRttMin = _RnsResultsRttMin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 7),
    _RnsResultsRttMin_Type()
)
rnsResultsRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsRttMin.setStatus("current")
_RnsResultsRttMax_Type = Gauge32
_RnsResultsRttMax_Object = MibTableColumn
rnsResultsRttMax = _RnsResultsRttMax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 8),
    _RnsResultsRttMax_Type()
)
rnsResultsRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsRttMax.setStatus("current")
_RnsResultsRTDOverThresholds_Type = Counter32
_RnsResultsRTDOverThresholds_Object = MibTableColumn
rnsResultsRTDOverThresholds = _RnsResultsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 9),
    _RnsResultsRTDOverThresholds_Type()
)
rnsResultsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsRTDOverThresholds.setStatus("current")
_RnsResultsTimeouts_Type = Counter32
_RnsResultsTimeouts_Object = MibTableColumn
rnsResultsTimeouts = _RnsResultsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 10),
    _RnsResultsTimeouts_Type()
)
rnsResultsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsTimeouts.setStatus("current")
_RnsResultsBusies_Type = Counter32
_RnsResultsBusies_Object = MibTableColumn
rnsResultsBusies = _RnsResultsBusies_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 11),
    _RnsResultsBusies_Type()
)
rnsResultsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsBusies.setStatus("current")
_RnsResultsJitter_Type = Counter32
_RnsResultsJitter_Object = MibTableColumn
rnsResultsJitter = _RnsResultsJitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 12),
    _RnsResultsJitter_Type()
)
rnsResultsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsJitter.setStatus("current")
_RnsResultsSquareSumRtt_Type = Gauge32
_RnsResultsSquareSumRtt_Object = MibTableColumn
rnsResultsSquareSumRtt = _RnsResultsSquareSumRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 13),
    _RnsResultsSquareSumRtt_Type()
)
rnsResultsSquareSumRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsSquareSumRtt.setStatus("current")
_RnsResultsLossRatio_Type = DisplayString
_RnsResultsLossRatio_Object = MibTableColumn
rnsResultsLossRatio = _RnsResultsLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 14),
    _RnsResultsLossRatio_Type()
)
rnsResultsLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsLossRatio.setStatus("current")
_RnsResultsLossRatioPermillage_Type = DisplayString
_RnsResultsLossRatioPermillage_Object = MibTableColumn
rnsResultsLossRatioPermillage = _RnsResultsLossRatioPermillage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 15),
    _RnsResultsLossRatioPermillage_Type()
)
rnsResultsLossRatioPermillage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsLossRatioPermillage.setStatus("current")
_RnsResultsNoconnect_Type = Counter32
_RnsResultsNoconnect_Object = MibTableColumn
rnsResultsNoconnect = _RnsResultsNoconnect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 16),
    _RnsResultsNoconnect_Type()
)
rnsResultsNoconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsNoconnect.setStatus("current")
_RnsResultsDisconnect_Type = Counter32
_RnsResultsDisconnect_Object = MibTableColumn
rnsResultsDisconnect = _RnsResultsDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 17),
    _RnsResultsDisconnect_Type()
)
rnsResultsDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsDisconnect.setStatus("current")
_RnsResultsIntervalerr_Type = Counter32
_RnsResultsIntervalerr_Object = MibTableColumn
rnsResultsIntervalerr = _RnsResultsIntervalerr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 18),
    _RnsResultsIntervalerr_Type()
)
rnsResultsIntervalerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsIntervalerr.setStatus("current")
_RnsResultsSeqerr_Type = Counter32
_RnsResultsSeqerr_Object = MibTableColumn
rnsResultsSeqerr = _RnsResultsSeqerr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 19),
    _RnsResultsSeqerr_Type()
)
rnsResultsSeqerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsSeqerr.setStatus("current")
_RnsResultsLastrecvtm_Type = DisplayString
_RnsResultsLastrecvtm_Object = MibTableColumn
rnsResultsLastrecvtm = _RnsResultsLastrecvtm_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 3, 1, 1, 20),
    _RnsResultsLastrecvtm_Type()
)
rnsResultsLastrecvtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsResultsLastrecvtm.setStatus("current")
_RnsServer_ObjectIdentity = ObjectIdentity
rnsServer = _RnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 4)
)


class _RnsServerUdpPort_Type(Integer32):
    """Custom type rnsServerUdpPort based on Integer32"""
    defaultValue = 0


_RnsServerUdpPort_Type.__name__ = "Integer32"
_RnsServerUdpPort_Object = MibScalar
rnsServerUdpPort = _RnsServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 4, 1),
    _RnsServerUdpPort_Type()
)
rnsServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsServerUdpPort.setStatus("current")
_RnsTwampLight_ObjectIdentity = ObjectIdentity
rnsTwampLight = _RnsTwampLight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5)
)
_RnsTwampLightControllerAdmin_ObjectIdentity = ObjectIdentity
rnsTwampLightControllerAdmin = _RnsTwampLightControllerAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1)
)


class _RnsTwampLightClientEnable_Type(Integer32):
    """Custom type rnsTwampLightClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RnsTwampLightClientEnable_Type.__name__ = "Integer32"
_RnsTwampLightClientEnable_Object = MibScalar
rnsTwampLightClientEnable = _RnsTwampLightClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 1),
    _RnsTwampLightClientEnable_Type()
)
rnsTwampLightClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsTwampLightClientEnable.setStatus("current")


class _RnsTwampLightSenderEnable_Type(Integer32):
    """Custom type rnsTwampLightSenderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RnsTwampLightSenderEnable_Type.__name__ = "Integer32"
_RnsTwampLightSenderEnable_Object = MibScalar
rnsTwampLightSenderEnable = _RnsTwampLightSenderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 2),
    _RnsTwampLightSenderEnable_Type()
)
rnsTwampLightSenderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsTwampLightSenderEnable.setStatus("current")
_RnsTwampLightClientTable_Object = MibTable
rnsTwampLightClientTable = _RnsTwampLightClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3)
)
if mibBuilder.loadTexts:
    rnsTwampLightClientTable.setStatus("current")
_RnsTwampLightClientEntry_Object = MibTableRow
rnsTwampLightClientEntry = _RnsTwampLightClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1)
)
rnsTwampLightClientEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsTwampClientSessionId"),
)
if mibBuilder.loadTexts:
    rnsTwampLightClientEntry.setStatus("current")


class _RnsTwampClientSessionId_Type(Integer32):
    """Custom type rnsTwampClientSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampClientSessionId_Type.__name__ = "Integer32"
_RnsTwampClientSessionId_Object = MibTableColumn
rnsTwampClientSessionId = _RnsTwampClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 1),
    _RnsTwampClientSessionId_Type()
)
rnsTwampClientSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampClientSessionId.setStatus("current")
_RnsTwampClientSenderIP_Type = InetAddress
_RnsTwampClientSenderIP_Object = MibTableColumn
rnsTwampClientSenderIP = _RnsTwampClientSenderIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 2),
    _RnsTwampClientSenderIP_Type()
)
rnsTwampClientSenderIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientSenderIP.setStatus("current")
_RnsTwampClientReflectorIP_Type = InetAddress
_RnsTwampClientReflectorIP_Object = MibTableColumn
rnsTwampClientReflectorIP = _RnsTwampClientReflectorIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 3),
    _RnsTwampClientReflectorIP_Type()
)
rnsTwampClientReflectorIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientReflectorIP.setStatus("current")
_RnsTwampClientSenderPort_Type = InetPortNumber
_RnsTwampClientSenderPort_Object = MibTableColumn
rnsTwampClientSenderPort = _RnsTwampClientSenderPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 4),
    _RnsTwampClientSenderPort_Type()
)
rnsTwampClientSenderPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientSenderPort.setStatus("current")
_RnsTwampClientReflectorPort_Type = InetPortNumber
_RnsTwampClientReflectorPort_Object = MibTableColumn
rnsTwampClientReflectorPort = _RnsTwampClientReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 5),
    _RnsTwampClientReflectorPort_Type()
)
rnsTwampClientReflectorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientReflectorPort.setStatus("current")
_RnsTwampClientSenderVrfName_Type = DisplayString
_RnsTwampClientSenderVrfName_Object = MibTableColumn
rnsTwampClientSenderVrfName = _RnsTwampClientSenderVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 6),
    _RnsTwampClientSenderVrfName_Type()
)
rnsTwampClientSenderVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientSenderVrfName.setStatus("current")
_RnsTwampClientDscp_Type = Unsigned32
_RnsTwampClientDscp_Object = MibTableColumn
rnsTwampClientDscp = _RnsTwampClientDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 7),
    _RnsTwampClientDscp_Type()
)
rnsTwampClientDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientDscp.setStatus("current")


class _RnsTwampClientPaddLength_Type(Unsigned32):
    """Custom type rnsTwampClientPaddLength based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1454),
    )


_RnsTwampClientPaddLength_Type.__name__ = "Unsigned32"
_RnsTwampClientPaddLength_Object = MibTableColumn
rnsTwampClientPaddLength = _RnsTwampClientPaddLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 8),
    _RnsTwampClientPaddLength_Type()
)
rnsTwampClientPaddLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientPaddLength.setStatus("current")


class _RnsTwampClientPadValue_Type(Integer32):
    """Custom type rnsTwampClientPadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allzero", 0),
          ("value0x55", 1),
          ("value0xaa", 2),
          ("allone", 3))
    )


_RnsTwampClientPadValue_Type.__name__ = "Integer32"
_RnsTwampClientPadValue_Object = MibTableColumn
rnsTwampClientPadValue = _RnsTwampClientPadValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 9),
    _RnsTwampClientPadValue_Type()
)
rnsTwampClientPadValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientPadValue.setStatus("current")


class _RnsTwampClientDelayHighThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientDelayHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_RnsTwampClientDelayHighThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientDelayHighThreshold_Object = MibTableColumn
rnsTwampClientDelayHighThreshold = _RnsTwampClientDelayHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 10),
    _RnsTwampClientDelayHighThreshold_Type()
)
rnsTwampClientDelayHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientDelayHighThreshold.setStatus("current")


class _RnsTwampClientDelayLowThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientDelayLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_RnsTwampClientDelayLowThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientDelayLowThreshold_Object = MibTableColumn
rnsTwampClientDelayLowThreshold = _RnsTwampClientDelayLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 11),
    _RnsTwampClientDelayLowThreshold_Type()
)
rnsTwampClientDelayLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientDelayLowThreshold.setStatus("current")


class _RnsTwampClientJitterHighThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientJitterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_RnsTwampClientJitterHighThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientJitterHighThreshold_Object = MibTableColumn
rnsTwampClientJitterHighThreshold = _RnsTwampClientJitterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 12),
    _RnsTwampClientJitterHighThreshold_Type()
)
rnsTwampClientJitterHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientJitterHighThreshold.setStatus("current")


class _RnsTwampClientJitterLowThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientJitterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_RnsTwampClientJitterLowThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientJitterLowThreshold_Object = MibTableColumn
rnsTwampClientJitterLowThreshold = _RnsTwampClientJitterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 13),
    _RnsTwampClientJitterLowThreshold_Type()
)
rnsTwampClientJitterLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientJitterLowThreshold.setStatus("current")


class _RnsTwampClientLossHighThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientLossHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 999999),
    )


_RnsTwampClientLossHighThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientLossHighThreshold_Object = MibTableColumn
rnsTwampClientLossHighThreshold = _RnsTwampClientLossHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 14),
    _RnsTwampClientLossHighThreshold_Type()
)
rnsTwampClientLossHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientLossHighThreshold.setStatus("current")


class _RnsTwampClientLossLowThreshold_Type(Unsigned32):
    """Custom type rnsTwampClientLossLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999998),
    )


_RnsTwampClientLossLowThreshold_Type.__name__ = "Unsigned32"
_RnsTwampClientLossLowThreshold_Object = MibTableColumn
rnsTwampClientLossLowThreshold = _RnsTwampClientLossLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 15),
    _RnsTwampClientLossLowThreshold_Type()
)
rnsTwampClientLossLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientLossLowThreshold.setStatus("current")
_RnsTwampClientBindInterface_Type = DisplayString
_RnsTwampClientBindInterface_Object = MibTableColumn
rnsTwampClientBindInterface = _RnsTwampClientBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 16),
    _RnsTwampClientBindInterface_Type()
)
rnsTwampClientBindInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientBindInterface.setStatus("current")


class _RnsTwampClientResetStatic_Type(Integer32):
    """Custom type rnsTwampClientResetStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("donotrestsession", 0),
          ("restsession", 1))
    )


_RnsTwampClientResetStatic_Type.__name__ = "Integer32"
_RnsTwampClientResetStatic_Object = MibTableColumn
rnsTwampClientResetStatic = _RnsTwampClientResetStatic_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 17),
    _RnsTwampClientResetStatic_Type()
)
rnsTwampClientResetStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsTwampClientResetStatic.setStatus("current")
_RnsTwampClientDescription_Type = DisplayString
_RnsTwampClientDescription_Object = MibTableColumn
rnsTwampClientDescription = _RnsTwampClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 18),
    _RnsTwampClientDescription_Type()
)
rnsTwampClientDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientDescription.setStatus("current")
_RnsTwampClientStatus_Type = RowStatus
_RnsTwampClientStatus_Object = MibTableColumn
rnsTwampClientStatus = _RnsTwampClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 3, 1, 19),
    _RnsTwampClientStatus_Type()
)
rnsTwampClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampClientStatus.setStatus("current")
_RnsTwampLightSenderTable_Object = MibTable
rnsTwampLightSenderTable = _RnsTwampLightSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4)
)
if mibBuilder.loadTexts:
    rnsTwampLightSenderTable.setStatus("current")
_RnsTwampLightSenderEntry_Object = MibTableRow
rnsTwampLightSenderEntry = _RnsTwampLightSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1)
)
rnsTwampLightSenderEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsTwampSenderSessionId"),
)
if mibBuilder.loadTexts:
    rnsTwampLightSenderEntry.setStatus("current")


class _RnsTwampSenderSessionId_Type(Integer32):
    """Custom type rnsTwampSenderSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampSenderSessionId_Type.__name__ = "Integer32"
_RnsTwampSenderSessionId_Object = MibTableColumn
rnsTwampSenderSessionId = _RnsTwampSenderSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 1),
    _RnsTwampSenderSessionId_Type()
)
rnsTwampSenderSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampSenderSessionId.setStatus("current")


class _RnsTwampSessionType_Type(Integer32):
    """Custom type rnsTwampSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duration", 0),
          ("packetCount", 1),
          ("continual", 2))
    )


_RnsTwampSessionType_Type.__name__ = "Integer32"
_RnsTwampSessionType_Object = MibTableColumn
rnsTwampSessionType = _RnsTwampSessionType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 2),
    _RnsTwampSessionType_Type()
)
rnsTwampSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSessionType.setStatus("current")


class _RnsTwampSenderSessionDuration_Type(Unsigned32):
    """Custom type rnsTwampSenderSessionDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_RnsTwampSenderSessionDuration_Type.__name__ = "Unsigned32"
_RnsTwampSenderSessionDuration_Object = MibTableColumn
rnsTwampSenderSessionDuration = _RnsTwampSenderSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 3),
    _RnsTwampSenderSessionDuration_Type()
)
rnsTwampSenderSessionDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSenderSessionDuration.setStatus("current")


class _RnsTwampSenderPacketCount_Type(Unsigned32):
    """Custom type rnsTwampSenderPacketCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_RnsTwampSenderPacketCount_Type.__name__ = "Unsigned32"
_RnsTwampSenderPacketCount_Object = MibTableColumn
rnsTwampSenderPacketCount = _RnsTwampSenderPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 4),
    _RnsTwampSenderPacketCount_Type()
)
rnsTwampSenderPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSenderPacketCount.setStatus("current")


class _RnsTwampSenderSessionPeriod_Type(Unsigned32):
    """Custom type rnsTwampSenderSessionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RnsTwampSenderSessionPeriod_Type.__name__ = "Unsigned32"
_RnsTwampSenderSessionPeriod_Object = MibTableColumn
rnsTwampSenderSessionPeriod = _RnsTwampSenderSessionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 5),
    _RnsTwampSenderSessionPeriod_Type()
)
rnsTwampSenderSessionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSenderSessionPeriod.setStatus("current")


class _RnsTwampSenderSessionTimeOut_Type(Unsigned32):
    """Custom type rnsTwampSenderSessionTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RnsTwampSenderSessionTimeOut_Type.__name__ = "Unsigned32"
_RnsTwampSenderSessionTimeOut_Object = MibTableColumn
rnsTwampSenderSessionTimeOut = _RnsTwampSenderSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 6),
    _RnsTwampSenderSessionTimeOut_Type()
)
rnsTwampSenderSessionTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSenderSessionTimeOut.setStatus("current")
_RnsTwampSenderStatus_Type = RowStatus
_RnsTwampSenderStatus_Object = MibTableColumn
rnsTwampSenderStatus = _RnsTwampSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 4, 1, 7),
    _RnsTwampSenderStatus_Type()
)
rnsTwampSenderStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampSenderStatus.setStatus("current")
_RnsTwampLightStaticTable_Object = MibTable
rnsTwampLightStaticTable = _RnsTwampLightStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5)
)
if mibBuilder.loadTexts:
    rnsTwampLightStaticTable.setStatus("current")
_RnsTwampLightStaticEntry_Object = MibTableRow
rnsTwampLightStaticEntry = _RnsTwampLightStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1)
)
rnsTwampLightStaticEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsTwampLightStaticSessionId"),
)
if mibBuilder.loadTexts:
    rnsTwampLightStaticEntry.setStatus("current")


class _RnsTwampLightStaticSessionId_Type(Integer32):
    """Custom type rnsTwampLightStaticSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampLightStaticSessionId_Type.__name__ = "Integer32"
_RnsTwampLightStaticSessionId_Object = MibTableColumn
rnsTwampLightStaticSessionId = _RnsTwampLightStaticSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 1),
    _RnsTwampLightStaticSessionId_Type()
)
rnsTwampLightStaticSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightStaticSessionId.setStatus("current")
_RnsTwampLightMinDelayValue_Type = Counter32
_RnsTwampLightMinDelayValue_Object = MibTableColumn
rnsTwampLightMinDelayValue = _RnsTwampLightMinDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 2),
    _RnsTwampLightMinDelayValue_Type()
)
rnsTwampLightMinDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightMinDelayValue.setStatus("current")
_RnsTwampLightMaxDelayValue_Type = Counter32
_RnsTwampLightMaxDelayValue_Object = MibTableColumn
rnsTwampLightMaxDelayValue = _RnsTwampLightMaxDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 3),
    _RnsTwampLightMaxDelayValue_Type()
)
rnsTwampLightMaxDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightMaxDelayValue.setStatus("current")
_RnsTwampLightAvgDelayValue_Type = Counter32
_RnsTwampLightAvgDelayValue_Object = MibTableColumn
rnsTwampLightAvgDelayValue = _RnsTwampLightAvgDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 4),
    _RnsTwampLightAvgDelayValue_Type()
)
rnsTwampLightAvgDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightAvgDelayValue.setStatus("current")


class _RnsTwampLightDelayAlamrStatus_Type(Integer32):
    """Custom type rnsTwampLightDelayAlamrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noalarm", 0),
          ("alarmproduce", 1),
          ("alarmrecover", 2))
    )


_RnsTwampLightDelayAlamrStatus_Type.__name__ = "Integer32"
_RnsTwampLightDelayAlamrStatus_Object = MibTableColumn
rnsTwampLightDelayAlamrStatus = _RnsTwampLightDelayAlamrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 5),
    _RnsTwampLightDelayAlamrStatus_Type()
)
rnsTwampLightDelayAlamrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightDelayAlamrStatus.setStatus("current")
_RnsTwampLightMinJitterValue_Type = Counter32
_RnsTwampLightMinJitterValue_Object = MibTableColumn
rnsTwampLightMinJitterValue = _RnsTwampLightMinJitterValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 6),
    _RnsTwampLightMinJitterValue_Type()
)
rnsTwampLightMinJitterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightMinJitterValue.setStatus("current")
_RnsTwampLightMaxJitterValue_Type = Counter32
_RnsTwampLightMaxJitterValue_Object = MibTableColumn
rnsTwampLightMaxJitterValue = _RnsTwampLightMaxJitterValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 7),
    _RnsTwampLightMaxJitterValue_Type()
)
rnsTwampLightMaxJitterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightMaxJitterValue.setStatus("current")
_RnsTwampLightAvgJitterValue_Type = Counter32
_RnsTwampLightAvgJitterValue_Object = MibTableColumn
rnsTwampLightAvgJitterValue = _RnsTwampLightAvgJitterValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 8),
    _RnsTwampLightAvgJitterValue_Type()
)
rnsTwampLightAvgJitterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightAvgJitterValue.setStatus("current")


class _RnsTwampLightJitterAlamrStatus_Type(Integer32):
    """Custom type rnsTwampLightJitterAlamrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noalarm", 0),
          ("alarmproduce", 1),
          ("alarmrecover", 2))
    )


_RnsTwampLightJitterAlamrStatus_Type.__name__ = "Integer32"
_RnsTwampLightJitterAlamrStatus_Object = MibTableColumn
rnsTwampLightJitterAlamrStatus = _RnsTwampLightJitterAlamrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 9),
    _RnsTwampLightJitterAlamrStatus_Type()
)
rnsTwampLightJitterAlamrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightJitterAlamrStatus.setStatus("current")
_RnsTwampLightSendpacketsNum_Type = Counter32
_RnsTwampLightSendpacketsNum_Object = MibTableColumn
rnsTwampLightSendpacketsNum = _RnsTwampLightSendpacketsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 10),
    _RnsTwampLightSendpacketsNum_Type()
)
rnsTwampLightSendpacketsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightSendpacketsNum.setStatus("current")
_RnsTwampLightReceivepacketsNum_Type = Counter32
_RnsTwampLightReceivepacketsNum_Object = MibTableColumn
rnsTwampLightReceivepacketsNum = _RnsTwampLightReceivepacketsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 11),
    _RnsTwampLightReceivepacketsNum_Type()
)
rnsTwampLightReceivepacketsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightReceivepacketsNum.setStatus("current")
_RnsTwampLightLostCount_Type = Counter32
_RnsTwampLightLostCount_Object = MibTableColumn
rnsTwampLightLostCount = _RnsTwampLightLostCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 12),
    _RnsTwampLightLostCount_Type()
)
rnsTwampLightLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightLostCount.setStatus("current")
_RnsTwampLightLossRatio_Type = DisplayString
_RnsTwampLightLossRatio_Object = MibTableColumn
rnsTwampLightLossRatio = _RnsTwampLightLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 13),
    _RnsTwampLightLossRatio_Type()
)
rnsTwampLightLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightLossRatio.setStatus("current")


class _RnsTwampLightLossRatioAlamrStatus_Type(Integer32):
    """Custom type rnsTwampLightLossRatioAlamrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noalarm", 0),
          ("alarmproduce", 1),
          ("alarmrecover", 2))
    )


_RnsTwampLightLossRatioAlamrStatus_Type.__name__ = "Integer32"
_RnsTwampLightLossRatioAlamrStatus_Object = MibTableColumn
rnsTwampLightLossRatioAlamrStatus = _RnsTwampLightLossRatioAlamrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 5, 1, 14),
    _RnsTwampLightLossRatioAlamrStatus_Type()
)
rnsTwampLightLossRatioAlamrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightLossRatioAlamrStatus.setStatus("current")
_RnsTwampLightOperTable_Object = MibTable
rnsTwampLightOperTable = _RnsTwampLightOperTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7)
)
if mibBuilder.loadTexts:
    rnsTwampLightOperTable.setStatus("current")
_RnsTwampLightOperEntry_Object = MibTableRow
rnsTwampLightOperEntry = _RnsTwampLightOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1)
)
rnsTwampLightOperEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsTwampLightOperSessionId"),
)
if mibBuilder.loadTexts:
    rnsTwampLightOperEntry.setStatus("current")


class _RnsTwampLightOperSessionId_Type(Integer32):
    """Custom type rnsTwampLightOperSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampLightOperSessionId_Type.__name__ = "Integer32"
_RnsTwampLightOperSessionId_Object = MibTableColumn
rnsTwampLightOperSessionId = _RnsTwampLightOperSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1, 1),
    _RnsTwampLightOperSessionId_Type()
)
rnsTwampLightOperSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightOperSessionId.setStatus("current")


class _RnsTwampLightOperSessionState_Type(Integer32):
    """Custom type rnsTwampLightOperSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("stopped", 1),
          ("inactive", 2),
          ("isNotStartup", 3),
          ("absenceResource", 4),
          ("boardFault", 5))
    )


_RnsTwampLightOperSessionState_Type.__name__ = "Integer32"
_RnsTwampLightOperSessionState_Object = MibTableColumn
rnsTwampLightOperSessionState = _RnsTwampLightOperSessionState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1, 2),
    _RnsTwampLightOperSessionState_Type()
)
rnsTwampLightOperSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightOperSessionState.setStatus("current")


class _RnsTwampLightOperSessionMode_Type(Integer32):
    """Custom type rnsTwampLightOperSessionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unauthenticated", 0),
          ("authenticated", 1),
          ("encryption", 2))
    )


_RnsTwampLightOperSessionMode_Type.__name__ = "Integer32"
_RnsTwampLightOperSessionMode_Object = MibTableColumn
rnsTwampLightOperSessionMode = _RnsTwampLightOperSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1, 3),
    _RnsTwampLightOperSessionMode_Type()
)
rnsTwampLightOperSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightOperSessionMode.setStatus("current")
_RnsTwampLightOperSessionStartTime_Type = DisplayString
_RnsTwampLightOperSessionStartTime_Object = MibTableColumn
rnsTwampLightOperSessionStartTime = _RnsTwampLightOperSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1, 4),
    _RnsTwampLightOperSessionStartTime_Type()
)
rnsTwampLightOperSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightOperSessionStartTime.setStatus("current")
_RnsTwampLightOperSessionStopTime_Type = DisplayString
_RnsTwampLightOperSessionStopTime_Object = MibTableColumn
rnsTwampLightOperSessionStopTime = _RnsTwampLightOperSessionStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 1, 7, 1, 5),
    _RnsTwampLightOperSessionStopTime_Type()
)
rnsTwampLightOperSessionStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampLightOperSessionStopTime.setStatus("current")
_RnsTwampLightResponderAdmin_ObjectIdentity = ObjectIdentity
rnsTwampLightResponderAdmin = _RnsTwampLightResponderAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2)
)


class _RnsTwampLightResponderEnable_Type(Integer32):
    """Custom type rnsTwampLightResponderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RnsTwampLightResponderEnable_Type.__name__ = "Integer32"
_RnsTwampLightResponderEnable_Object = MibScalar
rnsTwampLightResponderEnable = _RnsTwampLightResponderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 1),
    _RnsTwampLightResponderEnable_Type()
)
rnsTwampLightResponderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnsTwampLightResponderEnable.setStatus("current")
_RnsTwampLightResponderTable_Object = MibTable
rnsTwampLightResponderTable = _RnsTwampLightResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2)
)
if mibBuilder.loadTexts:
    rnsTwampLightResponderTable.setStatus("current")
_RnsTwampLightResponderEntry_Object = MibTableRow
rnsTwampLightResponderEntry = _RnsTwampLightResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1)
)
rnsTwampLightResponderEntry.setIndexNames(
    (0, "RUIJIE-RNS-MIB", "rnsTwampResponderSessionId"),
)
if mibBuilder.loadTexts:
    rnsTwampLightResponderEntry.setStatus("current")


class _RnsTwampResponderSessionId_Type(Integer32):
    """Custom type rnsTwampResponderSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampResponderSessionId_Type.__name__ = "Integer32"
_RnsTwampResponderSessionId_Object = MibTableColumn
rnsTwampResponderSessionId = _RnsTwampResponderSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 1),
    _RnsTwampResponderSessionId_Type()
)
rnsTwampResponderSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnsTwampResponderSessionId.setStatus("current")
_RnsTwampResponderLocalIP_Type = InetAddress
_RnsTwampResponderLocalIP_Object = MibTableColumn
rnsTwampResponderLocalIP = _RnsTwampResponderLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 2),
    _RnsTwampResponderLocalIP_Type()
)
rnsTwampResponderLocalIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderLocalIP.setStatus("current")
_RnsTwampResponderRemoteIP_Type = InetAddress
_RnsTwampResponderRemoteIP_Object = MibTableColumn
rnsTwampResponderRemoteIP = _RnsTwampResponderRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 3),
    _RnsTwampResponderRemoteIP_Type()
)
rnsTwampResponderRemoteIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderRemoteIP.setStatus("current")
_RnsTwampResponderLocalPort_Type = InetPortNumber
_RnsTwampResponderLocalPort_Object = MibTableColumn
rnsTwampResponderLocalPort = _RnsTwampResponderLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 4),
    _RnsTwampResponderLocalPort_Type()
)
rnsTwampResponderLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderLocalPort.setStatus("current")
_RnsTwampResponderRemoterPort_Type = InetPortNumber
_RnsTwampResponderRemoterPort_Object = MibTableColumn
rnsTwampResponderRemoterPort = _RnsTwampResponderRemoterPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 5),
    _RnsTwampResponderRemoterPort_Type()
)
rnsTwampResponderRemoterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderRemoterPort.setStatus("current")
_RnsTwampResponderVrfName_Type = DisplayString
_RnsTwampResponderVrfName_Object = MibTableColumn
rnsTwampResponderVrfName = _RnsTwampResponderVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 6),
    _RnsTwampResponderVrfName_Type()
)
rnsTwampResponderVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderVrfName.setStatus("current")
_RnsTwampResponderInterfaceID_Type = InterfaceIndex
_RnsTwampResponderInterfaceID_Object = MibTableColumn
rnsTwampResponderInterfaceID = _RnsTwampResponderInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 7),
    _RnsTwampResponderInterfaceID_Type()
)
rnsTwampResponderInterfaceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderInterfaceID.setStatus("current")
_RnsTwampResponderInterfaceName_Type = DisplayString
_RnsTwampResponderInterfaceName_Object = MibTableColumn
rnsTwampResponderInterfaceName = _RnsTwampResponderInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 8),
    _RnsTwampResponderInterfaceName_Type()
)
rnsTwampResponderInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderInterfaceName.setStatus("current")
_RnsTwampResponderDescription_Type = DisplayString
_RnsTwampResponderDescription_Object = MibTableColumn
rnsTwampResponderDescription = _RnsTwampResponderDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 9),
    _RnsTwampResponderDescription_Type()
)
rnsTwampResponderDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderDescription.setStatus("current")
_RnsTwampResponderStatus_Type = RowStatus
_RnsTwampResponderStatus_Object = MibTableColumn
rnsTwampResponderStatus = _RnsTwampResponderStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 2, 2, 1, 10),
    _RnsTwampResponderStatus_Type()
)
rnsTwampResponderStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rnsTwampResponderStatus.setStatus("current")
_RnsTwampLightAlarmTraps_ObjectIdentity = ObjectIdentity
rnsTwampLightAlarmTraps = _RnsTwampLightAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 3)
)


class _RnsTwampLightAlarmSessionTraps_Type(Integer32):
    """Custom type rnsTwampLightAlarmSessionTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RnsTwampLightAlarmSessionTraps_Type.__name__ = "Integer32"
_RnsTwampLightAlarmSessionTraps_Object = MibScalar
rnsTwampLightAlarmSessionTraps = _RnsTwampLightAlarmSessionTraps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 3, 1),
    _RnsTwampLightAlarmSessionTraps_Type()
)
rnsTwampLightAlarmSessionTraps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsTwampLightAlarmSessionTraps.setStatus("current")


class _RnsTwampLightAlarmTypeTraps_Type(Integer32):
    """Custom type rnsTwampLightAlarmTypeTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("jitter", 2),
          ("lossratio", 3))
    )


_RnsTwampLightAlarmTypeTraps_Type.__name__ = "Integer32"
_RnsTwampLightAlarmTypeTraps_Object = MibScalar
rnsTwampLightAlarmTypeTraps = _RnsTwampLightAlarmTypeTraps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 3, 2),
    _RnsTwampLightAlarmTypeTraps_Type()
)
rnsTwampLightAlarmTypeTraps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsTwampLightAlarmTypeTraps.setStatus("current")


class _RnsTwampLightAlarmStatusTraps_Type(Integer32):
    """Custom type rnsTwampLightAlarmStatusTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 1),
          ("recoverd", 2))
    )


_RnsTwampLightAlarmStatusTraps_Type.__name__ = "Integer32"
_RnsTwampLightAlarmStatusTraps_Object = MibScalar
rnsTwampLightAlarmStatusTraps = _RnsTwampLightAlarmStatusTraps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 3, 3),
    _RnsTwampLightAlarmStatusTraps_Type()
)
rnsTwampLightAlarmStatusTraps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rnsTwampLightAlarmStatusTraps.setStatus("current")
_RnsTwampLightAlarmNotifications_ObjectIdentity = ObjectIdentity
rnsTwampLightAlarmNotifications = _RnsTwampLightAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 4)
)

# Managed Objects groups


# Notification objects

rnsTwampLightControlAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 160, 5, 4, 1)
)
rnsTwampLightControlAlarm.setObjects(
      *(("RUIJIE-RNS-MIB", "rnsTwampLightAlarmSessionTraps"),
        ("RUIJIE-RNS-MIB", "rnsTwampLightAlarmTypeTraps"),
        ("RUIJIE-RNS-MIB", "rnsTwampLightAlarmStatusTraps"))
)
if mibBuilder.loadTexts:
    rnsTwampLightControlAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RNS-MIB",
    **{"RnsType": RnsType,
       "ruijieRnsMIB": ruijieRnsMIB,
       "rnsBase": rnsBase,
       "rnsReset": rnsReset,
       "rnsClearStat": rnsClearStat,
       "rnsNumOfDetectEntry": rnsNumOfDetectEntry,
       "rnsSupportDetectType": rnsSupportDetectType,
       "rnsAdmin": rnsAdmin,
       "rnsDetectTable": rnsDetectTable,
       "rnsDetectEntry": rnsDetectEntry,
       "rnsDetectId": rnsDetectId,
       "rnsDetectTag": rnsDetectTag,
       "rnsDetectType": rnsDetectType,
       "rnsDetectFrequency": rnsDetectFrequency,
       "rnsDetectTimeout": rnsDetectTimeout,
       "rnsDetectThreshold": rnsDetectThreshold,
       "rnsDetectTargetHost": rnsDetectTargetHost,
       "rnsDetectTargetPort": rnsDetectTargetPort,
       "rnsDetectSourceAddress": rnsDetectSourceAddress,
       "rnsDetectOutInterface": rnsDetectOutInterface,
       "rnsDetectIsMgmt": rnsDetectIsMgmt,
       "rnsDetectNexthopAddressType": rnsDetectNexthopAddressType,
       "rnsDetectNexthopAddress": rnsDetectNexthopAddress,
       "rnsDetectVrfName": rnsDetectVrfName,
       "rnsDetectDataSize": rnsDetectDataSize,
       "rnsDetectDSField": rnsDetectDSField,
       "rnsDetectStatus": rnsDetectStatus,
       "rnsClearStatisTable": rnsClearStatisTable,
       "rnsClearStatisEntry": rnsClearStatisEntry,
       "rnsClearStatisId": rnsClearStatisId,
       "rnsClearStatisClear": rnsClearStatisClear,
       "rnsScheduleTable": rnsScheduleTable,
       "rnsScheduleEntry": rnsScheduleEntry,
       "rnsScheduleId": rnsScheduleId,
       "rnsScheduleStartType": rnsScheduleStartType,
       "rnsScheduleStartTime": rnsScheduleStartTime,
       "rnsScheduleLife": rnsScheduleLife,
       "rnsScheduleRecurring": rnsScheduleRecurring,
       "rnsScheduleStatus": rnsScheduleStatus,
       "rnsStats": rnsStats,
       "rnsResultsTable": rnsResultsTable,
       "rnsResultsEntry": rnsResultsEntry,
       "rnsResultsId": rnsResultsId,
       "rnsResultsLatestStatus": rnsResultsLatestStatus,
       "rnsResultsSuccessfuls": rnsResultsSuccessfuls,
       "rnsResultsFailures": rnsResultsFailures,
       "rnsResultsAttempts": rnsResultsAttempts,
       "rnsResultsRttAvg": rnsResultsRttAvg,
       "rnsResultsRttMin": rnsResultsRttMin,
       "rnsResultsRttMax": rnsResultsRttMax,
       "rnsResultsRTDOverThresholds": rnsResultsRTDOverThresholds,
       "rnsResultsTimeouts": rnsResultsTimeouts,
       "rnsResultsBusies": rnsResultsBusies,
       "rnsResultsJitter": rnsResultsJitter,
       "rnsResultsSquareSumRtt": rnsResultsSquareSumRtt,
       "rnsResultsLossRatio": rnsResultsLossRatio,
       "rnsResultsLossRatioPermillage": rnsResultsLossRatioPermillage,
       "rnsResultsNoconnect": rnsResultsNoconnect,
       "rnsResultsDisconnect": rnsResultsDisconnect,
       "rnsResultsIntervalerr": rnsResultsIntervalerr,
       "rnsResultsSeqerr": rnsResultsSeqerr,
       "rnsResultsLastrecvtm": rnsResultsLastrecvtm,
       "rnsServer": rnsServer,
       "rnsServerUdpPort": rnsServerUdpPort,
       "rnsTwampLight": rnsTwampLight,
       "rnsTwampLightControllerAdmin": rnsTwampLightControllerAdmin,
       "rnsTwampLightClientEnable": rnsTwampLightClientEnable,
       "rnsTwampLightSenderEnable": rnsTwampLightSenderEnable,
       "rnsTwampLightClientTable": rnsTwampLightClientTable,
       "rnsTwampLightClientEntry": rnsTwampLightClientEntry,
       "rnsTwampClientSessionId": rnsTwampClientSessionId,
       "rnsTwampClientSenderIP": rnsTwampClientSenderIP,
       "rnsTwampClientReflectorIP": rnsTwampClientReflectorIP,
       "rnsTwampClientSenderPort": rnsTwampClientSenderPort,
       "rnsTwampClientReflectorPort": rnsTwampClientReflectorPort,
       "rnsTwampClientSenderVrfName": rnsTwampClientSenderVrfName,
       "rnsTwampClientDscp": rnsTwampClientDscp,
       "rnsTwampClientPaddLength": rnsTwampClientPaddLength,
       "rnsTwampClientPadValue": rnsTwampClientPadValue,
       "rnsTwampClientDelayHighThreshold": rnsTwampClientDelayHighThreshold,
       "rnsTwampClientDelayLowThreshold": rnsTwampClientDelayLowThreshold,
       "rnsTwampClientJitterHighThreshold": rnsTwampClientJitterHighThreshold,
       "rnsTwampClientJitterLowThreshold": rnsTwampClientJitterLowThreshold,
       "rnsTwampClientLossHighThreshold": rnsTwampClientLossHighThreshold,
       "rnsTwampClientLossLowThreshold": rnsTwampClientLossLowThreshold,
       "rnsTwampClientBindInterface": rnsTwampClientBindInterface,
       "rnsTwampClientResetStatic": rnsTwampClientResetStatic,
       "rnsTwampClientDescription": rnsTwampClientDescription,
       "rnsTwampClientStatus": rnsTwampClientStatus,
       "rnsTwampLightSenderTable": rnsTwampLightSenderTable,
       "rnsTwampLightSenderEntry": rnsTwampLightSenderEntry,
       "rnsTwampSenderSessionId": rnsTwampSenderSessionId,
       "rnsTwampSessionType": rnsTwampSessionType,
       "rnsTwampSenderSessionDuration": rnsTwampSenderSessionDuration,
       "rnsTwampSenderPacketCount": rnsTwampSenderPacketCount,
       "rnsTwampSenderSessionPeriod": rnsTwampSenderSessionPeriod,
       "rnsTwampSenderSessionTimeOut": rnsTwampSenderSessionTimeOut,
       "rnsTwampSenderStatus": rnsTwampSenderStatus,
       "rnsTwampLightStaticTable": rnsTwampLightStaticTable,
       "rnsTwampLightStaticEntry": rnsTwampLightStaticEntry,
       "rnsTwampLightStaticSessionId": rnsTwampLightStaticSessionId,
       "rnsTwampLightMinDelayValue": rnsTwampLightMinDelayValue,
       "rnsTwampLightMaxDelayValue": rnsTwampLightMaxDelayValue,
       "rnsTwampLightAvgDelayValue": rnsTwampLightAvgDelayValue,
       "rnsTwampLightDelayAlamrStatus": rnsTwampLightDelayAlamrStatus,
       "rnsTwampLightMinJitterValue": rnsTwampLightMinJitterValue,
       "rnsTwampLightMaxJitterValue": rnsTwampLightMaxJitterValue,
       "rnsTwampLightAvgJitterValue": rnsTwampLightAvgJitterValue,
       "rnsTwampLightJitterAlamrStatus": rnsTwampLightJitterAlamrStatus,
       "rnsTwampLightSendpacketsNum": rnsTwampLightSendpacketsNum,
       "rnsTwampLightReceivepacketsNum": rnsTwampLightReceivepacketsNum,
       "rnsTwampLightLostCount": rnsTwampLightLostCount,
       "rnsTwampLightLossRatio": rnsTwampLightLossRatio,
       "rnsTwampLightLossRatioAlamrStatus": rnsTwampLightLossRatioAlamrStatus,
       "rnsTwampLightOperTable": rnsTwampLightOperTable,
       "rnsTwampLightOperEntry": rnsTwampLightOperEntry,
       "rnsTwampLightOperSessionId": rnsTwampLightOperSessionId,
       "rnsTwampLightOperSessionState": rnsTwampLightOperSessionState,
       "rnsTwampLightOperSessionMode": rnsTwampLightOperSessionMode,
       "rnsTwampLightOperSessionStartTime": rnsTwampLightOperSessionStartTime,
       "rnsTwampLightOperSessionStopTime": rnsTwampLightOperSessionStopTime,
       "rnsTwampLightResponderAdmin": rnsTwampLightResponderAdmin,
       "rnsTwampLightResponderEnable": rnsTwampLightResponderEnable,
       "rnsTwampLightResponderTable": rnsTwampLightResponderTable,
       "rnsTwampLightResponderEntry": rnsTwampLightResponderEntry,
       "rnsTwampResponderSessionId": rnsTwampResponderSessionId,
       "rnsTwampResponderLocalIP": rnsTwampResponderLocalIP,
       "rnsTwampResponderRemoteIP": rnsTwampResponderRemoteIP,
       "rnsTwampResponderLocalPort": rnsTwampResponderLocalPort,
       "rnsTwampResponderRemoterPort": rnsTwampResponderRemoterPort,
       "rnsTwampResponderVrfName": rnsTwampResponderVrfName,
       "rnsTwampResponderInterfaceID": rnsTwampResponderInterfaceID,
       "rnsTwampResponderInterfaceName": rnsTwampResponderInterfaceName,
       "rnsTwampResponderDescription": rnsTwampResponderDescription,
       "rnsTwampResponderStatus": rnsTwampResponderStatus,
       "rnsTwampLightAlarmTraps": rnsTwampLightAlarmTraps,
       "rnsTwampLightAlarmSessionTraps": rnsTwampLightAlarmSessionTraps,
       "rnsTwampLightAlarmTypeTraps": rnsTwampLightAlarmTypeTraps,
       "rnsTwampLightAlarmStatusTraps": rnsTwampLightAlarmStatusTraps,
       "rnsTwampLightAlarmNotifications": rnsTwampLightAlarmNotifications,
       "rnsTwampLightControlAlarm": rnsTwampLightControlAlarm}
)
