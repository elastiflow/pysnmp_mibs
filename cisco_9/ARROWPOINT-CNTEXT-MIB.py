# SNMP MIB module (ARROWPOINT-CNTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ARROWPOINT-CNTEXT-MIB.mib
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

(cntExt,) = mibBuilder.importSymbols(
    "CISCO-APENT-MIB",
    "cntExt")

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

_ApCntExtMib_ObjectIdentity = ObjectIdentity
apCntExtMib = _ApCntExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1)
)
_ApCntExtMibNotifs_ObjectIdentity = ObjectIdentity
apCntExtMibNotifs = _ApCntExtMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 0)
)
_ApCntExtMibObjects_ObjectIdentity = ObjectIdentity
apCntExtMibObjects = _ApCntExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 1)
)
_ApCntExtMibConform_ObjectIdentity = ObjectIdentity
apCntExtMibConform = _ApCntExtMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2)
)
_ApCntExtMibCompliances_ObjectIdentity = ObjectIdentity
apCntExtMibCompliances = _ApCntExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2, 1)
)
_ApCntExtMibCompliance_ObjectIdentity = ObjectIdentity
apCntExtMibCompliance = _ApCntExtMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2, 1, 1)
)
_ApCntExtMibGroups_ObjectIdentity = ObjectIdentity
apCntExtMibGroups = _ApCntExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2, 2)
)
_ApCntExtMibGroup_ObjectIdentity = ObjectIdentity
apCntExtMibGroup = _ApCntExtMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2, 2, 1)
)
_ApCntExtOptionalMibGroup_ObjectIdentity = ObjectIdentity
apCntExtOptionalMibGroup = _ApCntExtOptionalMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 1, 2, 2, 2)
)


class _ApCntRuleOrder_Type(Integer32):
    """Custom type apCntRuleOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hierarchicalFirst", 0),
          ("cacheRuleFirst", 1))
    )


_ApCntRuleOrder_Type.__name__ = "Integer32"
_ApCntRuleOrder_Object = MibScalar
apCntRuleOrder = _ApCntRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 2),
    _ApCntRuleOrder_Type()
)
apCntRuleOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntRuleOrder.setStatus("mandatory")
_ApCntTable_Object = MibTable
apCntTable = _ApCntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4)
)
if mibBuilder.loadTexts:
    apCntTable.setStatus("mandatory")
_ApCntEntry_Object = MibTableRow
apCntEntry = _ApCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1)
)
apCntEntry.setIndexNames(
    (0, "ARROWPOINT-CNTEXT-MIB", "apCntOwner"),
    (0, "ARROWPOINT-CNTEXT-MIB", "apCntName"),
)
if mibBuilder.loadTexts:
    apCntEntry.setStatus("mandatory")


class _ApCntOwner_Type(SnmpAdminString):
    """Custom type apCntOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntOwner_Type.__name__ = "SnmpAdminString"
_ApCntOwner_Object = MibTableColumn
apCntOwner = _ApCntOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 1),
    _ApCntOwner_Type()
)
apCntOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntOwner.setStatus("mandatory")


class _ApCntName_Type(SnmpAdminString):
    """Custom type apCntName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntName_Type.__name__ = "SnmpAdminString"
_ApCntName_Object = MibTableColumn
apCntName = _ApCntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 2),
    _ApCntName_Type()
)
apCntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntName.setStatus("mandatory")


class _ApCntIndex_Type(Integer32):
    """Custom type apCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ApCntIndex_Type.__name__ = "Integer32"
_ApCntIndex_Object = MibTableColumn
apCntIndex = _ApCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 3),
    _ApCntIndex_Type()
)
apCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntIndex.setStatus("mandatory")
_ApCntIPAddress_Type = IpAddress
_ApCntIPAddress_Object = MibTableColumn
apCntIPAddress = _ApCntIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 4),
    _ApCntIPAddress_Type()
)
apCntIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntIPAddress.setStatus("mandatory")


class _ApCntIPProtocol_Type(Integer32):
    """Custom type apCntIPProtocol based on Integer32"""
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


_ApCntIPProtocol_Type.__name__ = "Integer32"
_ApCntIPProtocol_Object = MibTableColumn
apCntIPProtocol = _ApCntIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 5),
    _ApCntIPProtocol_Type()
)
apCntIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntIPProtocol.setStatus("mandatory")


class _ApCntPort_Type(Integer32):
    """Custom type apCntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntPort_Type.__name__ = "Integer32"
_ApCntPort_Object = MibTableColumn
apCntPort = _ApCntPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 6),
    _ApCntPort_Type()
)
apCntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntPort.setStatus("mandatory")


class _ApCntUrl_Type(SnmpAdminString):
    """Custom type apCntUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_ApCntUrl_Type.__name__ = "SnmpAdminString"
_ApCntUrl_Object = MibTableColumn
apCntUrl = _ApCntUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 7),
    _ApCntUrl_Type()
)
apCntUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntUrl.setStatus("mandatory")


class _ApCntSticky_Type(Integer32):
    """Custom type apCntSticky based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ssl", 2),
          ("cookieurl", 3),
          ("url", 4),
          ("cookies", 5),
          ("sticky-srcip-dstport", 6),
          ("sticky-srcip", 7),
          ("arrowpoint-cookie", 8),
          ("wap-msisdn", 9),
          ("sip-call-id", 10))
    )


_ApCntSticky_Type.__name__ = "Integer32"
_ApCntSticky_Object = MibTableColumn
apCntSticky = _ApCntSticky_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 8),
    _ApCntSticky_Type()
)
apCntSticky.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSticky.setStatus("mandatory")


class _ApCntBalance_Type(Integer32):
    """Custom type apCntBalance based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 1),
          ("aca", 2),
          ("destip", 3),
          ("srcip", 4),
          ("domain", 5),
          ("url", 6),
          ("leastconn", 7),
          ("weightedrr", 8),
          ("domainhash", 9),
          ("urlhash", 10))
    )


_ApCntBalance_Type.__name__ = "Integer32"
_ApCntBalance_Object = MibTableColumn
apCntBalance = _ApCntBalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 9),
    _ApCntBalance_Type()
)
apCntBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntBalance.setStatus("mandatory")


class _ApCntQOSTag_Type(Integer32):
    """Custom type apCntQOSTag based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ApCntQOSTag_Type.__name__ = "Integer32"
_ApCntQOSTag_Object = MibTableColumn
apCntQOSTag = _ApCntQOSTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 10),
    _ApCntQOSTag_Type()
)
apCntQOSTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntQOSTag.setStatus("mandatory")


class _ApCntEnable_Type(Integer32):
    """Custom type apCntEnable based on Integer32"""
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


_ApCntEnable_Type.__name__ = "Integer32"
_ApCntEnable_Object = MibTableColumn
apCntEnable = _ApCntEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 11),
    _ApCntEnable_Type()
)
apCntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntEnable.setStatus("mandatory")


class _ApCntRedirect_Type(SnmpAdminString):
    """Custom type apCntRedirect based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_ApCntRedirect_Type.__name__ = "SnmpAdminString"
_ApCntRedirect_Object = MibTableColumn
apCntRedirect = _ApCntRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 12),
    _ApCntRedirect_Type()
)
apCntRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntRedirect.setStatus("mandatory")


class _ApCntDrop_Type(SnmpAdminString):
    """Custom type apCntDrop based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApCntDrop_Type.__name__ = "SnmpAdminString"
_ApCntDrop_Object = MibTableColumn
apCntDrop = _ApCntDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 13),
    _ApCntDrop_Type()
)
apCntDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntDrop.setStatus("mandatory")


class _ApCntSize_Type(Integer32):
    """Custom type apCntSize based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntSize_Type.__name__ = "Integer32"
_ApCntSize_Object = MibTableColumn
apCntSize = _ApCntSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 14),
    _ApCntSize_Type()
)
apCntSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSize.setStatus("obsolete")


class _ApCntPersistence_Type(Integer32):
    """Custom type apCntPersistence based on Integer32"""
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


