# SNMP MIB module (RUIJIE-WEB-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WEB-PORTAL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieWebPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69)
)
if mibBuilder.loadTexts:
    ruijieWebPortalMIB.setRevisions(
        ("2010-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWebPortalMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWebPortalMIBObjects = _RuijieWebPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1)
)
_RuijieWebPortalGlobalMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWebPortalGlobalMIBObjects = _RuijieWebPortalGlobalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1)
)


class _RuijieWebPortalGlbWebAuthType_Type(Integer32):
    """Custom type ruijieWebPortalGlbWebAuthType based on Integer32"""
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
        *(("internal", 0),
          ("customized", 1),
          ("external", 2))
    )


_RuijieWebPortalGlbWebAuthType_Type.__name__ = "Integer32"
_RuijieWebPortalGlbWebAuthType_Object = MibScalar
ruijieWebPortalGlbWebAuthType = _RuijieWebPortalGlbWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 1),
    _RuijieWebPortalGlbWebAuthType_Type()
)
ruijieWebPortalGlbWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbWebAuthType.setStatus("current")


class _RuijieWebPortalGlbMethodList_Type(DisplayString):
    """Custom type ruijieWebPortalGlbMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuijieWebPortalGlbMethodList_Type.__name__ = "DisplayString"
_RuijieWebPortalGlbMethodList_Object = MibScalar
ruijieWebPortalGlbMethodList = _RuijieWebPortalGlbMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 2),
    _RuijieWebPortalGlbMethodList_Type()
)
ruijieWebPortalGlbMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbMethodList.setStatus("current")


class _RuijieWebPortalGlbCustomizedPageName_Type(DisplayString):
    """Custom type ruijieWebPortalGlbCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalGlbCustomizedPageName_Type.__name__ = "DisplayString"
_RuijieWebPortalGlbCustomizedPageName_Object = MibScalar
ruijieWebPortalGlbCustomizedPageName = _RuijieWebPortalGlbCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 3),
    _RuijieWebPortalGlbCustomizedPageName_Type()
)
ruijieWebPortalGlbCustomizedPageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbCustomizedPageName.setStatus("current")


class _RuijieWebPortalGlbExternalWebPortalURL_Type(DisplayString):
    """Custom type ruijieWebPortalGlbExternalWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalGlbExternalWebPortalURL_Type.__name__ = "DisplayString"
_RuijieWebPortalGlbExternalWebPortalURL_Object = MibScalar
ruijieWebPortalGlbExternalWebPortalURL = _RuijieWebPortalGlbExternalWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 4),
    _RuijieWebPortalGlbExternalWebPortalURL_Type()
)
ruijieWebPortalGlbExternalWebPortalURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbExternalWebPortalURL.setStatus("current")


class _RuijieWebPortalGlbCustomizedLogoName_Type(DisplayString):
    """Custom type ruijieWebPortalGlbCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalGlbCustomizedLogoName_Type.__name__ = "DisplayString"
_RuijieWebPortalGlbCustomizedLogoName_Object = MibScalar
ruijieWebPortalGlbCustomizedLogoName = _RuijieWebPortalGlbCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 5),
    _RuijieWebPortalGlbCustomizedLogoName_Type()
)
ruijieWebPortalGlbCustomizedLogoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbCustomizedLogoName.setStatus("current")


class _RuijieWebPortalGlbEchoManufacturerLogo_Type(Integer32):
    """Custom type ruijieWebPortalGlbEchoManufacturerLogo based on Integer32"""
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


_RuijieWebPortalGlbEchoManufacturerLogo_Type.__name__ = "Integer32"
_RuijieWebPortalGlbEchoManufacturerLogo_Object = MibScalar
ruijieWebPortalGlbEchoManufacturerLogo = _RuijieWebPortalGlbEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 6),
    _RuijieWebPortalGlbEchoManufacturerLogo_Type()
)
ruijieWebPortalGlbEchoManufacturerLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbEchoManufacturerLogo.setStatus("current")


