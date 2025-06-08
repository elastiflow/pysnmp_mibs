# SNMP MIB module (TROPIC-CARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-CARD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(tnCardMIB,
 tnCardModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardMIB",
    "tnCardModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmCardCapacity,
 AluWdmWtClkValues,
 TropicCardCLEI,
 TropicCardHFD,
 TropicCardManufacturingPartNumber,
 TropicCardMarketingPartNumber,
 TropicCardSWGenericLoadName,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmCardCapacity",
    "AluWdmWtClkValues",
    "TropicCardCLEI",
    "TropicCardHFD",
    "TropicCardManufacturingPartNumber",
    "TropicCardMarketingPartNumber",
    "TropicCardSWGenericLoadName",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnCardMibModule.setRevisions(
        ("2008-04-11 12:00",
         "2008-05-29 12:00",
         "2008-06-05 12:00",
         "2008-09-19 12:00",
         "2008-09-24 12:00",
         "2008-09-26 12:00",
         "2009-02-01 12:00",
         "2009-02-10 12:00",
         "2009-03-31 12:00",
         "2011-05-19 12:00",
         "2011-05-23 12:00",
         "2012-07-10 12:00",
         "2012-07-17 12:00",
         "2012-09-06 12:00",
         "2013-05-21 12:00",
         "2013-08-16 12:00",
         "2013-11-18 12:00",
         "2013-12-15 12:00",
         "2013-12-26 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnCardConf_ObjectIdentity = ObjectIdentity
tnCardConf = _TnCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1)
)
_TnCardGroups_ObjectIdentity = ObjectIdentity
tnCardGroups = _TnCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1)
)
_TnCardCompliances_ObjectIdentity = ObjectIdentity
tnCardCompliances = _TnCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 2)
)
_TnCardObjs_ObjectIdentity = ObjectIdentity
tnCardObjs = _TnCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2)
)
_TnCardBasics_ObjectIdentity = ObjectIdentity
tnCardBasics = _TnCardBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1)
)
_TnCardTotal_Type = Integer32
_TnCardTotal_Object = MibScalar
tnCardTotal = _TnCardTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 1),
    _TnCardTotal_Type()
)
tnCardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardTotal.setStatus("current")
_TnCardTable_Object = MibTable
tnCardTable = _TnCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnCardTable.setStatus("current")
_TnCardEntry_Object = MibTableRow
tnCardEntry = _TnCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1)
)
tnCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardEntry.setStatus("current")


class _TnCardName_Type(SnmpAdminString):
    """Custom type tnCardName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCardName_Type.__name__ = "SnmpAdminString"
_TnCardName_Object = MibTableColumn
tnCardName = _TnCardName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 1),
    _TnCardName_Type()
)
tnCardName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardName.setStatus("current")


class _TnCardDescr_Type(SnmpAdminString):
    """Custom type tnCardDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCardDescr_Type.__name__ = "SnmpAdminString"
_TnCardDescr_Object = MibTableColumn
tnCardDescr = _TnCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 2),
    _TnCardDescr_Type()
)
tnCardDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardDescr.setStatus("current")


class _TnCardCLEI_Type(TropicCardCLEI):
    """Custom type tnCardCLEI based on TropicCardCLEI"""
    defaultValue = OctetString("")


_TnCardCLEI_Type.__name__ = "TropicCardCLEI"
_TnCardCLEI_Object = MibTableColumn
tnCardCLEI = _TnCardCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 3),
    _TnCardCLEI_Type()
)
tnCardCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCLEI.setStatus("current")


class _TnCardHFD_Type(TropicCardHFD):
    """Custom type tnCardHFD based on TropicCardHFD"""
    defaultValue = OctetString("")


_TnCardHFD_Type.__name__ = "TropicCardHFD"
_TnCardHFD_Object = MibTableColumn
tnCardHFD = _TnCardHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 4),
    _TnCardHFD_Type()
)
tnCardHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardHFD.setStatus("current")