_ApCntPersistence_Type.__name__ = "Integer32"
_ApCntPersistence_Object = MibTableColumn
apCntPersistence = _ApCntPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 15),
    _ApCntPersistence_Type()
)
apCntPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntPersistence.setStatus("mandatory")


class _ApCntAuthor_Type(SnmpAdminString):
    """Custom type apCntAuthor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApCntAuthor_Type.__name__ = "SnmpAdminString"
_ApCntAuthor_Object = MibTableColumn
apCntAuthor = _ApCntAuthor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 16),
    _ApCntAuthor_Type()
)
apCntAuthor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntAuthor.setStatus("mandatory")


class _ApCntSpider_Type(Integer32):
    """Custom type apCntSpider based on Integer32"""
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


_ApCntSpider_Type.__name__ = "Integer32"
_ApCntSpider_Object = MibTableColumn
apCntSpider = _ApCntSpider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 17),
    _ApCntSpider_Type()
)
apCntSpider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSpider.setStatus("mandatory")
_ApCntHits_Type = Counter32
_ApCntHits_Object = MibTableColumn
apCntHits = _ApCntHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 18),
    _ApCntHits_Type()
)
apCntHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntHits.setStatus("mandatory")
_ApCntRedirects_Type = Counter32
_ApCntRedirects_Object = MibTableColumn
apCntRedirects = _ApCntRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 19),
    _ApCntRedirects_Type()
)
apCntRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRedirects.setStatus("mandatory")
_ApCntDrops_Type = Counter32
_ApCntDrops_Object = MibTableColumn
apCntDrops = _ApCntDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 20),
    _ApCntDrops_Type()
)
apCntDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntDrops.setStatus("mandatory")
_ApCntRejNoServices_Type = Counter32
_ApCntRejNoServices_Object = MibTableColumn
apCntRejNoServices = _ApCntRejNoServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 21),
    _ApCntRejNoServices_Type()
)
apCntRejNoServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRejNoServices.setStatus("mandatory")
_ApCntRejServOverload_Type = Counter32
_ApCntRejServOverload_Object = MibTableColumn
apCntRejServOverload = _ApCntRejServOverload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 22),
    _ApCntRejServOverload_Type()
)
apCntRejServOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntRejServOverload.setStatus("mandatory")
_ApCntSpoofs_Type = Counter32
_ApCntSpoofs_Object = MibTableColumn
apCntSpoofs = _ApCntSpoofs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 23),
    _ApCntSpoofs_Type()
)
apCntSpoofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSpoofs.setStatus("mandatory")
_ApCntNats_Type = Counter32
_ApCntNats_Object = MibTableColumn
apCntNats = _ApCntNats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 24),
    _ApCntNats_Type()
)
apCntNats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNats.setStatus("mandatory")
_ApCntByteCount_Type = Counter32
_ApCntByteCount_Object = MibTableColumn
apCntByteCount = _ApCntByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 25),
    _ApCntByteCount_Type()
)
apCntByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntByteCount.setStatus("mandatory")
_ApCntFrameCount_Type = Counter32
_ApCntFrameCount_Object = MibTableColumn
apCntFrameCount = _ApCntFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 26),
    _ApCntFrameCount_Type()
)
apCntFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntFrameCount.setStatus("mandatory")


class _ApCntZeroButton_Type(Integer32):
    """Custom type apCntZeroButton based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ownerCurrentRule", 1),
          ("ownerAllRules", 2))
    )


_ApCntZeroButton_Type.__name__ = "Integer32"
_ApCntZeroButton_Object = MibTableColumn
apCntZeroButton = _ApCntZeroButton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 27),
    _ApCntZeroButton_Type()
)
apCntZeroButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntZeroButton.setStatus("mandatory")


class _ApCntHotListEnabled_Type(Integer32):
    """Custom type apCntHotListEnabled based on Integer32"""
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


_ApCntHotListEnabled_Type.__name__ = "Integer32"
_ApCntHotListEnabled_Object = MibTableColumn
apCntHotListEnabled = _ApCntHotListEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 28),
    _ApCntHotListEnabled_Type()
)
apCntHotListEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHotListEnabled.setStatus("mandatory")


class _ApCntHotListSize_Type(Integer32):
    """Custom type apCntHotListSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApCntHotListSize_Type.__name__ = "Integer32"
_ApCntHotListSize_Object = MibTableColumn
apCntHotListSize = _ApCntHotListSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 29),
    _ApCntHotListSize_Type()
)
apCntHotListSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHotListSize.setStatus("mandatory")


class _ApCntHotListThreshold_Type(Integer32):
    """Custom type apCntHotListThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntHotListThreshold_Type.__name__ = "Integer32"
_ApCntHotListThreshold_Object = MibTableColumn
apCntHotListThreshold = _ApCntHotListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 30),
    _ApCntHotListThreshold_Type()
)
apCntHotListThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHotListThreshold.setStatus("mandatory")


class _ApCntHotListType_Type(Integer32):
    """Custom type apCntHotListType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("hitCount", 0)
    )


_ApCntHotListType_Type.__name__ = "Integer32"
_ApCntHotListType_Object = MibTableColumn
apCntHotListType = _ApCntHotListType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 31),
    _ApCntHotListType_Type()
)
apCntHotListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHotListType.setStatus("mandatory")


class _ApCntHotListInterval_Type(Integer32):
    """Custom type apCntHotListInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ApCntHotListInterval_Type.__name__ = "Integer32"
_ApCntHotListInterval_Object = MibTableColumn
apCntHotListInterval = _ApCntHotListInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 32),
    _ApCntHotListInterval_Type()
)
apCntHotListInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHotListInterval.setStatus("mandatory")


class _ApCntFlowTrack_Type(Integer32):
    """Custom type apCntFlowTrack based on Integer32"""
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


_ApCntFlowTrack_Type.__name__ = "Integer32"
_ApCntFlowTrack_Object = MibTableColumn
apCntFlowTrack = _ApCntFlowTrack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 33),
    _ApCntFlowTrack_Type()
)
apCntFlowTrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowTrack.setStatus("mandatory")


class _ApCntWeightMask_Type(SnmpAdminString):
    """Custom type apCntWeightMask based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApCntWeightMask_Type.__name__ = "SnmpAdminString"
_ApCntWeightMask_Object = MibTableColumn
apCntWeightMask = _ApCntWeightMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 34),
    _ApCntWeightMask_Type()
)
apCntWeightMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntWeightMask.setStatus("mandatory")
_ApCntStickyMask_Type = IpAddress
_ApCntStickyMask_Object = MibTableColumn
apCntStickyMask = _ApCntStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 35),
    _ApCntStickyMask_Type()
)
apCntStickyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyMask.setStatus("mandatory")


class _ApCntCookieStartPos_Type(Integer32):
    """Custom type apCntCookieStartPos based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1999),
    )


_ApCntCookieStartPos_Type.__name__ = "Integer32"
_ApCntCookieStartPos_Object = MibTableColumn
apCntCookieStartPos = _ApCntCookieStartPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 36),
    _ApCntCookieStartPos_Type()
)
apCntCookieStartPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntCookieStartPos.setStatus("mandatory")


class _ApCntHeuristicCookieFence_Type(Integer32):
    """Custom type apCntHeuristicCookieFence based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2000),
    )


_ApCntHeuristicCookieFence_Type.__name__ = "Integer32"
_ApCntHeuristicCookieFence_Object = MibTableColumn
apCntHeuristicCookieFence = _ApCntHeuristicCookieFence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 37),
    _ApCntHeuristicCookieFence_Type()
)
apCntHeuristicCookieFence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHeuristicCookieFence.setStatus("mandatory")


class _ApCntEqlName_Type(SnmpAdminString):
    """Custom type apCntEqlName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApCntEqlName_Type.__name__ = "SnmpAdminString"
