# SNMP MIB module (SCTE-HMS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-COMMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:05 2025
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

(commonIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "commonIdent")

(scteHmsTree,) = mibBuilder.importSymbols(
    "SCTE-ROOT",
    "scteHmsTree")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommonAdminGroup_ObjectIdentity = ObjectIdentity
commonAdminGroup = _CommonAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1)
)


class _CommonLogicalID_Type(OctetString):
    """Custom type commonLogicalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CommonLogicalID_Type.__name__ = "OctetString"
_CommonLogicalID_Object = MibScalar
commonLogicalID = _CommonLogicalID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 1),
    _CommonLogicalID_Type()
)
commonLogicalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonLogicalID.setStatus("mandatory")


class _CommonVendor_Type(DisplayString):
    """Custom type commonVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonVendor_Type.__name__ = "DisplayString"
_CommonVendor_Object = MibScalar
commonVendor = _CommonVendor_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 2),
    _CommonVendor_Type()
)
commonVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonVendor.setStatus("mandatory")


class _CommonModelNumber_Type(DisplayString):
    """Custom type commonModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonModelNumber_Type.__name__ = "DisplayString"
_CommonModelNumber_Object = MibScalar
commonModelNumber = _CommonModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 3),
    _CommonModelNumber_Type()
)
commonModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonModelNumber.setStatus("mandatory")


class _CommonSerialNumber_Type(DisplayString):
    """Custom type commonSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonSerialNumber_Type.__name__ = "DisplayString"
_CommonSerialNumber_Object = MibScalar
commonSerialNumber = _CommonSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 4),
    _CommonSerialNumber_Type()
)
commonSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonSerialNumber.setStatus("mandatory")


class _CommonVendorInfo_Type(DisplayString):
    """Custom type commonVendorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonVendorInfo_Type.__name__ = "DisplayString"
_CommonVendorInfo_Object = MibScalar
commonVendorInfo = _CommonVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 5),
    _CommonVendorInfo_Type()
)
commonVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonVendorInfo.setStatus("optional")


class _CommonNEStatus_Type(OctetString):
    """Custom type commonNEStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_CommonNEStatus_Type.__name__ = "OctetString"
_CommonNEStatus_Object = MibScalar
commonNEStatus = _CommonNEStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 6),
    _CommonNEStatus_Type()
)
commonNEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNEStatus.setStatus("mandatory")


class _CommonReset_Type(Integer32):
    """Custom type commonReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CommonReset_Type.__name__ = "Integer32"
_CommonReset_Object = MibScalar
commonReset = _CommonReset_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 7),
    _CommonReset_Type()
)
commonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonReset.setStatus("mandatory")


class _CommonAlarmDetectionControl_Type(Integer32):
    """Custom type commonAlarmDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectionDisabled", 1),
          ("detectionEnabled", 2),
          ("detectionEnabledAndRegenerate", 3))
    )


_CommonAlarmDetectionControl_Type.__name__ = "Integer32"
_CommonAlarmDetectionControl_Object = MibScalar
commonAlarmDetectionControl = _CommonAlarmDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 8),
    _CommonAlarmDetectionControl_Type()
)
commonAlarmDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAlarmDetectionControl.setStatus("mandatory")
_CommonNetworkAddress_Type = IpAddress
_CommonNetworkAddress_Object = MibScalar
commonNetworkAddress = _CommonNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 9),
    _CommonNetworkAddress_Type()
)
commonNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNetworkAddress.setStatus("deprecated")
_CommonCheckCode_Type = Integer32
_CommonCheckCode_Object = MibScalar
commonCheckCode = _CommonCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 10),
    _CommonCheckCode_Type()
)
commonCheckCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonCheckCode.setStatus("mandatory")


class _CommonTrapCommunityString_Type(OctetString):
    """Custom type commonTrapCommunityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CommonTrapCommunityString_Type.__name__ = "OctetString"
_CommonTrapCommunityString_Object = MibScalar
commonTrapCommunityString = _CommonTrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 11),
    _CommonTrapCommunityString_Type()
)
commonTrapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonTrapCommunityString.setStatus("mandatory")


class _CommonTamperStatus_Type(Integer32):
    """Custom type commonTamperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intact", 1),
          ("compromised", 2))
    )


_CommonTamperStatus_Type.__name__ = "Integer32"
_CommonTamperStatus_Object = MibScalar
commonTamperStatus = _CommonTamperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 12),
    _CommonTamperStatus_Type()
)
commonTamperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonTamperStatus.setStatus("optional")


