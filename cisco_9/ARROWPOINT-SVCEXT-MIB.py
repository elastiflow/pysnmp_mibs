# SNMP MIB module (ARROWPOINT-SVCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ARROWPOINT-SVCEXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 19:35:05 2025
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

(svcExt,) = mibBuilder.importSymbols(
    "CISCO-APENT-MIB",
    "svcExt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(RowStatus,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSvcExtMib_ObjectIdentity = ObjectIdentity
apSvcExtMib = _ApSvcExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1)
)
_ApSvcExtMibNotifs_ObjectIdentity = ObjectIdentity
apSvcExtMibNotifs = _ApSvcExtMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 0)
)
_ApSvcExtMibObjects_ObjectIdentity = ObjectIdentity
apSvcExtMibObjects = _ApSvcExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 1)
)
_ApSvcExtMibConform_ObjectIdentity = ObjectIdentity
apSvcExtMibConform = _ApSvcExtMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2)
)
_ApSvcExtMibCompliances_ObjectIdentity = ObjectIdentity
apSvcExtMibCompliances = _ApSvcExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2, 1)
)
_ApSvcExtMibCompliance_ObjectIdentity = ObjectIdentity
apSvcExtMibCompliance = _ApSvcExtMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2, 1, 1)
)
_ApSvcExtMibGroups_ObjectIdentity = ObjectIdentity
apSvcExtMibGroups = _ApSvcExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2, 2)
)
_ApSvcExtMibGroup_ObjectIdentity = ObjectIdentity
apSvcExtMibGroup = _ApSvcExtMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2, 2, 1)
)
_ApSvcExtMibNotif_ObjectIdentity = ObjectIdentity
apSvcExtMibNotif = _ApSvcExtMibNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 2, 2, 2)
)
_ApSvcTable_Object = MibTable
apSvcTable = _ApSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2)
)
if mibBuilder.loadTexts:
    apSvcTable.setStatus("mandatory")
_ApSvcEntry_Object = MibTableRow
apSvcEntry = _ApSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1)
)
apSvcEntry.setIndexNames(
    (0, "ARROWPOINT-SVCEXT-MIB", "apSvcName"),
)
if mibBuilder.loadTexts:
    apSvcEntry.setStatus("mandatory")


class _ApSvcName_Type(SnmpAdminString):
    """Custom type apSvcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApSvcName_Type.__name__ = "SnmpAdminString"
_ApSvcName_Object = MibTableColumn
apSvcName = _ApSvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 1),
    _ApSvcName_Type()
)
apSvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcName.setStatus("mandatory")


class _ApSvcIndex_Type(Integer32):
    """Custom type apSvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ApSvcIndex_Type.__name__ = "Integer32"
_ApSvcIndex_Object = MibTableColumn
apSvcIndex = _ApSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 2),
    _ApSvcIndex_Type()
)
apSvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcIndex.setStatus("mandatory")
_ApSvcIPAddress_Type = IpAddress
_ApSvcIPAddress_Object = MibTableColumn
apSvcIPAddress = _ApSvcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 3),
    _ApSvcIPAddress_Type()
)
apSvcIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcIPAddress.setStatus("mandatory")


class _ApSvcIPProtocol_Type(Integer32):
    """Custom type apSvcIPProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_ApSvcIPProtocol_Type.__name__ = "Integer32"
_ApSvcIPProtocol_Object = MibTableColumn
apSvcIPProtocol = _ApSvcIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 4),
    _ApSvcIPProtocol_Type()
)
apSvcIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcIPProtocol.setStatus("mandatory")


class _ApSvcPort_Type(Integer32):
    """Custom type apSvcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcPort_Type.__name__ = "Integer32"
_ApSvcPort_Object = MibTableColumn
apSvcPort = _ApSvcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 5),
    _ApSvcPort_Type()
)
apSvcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPort.setStatus("mandatory")


class _ApSvcKALType_Type(Integer32):
    """Custom type apSvcKALType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("icmp", 1),
          ("http", 2),
          ("ftp", 3),
          ("tcp", 4),
          ("named", 5),
          ("script", 6),
          ("ssl", 7))
    )


_ApSvcKALType_Type.__name__ = "Integer32"
_ApSvcKALType_Object = MibTableColumn
apSvcKALType = _ApSvcKALType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 6),
    _ApSvcKALType_Type()
)
apSvcKALType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALType.setStatus("mandatory")


class _ApSvcKALFrequency_Type(Integer32):
    """Custom type apSvcKALFrequency based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcKALFrequency_Type.__name__ = "Integer32"
_ApSvcKALFrequency_Object = MibTableColumn
apSvcKALFrequency = _ApSvcKALFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 7),
    _ApSvcKALFrequency_Type()
)
apSvcKALFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALFrequency.setStatus("mandatory")


class _ApSvcKALMaxFailure_Type(Integer32):
    """Custom type apSvcKALMaxFailure based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApSvcKALMaxFailure_Type.__name__ = "Integer32"
_ApSvcKALMaxFailure_Object = MibTableColumn
apSvcKALMaxFailure = _ApSvcKALMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 8),
    _ApSvcKALMaxFailure_Type()
)
apSvcKALMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALMaxFailure.setStatus("mandatory")


class _ApSvcKALRetryPeriod_Type(Integer32):
    """Custom type apSvcKALRetryPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcKALRetryPeriod_Type.__name__ = "Integer32"
_ApSvcKALRetryPeriod_Object = MibTableColumn
apSvcKALRetryPeriod = _ApSvcKALRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 9),
    _ApSvcKALRetryPeriod_Type()
)
apSvcKALRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALRetryPeriod.setStatus("mandatory")


class _ApSvcKALUri_Type(SnmpAdminString):
    """Custom type apSvcKALUri based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcKALUri_Type.__name__ = "SnmpAdminString"
_ApSvcKALUri_Object = MibTableColumn
apSvcKALUri = _ApSvcKALUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 10),
    _ApSvcKALUri_Type()
)
apSvcKALUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALUri.setStatus("mandatory")


class _ApSvcKALMethod_Type(Integer32):
    """Custom type apSvcKALMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("head", 0),
          ("get", 1),
          ("post", 2))
    )


_ApSvcKALMethod_Type.__name__ = "Integer32"
_ApSvcKALMethod_Object = MibTableColumn
apSvcKALMethod = _ApSvcKALMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 11),
    _ApSvcKALMethod_Type()
)
apSvcKALMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALMethod.setStatus("mandatory")


class _ApSvcEnable_Type(Integer32):
    """Custom type apSvcEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcEnable_Type.__name__ = "Integer32"
_ApSvcEnable_Object = MibTableColumn
apSvcEnable = _ApSvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 12),
    _ApSvcEnable_Type()
)
apSvcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcEnable.setStatus("mandatory")


class _ApSvcType_Type(Integer32):
    """Custom type apSvcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("redirect", 2),
          ("proxyCache", 4),
          ("transparentCache", 8),
          ("automaticRedirect", 16),
          ("replicationStore", 32),
          ("replicationCache", 64),
          ("smashCache", 128),
          ("redundancyUp", 256),
          ("nciInfoOnly", 512),
          ("nciDirectReturn", 1024),
          ("replicationStoreRedirect", 2048),
          ("replicationCacheRedirect", 4096),
          ("sslAccel", 8192),
          ("sslAccelBackend", 16384),
          ("sslInit", 32768))
    )


_ApSvcType_Type.__name__ = "Integer32"
_ApSvcType_Object = MibTableColumn
apSvcType = _ApSvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 13),
    _ApSvcType_Type()
)
apSvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcType.setStatus("mandatory")


class _ApSvcQOSMinRate_Type(Integer32):
    """Custom type apSvcQOSMinRate based on Integer32"""
    defaultValue = 14400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcQOSMinRate_Type.__name__ = "Integer32"
_ApSvcQOSMinRate_Object = MibTableColumn
apSvcQOSMinRate = _ApSvcQOSMinRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 14),
    _ApSvcQOSMinRate_Type()
)
apSvcQOSMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcQOSMinRate.setStatus("mandatory")


class _ApSvcQOSMinBW_Type(Integer32):
    """Custom type apSvcQOSMinBW based on Integer32"""
    defaultValue = 100000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcQOSMinBW_Type.__name__ = "Integer32"