_ApCntEqlName_Object = MibTableColumn
apCntEqlName = _ApCntEqlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 38),
    _ApCntEqlName_Type()
)
apCntEqlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntEqlName.setStatus("mandatory")


class _ApCntCacheFalloverType_Type(Integer32):
    """Custom type apCntCacheFalloverType based on Integer32"""
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
        *(("linear", 1),
          ("next", 2),
          ("bypass", 3))
    )


_ApCntCacheFalloverType_Type.__name__ = "Integer32"
_ApCntCacheFalloverType_Object = MibTableColumn
apCntCacheFalloverType = _ApCntCacheFalloverType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 39),
    _ApCntCacheFalloverType_Type()
)
apCntCacheFalloverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntCacheFalloverType.setStatus("mandatory")


class _ApCntLocalLoadThreshold_Type(Integer32):
    """Custom type apCntLocalLoadThreshold based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_ApCntLocalLoadThreshold_Type.__name__ = "Integer32"
_ApCntLocalLoadThreshold_Object = MibTableColumn
apCntLocalLoadThreshold = _ApCntLocalLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 40),
    _ApCntLocalLoadThreshold_Type()
)
apCntLocalLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntLocalLoadThreshold.setStatus("mandatory")
_ApCntStatus_Type = RowStatus
_ApCntStatus_Object = MibTableColumn
apCntStatus = _ApCntStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 41),
    _ApCntStatus_Type()
)
apCntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStatus.setStatus("mandatory")


class _ApCntRedirectLoadThreshold_Type(Integer32):
    """Custom type apCntRedirectLoadThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntRedirectLoadThreshold_Type.__name__ = "Integer32"
_ApCntRedirectLoadThreshold_Object = MibTableColumn
apCntRedirectLoadThreshold = _ApCntRedirectLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 42),
    _ApCntRedirectLoadThreshold_Type()
)
apCntRedirectLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntRedirectLoadThreshold.setStatus("mandatory")


class _ApCntContentType_Type(Integer32):
    """Custom type apCntContentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("ftp-control", 2),
          ("realaudio-control", 3),
          ("ssl", 4),
          ("bypass", 5),
          ("sip", 6))
    )


_ApCntContentType_Type.__name__ = "Integer32"
_ApCntContentType_Object = MibTableColumn
apCntContentType = _ApCntContentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 43),
    _ApCntContentType_Type()
)
apCntContentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntContentType.setStatus("mandatory")


class _ApCntStickyInactivity_Type(Integer32):
    """Custom type apCntStickyInactivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntStickyInactivity_Type.__name__ = "Integer32"
_ApCntStickyInactivity_Object = MibTableColumn
apCntStickyInactivity = _ApCntStickyInactivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 44),
    _ApCntStickyInactivity_Type()
)
apCntStickyInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyInactivity.setStatus("mandatory")


class _ApCntDNSBalance_Type(Integer32):
    """Custom type apCntDNSBalance based on Integer32"""
    defaultValue = 3

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
        *(("preferlocal", 1),
          ("roundrobin", 2),
          ("useownerdnsbalance", 3),
          ("leastloaded", 4))
    )


_ApCntDNSBalance_Type.__name__ = "Integer32"
_ApCntDNSBalance_Object = MibTableColumn
apCntDNSBalance = _ApCntDNSBalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 45),
    _ApCntDNSBalance_Type()
)
apCntDNSBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntDNSBalance.setStatus("mandatory")


class _ApCntStickyGroup_Type(Integer32):
    """Custom type apCntStickyGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApCntStickyGroup_Type.__name__ = "Integer32"
_ApCntStickyGroup_Object = MibTableColumn
apCntStickyGroup = _ApCntStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 46),
    _ApCntStickyGroup_Type()
)
apCntStickyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyGroup.setStatus("mandatory")
_ApCntAppTypeBypasses_Type = Counter32
_ApCntAppTypeBypasses_Object = MibTableColumn
apCntAppTypeBypasses = _ApCntAppTypeBypasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 47),
    _ApCntAppTypeBypasses_Type()
)
apCntAppTypeBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAppTypeBypasses.setStatus("mandatory")
_ApCntNoSvcBypasses_Type = Counter32
_ApCntNoSvcBypasses_Object = MibTableColumn
apCntNoSvcBypasses = _ApCntNoSvcBypasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 48),
    _ApCntNoSvcBypasses_Type()
)
apCntNoSvcBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNoSvcBypasses.setStatus("mandatory")
_ApCntSvcLoadBypasses_Type = Counter32
_ApCntSvcLoadBypasses_Object = MibTableColumn
apCntSvcLoadBypasses = _ApCntSvcLoadBypasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 49),
    _ApCntSvcLoadBypasses_Type()
)
apCntSvcLoadBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSvcLoadBypasses.setStatus("mandatory")
_ApCntConnCtBypasses_Type = Counter32
_ApCntConnCtBypasses_Object = MibTableColumn
apCntConnCtBypasses = _ApCntConnCtBypasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 50),
    _ApCntConnCtBypasses_Type()
)
apCntConnCtBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntConnCtBypasses.setStatus("mandatory")


class _ApCntUrqlTblName_Type(SnmpAdminString):
    """Custom type apCntUrqlTblName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntUrqlTblName_Type.__name__ = "SnmpAdminString"
_ApCntUrqlTblName_Object = MibTableColumn
apCntUrqlTblName = _ApCntUrqlTblName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 51),
    _ApCntUrqlTblName_Type()
)
apCntUrqlTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntUrqlTblName.setStatus("mandatory")


class _ApCntStickyStrPre_Type(SnmpAdminString):
    """Custom type apCntStickyStrPre based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApCntStickyStrPre_Type.__name__ = "SnmpAdminString"
_ApCntStickyStrPre_Object = MibTableColumn
apCntStickyStrPre = _ApCntStickyStrPre_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 52),
    _ApCntStickyStrPre_Type()
)
apCntStickyStrPre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrPre.setStatus("mandatory")


class _ApCntStickyStrEos_Type(SnmpAdminString):
    """Custom type apCntStickyStrEos based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ApCntStickyStrEos_Type.__name__ = "SnmpAdminString"
_ApCntStickyStrEos_Object = MibTableColumn
apCntStickyStrEos = _ApCntStickyStrEos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 53),
    _ApCntStickyStrEos_Type()
)
apCntStickyStrEos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrEos.setStatus("mandatory")


class _ApCntStickyStrSkipLen_Type(Integer32):
    """Custom type apCntStickyStrSkipLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ApCntStickyStrSkipLen_Type.__name__ = "Integer32"
_ApCntStickyStrSkipLen_Object = MibTableColumn
apCntStickyStrSkipLen = _ApCntStickyStrSkipLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 54),
    _ApCntStickyStrSkipLen_Type()
)
apCntStickyStrSkipLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrSkipLen.setStatus("mandatory")


class _ApCntStickyStrProcLen_Type(Integer32):
    """Custom type apCntStickyStrProcLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ApCntStickyStrProcLen_Type.__name__ = "Integer32"
_ApCntStickyStrProcLen_Object = MibTableColumn
apCntStickyStrProcLen = _ApCntStickyStrProcLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 55),
    _ApCntStickyStrProcLen_Type()
)
apCntStickyStrProcLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrProcLen.setStatus("mandatory")


class _ApCntStickyStrAction_Type(Integer32):
    """Custom type apCntStickyStrAction based on Integer32"""
    defaultValue = 4

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
        *(("hash-a", 1),
          ("hash-xor", 2),
          ("hash-crc32", 3),
          ("match-service-cookie", 4))
    )


_ApCntStickyStrAction_Type.__name__ = "Integer32"
_ApCntStickyStrAction_Object = MibTableColumn
apCntStickyStrAction = _ApCntStickyStrAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 56),
    _ApCntStickyStrAction_Type()
)
apCntStickyStrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrAction.setStatus("mandatory")


class _ApCntStickyStrAsciiConv_Type(Integer32):
    """Custom type apCntStickyStrAsciiConv based on Integer32"""
    defaultValue = 1

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