class _RuijieWebPortalGlbWelcomeMsg_Type(OctetString):
    """Custom type ruijieWebPortalGlbWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_RuijieWebPortalGlbWelcomeMsg_Type.__name__ = "OctetString"
_RuijieWebPortalGlbWelcomeMsg_Object = MibScalar
ruijieWebPortalGlbWelcomeMsg = _RuijieWebPortalGlbWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 7),
    _RuijieWebPortalGlbWelcomeMsg_Type()
)
ruijieWebPortalGlbWelcomeMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbWelcomeMsg.setStatus("current")


class _RuijieWebPortalGlbWebPageTitle_Type(DisplayString):
    """Custom type ruijieWebPortalGlbWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalGlbWebPageTitle_Type.__name__ = "DisplayString"
_RuijieWebPortalGlbWebPageTitle_Object = MibScalar
ruijieWebPortalGlbWebPageTitle = _RuijieWebPortalGlbWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 1, 8),
    _RuijieWebPortalGlbWebPageTitle_Type()
)
ruijieWebPortalGlbWebPageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebPortalGlbWebPageTitle.setStatus("current")
_RuijieWebPortalLocalMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWebPortalLocalMIBObjects = _RuijieWebPortalLocalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2)
)
_RuijieWebPortalAuthTable_Object = MibTable
ruijieWebPortalAuthTable = _RuijieWebPortalAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieWebPortalAuthTable.setStatus("current")
_RuijieWebPortalAuthEntry_Object = MibTableRow
ruijieWebPortalAuthEntry = _RuijieWebPortalAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1)
)
ruijieWebPortalAuthEntry.setIndexNames(
    (0, "RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalNetMode"),
    (0, "RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalNetID"),
)
if mibBuilder.loadTexts:
    ruijieWebPortalAuthEntry.setStatus("current")


class _RuijieWebPortalNetMode_Type(Integer32):
    """Custom type ruijieWebPortalNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wlan", 1),
          ("ethernet", 2),
          ("vlan", 3))
    )


_RuijieWebPortalNetMode_Type.__name__ = "Integer32"
_RuijieWebPortalNetMode_Object = MibTableColumn
ruijieWebPortalNetMode = _RuijieWebPortalNetMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 1),
    _RuijieWebPortalNetMode_Type()
)
ruijieWebPortalNetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebPortalNetMode.setStatus("current")


class _RuijieWebPortalNetID_Type(Integer32):
    """Custom type ruijieWebPortalNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieWebPortalNetID_Type.__name__ = "Integer32"
_RuijieWebPortalNetID_Object = MibTableColumn
ruijieWebPortalNetID = _RuijieWebPortalNetID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 2),
    _RuijieWebPortalNetID_Type()
)
ruijieWebPortalNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebPortalNetID.setStatus("current")


class _RuijieWebPortalWebAuthType_Type(Integer32):
    """Custom type ruijieWebPortalWebAuthType based on Integer32"""
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
        *(("internal", 0),
          ("customized", 1),
          ("external", 2))
    )


_RuijieWebPortalWebAuthType_Type.__name__ = "Integer32"
_RuijieWebPortalWebAuthType_Object = MibTableColumn
ruijieWebPortalWebAuthType = _RuijieWebPortalWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 3),
    _RuijieWebPortalWebAuthType_Type()
)
ruijieWebPortalWebAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalWebAuthType.setStatus("current")


class _RuijieWebPortalUseGlbConfigFlag_Type(Integer32):
    """Custom type ruijieWebPortalUseGlbConfigFlag based on Integer32"""
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


_RuijieWebPortalUseGlbConfigFlag_Type.__name__ = "Integer32"
_RuijieWebPortalUseGlbConfigFlag_Object = MibTableColumn
ruijieWebPortalUseGlbConfigFlag = _RuijieWebPortalUseGlbConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 4),
    _RuijieWebPortalUseGlbConfigFlag_Type()
)
ruijieWebPortalUseGlbConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalUseGlbConfigFlag.setStatus("current")


class _RuijieWebPortalMetholdList_Type(DisplayString):
    """Custom type ruijieWebPortalMetholdList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieWebPortalMetholdList_Type.__name__ = "DisplayString"
_RuijieWebPortalMetholdList_Object = MibTableColumn
ruijieWebPortalMetholdList = _RuijieWebPortalMetholdList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 5),
    _RuijieWebPortalMetholdList_Type()
)
ruijieWebPortalMetholdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalMetholdList.setStatus("current")


class _RuijieWebPortalCustomizedPageName_Type(DisplayString):
    """Custom type ruijieWebPortalCustomizedPageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalCustomizedPageName_Type.__name__ = "DisplayString"