class _TnCardSerialNumber_Type(TropicCardSerialNumber):
    """Custom type tnCardSerialNumber based on TropicCardSerialNumber"""
    defaultValue = OctetString("")


_TnCardSerialNumber_Type.__name__ = "TropicCardSerialNumber"
_TnCardSerialNumber_Object = MibTableColumn
tnCardSerialNumber = _TnCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 5),
    _TnCardSerialNumber_Type()
)
tnCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSerialNumber.setStatus("current")


class _TnCardManufacturingPartNumber_Type(TropicCardManufacturingPartNumber):
    """Custom type tnCardManufacturingPartNumber based on TropicCardManufacturingPartNumber"""
    defaultValue = OctetString("")


_TnCardManufacturingPartNumber_Type.__name__ = "TropicCardManufacturingPartNumber"
_TnCardManufacturingPartNumber_Object = MibTableColumn
tnCardManufacturingPartNumber = _TnCardManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 6),
    _TnCardManufacturingPartNumber_Type()
)
tnCardManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardManufacturingPartNumber.setStatus("current")


class _TnCardMarketingPartNumber_Type(TropicCardMarketingPartNumber):
    """Custom type tnCardMarketingPartNumber based on TropicCardMarketingPartNumber"""
    defaultValue = OctetString("")


_TnCardMarketingPartNumber_Type.__name__ = "TropicCardMarketingPartNumber"
_TnCardMarketingPartNumber_Object = MibTableColumn
tnCardMarketingPartNumber = _TnCardMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 7),
    _TnCardMarketingPartNumber_Type()
)
tnCardMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMarketingPartNumber.setStatus("current")


class _TnCardSWGenericLoadName_Type(TropicCardSWGenericLoadName):
    """Custom type tnCardSWGenericLoadName based on TropicCardSWGenericLoadName"""
    defaultValue = OctetString("")


_TnCardSWGenericLoadName_Type.__name__ = "TropicCardSWGenericLoadName"
_TnCardSWGenericLoadName_Object = MibTableColumn
tnCardSWGenericLoadName = _TnCardSWGenericLoadName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 8),
    _TnCardSWGenericLoadName_Type()
)
tnCardSWGenericLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSWGenericLoadName.setStatus("current")