_ApCntStickyStrAsciiConv_Type.__name__ = "Integer32"
_ApCntStickyStrAsciiConv_Object = MibTableColumn
apCntStickyStrAsciiConv = _ApCntStickyStrAsciiConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 57),
    _ApCntStickyStrAsciiConv_Type()
)
apCntStickyStrAsciiConv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrAsciiConv.setStatus("mandatory")


class _ApCntPrimarySorryServer_Type(SnmpAdminString):
    """Custom type apCntPrimarySorryServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntPrimarySorryServer_Type.__name__ = "SnmpAdminString"
_ApCntPrimarySorryServer_Object = MibTableColumn
apCntPrimarySorryServer = _ApCntPrimarySorryServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 58),
    _ApCntPrimarySorryServer_Type()
)
apCntPrimarySorryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntPrimarySorryServer.setStatus("mandatory")


class _ApCntSecondSorryServer_Type(SnmpAdminString):
    """Custom type apCntSecondSorryServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntSecondSorryServer_Type.__name__ = "SnmpAdminString"
_ApCntSecondSorryServer_Object = MibTableColumn
apCntSecondSorryServer = _ApCntSecondSorryServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 59),
    _ApCntSecondSorryServer_Type()
)
apCntSecondSorryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSecondSorryServer.setStatus("mandatory")
_ApCntPrimarySorryHits_Type = Counter32
_ApCntPrimarySorryHits_Object = MibTableColumn
apCntPrimarySorryHits = _ApCntPrimarySorryHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 60),
    _ApCntPrimarySorryHits_Type()
)
apCntPrimarySorryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntPrimarySorryHits.setStatus("mandatory")
_ApCntSecondSorryHits_Type = Counter32
_ApCntSecondSorryHits_Object = MibTableColumn
apCntSecondSorryHits = _ApCntSecondSorryHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 61),
    _ApCntSecondSorryHits_Type()
)
apCntSecondSorryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntSecondSorryHits.setStatus("mandatory")


class _ApCntStickySrvrDownFailover_Type(Integer32):
    """Custom type apCntStickySrvrDownFailover based on Integer32"""
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
        *(("reject", 1),
          ("redirect", 2),
          ("balance", 3),
          ("sticky-srcip", 4),
          ("sticky-srcip-dstport", 5))
    )


_ApCntStickySrvrDownFailover_Type.__name__ = "Integer32"
_ApCntStickySrvrDownFailover_Object = MibTableColumn
apCntStickySrvrDownFailover = _ApCntStickySrvrDownFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 62),
    _ApCntStickySrvrDownFailover_Type()
)
apCntStickySrvrDownFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickySrvrDownFailover.setStatus("mandatory")


class _ApCntStickyStrType_Type(Integer32):
    """Custom type apCntStickyStrType based on Integer32"""
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
        *(("cookieurl", 1),
          ("url", 2),
          ("cookies", 3))
    )


_ApCntStickyStrType_Type.__name__ = "Integer32"
_ApCntStickyStrType_Object = MibTableColumn
apCntStickyStrType = _ApCntStickyStrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 63),
    _ApCntStickyStrType_Type()
)
apCntStickyStrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyStrType.setStatus("mandatory")


class _ApCntParamBypass_Type(Integer32):
    """Custom type apCntParamBypass based on Integer32"""
    defaultValue = 2

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


_ApCntParamBypass_Type.__name__ = "Integer32"
_ApCntParamBypass_Object = MibTableColumn
apCntParamBypass = _ApCntParamBypass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 64),
    _ApCntParamBypass_Type()
)
apCntParamBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntParamBypass.setStatus("mandatory")


class _ApCntAvgLocalLoad_Type(Integer32):
    """Custom type apCntAvgLocalLoad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntAvgLocalLoad_Type.__name__ = "Integer32"
_ApCntAvgLocalLoad_Object = MibTableColumn
apCntAvgLocalLoad = _ApCntAvgLocalLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 65),
    _ApCntAvgLocalLoad_Type()
)
apCntAvgLocalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAvgLocalLoad.setStatus("mandatory")


class _ApCntAvgRemoteLoad_Type(Integer32):
    """Custom type apCntAvgRemoteLoad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntAvgRemoteLoad_Type.__name__ = "Integer32"
_ApCntAvgRemoteLoad_Object = MibTableColumn
apCntAvgRemoteLoad = _ApCntAvgRemoteLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 66),
    _ApCntAvgRemoteLoad_Type()
)
apCntAvgRemoteLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAvgRemoteLoad.setStatus("mandatory")


class _ApCntDqlName_Type(SnmpAdminString):
    """Custom type apCntDqlName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntDqlName_Type.__name__ = "SnmpAdminString"
_ApCntDqlName_Object = MibTableColumn
apCntDqlName = _ApCntDqlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 67),
    _ApCntDqlName_Type()
)
apCntDqlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntDqlName.setStatus("mandatory")


class _ApCntIPAddressRange_Type(Integer32):
    """Custom type apCntIPAddressRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApCntIPAddressRange_Type.__name__ = "Integer32"
_ApCntIPAddressRange_Object = MibTableColumn
apCntIPAddressRange = _ApCntIPAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 68),
    _ApCntIPAddressRange_Type()
)
apCntIPAddressRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntIPAddressRange.setStatus("mandatory")


class _ApCntTagListName_Type(SnmpAdminString):
    """Custom type apCntTagListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntTagListName_Type.__name__ = "SnmpAdminString"
_ApCntTagListName_Object = MibTableColumn
apCntTagListName = _ApCntTagListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 69),
    _ApCntTagListName_Type()
)
apCntTagListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntTagListName.setStatus("mandatory")


class _ApCntStickyNoCookieAction_Type(Integer32):
    """Custom type apCntStickyNoCookieAction based on Integer32"""
    defaultValue = 1

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
        *(("loadbalance", 1),
          ("reject", 2),
          ("redirect", 3),
          ("service", 4))
    )


_ApCntStickyNoCookieAction_Type.__name__ = "Integer32"
_ApCntStickyNoCookieAction_Object = MibTableColumn
apCntStickyNoCookieAction = _ApCntStickyNoCookieAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 70),
    _ApCntStickyNoCookieAction_Type()
)
apCntStickyNoCookieAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyNoCookieAction.setStatus("mandatory")


class _ApCntStickyNoCookieString_Type(SnmpAdminString):
    """Custom type apCntStickyNoCookieString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_ApCntStickyNoCookieString_Type.__name__ = "SnmpAdminString"
_ApCntStickyNoCookieString_Object = MibTableColumn
apCntStickyNoCookieString = _ApCntStickyNoCookieString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 71),
    _ApCntStickyNoCookieString_Type()
)
apCntStickyNoCookieString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyNoCookieString.setStatus("mandatory")


class _ApCntStickyCookiePath_Type(SnmpAdminString):
    """Custom type apCntStickyCookiePath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_ApCntStickyCookiePath_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookiePath_Object = MibTableColumn
apCntStickyCookiePath = _ApCntStickyCookiePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 72),
    _ApCntStickyCookiePath_Type()
)
apCntStickyCookiePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookiePath.setStatus("mandatory")


class _ApCntStickyCookieExp_Type(SnmpAdminString):
    """Custom type apCntStickyCookieExp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ApCntStickyCookieExp_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookieExp_Object = MibTableColumn
apCntStickyCookieExp = _ApCntStickyCookieExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 73),
    _ApCntStickyCookieExp_Type()
)
apCntStickyCookieExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieExp.setStatus("mandatory")


class _ApCntStickyCacheExp_Type(Integer32):
    """Custom type apCntStickyCacheExp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ApCntStickyCacheExp_Type.__name__ = "Integer32"
_ApCntStickyCacheExp_Object = MibTableColumn
apCntStickyCacheExp = _ApCntStickyCacheExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 74),
    _ApCntStickyCacheExp_Type()
)
apCntStickyCacheExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCacheExp.setStatus("mandatory")


class _ApCntTagWeight_Type(Integer32):
    """Custom type apCntTagWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ApCntTagWeight_Type.__name__ = "Integer32"