_ApSvcQOSMinBW_Object = MibTableColumn
apSvcQOSMinBW = _ApSvcQOSMinBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 15),
    _ApSvcQOSMinBW_Type()
)
apSvcQOSMinBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcQOSMinBW.setStatus("mandatory")


class _ApSvcWeight_Type(Integer32):
    """Custom type apSvcWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ApSvcWeight_Type.__name__ = "Integer32"
_ApSvcWeight_Object = MibTableColumn
apSvcWeight = _ApSvcWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 16),
    _ApSvcWeight_Type()
)
apSvcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcWeight.setStatus("mandatory")


class _ApSvcState_Type(Integer32):
    """Custom type apSvcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("suspended", 1),
          ("down", 2),
          ("alive", 4),
          ("dying", 5))
    )


_ApSvcState_Type.__name__ = "Integer32"
_ApSvcState_Object = MibTableColumn
apSvcState = _ApSvcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 17),
    _ApSvcState_Type()
)
apSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcState.setStatus("mandatory")


class _ApSvcShortLoad_Type(Integer32):
    """Custom type apSvcShortLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcShortLoad_Type.__name__ = "Integer32"
_ApSvcShortLoad_Object = MibTableColumn
apSvcShortLoad = _ApSvcShortLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 18),
    _ApSvcShortLoad_Type()
)
apSvcShortLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcShortLoad.setStatus("mandatory")


class _ApSvcMaxConnections_Type(Integer32):
    """Custom type apSvcMaxConnections based on Integer32"""
    defaultValue = 65534

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 65534),
    )


_ApSvcMaxConnections_Type.__name__ = "Integer32"
_ApSvcMaxConnections_Object = MibTableColumn
apSvcMaxConnections = _ApSvcMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 19),
    _ApSvcMaxConnections_Type()
)
apSvcMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcMaxConnections.setStatus("mandatory")


class _ApSvcConnections_Type(Integer32):
    """Custom type apSvcConnections based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ApSvcConnections_Type.__name__ = "Integer32"
_ApSvcConnections_Object = MibTableColumn
apSvcConnections = _ApSvcConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 20),
    _ApSvcConnections_Type()
)
apSvcConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcConnections.setStatus("mandatory")


class _ApSvcTransitions_Type(Integer32):
    """Custom type apSvcTransitions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcTransitions_Type.__name__ = "Integer32"
_ApSvcTransitions_Object = MibTableColumn
apSvcTransitions = _ApSvcTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 21),
    _ApSvcTransitions_Type()
)
apSvcTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcTransitions.setStatus("mandatory")


class _ApSvcMaxContent_Type(Integer32):
    """Custom type apSvcMaxContent based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcMaxContent_Type.__name__ = "Integer32"
_ApSvcMaxContent_Object = MibTableColumn
apSvcMaxContent = _ApSvcMaxContent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 22),
    _ApSvcMaxContent_Type()
)
apSvcMaxContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcMaxContent.setStatus("mandatory")


class _ApSvcMaxUsage_Type(Integer32):
    """Custom type apSvcMaxUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApSvcMaxUsage_Type.__name__ = "Integer32"
_ApSvcMaxUsage_Object = MibTableColumn
apSvcMaxUsage = _ApSvcMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 23),
    _ApSvcMaxUsage_Type()
)
apSvcMaxUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcMaxUsage.setStatus("mandatory")


class _ApSvcMaxAge_Type(Integer32):
    """Custom type apSvcMaxAge based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ApSvcMaxAge_Type.__name__ = "Integer32"
_ApSvcMaxAge_Object = MibTableColumn
apSvcMaxAge = _ApSvcMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 24),
    _ApSvcMaxAge_Type()
)
apSvcMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcMaxAge.setStatus("mandatory")


class _ApSvcAccessRecordName_Type(SnmpAdminString):
    """Custom type apSvcAccessRecordName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApSvcAccessRecordName_Type.__name__ = "SnmpAdminString"
_ApSvcAccessRecordName_Object = MibTableColumn
apSvcAccessRecordName = _ApSvcAccessRecordName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 25),
    _ApSvcAccessRecordName_Type()
)
apSvcAccessRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcAccessRecordName.setStatus("mandatory")
_ApSvcStatus_Type = RowStatus
_ApSvcStatus_Object = MibTableColumn
apSvcStatus = _ApSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 26),
    _ApSvcStatus_Type()
)
apSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcStatus.setStatus("mandatory")


class _ApSvcCookie_Type(SnmpAdminString):
    """Custom type apSvcCookie based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ApSvcCookie_Type.__name__ = "SnmpAdminString"
_ApSvcCookie_Object = MibTableColumn
apSvcCookie = _ApSvcCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 27),
    _ApSvcCookie_Type()
)
apSvcCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCookie.setStatus("mandatory")


class _ApSvcKALPersistence_Type(Integer32):
    """Custom type apSvcKALPersistence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-persistent", 0),
          ("persistent", 1))
    )


_ApSvcKALPersistence_Type.__name__ = "Integer32"
_ApSvcKALPersistence_Object = MibTableColumn
apSvcKALPersistence = _ApSvcKALPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 28),
    _ApSvcKALPersistence_Type()
)
apSvcKALPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALPersistence.setStatus("mandatory")


class _ApSvcKALName_Type(SnmpAdminString):
    """Custom type apSvcKALName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApSvcKALName_Type.__name__ = "SnmpAdminString"
_ApSvcKALName_Object = MibTableColumn
apSvcKALName = _ApSvcKALName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 29),
    _ApSvcKALName_Type()
)
apSvcKALName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALName.setStatus("mandatory")


class _ApSvcLongLoad_Type(Integer32):
    """Custom type apSvcLongLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcLongLoad_Type.__name__ = "Integer32"
_ApSvcLongLoad_Object = MibTableColumn
apSvcLongLoad = _ApSvcLongLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 30),
    _ApSvcLongLoad_Type()
)
apSvcLongLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcLongLoad.setStatus("mandatory")


class _ApSvcKALPort_Type(Integer32):
    """Custom type apSvcKALPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcKALPort_Type.__name__ = "Integer32"
_ApSvcKALPort_Object = MibTableColumn
apSvcKALPort = _ApSvcKALPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 31),
    _ApSvcKALPort_Type()
)
apSvcKALPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALPort.setStatus("mandatory")


class _ApSvcPublishName_Type(SnmpAdminString):
    """Custom type apSvcPublishName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcPublishName_Type.__name__ = "SnmpAdminString"
_ApSvcPublishName_Object = MibTableColumn
apSvcPublishName = _ApSvcPublishName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 32),
    _ApSvcPublishName_Type()
)
apSvcPublishName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPublishName.setStatus("mandatory")


class _ApSvcPublishState_Type(Integer32):
    """Custom type apSvcPublishState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("publisher", 1),
          ("subscriber", 2))
    )


_ApSvcPublishState_Type.__name__ = "Integer32"
_ApSvcPublishState_Object = MibTableColumn
apSvcPublishState = _ApSvcPublishState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 33),
    _ApSvcPublishState_Type()
)
apSvcPublishState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPublishState.setStatus("mandatory")


class _ApSvcPublishInterval_Type(Integer32):
    """Custom type apSvcPublishInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcPublishInterval_Type.__name__ = "Integer32"
_ApSvcPublishInterval_Object = MibTableColumn
apSvcPublishInterval = _ApSvcPublishInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 34),
    _ApSvcPublishInterval_Type()
)
apSvcPublishInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPublishInterval.setStatus("mandatory")


class _ApSvcAccessType_Type(Integer32):
    """Custom type apSvcAccessType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp-access", 0),
          ("http-access", 1),
          ("no-access", 2))
    )


_ApSvcAccessType_Type.__name__ = "Integer32"
_ApSvcAccessType_Object = MibTableColumn
apSvcAccessType = _ApSvcAccessType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 35),
    _ApSvcAccessType_Type()
)
apSvcAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcAccessType.setStatus("mandatory")