class _TnCardHeight_Type(Integer32):
    """Custom type tnCardHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfHeight", 2),
          ("fullHeight", 3))
    )


_TnCardHeight_Type.__name__ = "Integer32"
_TnCardHeight_Object = MibTableColumn
tnCardHeight = _TnCardHeight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 10),
    _TnCardHeight_Type()
)
tnCardHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardHeight.setStatus("current")


class _TnCardWidth_Type(Integer32):
    """Custom type tnCardWidth based on Integer32"""
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
        *(("unknown", 1),
          ("singleWidth", 2),
          ("doubleWidth", 3),
          ("tripleWidth", 4))
    )


_TnCardWidth_Type.__name__ = "Integer32"
_TnCardWidth_Object = MibTableColumn
tnCardWidth = _TnCardWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 11),
    _TnCardWidth_Type()
)
tnCardWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardWidth.setStatus("current")
_TnCardTemperature_Type = Integer32
_TnCardTemperature_Object = MibTableColumn
tnCardTemperature = _TnCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 13),
    _TnCardTemperature_Type()
)
tnCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnCardTemperature.setUnits("Celsius")


class _TnCardHighTemperatureThresh_Type(Integer32):
    """Custom type tnCardHighTemperatureThresh based on Integer32"""
    defaultValue = 90


_TnCardHighTemperatureThresh_Type.__name__ = "Integer32"
_TnCardHighTemperatureThresh_Object = MibTableColumn
tnCardHighTemperatureThresh = _TnCardHighTemperatureThresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 14),
    _TnCardHighTemperatureThresh_Type()
)
tnCardHighTemperatureThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardHighTemperatureThresh.setStatus("current")
if mibBuilder.loadTexts:
    tnCardHighTemperatureThresh.setUnits("Celsius")


class _TnCardLowTemperatureThresh_Type(Integer32):
    """Custom type tnCardLowTemperatureThresh based on Integer32"""
    defaultValue = -5


_TnCardLowTemperatureThresh_Type.__name__ = "Integer32"
_TnCardLowTemperatureThresh_Object = MibTableColumn
tnCardLowTemperatureThresh = _TnCardLowTemperatureThresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 15),
    _TnCardLowTemperatureThresh_Type()
)
tnCardLowTemperatureThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLowTemperatureThresh.setStatus("current")
if mibBuilder.loadTexts:
    tnCardLowTemperatureThresh.setUnits("Celsius")


class _TnCardTemperatureTolerance_Type(Unsigned32):
    """Custom type tnCardTemperatureTolerance based on Unsigned32"""
    defaultValue = 3


_TnCardTemperatureTolerance_Type.__name__ = "Unsigned32"
_TnCardTemperatureTolerance_Object = MibTableColumn
tnCardTemperatureTolerance = _TnCardTemperatureTolerance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 16),
    _TnCardTemperatureTolerance_Type()
)
tnCardTemperatureTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardTemperatureTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tnCardTemperatureTolerance.setUnits("Celsius")
_TnCardStatusLEDColor_Type = TropicLEDColorType
_TnCardStatusLEDColor_Object = MibTableColumn
tnCardStatusLEDColor = _TnCardStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 17),
    _TnCardStatusLEDColor_Type()
)
tnCardStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatusLEDColor.setStatus("current")
_TnCardStatusLEDState_Type = TropicLEDStateType
_TnCardStatusLEDState_Object = MibTableColumn
tnCardStatusLEDState = _TnCardStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 18),
    _TnCardStatusLEDState_Type()
)
tnCardStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatusLEDState.setStatus("current")
_TnCardActivityLEDColor_Type = TropicLEDColorType
_TnCardActivityLEDColor_Object = MibTableColumn
tnCardActivityLEDColor = _TnCardActivityLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 19),
    _TnCardActivityLEDColor_Type()
)
tnCardActivityLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardActivityLEDColor.setStatus("current")
_TnCardActivityLEDState_Type = TropicLEDStateType
_TnCardActivityLEDState_Object = MibTableColumn
tnCardActivityLEDState = _TnCardActivityLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 20),
    _TnCardActivityLEDState_Type()
)
tnCardActivityLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardActivityLEDState.setStatus("current")


class _TnCardCompanyID_Type(SnmpAdminString):
    """Custom type tnCardCompanyID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardCompanyID_Type.__name__ = "SnmpAdminString"
_TnCardCompanyID_Object = MibTableColumn
tnCardCompanyID = _TnCardCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 21),
    _TnCardCompanyID_Type()
)
tnCardCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCompanyID.setStatus("current")


class _TnCardMnemonic_Type(SnmpAdminString):
    """Custom type tnCardMnemonic based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardMnemonic_Type.__name__ = "SnmpAdminString"
_TnCardMnemonic_Object = MibTableColumn
tnCardMnemonic = _TnCardMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 22),
    _TnCardMnemonic_Type()
)
tnCardMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMnemonic.setStatus("current")


class _TnCardSWPartNum_Type(SnmpAdminString):
    """Custom type tnCardSWPartNum based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardSWPartNum_Type.__name__ = "SnmpAdminString"
_TnCardSWPartNum_Object = MibTableColumn
tnCardSWPartNum = _TnCardSWPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 23),
    _TnCardSWPartNum_Type()
)
tnCardSWPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSWPartNum.setStatus("current")