_ApCntTagWeight_Object = MibTableColumn
apCntTagWeight = _ApCntTagWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 75),
    _ApCntTagWeight_Type()
)
apCntTagWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntTagWeight.setStatus("mandatory")


class _ApCntDNSEnable_Type(Integer32):
    """Custom type apCntDNSEnable based on Integer32"""
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


_ApCntDNSEnable_Type.__name__ = "Integer32"
_ApCntDNSEnable_Object = MibTableColumn
apCntDNSEnable = _ApCntDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 76),
    _ApCntDNSEnable_Type()
)
apCntDNSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntDNSEnable.setStatus("mandatory")


class _ApCntRedundancyL4StatelessEnabled_Type(Integer32):
    """Custom type apCntRedundancyL4StatelessEnabled based on Integer32"""
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


_ApCntRedundancyL4StatelessEnabled_Type.__name__ = "Integer32"
_ApCntRedundancyL4StatelessEnabled_Object = MibTableColumn
apCntRedundancyL4StatelessEnabled = _ApCntRedundancyL4StatelessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 77),
    _ApCntRedundancyL4StatelessEnabled_Type()
)
apCntRedundancyL4StatelessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntRedundancyL4StatelessEnabled.setStatus("mandatory")


class _ApCntStickyCookieText_Type(SnmpAdminString):
    """Custom type apCntStickyCookieText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_ApCntStickyCookieText_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookieText_Object = MibTableColumn
apCntStickyCookieText = _ApCntStickyCookieText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 78),
    _ApCntStickyCookieText_Type()
)
apCntStickyCookieText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieText.setStatus("mandatory")


class _ApCntStickyCookieUrl_Type(SnmpAdminString):
    """Custom type apCntStickyCookieUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_ApCntStickyCookieUrl_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookieUrl_Object = MibTableColumn
apCntStickyCookieUrl = _ApCntStickyCookieUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 79),
    _ApCntStickyCookieUrl_Type()
)
apCntStickyCookieUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieUrl.setStatus("mandatory")


class _ApCntStickyCookieBrowserExpire_Type(Integer32):
    """Custom type apCntStickyCookieBrowserExpire based on Integer32"""
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


_ApCntStickyCookieBrowserExpire_Type.__name__ = "Integer32"
_ApCntStickyCookieBrowserExpire_Object = MibTableColumn
apCntStickyCookieBrowserExpire = _ApCntStickyCookieBrowserExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 80),
    _ApCntStickyCookieBrowserExpire_Type()
)
apCntStickyCookieBrowserExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieBrowserExpire.setStatus("mandatory")


class _ApCntStickyCookieServerExpire_Type(Integer32):
    """Custom type apCntStickyCookieServerExpire based on Integer32"""
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


_ApCntStickyCookieServerExpire_Type.__name__ = "Integer32"
_ApCntStickyCookieServerExpire_Object = MibTableColumn
apCntStickyCookieServerExpire = _ApCntStickyCookieServerExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 81),
    _ApCntStickyCookieServerExpire_Type()
)
apCntStickyCookieServerExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieServerExpire.setStatus("mandatory")


class _ApCntStickyCookieHeadUrl_Type(Integer32):
    """Custom type apCntStickyCookieHeadUrl based on Integer32"""
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


_ApCntStickyCookieHeadUrl_Type.__name__ = "Integer32"
_ApCntStickyCookieHeadUrl_Object = MibTableColumn
apCntStickyCookieHeadUrl = _ApCntStickyCookieHeadUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 82),
    _ApCntStickyCookieHeadUrl_Type()
)
apCntStickyCookieHeadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieHeadUrl.setStatus("mandatory")


class _ApCntSessionRedundantIndex_Type(Integer32):
    """Custom type apCntSessionRedundantIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ApCntSessionRedundantIndex_Type.__name__ = "Integer32"
_ApCntSessionRedundantIndex_Object = MibTableColumn
apCntSessionRedundantIndex = _ApCntSessionRedundantIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 83),
    _ApCntSessionRedundantIndex_Type()
)
apCntSessionRedundantIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSessionRedundantIndex.setStatus("mandatory")


class _ApCntFlowRstReject_Type(Integer32):
    """Custom type apCntFlowRstReject based on Integer32"""
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


_ApCntFlowRstReject_Type.__name__ = "Integer32"
_ApCntFlowRstReject_Object = MibTableColumn
apCntFlowRstReject = _ApCntFlowRstReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 84),
    _ApCntFlowRstReject_Type()
)
apCntFlowRstReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowRstReject.setStatus("mandatory")


class _ApCntFlowTimeout_Type(Integer32):
    """Custom type apCntFlowTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ApCntFlowTimeout_Type.__name__ = "Integer32"
_ApCntFlowTimeout_Object = MibTableColumn
apCntFlowTimeout = _ApCntFlowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 86),
    _ApCntFlowTimeout_Type()
)
apCntFlowTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowTimeout.setStatus("mandatory")


class _ApCntFlowTimeoutStatus_Type(Integer32):
    """Custom type apCntFlowTimeoutStatus based on Integer32"""
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


_ApCntFlowTimeoutStatus_Type.__name__ = "Integer32"
_ApCntFlowTimeoutStatus_Object = MibTableColumn
apCntFlowTimeoutStatus = _ApCntFlowTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 87),
    _ApCntFlowTimeoutStatus_Type()
)
apCntFlowTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowTimeoutStatus.setStatus("mandatory")


class _ApCntVipPingResponse_Type(Integer32):
    """Custom type apCntVipPingResponse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("local-remote", 2))
    )


_ApCntVipPingResponse_Type.__name__ = "Integer32"
_ApCntVipPingResponse_Object = MibTableColumn
apCntVipPingResponse = _ApCntVipPingResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 88),
    _ApCntVipPingResponse_Type()
)
apCntVipPingResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntVipPingResponse.setStatus("mandatory")


class _ApCntStickyCookieName_Type(SnmpAdminString):
    """Custom type apCntStickyCookieName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntStickyCookieName_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookieName_Object = MibTableColumn
apCntStickyCookieName = _ApCntStickyCookieName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 89),
    _ApCntStickyCookieName_Type()
)
apCntStickyCookieName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieName.setStatus("mandatory")


class _ApCntLctCookieName_Type(SnmpAdminString):
    """Custom type apCntLctCookieName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntLctCookieName_Type.__name__ = "SnmpAdminString"
_ApCntLctCookieName_Object = MibTableColumn
apCntLctCookieName = _ApCntLctCookieName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 90),
    _ApCntLctCookieName_Type()
)
apCntLctCookieName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntLctCookieName.setStatus("mandatory")


class _ApCntLctCookieVal_Type(SnmpAdminString):
    """Custom type apCntLctCookieVal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntLctCookieVal_Type.__name__ = "SnmpAdminString"
_ApCntLctCookieVal_Object = MibTableColumn
apCntLctCookieVal = _ApCntLctCookieVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 91),
    _ApCntLctCookieVal_Type()
)
apCntLctCookieVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntLctCookieVal.setStatus("mandatory")


class _ApCntLctCookieExp_Type(SnmpAdminString):
    """Custom type apCntLctCookieExp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ApCntLctCookieExp_Type.__name__ = "SnmpAdminString"
_ApCntLctCookieExp_Object = MibTableColumn
apCntLctCookieExp = _ApCntLctCookieExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 92),
    _ApCntLctCookieExp_Type()
)
apCntLctCookieExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntLctCookieExp.setStatus("mandatory")


class _ApCntStickyCookieDomainName_Type(SnmpAdminString):
    """Custom type apCntStickyCookieDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApCntStickyCookieDomainName_Type.__name__ = "SnmpAdminString"
_ApCntStickyCookieDomainName_Object = MibTableColumn
apCntStickyCookieDomainName = _ApCntStickyCookieDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 93),
    _ApCntStickyCookieDomainName_Type()
)
apCntStickyCookieDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStickyCookieDomainName.setStatus("mandatory")


