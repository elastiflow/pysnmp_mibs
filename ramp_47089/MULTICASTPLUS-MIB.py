# SNMP MIB module (MULTICASTPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ramp_47089/MULTICASTPLUS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:46 2025
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

rampMpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47089, 1)
)
if mibBuilder.loadTexts:
    rampMpMIB.setRevisions(
        ("2016-09-08 12:00",
         "2016-05-26 18:00",
         "2016-05-26 12:00",
         "2016-05-26 00:00",
         "2016-05-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ramp_ObjectIdentity = ObjectIdentity
ramp = _Ramp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47089)
)
_RampMpSender_ObjectIdentity = ObjectIdentity
rampMpSender = _RampMpSender_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1)
)
_RampMpSenderTable_Object = MibTable
rampMpSenderTable = _RampMpSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rampMpSenderTable.setStatus("current")
_RampMpSenderEntry_Object = MibTableRow
rampMpSenderEntry = _RampMpSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1)
)
rampMpSenderEntry.setIndexNames(
    (0, "MULTICASTPLUS-MIB", "rampMpSenderIndex"),
)
if mibBuilder.loadTexts:
    rampMpSenderEntry.setStatus("current")
_RampMpSenderIndex_Type = Unsigned32
_RampMpSenderIndex_Object = MibTableColumn
rampMpSenderIndex = _RampMpSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 1),
    _RampMpSenderIndex_Type()
)
rampMpSenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rampMpSenderIndex.setStatus("current")
_RampMpSenderDescription_Type = SnmpAdminString
_RampMpSenderDescription_Object = MibTableColumn
rampMpSenderDescription = _RampMpSenderDescription_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 2),
    _RampMpSenderDescription_Type()
)
rampMpSenderDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderDescription.setStatus("current")