_RuijieWebPortalCustomizedPageName_Object = MibTableColumn
ruijieWebPortalCustomizedPageName = _RuijieWebPortalCustomizedPageName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 6),
    _RuijieWebPortalCustomizedPageName_Type()
)
ruijieWebPortalCustomizedPageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalCustomizedPageName.setStatus("current")


class _RuijieWebPortalExtWebPortalURL_Type(DisplayString):
    """Custom type ruijieWebPortalExtWebPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalExtWebPortalURL_Type.__name__ = "DisplayString"
_RuijieWebPortalExtWebPortalURL_Object = MibTableColumn
ruijieWebPortalExtWebPortalURL = _RuijieWebPortalExtWebPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 7),
    _RuijieWebPortalExtWebPortalURL_Type()
)
ruijieWebPortalExtWebPortalURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalExtWebPortalURL.setStatus("current")


class _RuijieWebPortalCustomizedLogoName_Type(DisplayString):
    """Custom type ruijieWebPortalCustomizedLogoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalCustomizedLogoName_Type.__name__ = "DisplayString"
_RuijieWebPortalCustomizedLogoName_Object = MibTableColumn
ruijieWebPortalCustomizedLogoName = _RuijieWebPortalCustomizedLogoName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 8),
    _RuijieWebPortalCustomizedLogoName_Type()
)
ruijieWebPortalCustomizedLogoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalCustomizedLogoName.setStatus("current")


class _RuijieWebPortalEchoManufacturerLogo_Type(Integer32):
    """Custom type ruijieWebPortalEchoManufacturerLogo based on Integer32"""
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


_RuijieWebPortalEchoManufacturerLogo_Type.__name__ = "Integer32"
_RuijieWebPortalEchoManufacturerLogo_Object = MibTableColumn
ruijieWebPortalEchoManufacturerLogo = _RuijieWebPortalEchoManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 9),
    _RuijieWebPortalEchoManufacturerLogo_Type()
)
ruijieWebPortalEchoManufacturerLogo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalEchoManufacturerLogo.setStatus("current")


class _RuijieWebPortalWelcomeMsg_Type(OctetString):
    """Custom type ruijieWebPortalWelcomeMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2047),
    )


_RuijieWebPortalWelcomeMsg_Type.__name__ = "OctetString"
_RuijieWebPortalWelcomeMsg_Object = MibTableColumn
ruijieWebPortalWelcomeMsg = _RuijieWebPortalWelcomeMsg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 10),
    _RuijieWebPortalWelcomeMsg_Type()
)
ruijieWebPortalWelcomeMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalWelcomeMsg.setStatus("current")


class _RuijieWebPortalWebPageTitle_Type(DisplayString):
    """Custom type ruijieWebPortalWebPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 130),
    )


_RuijieWebPortalWebPageTitle_Type.__name__ = "DisplayString"
_RuijieWebPortalWebPageTitle_Object = MibTableColumn
ruijieWebPortalWebPageTitle = _RuijieWebPortalWebPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 11),
    _RuijieWebPortalWebPageTitle_Type()
)
ruijieWebPortalWebPageTitle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalWebPageTitle.setStatus("current")
_RuijieWebPortalEntryStatus_Type = RowStatus
_RuijieWebPortalEntryStatus_Object = MibTableColumn
ruijieWebPortalEntryStatus = _RuijieWebPortalEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 1, 2, 1, 1, 12),
    _RuijieWebPortalEntryStatus_Type()
)
ruijieWebPortalEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebPortalEntryStatus.setStatus("current")
_RuijieWebPortalMIBConformance_ObjectIdentity = ObjectIdentity
ruijieWebPortalMIBConformance = _RuijieWebPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 2)
)
_RuijieWebPortalMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieWebPortalMIBCompliances = _RuijieWebPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 2, 1)
)
_RuijieWebPortalMIBGroups_ObjectIdentity = ObjectIdentity
ruijieWebPortalMIBGroups = _RuijieWebPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 2, 2)
)