class _ApCntStringMatchType_Type(Integer32):
    """Custom type apCntStringMatchType based on Integer32"""
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
        *(("specific", 1),
          ("first-service-match", 2),
          ("first-string-found", 3))
    )


_ApCntStringMatchType_Type.__name__ = "Integer32"
_ApCntStringMatchType_Object = MibTableColumn
apCntStringMatchType = _ApCntStringMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 94),
    _ApCntStringMatchType_Type()
)
apCntStringMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntStringMatchType.setStatus("mandatory")


class _ApCntSaspAgentLabel_Type(SnmpAdminString):
    """Custom type apCntSaspAgentLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApCntSaspAgentLabel_Type.__name__ = "SnmpAdminString"
_ApCntSaspAgentLabel_Object = MibTableColumn
apCntSaspAgentLabel = _ApCntSaspAgentLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 95),
    _ApCntSaspAgentLabel_Type()
)
apCntSaspAgentLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSaspAgentLabel.setStatus("mandatory")


class _ApCntArptLctReinsert100_Type(Integer32):
    """Custom type apCntArptLctReinsert100 based on Integer32"""
    defaultValue = 2

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


_ApCntArptLctReinsert100_Type.__name__ = "Integer32"
_ApCntArptLctReinsert100_Object = MibTableColumn
apCntArptLctReinsert100 = _ApCntArptLctReinsert100_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 4, 1, 96),
    _ApCntArptLctReinsert100_Type()
)
apCntArptLctReinsert100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntArptLctReinsert100.setStatus("mandatory")
_ApCntAclBypassCt_Type = Counter32
_ApCntAclBypassCt_Object = MibScalar
apCntAclBypassCt = _ApCntAclBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 5),
    _ApCntAclBypassCt_Type()
)
apCntAclBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntAclBypassCt.setStatus("mandatory")
_ApCntNoRuleBypassCt_Type = Counter32
_ApCntNoRuleBypassCt_Object = MibScalar
apCntNoRuleBypassCt = _ApCntNoRuleBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 6),
    _ApCntNoRuleBypassCt_Type()
)
apCntNoRuleBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntNoRuleBypassCt.setStatus("mandatory")
_ApCntCacheMissBypassCt_Type = Counter32
_ApCntCacheMissBypassCt_Object = MibScalar
apCntCacheMissBypassCt = _ApCntCacheMissBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 7),
    _ApCntCacheMissBypassCt_Type()
)
apCntCacheMissBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntCacheMissBypassCt.setStatus("mandatory")
_ApCntGarbageBypassCt_Type = Counter32
_ApCntGarbageBypassCt_Object = MibScalar
apCntGarbageBypassCt = _ApCntGarbageBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 8),
    _ApCntGarbageBypassCt_Type()
)
apCntGarbageBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntGarbageBypassCt.setStatus("mandatory")
_ApCntUrlParamsBypassCt_Type = Counter32
_ApCntUrlParamsBypassCt_Object = MibScalar
apCntUrlParamsBypassCt = _ApCntUrlParamsBypassCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 9),
    _ApCntUrlParamsBypassCt_Type()
)
apCntUrlParamsBypassCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntUrlParamsBypassCt.setStatus("mandatory")


class _ApCntBypassConnectionPersistence_Type(Integer32):
    """Custom type apCntBypassConnectionPersistence based on Integer32"""
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


_ApCntBypassConnectionPersistence_Type.__name__ = "Integer32"
_ApCntBypassConnectionPersistence_Object = MibScalar
apCntBypassConnectionPersistence = _ApCntBypassConnectionPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 10),
    _ApCntBypassConnectionPersistence_Type()
)
apCntBypassConnectionPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntBypassConnectionPersistence.setStatus("mandatory")


class _ApCntPersistenceResetMethod_Type(Integer32):
    """Custom type apCntPersistenceResetMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("redirect", 0),
          ("remap", 1))
    )


_ApCntPersistenceResetMethod_Type.__name__ = "Integer32"
_ApCntPersistenceResetMethod_Object = MibScalar
apCntPersistenceResetMethod = _ApCntPersistenceResetMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 11),
    _ApCntPersistenceResetMethod_Type()
)
apCntPersistenceResetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntPersistenceResetMethod.setStatus("mandatory")


class _ApCntGlobalPortmapBasePort_Type(Integer32):
    """Custom type apCntGlobalPortmapBasePort based on Integer32"""
    defaultValue = 2016

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2016, 63456),
    )


_ApCntGlobalPortmapBasePort_Type.__name__ = "Integer32"
_ApCntGlobalPortmapBasePort_Object = MibScalar
apCntGlobalPortmapBasePort = _ApCntGlobalPortmapBasePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 13),
    _ApCntGlobalPortmapBasePort_Type()
)
apCntGlobalPortmapBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntGlobalPortmapBasePort.setStatus("mandatory")


class _ApCntGlobalPortmapNumPorts_Type(Integer32):
    """Custom type apCntGlobalPortmapNumPorts based on Integer32"""
    defaultValue = 63488

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 63488),
    )


_ApCntGlobalPortmapNumPorts_Type.__name__ = "Integer32"
_ApCntGlobalPortmapNumPorts_Object = MibScalar
apCntGlobalPortmapNumPorts = _ApCntGlobalPortmapNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 14),
    _ApCntGlobalPortmapNumPorts_Type()
)
apCntGlobalPortmapNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntGlobalPortmapNumPorts.setStatus("mandatory")


class _ApCntNoFlowPortmapBasePort_Type(Integer32):
    """Custom type apCntNoFlowPortmapBasePort based on Integer32"""
    defaultValue = 2016

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2016, 63456),
    )


_ApCntNoFlowPortmapBasePort_Type.__name__ = "Integer32"
_ApCntNoFlowPortmapBasePort_Object = MibScalar
apCntNoFlowPortmapBasePort = _ApCntNoFlowPortmapBasePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 15),
    _ApCntNoFlowPortmapBasePort_Type()
)
apCntNoFlowPortmapBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntNoFlowPortmapBasePort.setStatus("mandatory")


class _ApCntNoFlowPortmapNumPorts_Type(Integer32):
    """Custom type apCntNoFlowPortmapNumPorts based on Integer32"""
    defaultValue = 63488

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 63488),
    )


_ApCntNoFlowPortmapNumPorts_Type.__name__ = "Integer32"
_ApCntNoFlowPortmapNumPorts_Object = MibScalar
apCntNoFlowPortmapNumPorts = _ApCntNoFlowPortmapNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 16),
    _ApCntNoFlowPortmapNumPorts_Type()
)
apCntNoFlowPortmapNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntNoFlowPortmapNumPorts.setStatus("mandatory")


class _ApCntSslL4Fallback_Type(Integer32):
    """Custom type apCntSslL4Fallback based on Integer32"""
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


_ApCntSslL4Fallback_Type.__name__ = "Integer32"
_ApCntSslL4Fallback_Object = MibScalar
apCntSslL4Fallback = _ApCntSslL4Fallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 17),
    _ApCntSslL4Fallback_Type()
)
apCntSslL4Fallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntSslL4Fallback.setStatus("mandatory")
_ApCntFlowStateTable_Object = MibTable
apCntFlowStateTable = _ApCntFlowStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19)
)
if mibBuilder.loadTexts:
    apCntFlowStateTable.setStatus("mandatory")
_ApCntFlowStateEntry_Object = MibTableRow
apCntFlowStateEntry = _ApCntFlowStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1)
)
apCntFlowStateEntry.setIndexNames(
    (0, "ARROWPOINT-CNTEXT-MIB", "apCntFlowStatePort"),
    (0, "ARROWPOINT-CNTEXT-MIB", "apCntFlowStateProtocol"),
)
if mibBuilder.loadTexts:
    apCntFlowStateEntry.setStatus("mandatory")