class _ApSvcKALHash_Type(SnmpAdminString):
    """Custom type apSvcKALHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALHash_Type.__name__ = "SnmpAdminString"
_ApSvcKALHash_Object = MibTableColumn
apSvcKALHash = _ApSvcKALHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 36),
    _ApSvcKALHash_Type()
)
apSvcKALHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALHash.setStatus("mandatory")


class _ApSvcKALFTPRecord_Type(SnmpAdminString):
    """Custom type apSvcKALFTPRecord based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApSvcKALFTPRecord_Type.__name__ = "SnmpAdminString"
_ApSvcKALFTPRecord_Object = MibTableColumn
apSvcKALFTPRecord = _ApSvcKALFTPRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 37),
    _ApSvcKALFTPRecord_Type()
)
apSvcKALFTPRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALFTPRecord.setStatus("mandatory")


class _ApSvcPublishFile_Type(SnmpAdminString):
    """Custom type apSvcPublishFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcPublishFile_Type.__name__ = "SnmpAdminString"
_ApSvcPublishFile_Object = MibTableColumn
apSvcPublishFile = _ApSvcPublishFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 38),
    _ApSvcPublishFile_Type()
)
apSvcPublishFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPublishFile.setStatus("mandatory")


class _ApSvcRedirectDomain_Type(SnmpAdminString):
    """Custom type apSvcRedirectDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcRedirectDomain_Type.__name__ = "SnmpAdminString"
_ApSvcRedirectDomain_Object = MibTableColumn
apSvcRedirectDomain = _ApSvcRedirectDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 39),
    _ApSvcRedirectDomain_Type()
)
apSvcRedirectDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcRedirectDomain.setStatus("mandatory")


class _ApSvcAvgLoad_Type(Integer32):
    """Custom type apSvcAvgLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcAvgLoad_Type.__name__ = "Integer32"
_ApSvcAvgLoad_Object = MibTableColumn
apSvcAvgLoad = _ApSvcAvgLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 40),
    _ApSvcAvgLoad_Type()
)
apSvcAvgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcAvgLoad.setStatus("mandatory")


class _ApSvcIPAddressRange_Type(Integer32):
    """Custom type apSvcIPAddressRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcIPAddressRange_Type.__name__ = "Integer32"
_ApSvcIPAddressRange_Object = MibTableColumn
apSvcIPAddressRange = _ApSvcIPAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 41),
    _ApSvcIPAddressRange_Type()
)
apSvcIPAddressRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcIPAddressRange.setStatus("mandatory")


class _ApSvcPortRange_Type(Integer32):
    """Custom type apSvcPortRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcPortRange_Type.__name__ = "Integer32"
_ApSvcPortRange_Object = MibTableColumn
apSvcPortRange = _ApSvcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 42),
    _ApSvcPortRange_Type()
)
apSvcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcPortRange.setStatus("mandatory")


class _ApSvcKALScriptName_Type(SnmpAdminString):
    """Custom type apSvcKALScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALScriptName_Type.__name__ = "SnmpAdminString"
_ApSvcKALScriptName_Object = MibTableColumn
apSvcKALScriptName = _ApSvcKALScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 43),
    _ApSvcKALScriptName_Type()
)
apSvcKALScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALScriptName.setStatus("mandatory")


class _ApSvcKALScriptArgs_Type(SnmpAdminString):
    """Custom type apSvcKALScriptArgs based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApSvcKALScriptArgs_Type.__name__ = "SnmpAdminString"
_ApSvcKALScriptArgs_Object = MibTableColumn
apSvcKALScriptArgs = _ApSvcKALScriptArgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 44),
    _ApSvcKALScriptArgs_Type()
)
apSvcKALScriptArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALScriptArgs.setStatus("mandatory")


class _ApSvcKALScriptLog_Type(SnmpAdminString):
    """Custom type apSvcKALScriptLog based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALScriptLog_Type.__name__ = "SnmpAdminString"
_ApSvcKALScriptLog_Object = MibTableColumn
apSvcKALScriptLog = _ApSvcKALScriptLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 45),
    _ApSvcKALScriptLog_Type()
)
apSvcKALScriptLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALScriptLog.setStatus("mandatory")


class _ApSvcCacheByPass_Type(Integer32):
    """Custom type apSvcCacheByPass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcCacheByPass_Type.__name__ = "Integer32"
_ApSvcCacheByPass_Object = MibTableColumn
apSvcCacheByPass = _ApSvcCacheByPass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 46),
    _ApSvcCacheByPass_Type()
)
apSvcCacheByPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCacheByPass.setStatus("mandatory")


class _ApSvcRedirectString_Type(SnmpAdminString):
    """Custom type apSvcRedirectString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_ApSvcRedirectString_Type.__name__ = "SnmpAdminString"
_ApSvcRedirectString_Object = MibTableColumn
apSvcRedirectString = _ApSvcRedirectString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 47),
    _ApSvcRedirectString_Type()
)
apSvcRedirectString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcRedirectString.setStatus("mandatory")


class _ApSvcKALScriptOutput_Type(Integer32):
    """Custom type apSvcKALScriptOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ApSvcKALScriptOutput_Type.__name__ = "Integer32"
_ApSvcKALScriptOutput_Object = MibTableColumn
apSvcKALScriptOutput = _ApSvcKALScriptOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 48),
    _ApSvcKALScriptOutput_Type()
)
apSvcKALScriptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALScriptOutput.setStatus("mandatory")


class _ApSvcTransparentHosttag_Type(Integer32):
    """Custom type apSvcTransparentHosttag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcTransparentHosttag_Type.__name__ = "Integer32"
_ApSvcTransparentHosttag_Object = MibTableColumn
apSvcTransparentHosttag = _ApSvcTransparentHosttag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 49),
    _ApSvcTransparentHosttag_Type()
)
apSvcTransparentHosttag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcTransparentHosttag.setStatus("mandatory")


class _ApSvcBypassHosttag_Type(Integer32):
    """Custom type apSvcBypassHosttag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcBypassHosttag_Type.__name__ = "Integer32"
_ApSvcBypassHosttag_Object = MibTableColumn
apSvcBypassHosttag = _ApSvcBypassHosttag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 50),
    _ApSvcBypassHosttag_Type()
)
apSvcBypassHosttag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcBypassHosttag.setStatus("mandatory")


class _ApSvcKALState_Type(Integer32):
    """Custom type apSvcKALState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("suspended", 1),
          ("down", 2),
          ("alive", 4),
          ("dying", 5))
    )


_ApSvcKALState_Type.__name__ = "Integer32"
_ApSvcKALState_Object = MibTableColumn
apSvcKALState = _ApSvcKALState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 51),
    _ApSvcKALState_Type()
)
apSvcKALState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcKALState.setStatus("mandatory")


class _ApSvcRedirectPrepend_Type(Integer32):
    """Custom type apSvcRedirectPrepend based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcRedirectPrepend_Type.__name__ = "Integer32"
_ApSvcRedirectPrepend_Object = MibTableColumn
apSvcRedirectPrepend = _ApSvcRedirectPrepend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 52),
    _ApSvcRedirectPrepend_Type()
)
apSvcRedirectPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcRedirectPrepend.setStatus("mandatory")


class _ApSvcSessionRedundantIndex_Type(Integer32):
    """Custom type apSvcSessionRedundantIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ApSvcSessionRedundantIndex_Type.__name__ = "Integer32"
_ApSvcSessionRedundantIndex_Object = MibTableColumn
apSvcSessionRedundantIndex = _ApSvcSessionRedundantIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 53),
    _ApSvcSessionRedundantIndex_Type()
)
apSvcSessionRedundantIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSessionRedundantIndex.setStatus("mandatory")


class _ApSvcSlot_Type(Integer32):
    """Custom type apSvcSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApSvcSlot_Type.__name__ = "Integer32"
_ApSvcSlot_Object = MibTableColumn
apSvcSlot = _ApSvcSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 54),
    _ApSvcSlot_Type()
)
apSvcSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSlot.setStatus("mandatory")


class _ApSvcSubSlot_Type(Integer32):
    """Custom type apSvcSubSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApSvcSubSlot_Type.__name__ = "Integer32"
_ApSvcSubSlot_Object = MibTableColumn
apSvcSubSlot = _ApSvcSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 55),
    _ApSvcSubSlot_Type()
)
apSvcSubSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSubSlot.setStatus("mandatory")