# Managed Objects groups

ruijieWebPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 2, 2, 1)
)
ruijieWebPortalMIBGroup.setObjects(
      *(("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbWebAuthType"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbMethodList"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbCustomizedPageName"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbExternalWebPortalURL"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbCustomizedLogoName"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbEchoManufacturerLogo"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbWelcomeMsg"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalGlbWebPageTitle"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalNetMode"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalNetID"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalWebAuthType"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalUseGlbConfigFlag"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalMetholdList"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalCustomizedPageName"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalExtWebPortalURL"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalCustomizedLogoName"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalEchoManufacturerLogo"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalWelcomeMsg"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalWebPageTitle"),
        ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalEntryStatus"))
)
if mibBuilder.loadTexts:
    ruijieWebPortalMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieWebPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 69, 2, 1, 1)
)
ruijieWebPortalMIBCompliance.setObjects(
    ("RUIJIE-WEB-PORTAL-MIB", "ruijieWebPortalMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieWebPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WEB-PORTAL-MIB",
    **{"ruijieWebPortalMIB": ruijieWebPortalMIB,
       "ruijieWebPortalMIBObjects": ruijieWebPortalMIBObjects,
       "ruijieWebPortalGlobalMIBObjects": ruijieWebPortalGlobalMIBObjects,
       "ruijieWebPortalGlbWebAuthType": ruijieWebPortalGlbWebAuthType,
       "ruijieWebPortalGlbMethodList": ruijieWebPortalGlbMethodList,
       "ruijieWebPortalGlbCustomizedPageName": ruijieWebPortalGlbCustomizedPageName,
       "ruijieWebPortalGlbExternalWebPortalURL": ruijieWebPortalGlbExternalWebPortalURL,
       "ruijieWebPortalGlbCustomizedLogoName": ruijieWebPortalGlbCustomizedLogoName,
       "ruijieWebPortalGlbEchoManufacturerLogo": ruijieWebPortalGlbEchoManufacturerLogo,
       "ruijieWebPortalGlbWelcomeMsg": ruijieWebPortalGlbWelcomeMsg,
       "ruijieWebPortalGlbWebPageTitle": ruijieWebPortalGlbWebPageTitle,
       "ruijieWebPortalLocalMIBObjects": ruijieWebPortalLocalMIBObjects,
       "ruijieWebPortalAuthTable": ruijieWebPortalAuthTable,
       "ruijieWebPortalAuthEntry": ruijieWebPortalAuthEntry,
       "ruijieWebPortalNetMode": ruijieWebPortalNetMode,
       "ruijieWebPortalNetID": ruijieWebPortalNetID,
       "ruijieWebPortalWebAuthType": ruijieWebPortalWebAuthType,
       "ruijieWebPortalUseGlbConfigFlag": ruijieWebPortalUseGlbConfigFlag,
       "ruijieWebPortalMetholdList": ruijieWebPortalMetholdList,
       "ruijieWebPortalCustomizedPageName": ruijieWebPortalCustomizedPageName,
       "ruijieWebPortalExtWebPortalURL": ruijieWebPortalExtWebPortalURL,
       "ruijieWebPortalCustomizedLogoName": ruijieWebPortalCustomizedLogoName,
       "ruijieWebPortalEchoManufacturerLogo": ruijieWebPortalEchoManufacturerLogo,
       "ruijieWebPortalWelcomeMsg": ruijieWebPortalWelcomeMsg,
       "ruijieWebPortalWebPageTitle": ruijieWebPortalWebPageTitle,
       "ruijieWebPortalEntryStatus": ruijieWebPortalEntryStatus,
       "ruijieWebPortalMIBConformance": ruijieWebPortalMIBConformance,
       "ruijieWebPortalMIBCompliances": ruijieWebPortalMIBCompliances,
       "ruijieWebPortalMIBCompliance": ruijieWebPortalMIBCompliance,
       "ruijieWebPortalMIBGroups": ruijieWebPortalMIBGroups,
       "ruijieWebPortalMIBGroup": ruijieWebPortalMIBGroup}
)