class _TnCardDate_Type(SnmpAdminString):
    """Custom type tnCardDate based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardDate_Type.__name__ = "SnmpAdminString"
_TnCardDate_Object = MibTableColumn
tnCardDate = _TnCardDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 24),
    _TnCardDate_Type()
)
tnCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardDate.setStatus("current")


class _TnCardExtraData_Type(SnmpAdminString):
    """Custom type tnCardExtraData based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardExtraData_Type.__name__ = "SnmpAdminString"
_TnCardExtraData_Object = MibTableColumn
tnCardExtraData = _TnCardExtraData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 25),
    _TnCardExtraData_Type()
)
tnCardExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardExtraData.setStatus("current")
_TnCardAnyPortsInService_Type = TruthValue
_TnCardAnyPortsInService_Object = MibTableColumn
tnCardAnyPortsInService = _TnCardAnyPortsInService_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 27),
    _TnCardAnyPortsInService_Type()
)
tnCardAnyPortsInService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAnyPortsInService.setStatus("current")


class _TnCardLastBootedFwBundleVer_Type(SnmpAdminString):
    """Custom type tnCardLastBootedFwBundleVer based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardLastBootedFwBundleVer_Type.__name__ = "SnmpAdminString"
_TnCardLastBootedFwBundleVer_Object = MibTableColumn
tnCardLastBootedFwBundleVer = _TnCardLastBootedFwBundleVer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 28),
    _TnCardLastBootedFwBundleVer_Type()
)
tnCardLastBootedFwBundleVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLastBootedFwBundleVer.setStatus("current")


class _TnCardNextFwBundleVer_Type(SnmpAdminString):
    """Custom type tnCardNextFwBundleVer based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardNextFwBundleVer_Type.__name__ = "SnmpAdminString"
_TnCardNextFwBundleVer_Object = MibTableColumn
tnCardNextFwBundleVer = _TnCardNextFwBundleVer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 29),
    _TnCardNextFwBundleVer_Type()
)
tnCardNextFwBundleVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardNextFwBundleVer.setStatus("current")


class _TnCardFactoryID_Type(SnmpAdminString):
    """Custom type tnCardFactoryID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardFactoryID_Type.__name__ = "SnmpAdminString"
_TnCardFactoryID_Object = MibTableColumn
tnCardFactoryID = _TnCardFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 30),
    _TnCardFactoryID_Type()
)
tnCardFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardFactoryID.setStatus("current")


class _TnCardCapacity_Type(AluWdmCardCapacity):
    """Custom type tnCardCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnCardCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnCardCapacity_Object = MibTableColumn
tnCardCapacity = _TnCardCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 31),
    _TnCardCapacity_Type()
)
tnCardCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardCapacity.setStatus("current")


class _TnCardLACPSystemPriority_Type(Unsigned32):
    """Custom type tnCardLACPSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCardLACPSystemPriority_Type.__name__ = "Unsigned32"
_TnCardLACPSystemPriority_Object = MibTableColumn
tnCardLACPSystemPriority = _TnCardLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 32),
    _TnCardLACPSystemPriority_Type()
)
tnCardLACPSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLACPSystemPriority.setStatus("current")
_TnCardMaxPower_Type = Unsigned32
_TnCardMaxPower_Object = MibTableColumn
tnCardMaxPower = _TnCardMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 33),
    _TnCardMaxPower_Type()
)
tnCardMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnCardMaxPower.setUnits("milli-Watts")


class _TnCardEthOamCcmFaultMgntMode_Type(Integer32):
    """Custom type tnCardEthOamCcmFaultMgntMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 1),
          ("itu", 2))
    )


_TnCardEthOamCcmFaultMgntMode_Type.__name__ = "Integer32"
_TnCardEthOamCcmFaultMgntMode_Object = MibTableColumn
tnCardEthOamCcmFaultMgntMode = _TnCardEthOamCcmFaultMgntMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 34),
    _TnCardEthOamCcmFaultMgntMode_Type()
)
tnCardEthOamCcmFaultMgntMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardEthOamCcmFaultMgntMode.setStatus("current")