class _CommonInternalTemperature_Type(Integer32):
    """Custom type commonInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 130),
    )


_CommonInternalTemperature_Type.__name__ = "Integer32"
_CommonInternalTemperature_Object = MibScalar
commonInternalTemperature = _CommonInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 13),
    _CommonInternalTemperature_Type()
)
commonInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonInternalTemperature.setStatus("optional")
_CommonTime_Type = Integer32
_CommonTime_Object = MibScalar
commonTime = _CommonTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 14),
    _CommonTime_Type()
)
commonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonTime.setStatus("optional")
_CommonVarBindings_Type = Integer32
_CommonVarBindings_Object = MibScalar
commonVarBindings = _CommonVarBindings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 15),
    _CommonVarBindings_Type()
)
commonVarBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonVarBindings.setStatus("mandatory")


class _CommonResetCause_Type(Integer32):
    """Custom type commonResetCause based on Integer32"""
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
        *(("other", 1),
          ("powerup", 2),
          ("command", 3),
          ("watchdog", 4),
          ("craft", 5))
    )


_CommonResetCause_Type.__name__ = "Integer32"
_CommonResetCause_Object = MibScalar
commonResetCause = _CommonResetCause_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 16),
    _CommonResetCause_Type()
)
commonResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonResetCause.setStatus("mandatory")


class _CommonCraftStatus_Type(Integer32):
    """Custom type commonCraftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_CommonCraftStatus_Type.__name__ = "Integer32"
_CommonCraftStatus_Object = MibScalar
commonCraftStatus = _CommonCraftStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 17),
    _CommonCraftStatus_Type()
)
commonCraftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonCraftStatus.setStatus("mandatory")
_CommonNetworkIpAddressType_Type = InetAddressType
_CommonNetworkIpAddressType_Object = MibScalar
commonNetworkIpAddressType = _CommonNetworkIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 18),
    _CommonNetworkIpAddressType_Type()
)
commonNetworkIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNetworkIpAddressType.setStatus("mandatory")
_CommonNetworkIpAddress_Type = InetAddress
_CommonNetworkIpAddress_Object = MibScalar
commonNetworkIpAddress = _CommonNetworkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 1, 19),
    _CommonNetworkIpAddress_Type()
)
commonNetworkIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNetworkIpAddress.setStatus("mandatory")
_CommonMACGroup_ObjectIdentity = ObjectIdentity
commonMACGroup = _CommonMACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2)
)


class _CommonBackoffPeriod_Type(Integer32):
    """Custom type commonBackoffPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CommonBackoffPeriod_Type.__name__ = "Integer32"
_CommonBackoffPeriod_Object = MibScalar
commonBackoffPeriod = _CommonBackoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 1),
    _CommonBackoffPeriod_Type()
)
commonBackoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffPeriod.setStatus("mandatory")


class _CommonACKTimeoutWindow_Type(Integer32):
    """Custom type commonACKTimeoutWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CommonACKTimeoutWindow_Type.__name__ = "Integer32"
_CommonACKTimeoutWindow_Object = MibScalar
commonACKTimeoutWindow = _CommonACKTimeoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 2),
    _CommonACKTimeoutWindow_Type()
)
commonACKTimeoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonACKTimeoutWindow.setStatus("mandatory")


class _CommonMaximumMACLayerRetries_Type(Integer32):
    """Custom type commonMaximumMACLayerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CommonMaximumMACLayerRetries_Type.__name__ = "Integer32"
_CommonMaximumMACLayerRetries_Object = MibScalar
commonMaximumMACLayerRetries = _CommonMaximumMACLayerRetries_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 3),
    _CommonMaximumMACLayerRetries_Type()
)
commonMaximumMACLayerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMaximumMACLayerRetries.setStatus("mandatory")
_CommonMaxPayloadSize_Type = Integer32
_CommonMaxPayloadSize_Object = MibScalar
commonMaxPayloadSize = _CommonMaxPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 4),
    _CommonMaxPayloadSize_Type()
)
commonMaxPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMaxPayloadSize.setStatus("mandatory")


class _CommonBackoffMinimumExponent_Type(Integer32):
    """Custom type commonBackoffMinimumExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CommonBackoffMinimumExponent_Type.__name__ = "Integer32"
_CommonBackoffMinimumExponent_Object = MibScalar
commonBackoffMinimumExponent = _CommonBackoffMinimumExponent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 5),
    _CommonBackoffMinimumExponent_Type()
)
commonBackoffMinimumExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffMinimumExponent.setStatus("mandatory")