class _RampMpSenderSourceFormat_Type(Integer32):
    """Custom type rampMpSenderSourceFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hls", 1),
          ("dash", 2))
    )


_RampMpSenderSourceFormat_Type.__name__ = "Integer32"
_RampMpSenderSourceFormat_Object = MibTableColumn
rampMpSenderSourceFormat = _RampMpSenderSourceFormat_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 3),
    _RampMpSenderSourceFormat_Type()
)
rampMpSenderSourceFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderSourceFormat.setStatus("current")
_RampMpSenderSourceUrl_Type = OctetString
_RampMpSenderSourceUrl_Object = MibTableColumn
rampMpSenderSourceUrl = _RampMpSenderSourceUrl_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 4),
    _RampMpSenderSourceUrl_Type()
)
rampMpSenderSourceUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderSourceUrl.setStatus("current")
_RampMpSenderMulticastAddress_Type = OctetString
_RampMpSenderMulticastAddress_Object = MibTableColumn
rampMpSenderMulticastAddress = _RampMpSenderMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 5),
    _RampMpSenderMulticastAddress_Type()
)
rampMpSenderMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderMulticastAddress.setStatus("current")
_RampMpSenderMulticastAddressIP_Type = IpAddress
_RampMpSenderMulticastAddressIP_Object = MibTableColumn
rampMpSenderMulticastAddressIP = _RampMpSenderMulticastAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 6),
    _RampMpSenderMulticastAddressIP_Type()
)
rampMpSenderMulticastAddressIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderMulticastAddressIP.setStatus("current")
_RampMpSenderMulticastAddressPort_Type = Unsigned32
_RampMpSenderMulticastAddressPort_Object = MibTableColumn
rampMpSenderMulticastAddressPort = _RampMpSenderMulticastAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 7),
    _RampMpSenderMulticastAddressPort_Type()
)
rampMpSenderMulticastAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderMulticastAddressPort.setStatus("current")
_RampMpSenderMulticastAddressTTL_Type = Unsigned32
_RampMpSenderMulticastAddressTTL_Object = MibTableColumn
rampMpSenderMulticastAddressTTL = _RampMpSenderMulticastAddressTTL_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 8),
    _RampMpSenderMulticastAddressTTL_Type()
)
rampMpSenderMulticastAddressTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderMulticastAddressTTL.setStatus("current")
_RampMpSenderHighAvailabilityAddress_Type = OctetString
_RampMpSenderHighAvailabilityAddress_Object = MibTableColumn
rampMpSenderHighAvailabilityAddress = _RampMpSenderHighAvailabilityAddress_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 9),
    _RampMpSenderHighAvailabilityAddress_Type()
)
rampMpSenderHighAvailabilityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityAddress.setStatus("current")
_RampMpSenderHighAvailabilityAddressIP_Type = IpAddress
_RampMpSenderHighAvailabilityAddressIP_Object = MibTableColumn
rampMpSenderHighAvailabilityAddressIP = _RampMpSenderHighAvailabilityAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 10),
    _RampMpSenderHighAvailabilityAddressIP_Type()
)
rampMpSenderHighAvailabilityAddressIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityAddressIP.setStatus("current")
_RampMpSenderHighAvailabilityAddressPort_Type = Unsigned32
_RampMpSenderHighAvailabilityAddressPort_Object = MibTableColumn
rampMpSenderHighAvailabilityAddressPort = _RampMpSenderHighAvailabilityAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 11),
    _RampMpSenderHighAvailabilityAddressPort_Type()
)
rampMpSenderHighAvailabilityAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityAddressPort.setStatus("current")
_RampMpSenderHighAvailabilityAddressTTL_Type = Unsigned32
_RampMpSenderHighAvailabilityAddressTTL_Object = MibTableColumn
rampMpSenderHighAvailabilityAddressTTL = _RampMpSenderHighAvailabilityAddressTTL_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 12),
    _RampMpSenderHighAvailabilityAddressTTL_Type()
)
rampMpSenderHighAvailabilityAddressTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityAddressTTL.setStatus("current")
_RampMpSenderHighAvailabilityActive_Type = TruthValue
_RampMpSenderHighAvailabilityActive_Object = MibTableColumn
rampMpSenderHighAvailabilityActive = _RampMpSenderHighAvailabilityActive_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 13),
    _RampMpSenderHighAvailabilityActive_Type()
)
rampMpSenderHighAvailabilityActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityActive.setStatus("current")
_RampMpSenderHighAvailabilityLastActiveTime_Type = TimeTicks
_RampMpSenderHighAvailabilityLastActiveTime_Object = MibTableColumn
rampMpSenderHighAvailabilityLastActiveTime = _RampMpSenderHighAvailabilityLastActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 14),
    _RampMpSenderHighAvailabilityLastActiveTime_Type()
)
rampMpSenderHighAvailabilityLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityLastActiveTime.setStatus("current")
_RampMpSenderHighAvailabilityLastStandbyTime_Type = TimeTicks
_RampMpSenderHighAvailabilityLastStandbyTime_Object = MibTableColumn
rampMpSenderHighAvailabilityLastStandbyTime = _RampMpSenderHighAvailabilityLastStandbyTime_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 15),
    _RampMpSenderHighAvailabilityLastStandbyTime_Type()
)
rampMpSenderHighAvailabilityLastStandbyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityLastStandbyTime.setStatus("current")
_RampMpSenderHighAvailabilitySourceOK_Type = TruthValue
_RampMpSenderHighAvailabilitySourceOK_Object = MibTableColumn
rampMpSenderHighAvailabilitySourceOK = _RampMpSenderHighAvailabilitySourceOK_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 16),
    _RampMpSenderHighAvailabilitySourceOK_Type()
)
rampMpSenderHighAvailabilitySourceOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilitySourceOK.setStatus("current")
_RampMpSenderHighAvailabilityLastSourceOKTime_Type = TimeTicks
_RampMpSenderHighAvailabilityLastSourceOKTime_Object = MibTableColumn
rampMpSenderHighAvailabilityLastSourceOKTime = _RampMpSenderHighAvailabilityLastSourceOKTime_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 17),
    _RampMpSenderHighAvailabilityLastSourceOKTime_Type()
)
rampMpSenderHighAvailabilityLastSourceOKTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityLastSourceOKTime.setStatus("current")
_RampMpSenderHighAvailabilityPriority_Type = Unsigned32
_RampMpSenderHighAvailabilityPriority_Object = MibTableColumn
rampMpSenderHighAvailabilityPriority = _RampMpSenderHighAvailabilityPriority_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 18),
    _RampMpSenderHighAvailabilityPriority_Type()
)
rampMpSenderHighAvailabilityPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityPriority.setStatus("current")
_RampMpSenderHighAvailabilityGroup_Type = Unsigned32
_RampMpSenderHighAvailabilityGroup_Object = MibTableColumn
rampMpSenderHighAvailabilityGroup = _RampMpSenderHighAvailabilityGroup_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 19),
    _RampMpSenderHighAvailabilityGroup_Type()
)
rampMpSenderHighAvailabilityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityGroup.setStatus("current")
_RampMpSenderHighAvailabilityUnicastAddressList_Type = OctetString
_RampMpSenderHighAvailabilityUnicastAddressList_Object = MibTableColumn
rampMpSenderHighAvailabilityUnicastAddressList = _RampMpSenderHighAvailabilityUnicastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 20),
    _RampMpSenderHighAvailabilityUnicastAddressList_Type()
)
rampMpSenderHighAvailabilityUnicastAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityUnicastAddressList.setStatus("current")
_RampMpSenderHighAvailabilityUnicastPort_Type = Unsigned32
_RampMpSenderHighAvailabilityUnicastPort_Object = MibTableColumn
rampMpSenderHighAvailabilityUnicastPort = _RampMpSenderHighAvailabilityUnicastPort_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 1, 1, 21),
    _RampMpSenderHighAvailabilityUnicastPort_Type()
)
rampMpSenderHighAvailabilityUnicastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityUnicastPort.setStatus("current")
_RampMpMulticastSentTable_Object = MibTable
rampMpMulticastSentTable = _RampMpMulticastSentTable_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rampMpMulticastSentTable.setStatus("current")
_RampMpMulticastSentEntry_Object = MibTableRow
rampMpMulticastSentEntry = _RampMpMulticastSentEntry_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1)
)
rampMpMulticastSentEntry.setIndexNames(
    (0, "MULTICASTPLUS-MIB", "rampMpSenderIndex"),
    (0, "MULTICASTPLUS-MIB", "rampMpMulticastSentTimeIntervalMinutes"),
)
if mibBuilder.loadTexts:
    rampMpMulticastSentEntry.setStatus("current")
_RampMpMulticastSentTimeIntervalMinutes_Type = Unsigned32
_RampMpMulticastSentTimeIntervalMinutes_Object = MibTableColumn
rampMpMulticastSentTimeIntervalMinutes = _RampMpMulticastSentTimeIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1, 1),
    _RampMpMulticastSentTimeIntervalMinutes_Type()
)
rampMpMulticastSentTimeIntervalMinutes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rampMpMulticastSentTimeIntervalMinutes.setStatus("current")
_RampMpMulticastSentAverageSegmentSizeBytes_Type = Unsigned32
_RampMpMulticastSentAverageSegmentSizeBytes_Object = MibTableColumn
rampMpMulticastSentAverageSegmentSizeBytes = _RampMpMulticastSentAverageSegmentSizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1, 2),
    _RampMpMulticastSentAverageSegmentSizeBytes_Type()
)
rampMpMulticastSentAverageSegmentSizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpMulticastSentAverageSegmentSizeBytes.setStatus("current")
_RampMpMulticastSentTotalBytes_Type = Unsigned32
_RampMpMulticastSentTotalBytes_Object = MibTableColumn
rampMpMulticastSentTotalBytes = _RampMpMulticastSentTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1, 3),
    _RampMpMulticastSentTotalBytes_Type()
)
rampMpMulticastSentTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpMulticastSentTotalBytes.setStatus("current")
_RampMpMulticastSentTotalSegments_Type = Unsigned32
_RampMpMulticastSentTotalSegments_Object = MibTableColumn
rampMpMulticastSentTotalSegments = _RampMpMulticastSentTotalSegments_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1, 4),
    _RampMpMulticastSentTotalSegments_Type()
)
rampMpMulticastSentTotalSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpMulticastSentTotalSegments.setStatus("current")
_RampMpMulticastSentAverageSegmentDurationMilliseconds_Type = Unsigned32
_RampMpMulticastSentAverageSegmentDurationMilliseconds_Object = MibTableColumn
rampMpMulticastSentAverageSegmentDurationMilliseconds = _RampMpMulticastSentAverageSegmentDurationMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 2, 1, 5),
    _RampMpMulticastSentAverageSegmentDurationMilliseconds_Type()
)
rampMpMulticastSentAverageSegmentDurationMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpMulticastSentAverageSegmentDurationMilliseconds.setStatus("current")
_RampMpMulticastLastSegmentSentTable_Object = MibTable
rampMpMulticastLastSegmentSentTable = _RampMpMulticastLastSegmentSentTable_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rampMpMulticastLastSegmentSentTable.setStatus("current")
_RampMpMulticastLastSegmentSentEntry_Object = MibTableRow
rampMpMulticastLastSegmentSentEntry = _RampMpMulticastLastSegmentSentEntry_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 3, 1)
)
rampMpMulticastLastSegmentSentEntry.setIndexNames(
    (0, "MULTICASTPLUS-MIB", "rampMpSenderIndex"),
    (0, "MULTICASTPLUS-MIB", "rampMpMulticastLastSegmentSentIndex"),
)
if mibBuilder.loadTexts:
    rampMpMulticastLastSegmentSentEntry.setStatus("current")
_RampMpMulticastLastSegmentSentIndex_Type = Unsigned32
_RampMpMulticastLastSegmentSentIndex_Object = MibTableColumn
rampMpMulticastLastSegmentSentIndex = _RampMpMulticastLastSegmentSentIndex_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 3, 1, 1),
    _RampMpMulticastLastSegmentSentIndex_Type()
)
rampMpMulticastLastSegmentSentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rampMpMulticastLastSegmentSentIndex.setStatus("current")
_RampMpMulticastLastSegmentSentTime_Type = TimeTicks
_RampMpMulticastLastSegmentSentTime_Object = MibTableColumn
rampMpMulticastLastSegmentSentTime = _RampMpMulticastLastSegmentSentTime_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 3, 1, 2),
    _RampMpMulticastLastSegmentSentTime_Type()
)
rampMpMulticastLastSegmentSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpMulticastLastSegmentSentTime.setStatus("current")
_RampMpMulticastLastSegmentSentDurationMilliseconds_Type = Unsigned32
_RampMpMulticastLastSegmentSentDurationMilliseconds_Object = MibTableColumn
rampMpMulticastLastSegmentSentDurationMilliseconds = _RampMpMulticastLastSegmentSentDurationMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 3, 1, 3),
    _RampMpMulticastLastSegmentSentDurationMilliseconds_Type()
)
rampMpMulticastLastSegmentSentDurationMilliseconds.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rampMpMulticastLastSegmentSentDurationMilliseconds.setStatus("current")
_RampMpSenderConformance_ObjectIdentity = ObjectIdentity
rampMpSenderConformance = _RampMpSenderConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 4)
)
_RampMpReceiverDiagnostics_ObjectIdentity = ObjectIdentity
rampMpReceiverDiagnostics = _RampMpReceiverDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2)
)
_RampMpReceiverDiagnosticsConformance_ObjectIdentity = ObjectIdentity
rampMpReceiverDiagnosticsConformance = _RampMpReceiverDiagnosticsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 1)
)
_RampMpReceiverDiagnosticsRegionalTable_Object = MibTable
rampMpReceiverDiagnosticsRegionalTable = _RampMpReceiverDiagnosticsRegionalTable_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalTable.setStatus("current")
_RampMpReceiverDiagnosticsRegionalEntry_Object = MibTableRow
rampMpReceiverDiagnosticsRegionalEntry = _RampMpReceiverDiagnosticsRegionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1)
)
rampMpReceiverDiagnosticsRegionalEntry.setIndexNames(
    (0, "MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalIndex"),
)
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalEntry.setStatus("current")
_RampMpReceiverDiagnosticsRegionalIndex_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalIndex_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalIndex = _RampMpReceiverDiagnosticsRegionalIndex_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 1),
    _RampMpReceiverDiagnosticsRegionalIndex_Type()
)
rampMpReceiverDiagnosticsRegionalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalIndex.setStatus("current")
_RampMpReceiverDiagnosticsRegionalRegionLocation_Type = SnmpAdminString
_RampMpReceiverDiagnosticsRegionalRegionLocation_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalRegionLocation = _RampMpReceiverDiagnosticsRegionalRegionLocation_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 2),
    _RampMpReceiverDiagnosticsRegionalRegionLocation_Type()
)
rampMpReceiverDiagnosticsRegionalRegionLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalRegionLocation.setStatus("current")
_RampMpReceiverDiagnosticsRegionalCIDRs_Type = OctetString
_RampMpReceiverDiagnosticsRegionalCIDRs_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalCIDRs = _RampMpReceiverDiagnosticsRegionalCIDRs_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 3),
    _RampMpReceiverDiagnosticsRegionalCIDRs_Type()
)
rampMpReceiverDiagnosticsRegionalCIDRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalCIDRs.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumReceivers_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumReceivers_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumReceivers = _RampMpReceiverDiagnosticsRegionalNumReceivers_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 4),
    _RampMpReceiverDiagnosticsRegionalNumReceivers_Type()
)
rampMpReceiverDiagnosticsRegionalNumReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumReceivers.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumNoMulticastReceived_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumNoMulticastReceived_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived = _RampMpReceiverDiagnosticsRegionalNumNoMulticastReceived_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 5),
    _RampMpReceiverDiagnosticsRegionalNumNoMulticastReceived_Type()
)
rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumStaleData_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumStaleData_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumStaleData = _RampMpReceiverDiagnosticsRegionalNumStaleData_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 6),
    _RampMpReceiverDiagnosticsRegionalNumStaleData_Type()
)
rampMpReceiverDiagnosticsRegionalNumStaleData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumStaleData.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumLowPacketLoss_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumLowPacketLoss_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumLowPacketLoss = _RampMpReceiverDiagnosticsRegionalNumLowPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 7),
    _RampMpReceiverDiagnosticsRegionalNumLowPacketLoss_Type()
)
rampMpReceiverDiagnosticsRegionalNumLowPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumLowPacketLoss.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumHighPacketLoss_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumHighPacketLoss_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumHighPacketLoss = _RampMpReceiverDiagnosticsRegionalNumHighPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 8),
    _RampMpReceiverDiagnosticsRegionalNumHighPacketLoss_Type()
)
rampMpReceiverDiagnosticsRegionalNumHighPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumHighPacketLoss.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumNoRecentPlay_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumNoRecentPlay_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumNoRecentPlay = _RampMpReceiverDiagnosticsRegionalNumNoRecentPlay_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 9),
    _RampMpReceiverDiagnosticsRegionalNumNoRecentPlay_Type()
)
rampMpReceiverDiagnosticsRegionalNumNoRecentPlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumNoRecentPlay.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumRecentLivePlay_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumRecentLivePlay_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumRecentLivePlay = _RampMpReceiverDiagnosticsRegionalNumRecentLivePlay_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 10),
    _RampMpReceiverDiagnosticsRegionalNumRecentLivePlay_Type()
)
rampMpReceiverDiagnosticsRegionalNumRecentLivePlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumRecentLivePlay.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumRecentDVRPlay_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumRecentDVRPlay_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay = _RampMpReceiverDiagnosticsRegionalNumRecentDVRPlay_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 11),
    _RampMpReceiverDiagnosticsRegionalNumRecentDVRPlay_Type()
)
rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumRecentLateSegs_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumRecentLateSegs_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumRecentLateSegs = _RampMpReceiverDiagnosticsRegionalNumRecentLateSegs_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 12),
    _RampMpReceiverDiagnosticsRegionalNumRecentLateSegs_Type()
)
rampMpReceiverDiagnosticsRegionalNumRecentLateSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumRecentLateSegs.setStatus("current")
_RampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs_Type = Unsigned32
_RampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs_Object = MibTableColumn
rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs = _RampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs_Object(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 2, 1, 13),
    _RampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs_Type()
)
rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs.setStatus("current")

# Managed Objects groups

rampMpSenderBasicObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 4, 1)
)
rampMpSenderBasicObjectGroup.setObjects(
      *(("MULTICASTPLUS-MIB", "rampMpSenderDescription"),
        ("MULTICASTPLUS-MIB", "rampMpSenderSourceFormat"),
        ("MULTICASTPLUS-MIB", "rampMpSenderSourceUrl"),
        ("MULTICASTPLUS-MIB", "rampMpSenderMulticastAddress"),
        ("MULTICASTPLUS-MIB", "rampMpSenderMulticastAddressIP"),
        ("MULTICASTPLUS-MIB", "rampMpSenderMulticastAddressPort"),
        ("MULTICASTPLUS-MIB", "rampMpSenderMulticastAddressTTL"),
        ("MULTICASTPLUS-MIB", "rampMpMulticastSentAverageSegmentSizeBytes"),
        ("MULTICASTPLUS-MIB", "rampMpMulticastSentTotalBytes"),
        ("MULTICASTPLUS-MIB", "rampMpMulticastSentTotalSegments"),
        ("MULTICASTPLUS-MIB", "rampMpMulticastSentAverageSegmentDurationMilliseconds"),
        ("MULTICASTPLUS-MIB", "rampMpMulticastLastSegmentSentTime"))
)
if mibBuilder.loadTexts:
    rampMpSenderBasicObjectGroup.setStatus("current")

rampMpSenderHighAvailabilityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 4, 2)
)
rampMpSenderHighAvailabilityObjectGroup.setObjects(
      *(("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityAddress"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityAddressIP"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityAddressPort"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityAddressTTL"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityUnicastAddressList"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityUnicastPort"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityActive"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityLastActiveTime"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityLastStandbyTime"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilitySourceOK"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityLastSourceOKTime"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityPriority"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityGroup"))
)
if mibBuilder.loadTexts:
    rampMpSenderHighAvailabilityObjectGroup.setStatus("current")

rampMpReceiverDiagnosticsRegionalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 1, 1)
)
rampMpReceiverDiagnosticsRegionalObjectGroup.setObjects(
      *(("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalRegionLocation"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalCIDRs"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumReceivers"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumStaleData"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumLowPacketLoss"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumHighPacketLoss"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumNoRecentPlay"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumRecentLivePlay"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumRecentLateSegs"),
        ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs"))
)
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsRegionalObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rampMpSenderCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47089, 1, 1, 4, 3)
)
rampMpSenderCompliance.setObjects(
      *(("MULTICASTPLUS-MIB", "rampMpSenderBasicObjectGroup"),
        ("MULTICASTPLUS-MIB", "rampMpSenderHighAvailabilityObjectGroup"))
)
if mibBuilder.loadTexts:
    rampMpSenderCompliance.setStatus(
        "current"
    )

rampMpReceiverDiagnosticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47089, 1, 2, 1, 2)
)
rampMpReceiverDiagnosticsCompliance.setObjects(
    ("MULTICASTPLUS-MIB", "rampMpReceiverDiagnosticsRegionalObjectGroup")
)
if mibBuilder.loadTexts:
    rampMpReceiverDiagnosticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTICASTPLUS-MIB",
    **{"ramp": ramp,
       "rampMpMIB": rampMpMIB,
       "rampMpSender": rampMpSender,
       "rampMpSenderTable": rampMpSenderTable,
       "rampMpSenderEntry": rampMpSenderEntry,
       "rampMpSenderIndex": rampMpSenderIndex,
       "rampMpSenderDescription": rampMpSenderDescription,
       "rampMpSenderSourceFormat": rampMpSenderSourceFormat,
       "rampMpSenderSourceUrl": rampMpSenderSourceUrl,
       "rampMpSenderMulticastAddress": rampMpSenderMulticastAddress,
       "rampMpSenderMulticastAddressIP": rampMpSenderMulticastAddressIP,
       "rampMpSenderMulticastAddressPort": rampMpSenderMulticastAddressPort,
       "rampMpSenderMulticastAddressTTL": rampMpSenderMulticastAddressTTL,
       "rampMpSenderHighAvailabilityAddress": rampMpSenderHighAvailabilityAddress,
       "rampMpSenderHighAvailabilityAddressIP": rampMpSenderHighAvailabilityAddressIP,
       "rampMpSenderHighAvailabilityAddressPort": rampMpSenderHighAvailabilityAddressPort,
       "rampMpSenderHighAvailabilityAddressTTL": rampMpSenderHighAvailabilityAddressTTL,
       "rampMpSenderHighAvailabilityActive": rampMpSenderHighAvailabilityActive,
       "rampMpSenderHighAvailabilityLastActiveTime": rampMpSenderHighAvailabilityLastActiveTime,
       "rampMpSenderHighAvailabilityLastStandbyTime": rampMpSenderHighAvailabilityLastStandbyTime,
       "rampMpSenderHighAvailabilitySourceOK": rampMpSenderHighAvailabilitySourceOK,
       "rampMpSenderHighAvailabilityLastSourceOKTime": rampMpSenderHighAvailabilityLastSourceOKTime,
       "rampMpSenderHighAvailabilityPriority": rampMpSenderHighAvailabilityPriority,
       "rampMpSenderHighAvailabilityGroup": rampMpSenderHighAvailabilityGroup,
       "rampMpSenderHighAvailabilityUnicastAddressList": rampMpSenderHighAvailabilityUnicastAddressList,
       "rampMpSenderHighAvailabilityUnicastPort": rampMpSenderHighAvailabilityUnicastPort,
       "rampMpMulticastSentTable": rampMpMulticastSentTable,
       "rampMpMulticastSentEntry": rampMpMulticastSentEntry,
       "rampMpMulticastSentTimeIntervalMinutes": rampMpMulticastSentTimeIntervalMinutes,
       "rampMpMulticastSentAverageSegmentSizeBytes": rampMpMulticastSentAverageSegmentSizeBytes,
       "rampMpMulticastSentTotalBytes": rampMpMulticastSentTotalBytes,
       "rampMpMulticastSentTotalSegments": rampMpMulticastSentTotalSegments,
       "rampMpMulticastSentAverageSegmentDurationMilliseconds": rampMpMulticastSentAverageSegmentDurationMilliseconds,
       "rampMpMulticastLastSegmentSentTable": rampMpMulticastLastSegmentSentTable,
       "rampMpMulticastLastSegmentSentEntry": rampMpMulticastLastSegmentSentEntry,
       "rampMpMulticastLastSegmentSentIndex": rampMpMulticastLastSegmentSentIndex,
       "rampMpMulticastLastSegmentSentTime": rampMpMulticastLastSegmentSentTime,
       "rampMpMulticastLastSegmentSentDurationMilliseconds": rampMpMulticastLastSegmentSentDurationMilliseconds,
       "rampMpSenderConformance": rampMpSenderConformance,
       "rampMpSenderBasicObjectGroup": rampMpSenderBasicObjectGroup,
       "rampMpSenderHighAvailabilityObjectGroup": rampMpSenderHighAvailabilityObjectGroup,
       "rampMpSenderCompliance": rampMpSenderCompliance,
       "rampMpReceiverDiagnostics": rampMpReceiverDiagnostics,
       "rampMpReceiverDiagnosticsConformance": rampMpReceiverDiagnosticsConformance,
       "rampMpReceiverDiagnosticsRegionalObjectGroup": rampMpReceiverDiagnosticsRegionalObjectGroup,
       "rampMpReceiverDiagnosticsCompliance": rampMpReceiverDiagnosticsCompliance,
       "rampMpReceiverDiagnosticsRegionalTable": rampMpReceiverDiagnosticsRegionalTable,
       "rampMpReceiverDiagnosticsRegionalEntry": rampMpReceiverDiagnosticsRegionalEntry,
       "rampMpReceiverDiagnosticsRegionalIndex": rampMpReceiverDiagnosticsRegionalIndex,
       "rampMpReceiverDiagnosticsRegionalRegionLocation": rampMpReceiverDiagnosticsRegionalRegionLocation,
       "rampMpReceiverDiagnosticsRegionalCIDRs": rampMpReceiverDiagnosticsRegionalCIDRs,
       "rampMpReceiverDiagnosticsRegionalNumReceivers": rampMpReceiverDiagnosticsRegionalNumReceivers,
       "rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived": rampMpReceiverDiagnosticsRegionalNumNoMulticastReceived,
       "rampMpReceiverDiagnosticsRegionalNumStaleData": rampMpReceiverDiagnosticsRegionalNumStaleData,
       "rampMpReceiverDiagnosticsRegionalNumLowPacketLoss": rampMpReceiverDiagnosticsRegionalNumLowPacketLoss,
       "rampMpReceiverDiagnosticsRegionalNumHighPacketLoss": rampMpReceiverDiagnosticsRegionalNumHighPacketLoss,
       "rampMpReceiverDiagnosticsRegionalNumNoRecentPlay": rampMpReceiverDiagnosticsRegionalNumNoRecentPlay,
       "rampMpReceiverDiagnosticsRegionalNumRecentLivePlay": rampMpReceiverDiagnosticsRegionalNumRecentLivePlay,
       "rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay": rampMpReceiverDiagnosticsRegionalNumRecentDVRPlay,
       "rampMpReceiverDiagnosticsRegionalNumRecentLateSegs": rampMpReceiverDiagnosticsRegionalNumRecentLateSegs,
       "rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs": rampMpReceiverDiagnosticsRegionalNumLifetimeLateSegs}
)