class _TnCardClkSwitch_Type(AluWdmWtClkValues):
    """Custom type tnCardClkSwitch based on AluWdmWtClkValues"""
    defaultValue = 1


_TnCardClkSwitch_Type.__name__ = "AluWdmWtClkValues"
_TnCardClkSwitch_Object = MibTableColumn
tnCardClkSwitch = _TnCardClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 35),
    _TnCardClkSwitch_Type()
)
tnCardClkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardClkSwitch.setStatus("current")
_TnCardRtrvClkSwitch_Type = AluWdmWtClkValues
_TnCardRtrvClkSwitch_Object = MibTableColumn
tnCardRtrvClkSwitch = _TnCardRtrvClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 36),
    _TnCardRtrvClkSwitch_Type()
)
tnCardRtrvClkSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRtrvClkSwitch.setStatus("current")


class _TnCardWtClkMeasureValues_Type(OctetString):
    """Custom type tnCardWtClkMeasureValues based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnCardWtClkMeasureValues_Type.__name__ = "OctetString"
_TnCardWtClkMeasureValues_Object = MibTableColumn
tnCardWtClkMeasureValues = _TnCardWtClkMeasureValues_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 37),
    _TnCardWtClkMeasureValues_Type()
)
tnCardWtClkMeasureValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardWtClkMeasureValues.setStatus("current")
_TnCardAssemblyTable_Object = MibTable
tnCardAssemblyTable = _TnCardAssemblyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnCardAssemblyTable.setStatus("current")
_TnCardAssemblyEntry_Object = MibTableRow
tnCardAssemblyEntry = _TnCardAssemblyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1)
)
tnCardAssemblyEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-CARD-MIB", "tnCardAssemblyIndex"),
)
if mibBuilder.loadTexts:
    tnCardAssemblyEntry.setStatus("current")


class _TnCardAssemblyIndex_Type(Integer32):
    """Custom type tnCardAssemblyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TnCardAssemblyIndex_Type.__name__ = "Integer32"
_TnCardAssemblyIndex_Object = MibTableColumn
tnCardAssemblyIndex = _TnCardAssemblyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 1),
    _TnCardAssemblyIndex_Type()
)
tnCardAssemblyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCardAssemblyIndex.setStatus("current")