class _CommonBackoffMaximumExponent_Type(Integer32):
    """Custom type commonBackoffMaximumExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CommonBackoffMaximumExponent_Type.__name__ = "Integer32"
_CommonBackoffMaximumExponent_Object = MibScalar
commonBackoffMaximumExponent = _CommonBackoffMaximumExponent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 6),
    _CommonBackoffMaximumExponent_Type()
)
commonBackoffMaximumExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffMaximumExponent.setStatus("mandatory")
_CommonPhysAddress_Type = OctetString
_CommonPhysAddress_Object = MibScalar
commonPhysAddress = _CommonPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2, 7),
    _CommonPhysAddress_Type()
)
commonPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonPhysAddress.setStatus("mandatory")
_CommonMulticastGroup_ObjectIdentity = ObjectIdentity
commonMulticastGroup = _CommonMulticastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3)
)


class _CommonMaxMulticastAddresses_Type(Integer32):
    """Custom type commonMaxMulticastAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_CommonMaxMulticastAddresses_Type.__name__ = "Integer32"
_CommonMaxMulticastAddresses_Object = MibScalar
commonMaxMulticastAddresses = _CommonMaxMulticastAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3, 1),
    _CommonMaxMulticastAddresses_Type()
)
commonMaxMulticastAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMaxMulticastAddresses.setStatus("mandatory")
_CommonMulticastAddressTable_Object = MibTable
commonMulticastAddressTable = _CommonMulticastAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    commonMulticastAddressTable.setStatus("mandatory")
_CommonMulticastAddressEntry_Object = MibTableRow
commonMulticastAddressEntry = _CommonMulticastAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3, 2, 1)
)
commonMulticastAddressEntry.setIndexNames(
    (0, "SCTE-HMS-COMMON-MIB", "commonMulticastAddressIndex"),
)
if mibBuilder.loadTexts:
    commonMulticastAddressEntry.setStatus("mandatory")


class _CommonMulticastAddressIndex_Type(Integer32):
    """Custom type commonMulticastAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CommonMulticastAddressIndex_Type.__name__ = "Integer32"
_CommonMulticastAddressIndex_Object = MibTableColumn
commonMulticastAddressIndex = _CommonMulticastAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3, 2, 1, 1),
    _CommonMulticastAddressIndex_Type()
)
commonMulticastAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMulticastAddressIndex.setStatus("mandatory")


class _CommonMulticastAddressNumber_Type(OctetString):
    """Custom type commonMulticastAddressNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_CommonMulticastAddressNumber_Type.__name__ = "OctetString"
_CommonMulticastAddressNumber_Object = MibTableColumn
commonMulticastAddressNumber = _CommonMulticastAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 3, 2, 1, 2),
    _CommonMulticastAddressNumber_Type()
)
commonMulticastAddressNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMulticastAddressNumber.setStatus("mandatory")
_CommonStatsGroup_ObjectIdentity = ObjectIdentity
commonStatsGroup = _CommonStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4)
)
_CommonMacStats_ObjectIdentity = ObjectIdentity
commonMacStats = _CommonMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1)
)
_CommonForwardPathLOSEvents_Type = Counter32
_CommonForwardPathLOSEvents_Object = MibScalar
commonForwardPathLOSEvents = _CommonForwardPathLOSEvents_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1, 1),
    _CommonForwardPathLOSEvents_Type()
)
commonForwardPathLOSEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathLOSEvents.setStatus("optional")
_CommonForwardPathFramingErrors_Type = Counter32
_CommonForwardPathFramingErrors_Object = MibScalar
commonForwardPathFramingErrors = _CommonForwardPathFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1, 2),
    _CommonForwardPathFramingErrors_Type()
)
commonForwardPathFramingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathFramingErrors.setStatus("optional")
_CommonForwardPathCRCErrors_Type = Counter32
_CommonForwardPathCRCErrors_Object = MibScalar
commonForwardPathCRCErrors = _CommonForwardPathCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1, 3),
    _CommonForwardPathCRCErrors_Type()
)
commonForwardPathCRCErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathCRCErrors.setStatus("optional")
_CommonInvalidMacCmds_Type = Counter32
_CommonInvalidMacCmds_Object = MibScalar
commonInvalidMacCmds = _CommonInvalidMacCmds_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1, 4),
    _CommonInvalidMacCmds_Type()
)
commonInvalidMacCmds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonInvalidMacCmds.setStatus("optional")
_CommonRfGroup_ObjectIdentity = ObjectIdentity
commonRfGroup = _CommonRfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5)
)


class _CommonReturnPathFrequency_Type(Integer32):
    """Custom type commonReturnPathFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CommonReturnPathFrequency_Type.__name__ = "Integer32"
_CommonReturnPathFrequency_Object = MibScalar
commonReturnPathFrequency = _CommonReturnPathFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5, 1),
    _CommonReturnPathFrequency_Type()
)
commonReturnPathFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonReturnPathFrequency.setStatus("mandatory")


class _CommonForwardPathFrequency_Type(Integer32):
    """Custom type commonForwardPathFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CommonForwardPathFrequency_Type.__name__ = "Integer32"