class _ApCntFlowStatePort_Type(Integer32):
    """Custom type apCntFlowStatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApCntFlowStatePort_Type.__name__ = "Integer32"
_ApCntFlowStatePort_Object = MibTableColumn
apCntFlowStatePort = _ApCntFlowStatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 1),
    _ApCntFlowStatePort_Type()
)
apCntFlowStatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowStatePort.setStatus("mandatory")


class _ApCntFlowStateProtocol_Type(Integer32):
    """Custom type apCntFlowStateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_ApCntFlowStateProtocol_Type.__name__ = "Integer32"
_ApCntFlowStateProtocol_Object = MibTableColumn
apCntFlowStateProtocol = _ApCntFlowStateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 2),
    _ApCntFlowStateProtocol_Type()
)
apCntFlowStateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowStateProtocol.setStatus("mandatory")


class _ApCntFlowStateNatingState_Type(Integer32):
    """Custom type apCntFlowStateNatingState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat-enable", 1),
          ("nat-disable", 2))
    )


_ApCntFlowStateNatingState_Type.__name__ = "Integer32"
_ApCntFlowStateNatingState_Object = MibTableColumn
apCntFlowStateNatingState = _ApCntFlowStateNatingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 3),
    _ApCntFlowStateNatingState_Type()
)
apCntFlowStateNatingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowStateNatingState.setStatus("mandatory")


class _ApCntFlowStateFlowState_Type(Integer32):
    """Custom type apCntFlowStateFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flow-enable", 1),
          ("flow-disable", 2))
    )


_ApCntFlowStateFlowState_Type.__name__ = "Integer32"
_ApCntFlowStateFlowState_Object = MibTableColumn
apCntFlowStateFlowState = _ApCntFlowStateFlowState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 4),
    _ApCntFlowStateFlowState_Type()
)
apCntFlowStateFlowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowStateFlowState.setStatus("mandatory")
_ApCntFlowStateStatus_Type = RowStatus
_ApCntFlowStateStatus_Object = MibTableColumn
apCntFlowStateStatus = _ApCntFlowStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 5),
    _ApCntFlowStateStatus_Type()
)
apCntFlowStateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFlowStateStatus.setStatus("mandatory")
_ApCntFlowStateHitCount_Type = Counter32
_ApCntFlowStateHitCount_Object = MibTableColumn
apCntFlowStateHitCount = _ApCntFlowStateHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 19, 1, 6),
    _ApCntFlowStateHitCount_Type()
)
apCntFlowStateHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntFlowStateHitCount.setStatus("mandatory")


class _ApCntParse2518ExtMethod_Type(Integer32):
    """Custom type apCntParse2518ExtMethod based on Integer32"""
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


_ApCntParse2518ExtMethod_Type.__name__ = "Integer32"
_ApCntParse2518ExtMethod_Object = MibScalar
apCntParse2518ExtMethod = _ApCntParse2518ExtMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 20),
    _ApCntParse2518ExtMethod_Type()
)
apCntParse2518ExtMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntParse2518ExtMethod.setStatus("mandatory")
_ApCntUserDefinedMethodTable_Object = MibTable
apCntUserDefinedMethodTable = _ApCntUserDefinedMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21)
)
if mibBuilder.loadTexts:
    apCntUserDefinedMethodTable.setStatus("mandatory")
_ApCntUserDefinedMethodEntry_Object = MibTableRow
apCntUserDefinedMethodEntry = _ApCntUserDefinedMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21, 1)
)
apCntUserDefinedMethodEntry.setIndexNames(
    (0, "ARROWPOINT-CNTEXT-MIB", "apCntUserDefinedMethodName"),
)
if mibBuilder.loadTexts:
    apCntUserDefinedMethodEntry.setStatus("mandatory")


class _ApCntUserDefinedMethodName_Type(SnmpAdminString):
    """Custom type apCntUserDefinedMethodName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_ApCntUserDefinedMethodName_Type.__name__ = "SnmpAdminString"
_ApCntUserDefinedMethodName_Object = MibTableColumn
apCntUserDefinedMethodName = _ApCntUserDefinedMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21, 1, 1),
    _ApCntUserDefinedMethodName_Type()
)
apCntUserDefinedMethodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apCntUserDefinedMethodName.setStatus("mandatory")


class _ApCntUserDefinedMethodFlag_Type(Integer32):
    """Custom type apCntUserDefinedMethodFlag based on Integer32"""
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
        *(("urlURI", 1),
          ("authorityURI", 2),
          ("wildcardURI", 3))
    )


_ApCntUserDefinedMethodFlag_Type.__name__ = "Integer32"
_ApCntUserDefinedMethodFlag_Object = MibTableColumn
apCntUserDefinedMethodFlag = _ApCntUserDefinedMethodFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21, 1, 2),
    _ApCntUserDefinedMethodFlag_Type()
)
apCntUserDefinedMethodFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntUserDefinedMethodFlag.setStatus("mandatory")
_ApCntUserDefinedMethodStatus_Type = RowStatus
_ApCntUserDefinedMethodStatus_Object = MibTableColumn
apCntUserDefinedMethodStatus = _ApCntUserDefinedMethodStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21, 1, 3),
    _ApCntUserDefinedMethodStatus_Type()
)
apCntUserDefinedMethodStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntUserDefinedMethodStatus.setStatus("mandatory")
_ApCntUserDefinedMethodHitCount_Type = Counter32
_ApCntUserDefinedMethodHitCount_Object = MibTableColumn
apCntUserDefinedMethodHitCount = _ApCntUserDefinedMethodHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 21, 1, 4),
    _ApCntUserDefinedMethodHitCount_Type()
)
apCntUserDefinedMethodHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntUserDefinedMethodHitCount.setStatus("mandatory")


class _ApCntHttpRedirectOption_Type(Integer32):
    """Custom type apCntHttpRedirectOption based on Integer32"""
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
        *(("fin-rst", 1),
          ("fin-fin", 2),
          ("rst-rst", 3))
    )


_ApCntHttpRedirectOption_Type.__name__ = "Integer32"
_ApCntHttpRedirectOption_Object = MibScalar
apCntHttpRedirectOption = _ApCntHttpRedirectOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 22),
    _ApCntHttpRedirectOption_Type()
)
apCntHttpRedirectOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntHttpRedirectOption.setStatus("mandatory")


class _ApCntFtpDataChannelTimeout_Type(Integer32):
    """Custom type apCntFtpDataChannelTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_ApCntFtpDataChannelTimeout_Type.__name__ = "Integer32"
_ApCntFtpDataChannelTimeout_Object = MibScalar
apCntFtpDataChannelTimeout = _ApCntFtpDataChannelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 23),
    _ApCntFtpDataChannelTimeout_Type()
)
apCntFtpDataChannelTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntFtpDataChannelTimeout.setStatus("mandatory")