class _ApSvcSslSessCache_Type(Integer32):
    """Custom type apSvcSslSessCache based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApSvcSslSessCache_Type.__name__ = "Integer32"
_ApSvcSslSessCache_Object = MibTableColumn
apSvcSslSessCache = _ApSvcSslSessCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 56),
    _ApSvcSslSessCache_Type()
)
apSvcSslSessCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSslSessCache.setStatus("mandatory")


class _ApSvcDFPState_Type(Integer32):
    """Custom type apSvcDFPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcDFPState_Type.__name__ = "Integer32"
_ApSvcDFPState_Object = MibTableColumn
apSvcDFPState = _ApSvcDFPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 57),
    _ApSvcDFPState_Type()
)
apSvcDFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcDFPState.setStatus("mandatory")


class _ApSvcDFPWeight_Type(Integer32):
    """Custom type apSvcDFPWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApSvcDFPWeight_Type.__name__ = "Integer32"
_ApSvcDFPWeight_Object = MibTableColumn
apSvcDFPWeight = _ApSvcDFPWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 58),
    _ApSvcDFPWeight_Type()
)
apSvcDFPWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcDFPWeight.setStatus("mandatory")


class _ApSvcKALMethodDesiredRsp_Type(Integer32):
    """Custom type apSvcKALMethodDesiredRsp based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_ApSvcKALMethodDesiredRsp_Type.__name__ = "Integer32"
_ApSvcKALMethodDesiredRsp_Object = MibTableColumn
apSvcKALMethodDesiredRsp = _ApSvcKALMethodDesiredRsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 59),
    _ApSvcKALMethodDesiredRsp_Type()
)
apSvcKALMethodDesiredRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALMethodDesiredRsp.setStatus("mandatory")
_ApSvcTotalBackupConnections_Type = Counter32
_ApSvcTotalBackupConnections_Object = MibTableColumn
apSvcTotalBackupConnections = _ApSvcTotalBackupConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 60),
    _ApSvcTotalBackupConnections_Type()
)
apSvcTotalBackupConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcTotalBackupConnections.setStatus("mandatory")
_ApSvcTotalLocalConnections_Type = Counter32
_ApSvcTotalLocalConnections_Object = MibTableColumn
apSvcTotalLocalConnections = _ApSvcTotalLocalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 61),
    _ApSvcTotalLocalConnections_Type()
)
apSvcTotalLocalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcTotalLocalConnections.setStatus("mandatory")


class _ApSvcCurrentBackupConnections_Type(Integer32):
    """Custom type apSvcCurrentBackupConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcCurrentBackupConnections_Type.__name__ = "Integer32"
_ApSvcCurrentBackupConnections_Object = MibTableColumn
apSvcCurrentBackupConnections = _ApSvcCurrentBackupConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 62),
    _ApSvcCurrentBackupConnections_Type()
)
apSvcCurrentBackupConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCurrentBackupConnections.setStatus("mandatory")


class _ApSvcCurrentLocalConnections_Type(Integer32):
    """Custom type apSvcCurrentLocalConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcCurrentLocalConnections_Type.__name__ = "Integer32"
_ApSvcCurrentLocalConnections_Object = MibTableColumn
apSvcCurrentLocalConnections = _ApSvcCurrentLocalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 63),
    _ApSvcCurrentLocalConnections_Type()
)
apSvcCurrentLocalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCurrentLocalConnections.setStatus("mandatory")


class _ApSvcAuthor_Type(SnmpAdminString):
    """Custom type apSvcAuthor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApSvcAuthor_Type.__name__ = "SnmpAdminString"
_ApSvcAuthor_Object = MibTableColumn
apSvcAuthor = _ApSvcAuthor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 64),
    _ApSvcAuthor_Type()
)
apSvcAuthor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcAuthor.setStatus("mandatory")


class _ApSvcAvgResponseTime_Type(Integer32):
    """Custom type apSvcAvgResponseTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcAvgResponseTime_Type.__name__ = "Integer32"
_ApSvcAvgResponseTime_Object = MibTableColumn
apSvcAvgResponseTime = _ApSvcAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 65),
    _ApSvcAvgResponseTime_Type()
)
apSvcAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcAvgResponseTime.setStatus("mandatory")


class _ApSvcPeakAvgResponseTime_Type(Integer32):
    """Custom type apSvcPeakAvgResponseTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSvcPeakAvgResponseTime_Type.__name__ = "Integer32"
_ApSvcPeakAvgResponseTime_Object = MibTableColumn
apSvcPeakAvgResponseTime = _ApSvcPeakAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 66),
    _ApSvcPeakAvgResponseTime_Type()
)
apSvcPeakAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcPeakAvgResponseTime.setStatus("mandatory")


class _ApSvcKALGraceful_Type(Integer32):
    """Custom type apSvcKALGraceful based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApSvcKALGraceful_Type.__name__ = "Integer32"
_ApSvcKALGraceful_Object = MibTableColumn
apSvcKALGraceful = _ApSvcKALGraceful_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 67),
    _ApSvcKALGraceful_Type()
)
apSvcKALGraceful.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALGraceful.setStatus("mandatory")


class _ApSvcLoad_Type(Integer32):
    """Custom type apSvcLoad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ApSvcLoad_Type.__name__ = "Integer32"
_ApSvcLoad_Object = MibTableColumn
apSvcLoad = _ApSvcLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 68),
    _ApSvcLoad_Type()
)
apSvcLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoad.setStatus("mandatory")


class _ApSvcKALEncrypt_Type(Integer32):
    """Custom type apSvcKALEncrypt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ApSvcKALEncrypt_Type.__name__ = "Integer32"
_ApSvcKALEncrypt_Object = MibTableColumn
apSvcKALEncrypt = _ApSvcKALEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 69),
    _ApSvcKALEncrypt_Type()
)
apSvcKALEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcKALEncrypt.setStatus("mandatory")


class _ApSvcCompressionEnable_Type(Integer32):
    """Custom type apSvcCompressionEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ApSvcCompressionEnable_Type.__name__ = "Integer32"
_ApSvcCompressionEnable_Object = MibTableColumn
apSvcCompressionEnable = _ApSvcCompressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 70),
    _ApSvcCompressionEnable_Type()
)
apSvcCompressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompressionEnable.setStatus("mandatory")


class _ApSvcCompressionAcceptOmit_Type(Integer32):
    """Custom type apSvcCompressionAcceptOmit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("identity", 1),
          ("deflate", 2),
          ("gzip", 3))
    )


_ApSvcCompressionAcceptOmit_Type.__name__ = "Integer32"
_ApSvcCompressionAcceptOmit_Object = MibTableColumn
apSvcCompressionAcceptOmit = _ApSvcCompressionAcceptOmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 71),
    _ApSvcCompressionAcceptOmit_Type()
)
apSvcCompressionAcceptOmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompressionAcceptOmit.setStatus("mandatory")


class _ApSvcCompressionEncode_Type(Integer32):
    """Custom type apSvcCompressionEncode based on Integer32"""
    defaultValue = 3

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
        *(("gzip", 1),
          ("deflate", 2),
          ("auto", 3),
          ("force-gzip", 4),
          ("force-deflate", 5))
    )


_ApSvcCompressionEncode_Type.__name__ = "Integer32"
_ApSvcCompressionEncode_Object = MibTableColumn
apSvcCompressionEncode = _ApSvcCompressionEncode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 72),
    _ApSvcCompressionEncode_Type()
)
apSvcCompressionEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompressionEncode.setStatus("mandatory")


class _ApSvcCompressionType_Type(Integer32):
    """Custom type apSvcCompressionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ascii", 2),
          ("numeric", 3))
    )


_ApSvcCompressionType_Type.__name__ = "Integer32"
_ApSvcCompressionType_Object = MibTableColumn
apSvcCompressionType = _ApSvcCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 73),
    _ApSvcCompressionType_Type()
)
apSvcCompressionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompressionType.setStatus("mandatory")


class _ApSvcCompTcpBufRx_Type(Integer32):
    """Custom type apSvcCompTcpBufRx based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16400, 262144),
    )


_ApSvcCompTcpBufRx_Type.__name__ = "Integer32"
_ApSvcCompTcpBufRx_Object = MibTableColumn
apSvcCompTcpBufRx = _ApSvcCompTcpBufRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 74),
    _ApSvcCompTcpBufRx_Type()
)
apSvcCompTcpBufRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompTcpBufRx.setStatus("mandatory")