class _TnCardAssemblyName_Type(SnmpAdminString):
    """Custom type tnCardAssemblyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCardAssemblyName_Type.__name__ = "SnmpAdminString"
_TnCardAssemblyName_Object = MibTableColumn
tnCardAssemblyName = _TnCardAssemblyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 2),
    _TnCardAssemblyName_Type()
)
tnCardAssemblyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyName.setStatus("current")
_TnCardAssemblyCLEI_Type = TropicCardCLEI
_TnCardAssemblyCLEI_Object = MibTableColumn
tnCardAssemblyCLEI = _TnCardAssemblyCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 3),
    _TnCardAssemblyCLEI_Type()
)
tnCardAssemblyCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyCLEI.setStatus("current")
_TnCardAssemblyHFD_Type = TropicCardHFD
_TnCardAssemblyHFD_Object = MibTableColumn
tnCardAssemblyHFD = _TnCardAssemblyHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 4),
    _TnCardAssemblyHFD_Type()
)
tnCardAssemblyHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyHFD.setStatus("current")
_TnCardAssemblySerialNumber_Type = TropicCardSerialNumber
_TnCardAssemblySerialNumber_Object = MibTableColumn
tnCardAssemblySerialNumber = _TnCardAssemblySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 5),
    _TnCardAssemblySerialNumber_Type()
)
tnCardAssemblySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblySerialNumber.setStatus("current")
_TnCardAssemblyManufacturingPartNumber_Type = TropicCardManufacturingPartNumber
_TnCardAssemblyManufacturingPartNumber_Object = MibTableColumn
tnCardAssemblyManufacturingPartNumber = _TnCardAssemblyManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 6),
    _TnCardAssemblyManufacturingPartNumber_Type()
)
tnCardAssemblyManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyManufacturingPartNumber.setStatus("current")
_TnCardAssemblyMarketingPartNumber_Type = TropicCardMarketingPartNumber
_TnCardAssemblyMarketingPartNumber_Object = MibTableColumn
tnCardAssemblyMarketingPartNumber = _TnCardAssemblyMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 7),
    _TnCardAssemblyMarketingPartNumber_Type()
)
tnCardAssemblyMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyMarketingPartNumber.setStatus("current")

# Managed Objects groups

tnCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 1)
)
tnCardScalarsGroup.setObjects(
    ("TROPIC-CARD-MIB", "tnCardTotal")
)
if mibBuilder.loadTexts:
    tnCardScalarsGroup.setStatus("current")

tnCardTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 2)
)
tnCardTableGroup.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardName"),
        ("TROPIC-CARD-MIB", "tnCardDescr"),
        ("TROPIC-CARD-MIB", "tnCardCLEI"),
        ("TROPIC-CARD-MIB", "tnCardHFD"),
        ("TROPIC-CARD-MIB", "tnCardSerialNumber"),
        ("TROPIC-CARD-MIB", "tnCardManufacturingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardMarketingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardSWGenericLoadName"),
        ("TROPIC-CARD-MIB", "tnCardHeight"),
        ("TROPIC-CARD-MIB", "tnCardWidth"),
        ("TROPIC-CARD-MIB", "tnCardTemperature"),
        ("TROPIC-CARD-MIB", "tnCardHighTemperatureThresh"),
        ("TROPIC-CARD-MIB", "tnCardLowTemperatureThresh"),
        ("TROPIC-CARD-MIB", "tnCardTemperatureTolerance"),
        ("TROPIC-CARD-MIB", "tnCardStatusLEDColor"),
        ("TROPIC-CARD-MIB", "tnCardStatusLEDState"),
        ("TROPIC-CARD-MIB", "tnCardActivityLEDColor"),
        ("TROPIC-CARD-MIB", "tnCardActivityLEDState"),
        ("TROPIC-CARD-MIB", "tnCardCompanyID"),
        ("TROPIC-CARD-MIB", "tnCardMnemonic"),
        ("TROPIC-CARD-MIB", "tnCardSWPartNum"),
        ("TROPIC-CARD-MIB", "tnCardDate"),
        ("TROPIC-CARD-MIB", "tnCardExtraData"),
        ("TROPIC-CARD-MIB", "tnCardAnyPortsInService"),
        ("TROPIC-CARD-MIB", "tnCardLastBootedFwBundleVer"),
        ("TROPIC-CARD-MIB", "tnCardNextFwBundleVer"),
        ("TROPIC-CARD-MIB", "tnCardFactoryID"),
        ("TROPIC-CARD-MIB", "tnCardCapacity"),
        ("TROPIC-CARD-MIB", "tnCardLACPSystemPriority"),
        ("TROPIC-CARD-MIB", "tnCardMaxPower"),
        ("TROPIC-CARD-MIB", "tnCardEthOamCcmFaultMgntMode"),
        ("TROPIC-CARD-MIB", "tnCardClkSwitch"),
        ("TROPIC-CARD-MIB", "tnCardRtrvClkSwitch"),
        ("TROPIC-CARD-MIB", "tnCardWtClkMeasureValues"))
)
if mibBuilder.loadTexts:
    tnCardTableGroup.setStatus("current")

tnCardAssemblyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 3)
)
tnCardAssemblyTableGroup.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardAssemblyName"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyCLEI"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyHFD"),
        ("TROPIC-CARD-MIB", "tnCardAssemblySerialNumber"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyManufacturingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyMarketingPartNumber"))
)
if mibBuilder.loadTexts:
    tnCardAssemblyTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnCardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 2, 1)
)
tnCardCompliance.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardScalarsGroup"),
        ("TROPIC-CARD-MIB", "tnCardTableGroup"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyTableGroup"))
)
if mibBuilder.loadTexts:
    tnCardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-CARD-MIB",
    **{"tnCardMibModule": tnCardMibModule,
       "tnCardConf": tnCardConf,
       "tnCardGroups": tnCardGroups,
       "tnCardScalarsGroup": tnCardScalarsGroup,
       "tnCardTableGroup": tnCardTableGroup,
       "tnCardAssemblyTableGroup": tnCardAssemblyTableGroup,
       "tnCardCompliances": tnCardCompliances,
       "tnCardCompliance": tnCardCompliance,
       "tnCardObjs": tnCardObjs,
       "tnCardBasics": tnCardBasics,
       "tnCardTotal": tnCardTotal,
       "tnCardTable": tnCardTable,
       "tnCardEntry": tnCardEntry,
       "tnCardName": tnCardName,
       "tnCardDescr": tnCardDescr,
       "tnCardCLEI": tnCardCLEI,
       "tnCardHFD": tnCardHFD,
       "tnCardSerialNumber": tnCardSerialNumber,
       "tnCardManufacturingPartNumber": tnCardManufacturingPartNumber,
       "tnCardMarketingPartNumber": tnCardMarketingPartNumber,
       "tnCardSWGenericLoadName": tnCardSWGenericLoadName,
       "tnCardHeight": tnCardHeight,
       "tnCardWidth": tnCardWidth,
       "tnCardTemperature": tnCardTemperature,
       "tnCardHighTemperatureThresh": tnCardHighTemperatureThresh,
       "tnCardLowTemperatureThresh": tnCardLowTemperatureThresh,
       "tnCardTemperatureTolerance": tnCardTemperatureTolerance,
       "tnCardStatusLEDColor": tnCardStatusLEDColor,
       "tnCardStatusLEDState": tnCardStatusLEDState,
       "tnCardActivityLEDColor": tnCardActivityLEDColor,
       "tnCardActivityLEDState": tnCardActivityLEDState,
       "tnCardCompanyID": tnCardCompanyID,
       "tnCardMnemonic": tnCardMnemonic,
       "tnCardSWPartNum": tnCardSWPartNum,
       "tnCardDate": tnCardDate,
       "tnCardExtraData": tnCardExtraData,
       "tnCardAnyPortsInService": tnCardAnyPortsInService,
       "tnCardLastBootedFwBundleVer": tnCardLastBootedFwBundleVer,
       "tnCardNextFwBundleVer": tnCardNextFwBundleVer,
       "tnCardFactoryID": tnCardFactoryID,
       "tnCardCapacity": tnCardCapacity,
       "tnCardLACPSystemPriority": tnCardLACPSystemPriority,
       "tnCardMaxPower": tnCardMaxPower,
       "tnCardEthOamCcmFaultMgntMode": tnCardEthOamCcmFaultMgntMode,
       "tnCardClkSwitch": tnCardClkSwitch,
       "tnCardRtrvClkSwitch": tnCardRtrvClkSwitch,
       "tnCardWtClkMeasureValues": tnCardWtClkMeasureValues,
       "tnCardAssemblyTable": tnCardAssemblyTable,
       "tnCardAssemblyEntry": tnCardAssemblyEntry,
       "tnCardAssemblyIndex": tnCardAssemblyIndex,
       "tnCardAssemblyName": tnCardAssemblyName,
       "tnCardAssemblyCLEI": tnCardAssemblyCLEI,
       "tnCardAssemblyHFD": tnCardAssemblyHFD,
       "tnCardAssemblySerialNumber": tnCardAssemblySerialNumber,
       "tnCardAssemblyManufacturingPartNumber": tnCardAssemblyManufacturingPartNumber,
       "tnCardAssemblyMarketingPartNumber": tnCardAssemblyMarketingPartNumber}
)
