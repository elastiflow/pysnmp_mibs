# SNMP MIB module (SCTE-HMS-COMMON-BKTEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-COMMON-BKTEL-MIB.mib
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
    commonNetworkAddress.setStatus("mandatory")
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
_CommonMACGroup_ObjectIdentity = ObjectIdentity
commonMACGroup = _CommonMACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 2)
)
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
_CommonStatsGroup_ObjectIdentity = ObjectIdentity
commonStatsGroup = _CommonStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4)
)
_CommonMacStats_ObjectIdentity = ObjectIdentity
commonMacStats = _CommonMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 4, 1)
)
_CommonRfGroup_ObjectIdentity = ObjectIdentity
commonRfGroup = _CommonRfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3, 5)
)

# Managed Objects groups


# Notification objects

hmsColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 0)
)
hmsColdStart.setObjects(
      *(("SCTE-HMS-COMMON-BKTEL-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-BKTEL-MIB", "commonLogicalID"))
)
if mibBuilder.loadTexts:
    hmsColdStart.setStatus(
        ""
    )

hmsWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 2)
)
hmsWarmStart.setObjects(
      *(("SCTE-HMS-COMMON-BKTEL-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-BKTEL-MIB", "commonLogicalID"))
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
    "SCTE-HMS-COMMON-BKTEL-MIB",
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
       "commonMACGroup": commonMACGroup,
       "commonPhysAddress": commonPhysAddress,
       "commonMulticastGroup": commonMulticastGroup,
       "commonStatsGroup": commonStatsGroup,
       "commonMacStats": commonMacStats,
       "commonRfGroup": commonRfGroup}
)