class _ApSvcCompTcpBufTx_Type(Integer32):
    """Custom type apSvcCompTcpBufTx based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16400, 262144),
    )


_ApSvcCompTcpBufTx_Type.__name__ = "Integer32"
_ApSvcCompTcpBufTx_Object = MibTableColumn
apSvcCompTcpBufTx = _ApSvcCompTcpBufTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 75),
    _ApSvcCompTcpBufTx_Type()
)
apSvcCompTcpBufTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompTcpBufTx.setStatus("mandatory")


class _ApSvcCompVirTcpInactTo_Type(Integer32):
    """Custom type apSvcCompVirTcpInactTo based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcCompVirTcpInactTo_Type.__name__ = "Integer32"
_ApSvcCompVirTcpInactTo_Object = MibTableColumn
apSvcCompVirTcpInactTo = _ApSvcCompVirTcpInactTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 76),
    _ApSvcCompVirTcpInactTo_Type()
)
apSvcCompVirTcpInactTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpInactTo.setStatus("mandatory")


class _ApSvcCompVirTcpSynTo_Type(Integer32):
    """Custom type apSvcCompVirTcpSynTo based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ApSvcCompVirTcpSynTo_Type.__name__ = "Integer32"
_ApSvcCompVirTcpSynTo_Object = MibTableColumn
apSvcCompVirTcpSynTo = _ApSvcCompVirTcpSynTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 77),
    _ApSvcCompVirTcpSynTo_Type()
)
apSvcCompVirTcpSynTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpSynTo.setStatus("mandatory")


class _ApSvcCompVirTcpFinTo_Type(Integer32):
    """Custom type apSvcCompVirTcpFinTo based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcCompVirTcpFinTo_Type.__name__ = "Integer32"
_ApSvcCompVirTcpFinTo_Object = MibTableColumn
apSvcCompVirTcpFinTo = _ApSvcCompVirTcpFinTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 78),
    _ApSvcCompVirTcpFinTo_Type()
)
apSvcCompVirTcpFinTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpFinTo.setStatus("mandatory")


class _ApSvcCompVirTcpNagleState_Type(Integer32):
    """Custom type apSvcCompVirTcpNagleState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcCompVirTcpNagleState_Type.__name__ = "Integer32"
_ApSvcCompVirTcpNagleState_Object = MibTableColumn
apSvcCompVirTcpNagleState = _ApSvcCompVirTcpNagleState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 79),
    _ApSvcCompVirTcpNagleState_Type()
)
apSvcCompVirTcpNagleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpNagleState.setStatus("mandatory")


class _ApSvcCompVirTcpMinRetrans_Type(Integer32):
    """Custom type apSvcCompVirTcpMinRetrans based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ApSvcCompVirTcpMinRetrans_Type.__name__ = "Integer32"
_ApSvcCompVirTcpMinRetrans_Object = MibTableColumn
apSvcCompVirTcpMinRetrans = _ApSvcCompVirTcpMinRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 80),
    _ApSvcCompVirTcpMinRetrans_Type()
)
apSvcCompVirTcpMinRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpMinRetrans.setStatus("mandatory")


class _ApSvcCompVirTcpAckDelay_Type(Integer32):
    """Custom type apSvcCompVirTcpAckDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ApSvcCompVirTcpAckDelay_Type.__name__ = "Integer32"
_ApSvcCompVirTcpAckDelay_Object = MibTableColumn
apSvcCompVirTcpAckDelay = _ApSvcCompVirTcpAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 81),
    _ApSvcCompVirTcpAckDelay_Type()
)
apSvcCompVirTcpAckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompVirTcpAckDelay.setStatus("mandatory")


class _ApSvcCompSvrTcpInactTo_Type(Integer32):
    """Custom type apSvcCompSvrTcpInactTo based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcCompSvrTcpInactTo_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpInactTo_Object = MibTableColumn
apSvcCompSvrTcpInactTo = _ApSvcCompSvrTcpInactTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 82),
    _ApSvcCompSvrTcpInactTo_Type()
)
apSvcCompSvrTcpInactTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpInactTo.setStatus("mandatory")


class _ApSvcCompSvrTcpSynTo_Type(Integer32):
    """Custom type apSvcCompSvrTcpSynTo based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ApSvcCompSvrTcpSynTo_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpSynTo_Object = MibTableColumn
apSvcCompSvrTcpSynTo = _ApSvcCompSvrTcpSynTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 83),
    _ApSvcCompSvrTcpSynTo_Type()
)
apSvcCompSvrTcpSynTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpSynTo.setStatus("mandatory")


class _ApSvcCompSvrTcpFinTo_Type(Integer32):
    """Custom type apSvcCompSvrTcpFinTo based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcCompSvrTcpFinTo_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpFinTo_Object = MibTableColumn
apSvcCompSvrTcpFinTo = _ApSvcCompSvrTcpFinTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 84),
    _ApSvcCompSvrTcpFinTo_Type()
)
apSvcCompSvrTcpFinTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpFinTo.setStatus("mandatory")


class _ApSvcCompSvrTcpNagleState_Type(Integer32):
    """Custom type apSvcCompSvrTcpNagleState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcCompSvrTcpNagleState_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpNagleState_Object = MibTableColumn
apSvcCompSvrTcpNagleState = _ApSvcCompSvrTcpNagleState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 85),
    _ApSvcCompSvrTcpNagleState_Type()
)
apSvcCompSvrTcpNagleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpNagleState.setStatus("mandatory")


class _ApSvcCompSvrTcpAckDelay_Type(Integer32):
    """Custom type apSvcCompSvrTcpAckDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ApSvcCompSvrTcpAckDelay_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpAckDelay_Object = MibTableColumn
apSvcCompSvrTcpAckDelay = _ApSvcCompSvrTcpAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 86),
    _ApSvcCompSvrTcpAckDelay_Type()
)
apSvcCompSvrTcpAckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpAckDelay.setStatus("mandatory")


class _ApSvcCompSvrTcpMinRetrans_Type(Integer32):
    """Custom type apSvcCompSvrTcpMinRetrans based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ApSvcCompSvrTcpMinRetrans_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpMinRetrans_Object = MibTableColumn
apSvcCompSvrTcpMinRetrans = _ApSvcCompSvrTcpMinRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 87),
    _ApSvcCompSvrTcpMinRetrans_Type()
)
apSvcCompSvrTcpMinRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpMinRetrans.setStatus("mandatory")


class _ApSvcCompSvrTcpCompQueueDelay_Type(Integer32):
    """Custom type apSvcCompSvrTcpCompQueueDelay based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_ApSvcCompSvrTcpCompQueueDelay_Type.__name__ = "Integer32"
_ApSvcCompSvrTcpCompQueueDelay_Object = MibTableColumn
apSvcCompSvrTcpCompQueueDelay = _ApSvcCompSvrTcpCompQueueDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 2, 1, 88),
    _ApSvcCompSvrTcpCompQueueDelay_Type()
)
apSvcCompSvrTcpCompQueueDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcCompSvrTcpCompQueueDelay.setStatus("mandatory")


class _ApSvcLoadThreshold_Type(Integer32):
    """Custom type apSvcLoadThreshold based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_ApSvcLoadThreshold_Type.__name__ = "Integer32"
_ApSvcLoadThreshold_Object = MibScalar
apSvcLoadThreshold = _ApSvcLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 3),
    _ApSvcLoadThreshold_Type()
)
apSvcLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadThreshold.setStatus("mandatory")


class _ApSvcLoadStepSize_Type(Integer32):
    """Custom type apSvcLoadStepSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ApSvcLoadStepSize_Type.__name__ = "Integer32"
_ApSvcLoadStepSize_Object = MibScalar
apSvcLoadStepSize = _ApSvcLoadStepSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 4),
    _ApSvcLoadStepSize_Type()
)
apSvcLoadStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadStepSize.setStatus("mandatory")