class _ApCntMaxSaspWeight_Type(Integer32):
    """Custom type apCntMaxSaspWeight based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApCntMaxSaspWeight_Type.__name__ = "Integer32"
_ApCntMaxSaspWeight_Object = MibScalar
apCntMaxSaspWeight = _ApCntMaxSaspWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 16, 24),
    _ApCntMaxSaspWeight_Type()
)
apCntMaxSaspWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntMaxSaspWeight.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARROWPOINT-CNTEXT-MIB",
    **{"apCntExtMib": apCntExtMib,
       "apCntExtMibNotifs": apCntExtMibNotifs,
       "apCntExtMibObjects": apCntExtMibObjects,
       "apCntExtMibConform": apCntExtMibConform,
       "apCntExtMibCompliances": apCntExtMibCompliances,
       "apCntExtMibCompliance": apCntExtMibCompliance,
       "apCntExtMibGroups": apCntExtMibGroups,
       "apCntExtMibGroup": apCntExtMibGroup,
       "apCntExtOptionalMibGroup": apCntExtOptionalMibGroup,
       "apCntRuleOrder": apCntRuleOrder,
       "apCntTable": apCntTable,
       "apCntEntry": apCntEntry,
       "apCntOwner": apCntOwner,
       "apCntName": apCntName,
       "apCntIndex": apCntIndex,
       "apCntIPAddress": apCntIPAddress,
       "apCntIPProtocol": apCntIPProtocol,
       "apCntPort": apCntPort,
       "apCntUrl": apCntUrl,
       "apCntSticky": apCntSticky,
       "apCntBalance": apCntBalance,
       "apCntQOSTag": apCntQOSTag,
       "apCntEnable": apCntEnable,
       "apCntRedirect": apCntRedirect,
       "apCntDrop": apCntDrop,
       "apCntSize": apCntSize,
       "apCntPersistence": apCntPersistence,
       "apCntAuthor": apCntAuthor,
       "apCntSpider": apCntSpider,
       "apCntHits": apCntHits,
       "apCntRedirects": apCntRedirects,
       "apCntDrops": apCntDrops,
       "apCntRejNoServices": apCntRejNoServices,
       "apCntRejServOverload": apCntRejServOverload,
       "apCntSpoofs": apCntSpoofs,
       "apCntNats": apCntNats,
       "apCntByteCount": apCntByteCount,
       "apCntFrameCount": apCntFrameCount,
       "apCntZeroButton": apCntZeroButton,
       "apCntHotListEnabled": apCntHotListEnabled,
       "apCntHotListSize": apCntHotListSize,
       "apCntHotListThreshold": apCntHotListThreshold,
       "apCntHotListType": apCntHotListType,
       "apCntHotListInterval": apCntHotListInterval,
       "apCntFlowTrack": apCntFlowTrack,
       "apCntWeightMask": apCntWeightMask,
       "apCntStickyMask": apCntStickyMask,
       "apCntCookieStartPos": apCntCookieStartPos,
       "apCntHeuristicCookieFence": apCntHeuristicCookieFence,
       "apCntEqlName": apCntEqlName,
       "apCntCacheFalloverType": apCntCacheFalloverType,
       "apCntLocalLoadThreshold": apCntLocalLoadThreshold,
       "apCntStatus": apCntStatus,
       "apCntRedirectLoadThreshold": apCntRedirectLoadThreshold,
       "apCntContentType": apCntContentType,
       "apCntStickyInactivity": apCntStickyInactivity,
       "apCntDNSBalance": apCntDNSBalance,
       "apCntStickyGroup": apCntStickyGroup,
       "apCntAppTypeBypasses": apCntAppTypeBypasses,
       "apCntNoSvcBypasses": apCntNoSvcBypasses,
       "apCntSvcLoadBypasses": apCntSvcLoadBypasses,
       "apCntConnCtBypasses": apCntConnCtBypasses,
       "apCntUrqlTblName": apCntUrqlTblName,
       "apCntStickyStrPre": apCntStickyStrPre,
       "apCntStickyStrEos": apCntStickyStrEos,
       "apCntStickyStrSkipLen": apCntStickyStrSkipLen,
       "apCntStickyStrProcLen": apCntStickyStrProcLen,
       "apCntStickyStrAction": apCntStickyStrAction,
       "apCntStickyStrAsciiConv": apCntStickyStrAsciiConv,
       "apCntPrimarySorryServer": apCntPrimarySorryServer,
       "apCntSecondSorryServer": apCntSecondSorryServer,
       "apCntPrimarySorryHits": apCntPrimarySorryHits,
       "apCntSecondSorryHits": apCntSecondSorryHits,
       "apCntStickySrvrDownFailover": apCntStickySrvrDownFailover,
       "apCntStickyStrType": apCntStickyStrType,
       "apCntParamBypass": apCntParamBypass,
       "apCntAvgLocalLoad": apCntAvgLocalLoad,
       "apCntAvgRemoteLoad": apCntAvgRemoteLoad,
       "apCntDqlName": apCntDqlName,
       "apCntIPAddressRange": apCntIPAddressRange,
       "apCntTagListName": apCntTagListName,
       "apCntStickyNoCookieAction": apCntStickyNoCookieAction,
       "apCntStickyNoCookieString": apCntStickyNoCookieString,
       "apCntStickyCookiePath": apCntStickyCookiePath,
       "apCntStickyCookieExp": apCntStickyCookieExp,
       "apCntStickyCacheExp": apCntStickyCacheExp,
       "apCntTagWeight": apCntTagWeight,
       "apCntDNSEnable": apCntDNSEnable,
       "apCntRedundancyL4StatelessEnabled": apCntRedundancyL4StatelessEnabled,
       "apCntStickyCookieText": apCntStickyCookieText,
       "apCntStickyCookieUrl": apCntStickyCookieUrl,
       "apCntStickyCookieBrowserExpire": apCntStickyCookieBrowserExpire,
       "apCntStickyCookieServerExpire": apCntStickyCookieServerExpire,
       "apCntStickyCookieHeadUrl": apCntStickyCookieHeadUrl,
       "apCntSessionRedundantIndex": apCntSessionRedundantIndex,
       "apCntFlowRstReject": apCntFlowRstReject,
       "apCntFlowTimeout": apCntFlowTimeout,
       "apCntFlowTimeoutStatus": apCntFlowTimeoutStatus,
       "apCntVipPingResponse": apCntVipPingResponse,
       "apCntStickyCookieName": apCntStickyCookieName,
       "apCntLctCookieName": apCntLctCookieName,
       "apCntLctCookieVal": apCntLctCookieVal,
       "apCntLctCookieExp": apCntLctCookieExp,
       "apCntStickyCookieDomainName": apCntStickyCookieDomainName,
       "apCntStringMatchType": apCntStringMatchType,
       "apCntSaspAgentLabel": apCntSaspAgentLabel,
       "apCntArptLctReinsert100": apCntArptLctReinsert100,
       "apCntAclBypassCt": apCntAclBypassCt,
       "apCntNoRuleBypassCt": apCntNoRuleBypassCt,
       "apCntCacheMissBypassCt": apCntCacheMissBypassCt,
       "apCntGarbageBypassCt": apCntGarbageBypassCt,
       "apCntUrlParamsBypassCt": apCntUrlParamsBypassCt,
       "apCntBypassConnectionPersistence": apCntBypassConnectionPersistence,
       "apCntPersistenceResetMethod": apCntPersistenceResetMethod,
       "apCntGlobalPortmapBasePort": apCntGlobalPortmapBasePort,
       "apCntGlobalPortmapNumPorts": apCntGlobalPortmapNumPorts,
       "apCntNoFlowPortmapBasePort": apCntNoFlowPortmapBasePort,
       "apCntNoFlowPortmapNumPorts": apCntNoFlowPortmapNumPorts,
       "apCntSslL4Fallback": apCntSslL4Fallback,
       "apCntFlowStateTable": apCntFlowStateTable,
       "apCntFlowStateEntry": apCntFlowStateEntry,
       "apCntFlowStatePort": apCntFlowStatePort,
       "apCntFlowStateProtocol": apCntFlowStateProtocol,
       "apCntFlowStateNatingState": apCntFlowStateNatingState,
       "apCntFlowStateFlowState": apCntFlowStateFlowState,
       "apCntFlowStateStatus": apCntFlowStateStatus,
       "apCntFlowStateHitCount": apCntFlowStateHitCount,
       "apCntParse2518ExtMethod": apCntParse2518ExtMethod,
       "apCntUserDefinedMethodTable": apCntUserDefinedMethodTable,
       "apCntUserDefinedMethodEntry": apCntUserDefinedMethodEntry,
       "apCntUserDefinedMethodName": apCntUserDefinedMethodName,
       "apCntUserDefinedMethodFlag": apCntUserDefinedMethodFlag,
       "apCntUserDefinedMethodStatus": apCntUserDefinedMethodStatus,
       "apCntUserDefinedMethodHitCount": apCntUserDefinedMethodHitCount,
       "apCntHttpRedirectOption": apCntHttpRedirectOption,
       "apCntFtpDataChannelTimeout": apCntFtpDataChannelTimeout,
       "apCntMaxSaspWeight": apCntMaxSaspWeight}
)