_CommonForwardPathFrequency_Object = MibScalar
commonForwardPathFrequency = _CommonForwardPathFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5, 2),
    _CommonForwardPathFrequency_Type()
)
commonForwardPathFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonForwardPathFrequency.setStatus("mandatory")
_CommonProvisionedReturnPowerLevel_Type = Integer32
_CommonProvisionedReturnPowerLevel_Object = MibScalar
commonProvisionedReturnPowerLevel = _CommonProvisionedReturnPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5, 3),
    _CommonProvisionedReturnPowerLevel_Type()
)
commonProvisionedReturnPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProvisionedReturnPowerLevel.setStatus("mandatory")


class _CommonForwardPathReceiveLevel_Type(Integer32):
    """Custom type commonForwardPathReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CommonForwardPathReceiveLevel_Type.__name__ = "Integer32"
_CommonForwardPathReceiveLevel_Object = MibScalar
commonForwardPathReceiveLevel = _CommonForwardPathReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5, 4),
    _CommonForwardPathReceiveLevel_Type()
)
commonForwardPathReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonForwardPathReceiveLevel.setStatus("optional")


class _CommonMaxReturnPower_Type(Integer32):
    """Custom type commonMaxReturnPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 600),
    )


_CommonMaxReturnPower_Type.__name__ = "Integer32"
_CommonMaxReturnPower_Object = MibScalar
commonMaxReturnPower = _CommonMaxReturnPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5, 5),
    _CommonMaxReturnPower_Type()
)
commonMaxReturnPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMaxReturnPower.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hmsColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 0)
)
hmsColdStart.setObjects(
      *(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-MIB", "commonLogicalID"))
)
if mibBuilder.loadTexts:
    hmsColdStart.setStatus(
        ""
    )

hmsWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 2)
)
hmsWarmStart.setObjects(
      *(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-MIB", "commonLogicalID"))
)
if mibBuilder.loadTexts:
    hmsWarmStart.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-COMMON-MIB",
    **{"hmsColdStart": hmsColdStart,
       "hmsWarmStart": hmsWarmStart,
       "commonAdminGroup": commonAdminGroup,
       "commonLogicalID": commonLogicalID,
       "commonVendor": commonVendor,
       "commonModelNumber": commonModelNumber,
       "commonSerialNumber": commonSerialNumber,
       "commonVendorInfo": commonVendorInfo,
       "commonNEStatus": commonNEStatus,
       "commonReset": commonReset,
       "commonAlarmDetectionControl": commonAlarmDetectionControl,
       "commonNetworkAddress": commonNetworkAddress,
       "commonCheckCode": commonCheckCode,
       "commonTrapCommunityString": commonTrapCommunityString,
       "commonTamperStatus": commonTamperStatus,
       "commonInternalTemperature": commonInternalTemperature,
       "commonTime": commonTime,
       "commonVarBindings": commonVarBindings,
       "commonResetCause": commonResetCause,
       "commonCraftStatus": commonCraftStatus,
       "commonNetworkIpAddressType": commonNetworkIpAddressType,
       "commonNetworkIpAddress": commonNetworkIpAddress,
       "commonMACGroup": commonMACGroup,
       "commonBackoffPeriod": commonBackoffPeriod,
       "commonACKTimeoutWindow": commonACKTimeoutWindow,
       "commonMaximumMACLayerRetries": commonMaximumMACLayerRetries,
       "commonMaxPayloadSize": commonMaxPayloadSize,
       "commonBackoffMinimumExponent": commonBackoffMinimumExponent,
       "commonBackoffMaximumExponent": commonBackoffMaximumExponent,
       "commonPhysAddress": commonPhysAddress,
       "commonMulticastGroup": commonMulticastGroup,
       "commonMaxMulticastAddresses": commonMaxMulticastAddresses,
       "commonMulticastAddressTable": commonMulticastAddressTable,
       "commonMulticastAddressEntry": commonMulticastAddressEntry,
       "commonMulticastAddressIndex": commonMulticastAddressIndex,
       "commonMulticastAddressNumber": commonMulticastAddressNumber,
       "commonStatsGroup": commonStatsGroup,
       "commonMacStats": commonMacStats,
       "commonForwardPathLOSEvents": commonForwardPathLOSEvents,
       "commonForwardPathFramingErrors": commonForwardPathFramingErrors,
       "commonForwardPathCRCErrors": commonForwardPathCRCErrors,
       "commonInvalidMacCmds": commonInvalidMacCmds,
       "commonRfGroup": commonRfGroup,
       "commonReturnPathFrequency": commonReturnPathFrequency,
       "commonForwardPathFrequency": commonForwardPathFrequency,
       "commonProvisionedReturnPowerLevel": commonProvisionedReturnPowerLevel,
       "commonForwardPathReceiveLevel": commonForwardPathReceiveLevel,
       "commonMaxReturnPower": commonMaxReturnPower}
)