class _ApSvcLoadStepStatic_Type(Integer32):
    """Custom type apSvcLoadStepStatic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcLoadStepStatic_Type.__name__ = "Integer32"
_ApSvcLoadStepStatic_Object = MibScalar
apSvcLoadStepStatic = _ApSvcLoadStepStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 5),
    _ApSvcLoadStepStatic_Type()
)
apSvcLoadStepStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadStepStatic.setStatus("mandatory")


class _ApSvcLoadDecayInterval_Type(Integer32):
    """Custom type apSvcLoadDecayInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ApSvcLoadDecayInterval_Type.__name__ = "Integer32"
_ApSvcLoadDecayInterval_Object = MibScalar
apSvcLoadDecayInterval = _ApSvcLoadDecayInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 6),
    _ApSvcLoadDecayInterval_Type()
)
apSvcLoadDecayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadDecayInterval.setStatus("mandatory")


class _ApSvcLoadEnable_Type(Integer32):
    """Custom type apSvcLoadEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcLoadEnable_Type.__name__ = "Integer32"
_ApSvcLoadEnable_Object = MibScalar
apSvcLoadEnable = _ApSvcLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 7),
    _ApSvcLoadEnable_Type()
)
apSvcLoadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadEnable.setStatus("mandatory")


class _ApSvcLoadSvcStatRptTimeout_Type(Integer32):
    """Custom type apSvcLoadSvcStatRptTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_ApSvcLoadSvcStatRptTimeout_Type.__name__ = "Integer32"
_ApSvcLoadSvcStatRptTimeout_Object = MibScalar
apSvcLoadSvcStatRptTimeout = _ApSvcLoadSvcStatRptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 8),
    _ApSvcLoadSvcStatRptTimeout_Type()
)
apSvcLoadSvcStatRptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadSvcStatRptTimeout.setStatus("mandatory")


class _ApSvcLoadInfoTimeout_Type(Integer32):
    """Custom type apSvcLoadInfoTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_ApSvcLoadInfoTimeout_Type.__name__ = "Integer32"
_ApSvcLoadInfoTimeout_Object = MibScalar
apSvcLoadInfoTimeout = _ApSvcLoadInfoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 9),
    _ApSvcLoadInfoTimeout_Type()
)
apSvcLoadInfoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadInfoTimeout.setStatus("mandatory")


class _ApSvcTrapEventText_Type(SnmpAdminString):
    """Custom type apSvcTrapEventText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSvcTrapEventText_Type.__name__ = "SnmpAdminString"
_ApSvcTrapEventText_Object = MibScalar
apSvcTrapEventText = _ApSvcTrapEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 10),
    _ApSvcTrapEventText_Type()
)
apSvcTrapEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcTrapEventText.setStatus("mandatory")
_ApSvcSsllTable_Object = MibTable
apSvcSsllTable = _ApSvcSsllTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 11)
)
if mibBuilder.loadTexts:
    apSvcSsllTable.setStatus("mandatory")
_ApSvcSsllEntry_Object = MibTableRow
apSvcSsllEntry = _ApSvcSsllEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 11, 1)
)
apSvcSsllEntry.setIndexNames(
    (0, "ARROWPOINT-SVCEXT-MIB", "apSvcName"),
    (0, "ARROWPOINT-SVCEXT-MIB", "apSvcSsllName"),
)
if mibBuilder.loadTexts:
    apSvcSsllEntry.setStatus("mandatory")


class _ApSvcSsllName_Type(SnmpAdminString):
    """Custom type apSvcSsllName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApSvcSsllName_Type.__name__ = "SnmpAdminString"
_ApSvcSsllName_Object = MibTableColumn
apSvcSsllName = _ApSvcSsllName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 11, 1, 1),
    _ApSvcSsllName_Type()
)
apSvcSsllName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSsllName.setStatus("mandatory")
_ApSvcSsllStatus_Type = RowStatus
_ApSvcSsllStatus_Object = MibTableColumn
apSvcSsllStatus = _ApSvcSsllStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 11, 1, 2),
    _ApSvcSsllStatus_Type()
)
apSvcSsllStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcSsllStatus.setStatus("mandatory")


class _ApSvcLoadCalcMethod_Type(Integer32):
    """Custom type apSvcLoadCalcMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("relative", 0),
          ("absolute", 1))
    )


_ApSvcLoadCalcMethod_Type.__name__ = "Integer32"
_ApSvcLoadCalcMethod_Object = MibScalar
apSvcLoadCalcMethod = _ApSvcLoadCalcMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 12),
    _ApSvcLoadCalcMethod_Type()
)
apSvcLoadCalcMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadCalcMethod.setStatus("mandatory")


class _ApSvcLoadAbsoluteSensitivity_Type(Integer32):
    """Custom type apSvcLoadAbsoluteSensitivity based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_ApSvcLoadAbsoluteSensitivity_Type.__name__ = "Integer32"
_ApSvcLoadAbsoluteSensitivity_Object = MibScalar
apSvcLoadAbsoluteSensitivity = _ApSvcLoadAbsoluteSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 13),
    _ApSvcLoadAbsoluteSensitivity_Type()
)
apSvcLoadAbsoluteSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadAbsoluteSensitivity.setStatus("mandatory")


class _ApSvcReplicationFileError_Type(Integer32):
    """Custom type apSvcReplicationFileError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("retry", 0),
          ("skip", 1))
    )


_ApSvcReplicationFileError_Type.__name__ = "Integer32"
_ApSvcReplicationFileError_Object = MibScalar
apSvcReplicationFileError = _ApSvcReplicationFileError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 14),
    _ApSvcReplicationFileError_Type()
)
apSvcReplicationFileError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcReplicationFileError.setStatus("mandatory")
_ApSvcCompStatTable_Object = MibTable
apSvcCompStatTable = _ApSvcCompStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15)
)
if mibBuilder.loadTexts:
    apSvcCompStatTable.setStatus("mandatory")
_ApSvcCompStatEntry_Object = MibTableRow
apSvcCompStatEntry = _ApSvcCompStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1)
)
apSvcCompStatEntry.setIndexNames(
    (0, "ARROWPOINT-SVCEXT-MIB", "apSvcName"),
)
if mibBuilder.loadTexts:
    apSvcCompStatEntry.setStatus("mandatory")
_ApSvcCompStatunCmpBytesIn_Type = Counter64
_ApSvcCompStatunCmpBytesIn_Object = MibTableColumn
apSvcCompStatunCmpBytesIn = _ApSvcCompStatunCmpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 1),
    _ApSvcCompStatunCmpBytesIn_Type()
)
apSvcCompStatunCmpBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatunCmpBytesIn.setStatus("mandatory")
_ApSvcCompStatcmpBytesOut_Type = Counter64
_ApSvcCompStatcmpBytesOut_Object = MibTableColumn
apSvcCompStatcmpBytesOut = _ApSvcCompStatcmpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 2),
    _ApSvcCompStatcmpBytesOut_Type()
)
apSvcCompStatcmpBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatcmpBytesOut.setStatus("mandatory")
_ApSvcCompStatflowBypassedBytesOut_Type = Counter64
_ApSvcCompStatflowBypassedBytesOut_Object = MibTableColumn
apSvcCompStatflowBypassedBytesOut = _ApSvcCompStatflowBypassedBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 3),
    _ApSvcCompStatflowBypassedBytesOut_Type()
)
apSvcCompStatflowBypassedBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatflowBypassedBytesOut.setStatus("mandatory")
_ApSvcCompStatunCmpFilesIn_Type = Counter32
_ApSvcCompStatunCmpFilesIn_Object = MibTableColumn
apSvcCompStatunCmpFilesIn = _ApSvcCompStatunCmpFilesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 4),
    _ApSvcCompStatunCmpFilesIn_Type()
)
apSvcCompStatunCmpFilesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatunCmpFilesIn.setStatus("mandatory")
_ApSvcCompStatcmpFilesOut_Type = Counter32
_ApSvcCompStatcmpFilesOut_Object = MibTableColumn
apSvcCompStatcmpFilesOut = _ApSvcCompStatcmpFilesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 5),
    _ApSvcCompStatcmpFilesOut_Type()
)
apSvcCompStatcmpFilesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatcmpFilesOut.setStatus("mandatory")
_ApSvcCompStatflowBypassedFilesOut_Type = Counter32
_ApSvcCompStatflowBypassedFilesOut_Object = MibTableColumn
apSvcCompStatflowBypassedFilesOut = _ApSvcCompStatflowBypassedFilesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 6),
    _ApSvcCompStatflowBypassedFilesOut_Type()
)
apSvcCompStatflowBypassedFilesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatflowBypassedFilesOut.setStatus("mandatory")
_ApSvcCompStatcmpRatio_Type = Counter32
_ApSvcCompStatcmpRatio_Object = MibTableColumn
apSvcCompStatcmpRatio = _ApSvcCompStatcmpRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 7),
    _ApSvcCompStatcmpRatio_Type()
)
apSvcCompStatcmpRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatcmpRatio.setStatus("mandatory")
_ApSvcCompStatRstMethod_Type = Counter32
_ApSvcCompStatRstMethod_Object = MibTableColumn
apSvcCompStatRstMethod = _ApSvcCompStatRstMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 8),
    _ApSvcCompStatRstMethod_Type()
)
apSvcCompStatRstMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatRstMethod.setStatus("mandatory")
_ApSvcCompStatRstPipeline_Type = Counter32
_ApSvcCompStatRstPipeline_Object = MibTableColumn
apSvcCompStatRstPipeline = _ApSvcCompStatRstPipeline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 9),
    _ApSvcCompStatRstPipeline_Type()
)
apSvcCompStatRstPipeline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatRstPipeline.setStatus("mandatory")
_ApSvcCompStatRstClientTag_Type = Counter32
_ApSvcCompStatRstClientTag_Object = MibTableColumn
apSvcCompStatRstClientTag = _ApSvcCompStatRstClientTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 10),
    _ApSvcCompStatRstClientTag_Type()
)
apSvcCompStatRstClientTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatRstClientTag.setStatus("mandatory")
_ApSvcCompStatRstServerTag_Type = Counter32
_ApSvcCompStatRstServerTag_Object = MibTableColumn
apSvcCompStatRstServerTag = _ApSvcCompStatRstServerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 11),
    _ApSvcCompStatRstServerTag_Type()
)
apSvcCompStatRstServerTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatRstServerTag.setStatus("mandatory")
_ApSvcCompStatRstOther_Type = Counter32
_ApSvcCompStatRstOther_Object = MibTableColumn
apSvcCompStatRstOther = _ApSvcCompStatRstOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 12),
    _ApSvcCompStatRstOther_Type()
)
apSvcCompStatRstOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatRstOther.setStatus("mandatory")
_ApSvcCompStatBypCliTotal_Type = Counter32
_ApSvcCompStatBypCliTotal_Object = MibTableColumn
apSvcCompStatBypCliTotal = _ApSvcCompStatBypCliTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 13),
    _ApSvcCompStatBypCliTotal_Type()
)
apSvcCompStatBypCliTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypCliTotal.setStatus("mandatory")
_ApSvcCompStatBypCliMethod_Type = Counter32
_ApSvcCompStatBypCliMethod_Object = MibTableColumn
apSvcCompStatBypCliMethod = _ApSvcCompStatBypCliMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 14),
    _ApSvcCompStatBypCliMethod_Type()
)
apSvcCompStatBypCliMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypCliMethod.setStatus("mandatory")
_ApSvcCompStatBypCliVersion_Type = Counter32
_ApSvcCompStatBypCliVersion_Object = MibTableColumn
apSvcCompStatBypCliVersion = _ApSvcCompStatBypCliVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 15),
    _ApSvcCompStatBypCliVersion_Type()
)
apSvcCompStatBypCliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypCliVersion.setStatus("mandatory")
_ApSvcCompStatBypCliAccept_Type = Counter32
_ApSvcCompStatBypCliAccept_Object = MibTableColumn
apSvcCompStatBypCliAccept = _ApSvcCompStatBypCliAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 16),
    _ApSvcCompStatBypCliAccept_Type()
)
apSvcCompStatBypCliAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypCliAccept.setStatus("mandatory")
_ApSvcCompStatBypCliFileExt_Type = Counter32
_ApSvcCompStatBypCliFileExt_Object = MibTableColumn
apSvcCompStatBypCliFileExt = _ApSvcCompStatBypCliFileExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 17),
    _ApSvcCompStatBypCliFileExt_Type()
)
apSvcCompStatBypCliFileExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypCliFileExt.setStatus("mandatory")
_ApSvcCompStatBypSvrTotal_Type = Counter32
_ApSvcCompStatBypSvrTotal_Object = MibTableColumn
apSvcCompStatBypSvrTotal = _ApSvcCompStatBypSvrTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 18),
    _ApSvcCompStatBypSvrTotal_Type()
)
apSvcCompStatBypSvrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrTotal.setStatus("mandatory")
_ApSvcCompStatBypSvrStatus_Type = Counter32
_ApSvcCompStatBypSvrStatus_Object = MibTableColumn
apSvcCompStatBypSvrStatus = _ApSvcCompStatBypSvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 19),
    _ApSvcCompStatBypSvrStatus_Type()
)
apSvcCompStatBypSvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrStatus.setStatus("mandatory")
_ApSvcCompStatBypSvrVersion_Type = Counter32
_ApSvcCompStatBypSvrVersion_Object = MibTableColumn
apSvcCompStatBypSvrVersion = _ApSvcCompStatBypSvrVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 20),
    _ApSvcCompStatBypSvrVersion_Type()
)
apSvcCompStatBypSvrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrVersion.setStatus("mandatory")
_ApSvcCompStatBypSvrEncoded_Type = Counter32
_ApSvcCompStatBypSvrEncoded_Object = MibTableColumn
apSvcCompStatBypSvrEncoded = _ApSvcCompStatBypSvrEncoded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 21),
    _ApSvcCompStatBypSvrEncoded_Type()
)
apSvcCompStatBypSvrEncoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrEncoded.setStatus("mandatory")
_ApSvcCompStatBypSvrSize_Type = Counter32
_ApSvcCompStatBypSvrSize_Object = MibTableColumn
apSvcCompStatBypSvrSize = _ApSvcCompStatBypSvrSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 22),
    _ApSvcCompStatBypSvrSize_Type()
)
apSvcCompStatBypSvrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrSize.setStatus("mandatory")
_ApSvcCompStatBypSvrCntType_Type = Counter32
_ApSvcCompStatBypSvrCntType_Object = MibTableColumn
apSvcCompStatBypSvrCntType = _ApSvcCompStatBypSvrCntType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 15, 1, 23),
    _ApSvcCompStatBypSvrCntType_Type()
)
apSvcCompStatBypSvrCntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcCompStatBypSvrCntType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

apSvcTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 15, 1, 0, 1)
)
apSvcTransitionTrap.setObjects(
    ("ARROWPOINT-SVCEXT-MIB", "apSvcTrapEventText")
)
if mibBuilder.loadTexts:
    apSvcTransitionTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARROWPOINT-SVCEXT-MIB",
    **{"apSvcExtMib": apSvcExtMib,
       "apSvcExtMibNotifs": apSvcExtMibNotifs,
       "apSvcTransitionTrap": apSvcTransitionTrap,
       "apSvcExtMibObjects": apSvcExtMibObjects,
       "apSvcExtMibConform": apSvcExtMibConform,
       "apSvcExtMibCompliances": apSvcExtMibCompliances,
       "apSvcExtMibCompliance": apSvcExtMibCompliance,
       "apSvcExtMibGroups": apSvcExtMibGroups,
       "apSvcExtMibGroup": apSvcExtMibGroup,
       "apSvcExtMibNotif": apSvcExtMibNotif,
       "apSvcTable": apSvcTable,
       "apSvcEntry": apSvcEntry,
       "apSvcName": apSvcName,
       "apSvcIndex": apSvcIndex,
       "apSvcIPAddress": apSvcIPAddress,
       "apSvcIPProtocol": apSvcIPProtocol,
       "apSvcPort": apSvcPort,
       "apSvcKALType": apSvcKALType,
       "apSvcKALFrequency": apSvcKALFrequency,
       "apSvcKALMaxFailure": apSvcKALMaxFailure,
       "apSvcKALRetryPeriod": apSvcKALRetryPeriod,
       "apSvcKALUri": apSvcKALUri,
       "apSvcKALMethod": apSvcKALMethod,
       "apSvcEnable": apSvcEnable,
       "apSvcType": apSvcType,
       "apSvcQOSMinRate": apSvcQOSMinRate,
       "apSvcQOSMinBW": apSvcQOSMinBW,
       "apSvcWeight": apSvcWeight,
       "apSvcState": apSvcState,
       "apSvcShortLoad": apSvcShortLoad,
       "apSvcMaxConnections": apSvcMaxConnections,
       "apSvcConnections": apSvcConnections,
       "apSvcTransitions": apSvcTransitions,
       "apSvcMaxContent": apSvcMaxContent,
       "apSvcMaxUsage": apSvcMaxUsage,
       "apSvcMaxAge": apSvcMaxAge,
       "apSvcAccessRecordName": apSvcAccessRecordName,
       "apSvcStatus": apSvcStatus,
       "apSvcCookie": apSvcCookie,
       "apSvcKALPersistence": apSvcKALPersistence,
       "apSvcKALName": apSvcKALName,
       "apSvcLongLoad": apSvcLongLoad,
       "apSvcKALPort": apSvcKALPort,
       "apSvcPublishName": apSvcPublishName,
       "apSvcPublishState": apSvcPublishState,
       "apSvcPublishInterval": apSvcPublishInterval,
       "apSvcAccessType": apSvcAccessType,
       "apSvcKALHash": apSvcKALHash,
       "apSvcKALFTPRecord": apSvcKALFTPRecord,
       "apSvcPublishFile": apSvcPublishFile,
       "apSvcRedirectDomain": apSvcRedirectDomain,
       "apSvcAvgLoad": apSvcAvgLoad,
       "apSvcIPAddressRange": apSvcIPAddressRange,
       "apSvcPortRange": apSvcPortRange,
       "apSvcKALScriptName": apSvcKALScriptName,
       "apSvcKALScriptArgs": apSvcKALScriptArgs,
       "apSvcKALScriptLog": apSvcKALScriptLog,
       "apSvcCacheByPass": apSvcCacheByPass,
       "apSvcRedirectString": apSvcRedirectString,
       "apSvcKALScriptOutput": apSvcKALScriptOutput,
       "apSvcTransparentHosttag": apSvcTransparentHosttag,
       "apSvcBypassHosttag": apSvcBypassHosttag,
       "apSvcKALState": apSvcKALState,
       "apSvcRedirectPrepend": apSvcRedirectPrepend,
       "apSvcSessionRedundantIndex": apSvcSessionRedundantIndex,
       "apSvcSlot": apSvcSlot,
       "apSvcSubSlot": apSvcSubSlot,
       "apSvcSslSessCache": apSvcSslSessCache,
       "apSvcDFPState": apSvcDFPState,
       "apSvcDFPWeight": apSvcDFPWeight,
       "apSvcKALMethodDesiredRsp": apSvcKALMethodDesiredRsp,
       "apSvcTotalBackupConnections": apSvcTotalBackupConnections,
       "apSvcTotalLocalConnections": apSvcTotalLocalConnections,
       "apSvcCurrentBackupConnections": apSvcCurrentBackupConnections,
       "apSvcCurrentLocalConnections": apSvcCurrentLocalConnections,
       "apSvcAuthor": apSvcAuthor,
       "apSvcAvgResponseTime": apSvcAvgResponseTime,
       "apSvcPeakAvgResponseTime": apSvcPeakAvgResponseTime,
       "apSvcKALGraceful": apSvcKALGraceful,
       "apSvcLoad": apSvcLoad,
       "apSvcKALEncrypt": apSvcKALEncrypt,
       "apSvcCompressionEnable": apSvcCompressionEnable,
       "apSvcCompressionAcceptOmit": apSvcCompressionAcceptOmit,
       "apSvcCompressionEncode": apSvcCompressionEncode,
       "apSvcCompressionType": apSvcCompressionType,
       "apSvcCompTcpBufRx": apSvcCompTcpBufRx,
       "apSvcCompTcpBufTx": apSvcCompTcpBufTx,
       "apSvcCompVirTcpInactTo": apSvcCompVirTcpInactTo,
       "apSvcCompVirTcpSynTo": apSvcCompVirTcpSynTo,
       "apSvcCompVirTcpFinTo": apSvcCompVirTcpFinTo,
       "apSvcCompVirTcpNagleState": apSvcCompVirTcpNagleState,
       "apSvcCompVirTcpMinRetrans": apSvcCompVirTcpMinRetrans,
       "apSvcCompVirTcpAckDelay": apSvcCompVirTcpAckDelay,
       "apSvcCompSvrTcpInactTo": apSvcCompSvrTcpInactTo,
       "apSvcCompSvrTcpSynTo": apSvcCompSvrTcpSynTo,
       "apSvcCompSvrTcpFinTo": apSvcCompSvrTcpFinTo,
       "apSvcCompSvrTcpNagleState": apSvcCompSvrTcpNagleState,
       "apSvcCompSvrTcpAckDelay": apSvcCompSvrTcpAckDelay,
       "apSvcCompSvrTcpMinRetrans": apSvcCompSvrTcpMinRetrans,
       "apSvcCompSvrTcpCompQueueDelay": apSvcCompSvrTcpCompQueueDelay,
       "apSvcLoadThreshold": apSvcLoadThreshold,
       "apSvcLoadStepSize": apSvcLoadStepSize,
       "apSvcLoadStepStatic": apSvcLoadStepStatic,
       "apSvcLoadDecayInterval": apSvcLoadDecayInterval,
       "apSvcLoadEnable": apSvcLoadEnable,
       "apSvcLoadSvcStatRptTimeout": apSvcLoadSvcStatRptTimeout,
       "apSvcLoadInfoTimeout": apSvcLoadInfoTimeout,
       "apSvcTrapEventText": apSvcTrapEventText,
       "apSvcSsllTable": apSvcSsllTable,
       "apSvcSsllEntry": apSvcSsllEntry,
       "apSvcSsllName": apSvcSsllName,
       "apSvcSsllStatus": apSvcSsllStatus,
       "apSvcLoadCalcMethod": apSvcLoadCalcMethod,
       "apSvcLoadAbsoluteSensitivity": apSvcLoadAbsoluteSensitivity,
       "apSvcReplicationFileError": apSvcReplicationFileError,
       "apSvcCompStatTable": apSvcCompStatTable,
       "apSvcCompStatEntry": apSvcCompStatEntry,
       "apSvcCompStatunCmpBytesIn": apSvcCompStatunCmpBytesIn,
       "apSvcCompStatcmpBytesOut": apSvcCompStatcmpBytesOut,
       "apSvcCompStatflowBypassedBytesOut": apSvcCompStatflowBypassedBytesOut,
       "apSvcCompStatunCmpFilesIn": apSvcCompStatunCmpFilesIn,
       "apSvcCompStatcmpFilesOut": apSvcCompStatcmpFilesOut,
       "apSvcCompStatflowBypassedFilesOut": apSvcCompStatflowBypassedFilesOut,
       "apSvcCompStatcmpRatio": apSvcCompStatcmpRatio,
       "apSvcCompStatRstMethod": apSvcCompStatRstMethod,
       "apSvcCompStatRstPipeline": apSvcCompStatRstPipeline,
       "apSvcCompStatRstClientTag": apSvcCompStatRstClientTag,
       "apSvcCompStatRstServerTag": apSvcCompStatRstServerTag,
       "apSvcCompStatRstOther": apSvcCompStatRstOther,
       "apSvcCompStatBypCliTotal": apSvcCompStatBypCliTotal,
       "apSvcCompStatBypCliMethod": apSvcCompStatBypCliMethod,
       "apSvcCompStatBypCliVersion": apSvcCompStatBypCliVersion,
       "apSvcCompStatBypCliAccept": apSvcCompStatBypCliAccept,
       "apSvcCompStatBypCliFileExt": apSvcCompStatBypCliFileExt,
       "apSvcCompStatBypSvrTotal": apSvcCompStatBypSvrTotal,
       "apSvcCompStatBypSvrStatus": apSvcCompStatBypSvrStatus,
       "apSvcCompStatBypSvrVersion": apSvcCompStatBypSvrVersion,
       "apSvcCompStatBypSvrEncoded": apSvcCompStatBypSvrEncoded,
       "apSvcCompStatBypSvrSize": apSvcCompStatBypSvrSize,
       "apSvcCompStatBypSvrCntType": apSvcCompStatBypSvrCntType}
)
