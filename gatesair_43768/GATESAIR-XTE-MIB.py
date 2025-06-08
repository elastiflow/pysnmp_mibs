# SNMP MIB module (GATESAIR-XTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gatesair_43768/GATESAIR-XTE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:36 2025
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

(eventCount,
 eventDescription,
 eventPriority,
 eventTimeStamp) = mibBuilder.importSymbols(
    "GATESAIR-COMMONVARBINDS-MIB",
    "eventCount",
    "eventDescription",
    "eventPriority",
    "eventTimeStamp")

(exciter,
 transmissionMibs) = mibBuilder.importSymbols(
    "GATESAIR-SMI",
    "exciter",
    "transmissionMibs")

(EnabledDisabled,
 SNMPEventType,
 YesNo) = mibBuilder.importSymbols(
    "GATESAIR-TC",
    "EnabledDisabled",
    "SNMPEventType",
    "YesNo")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

xteBaseMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 2, 4)
)
if mibBuilder.loadTexts:
    xteBaseMibModule.setRevisions(
        ("2016-09-22 11:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class XteSummaryStatus(TextualConvention, Integer32):
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
        *(("ok", 1),
          ("fault", 2),
          ("warning", 3),
          ("na", 4))
    )



class XteInputSelection(TextualConvention, Integer32):
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



class XteInputStatus(TextualConvention, Integer32):
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
        *(("ok", 1),
          ("missing", 2),
          ("error", 3),
          ("none", 4))
    )



class XteInputMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("autoReturn", 3))
    )



class XteAutoManual(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )



class XteRtacMode(TextualConvention, Integer32):
    status = "current"
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
        *(("na", 1),
          ("adapt", 2),
          ("bypass", 3),
          ("hold", 4),
          ("stored", 5))
    )



class XteRtacModeAfterACLoss(TextualConvention, Integer32):
    status = "current"
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
        *(("adapt", 1),
          ("bypass", 2),
          ("hold", 3),
          ("stored", 4),
          ("current", 5))
    )



class XteNetworkDuplex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )



class XteFtrReferenceStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2),
          ("warning", 3))
    )



class XtePllStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("notlocked", 2))
    )



class XteInputNetworkMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )



# MIB Managed Objects in the order of their OIDs

_XteBaseMib_ObjectIdentity = ObjectIdentity
xteBaseMib = _XteBaseMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    xteBaseMib.setStatus("current")
_XteEvents_ObjectIdentity = ObjectIdentity
xteEvents = _XteEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1)
)
_XteEventsV2_ObjectIdentity = ObjectIdentity
xteEventsV2 = _XteEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0)
)
_XteObjects_ObjectIdentity = ObjectIdentity
xteObjects = _XteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2)
)


class _XteMibRevision_Type(OctetString):
    """Custom type xteMibRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteMibRevision_Type.__name__ = "OctetString"
_XteMibRevision_Object = MibScalar
xteMibRevision = _XteMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 1),
    _XteMibRevision_Type()
)
xteMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteMibRevision.setStatus("current")
_XteVersion_ObjectIdentity = ObjectIdentity
xteVersion = _XteVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2)
)
_XteVerSoftware_ObjectIdentity = ObjectIdentity
xteVerSoftware = _XteVerSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1)
)


class _XteVerSwPartNumber_Type(OctetString):
    """Custom type xteVerSwPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwPartNumber_Type.__name__ = "OctetString"
_XteVerSwPartNumber_Object = MibScalar
xteVerSwPartNumber = _XteVerSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 1),
    _XteVerSwPartNumber_Type()
)
xteVerSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwPartNumber.setStatus("current")


class _XteVerSwRev_Type(OctetString):
    """Custom type xteVerSwRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwRev_Type.__name__ = "OctetString"
_XteVerSwRev_Object = MibScalar
xteVerSwRev = _XteVerSwRev_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 2),
    _XteVerSwRev_Type()
)
xteVerSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwRev.setStatus("current")


class _XteVerSwUboot_Type(OctetString):
    """Custom type xteVerSwUboot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwUboot_Type.__name__ = "OctetString"
_XteVerSwUboot_Object = MibScalar
xteVerSwUboot = _XteVerSwUboot_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 3),
    _XteVerSwUboot_Type()
)
xteVerSwUboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwUboot.setStatus("current")


class _XteVerSwWebboot_Type(OctetString):
    """Custom type xteVerSwWebboot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwWebboot_Type.__name__ = "OctetString"
_XteVerSwWebboot_Object = MibScalar
xteVerSwWebboot = _XteVerSwWebboot_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 4),
    _XteVerSwWebboot_Type()
)
xteVerSwWebboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwWebboot.setStatus("current")


class _XteVerSwXtmod_Type(OctetString):
    """Custom type xteVerSwXtmod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwXtmod_Type.__name__ = "OctetString"
_XteVerSwXtmod_Object = MibScalar
xteVerSwXtmod = _XteVerSwXtmod_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 5),
    _XteVerSwXtmod_Type()
)
xteVerSwXtmod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwXtmod.setStatus("current")


class _XteVerSwLinux_Type(OctetString):
    """Custom type xteVerSwLinux based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwLinux_Type.__name__ = "OctetString"
_XteVerSwLinux_Object = MibScalar
xteVerSwLinux = _XteVerSwLinux_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 6),
    _XteVerSwLinux_Type()
)
xteVerSwLinux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwLinux.setStatus("current")


class _XteVerSwDevTree_Type(OctetString):
    """Custom type xteVerSwDevTree based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwDevTree_Type.__name__ = "OctetString"
_XteVerSwDevTree_Object = MibScalar
xteVerSwDevTree = _XteVerSwDevTree_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 7),
    _XteVerSwDevTree_Type()
)
xteVerSwDevTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwDevTree.setStatus("current")


class _XteVerSwFpga1_Type(OctetString):
    """Custom type xteVerSwFpga1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwFpga1_Type.__name__ = "OctetString"
_XteVerSwFpga1_Object = MibScalar
xteVerSwFpga1 = _XteVerSwFpga1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 8),
    _XteVerSwFpga1_Type()
)
xteVerSwFpga1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwFpga1.setStatus("current")


class _XteVerSwFpga2_Type(OctetString):
    """Custom type xteVerSwFpga2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwFpga2_Type.__name__ = "OctetString"
_XteVerSwFpga2_Object = MibScalar
xteVerSwFpga2 = _XteVerSwFpga2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 9),
    _XteVerSwFpga2_Type()
)
xteVerSwFpga2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwFpga2.setStatus("current")


class _XteVerSwCpld_Type(OctetString):
    """Custom type xteVerSwCpld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XteVerSwCpld_Type.__name__ = "OctetString"
_XteVerSwCpld_Object = MibScalar
xteVerSwCpld = _XteVerSwCpld_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 1, 10),
    _XteVerSwCpld_Type()
)
xteVerSwCpld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerSwCpld.setStatus("current")
_XteVerHardware_ObjectIdentity = ObjectIdentity
xteVerHardware = _XteVerHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 2)
)


class _XteVerHwModulator_Type(OctetString):
    """Custom type xteVerHwModulator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XteVerHwModulator_Type.__name__ = "OctetString"
_XteVerHwModulator_Object = MibScalar
xteVerHwModulator = _XteVerHwModulator_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 2, 1),
    _XteVerHwModulator_Type()
)
xteVerHwModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerHwModulator.setStatus("current")


class _XteVerHwBackplane_Type(OctetString):
    """Custom type xteVerHwBackplane based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XteVerHwBackplane_Type.__name__ = "OctetString"
_XteVerHwBackplane_Object = MibScalar
xteVerHwBackplane = _XteVerHwBackplane_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 2, 2),
    _XteVerHwBackplane_Type()
)
xteVerHwBackplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerHwBackplane.setStatus("current")


class _XteVerHwPwrSupplyCtrl_Type(OctetString):
    """Custom type xteVerHwPwrSupplyCtrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XteVerHwPwrSupplyCtrl_Type.__name__ = "OctetString"
_XteVerHwPwrSupplyCtrl_Object = MibScalar
xteVerHwPwrSupplyCtrl = _XteVerHwPwrSupplyCtrl_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 2, 3),
    _XteVerHwPwrSupplyCtrl_Type()
)
xteVerHwPwrSupplyCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerHwPwrSupplyCtrl.setStatus("current")


class _XteVerHwPwrAmp_Type(OctetString):
    """Custom type xteVerHwPwrAmp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XteVerHwPwrAmp_Type.__name__ = "OctetString"
_XteVerHwPwrAmp_Object = MibScalar
xteVerHwPwrAmp = _XteVerHwPwrAmp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 2, 2, 4),
    _XteVerHwPwrAmp_Type()
)
xteVerHwPwrAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteVerHwPwrAmp.setStatus("current")
_XteGeneral_ObjectIdentity = ObjectIdentity
xteGeneral = _XteGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3)
)


class _XteActive_Type(Integer32):
    """Custom type xteActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2))
    )


_XteActive_Type.__name__ = "Integer32"
_XteActive_Object = MibScalar
xteActive = _XteActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 1),
    _XteActive_Type()
)
xteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteActive.setStatus("current")
_XteStatus_Type = XteSummaryStatus
_XteStatus_Object = MibScalar
xteStatus = _XteStatus_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 2),
    _XteStatus_Type()
)
xteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteStatus.setStatus("current")


class _XteStationName_Type(OctetString):
    """Custom type xteStationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_XteStationName_Type.__name__ = "OctetString"
_XteStationName_Object = MibScalar
xteStationName = _XteStationName_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 3),
    _XteStationName_Type()
)
xteStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteStationName.setStatus("current")


class _XteModelNumber_Type(OctetString):
    """Custom type xteModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_XteModelNumber_Type.__name__ = "OctetString"
_XteModelNumber_Object = MibScalar
xteModelNumber = _XteModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 4),
    _XteModelNumber_Type()
)
xteModelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteModelNumber.setStatus("current")


class _XteSerialNumber_Type(OctetString):
    """Custom type xteSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteSerialNumber_Type.__name__ = "OctetString"
_XteSerialNumber_Object = MibScalar
xteSerialNumber = _XteSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 5),
    _XteSerialNumber_Type()
)
xteSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteSerialNumber.setStatus("current")
_XteDateAndTime_ObjectIdentity = ObjectIdentity
xteDateAndTime = _XteDateAndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6)
)


class _XteTimeOfDay_Type(OctetString):
    """Custom type xteTimeOfDay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteTimeOfDay_Type.__name__ = "OctetString"
_XteTimeOfDay_Object = MibScalar
xteTimeOfDay = _XteTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 1),
    _XteTimeOfDay_Type()
)
xteTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteTimeOfDay.setStatus("current")
_XteUTCOffset_Type = Integer32
_XteUTCOffset_Object = MibScalar
xteUTCOffset = _XteUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 2),
    _XteUTCOffset_Type()
)
xteUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteUTCOffset.setStatus("current")


class _XteTimeSource_Type(Integer32):
    """Custom type xteTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 1),
          ("disabled", 2),
          ("gps", 3))
    )


_XteTimeSource_Type.__name__ = "Integer32"
_XteTimeSource_Object = MibScalar
xteTimeSource = _XteTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 3),
    _XteTimeSource_Type()
)
xteTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteTimeSource.setStatus("current")


class _XteNTPServerName1_Type(OctetString):
    """Custom type xteNTPServerName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteNTPServerName1_Type.__name__ = "OctetString"
_XteNTPServerName1_Object = MibScalar
xteNTPServerName1 = _XteNTPServerName1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 4),
    _XteNTPServerName1_Type()
)
xteNTPServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteNTPServerName1.setStatus("current")


class _XteNTPServerName2_Type(OctetString):
    """Custom type xteNTPServerName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteNTPServerName2_Type.__name__ = "OctetString"
_XteNTPServerName2_Object = MibScalar
xteNTPServerName2 = _XteNTPServerName2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 5),
    _XteNTPServerName2_Type()
)
xteNTPServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteNTPServerName2.setStatus("current")


class _XteNTPServerName3_Type(OctetString):
    """Custom type xteNTPServerName3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteNTPServerName3_Type.__name__ = "OctetString"
_XteNTPServerName3_Object = MibScalar
xteNTPServerName3 = _XteNTPServerName3_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 6),
    _XteNTPServerName3_Type()
)
xteNTPServerName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteNTPServerName3.setStatus("current")


class _XteNTPServerName4_Type(OctetString):
    """Custom type xteNTPServerName4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteNTPServerName4_Type.__name__ = "OctetString"
_XteNTPServerName4_Object = MibScalar
xteNTPServerName4 = _XteNTPServerName4_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 7),
    _XteNTPServerName4_Type()
)
xteNTPServerName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteNTPServerName4.setStatus("current")


class _XteNTPServerName5_Type(OctetString):
    """Custom type xteNTPServerName5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XteNTPServerName5_Type.__name__ = "OctetString"
_XteNTPServerName5_Object = MibScalar
xteNTPServerName5 = _XteNTPServerName5_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 3, 6, 8),
    _XteNTPServerName5_Type()
)
xteNTPServerName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteNTPServerName5.setStatus("current")
_XteInput_ObjectIdentity = ObjectIdentity
xteInput = _XteInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5)
)


class _XteInputPowerOn_Type(Integer32):
    """Custom type xteInputPowerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_XteInputPowerOn_Type.__name__ = "Integer32"
_XteInputPowerOn_Object = MibScalar
xteInputPowerOn = _XteInputPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 1),
    _XteInputPowerOn_Type()
)
xteInputPowerOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputPowerOn.setStatus("current")
_XteInputActive_Type = XteInputSelection
_XteInputActive_Object = MibScalar
xteInputActive = _XteInputActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 2),
    _XteInputActive_Type()
)
xteInputActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputActive.setStatus("current")
_XteInputStatusPrimary_Type = XteInputStatus
_XteInputStatusPrimary_Object = MibScalar
xteInputStatusPrimary = _XteInputStatusPrimary_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 3),
    _XteInputStatusPrimary_Type()
)
xteInputStatusPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteInputStatusPrimary.setStatus("current")
_XteInputStatusSecondary_Type = XteInputStatus
_XteInputStatusSecondary_Object = MibScalar
xteInputStatusSecondary = _XteInputStatusSecondary_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 4),
    _XteInputStatusSecondary_Type()
)
xteInputStatusSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteInputStatusSecondary.setStatus("current")
_XteInputMuteOnTsLoss_Type = YesNo
_XteInputMuteOnTsLoss_Object = MibScalar
xteInputMuteOnTsLoss = _XteInputMuteOnTsLoss_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 5),
    _XteInputMuteOnTsLoss_Type()
)
xteInputMuteOnTsLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputMuteOnTsLoss.setStatus("current")
_XteInputSwitchMode_Type = XteInputMode
_XteInputSwitchMode_Object = MibScalar
xteInputSwitchMode = _XteInputSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 6),
    _XteInputSwitchMode_Type()
)
xteInputSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputSwitchMode.setStatus("current")
_XteInputSwitchTimeout_Type = Integer32
_XteInputSwitchTimeout_Object = MibScalar
xteInputSwitchTimeout = _XteInputSwitchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 7),
    _XteInputSwitchTimeout_Type()
)
xteInputSwitchTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputSwitchTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xteInputSwitchTimeout.setUnits("S")
_XteInputSwitchElapsedTime_Type = Integer32
_XteInputSwitchElapsedTime_Object = MibScalar
xteInputSwitchElapsedTime = _XteInputSwitchElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 8),
    _XteInputSwitchElapsedTime_Type()
)
xteInputSwitchElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteInputSwitchElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    xteInputSwitchElapsedTime.setUnits("S")
_XteInputSwitchCountMax_Type = Integer32
_XteInputSwitchCountMax_Object = MibScalar
xteInputSwitchCountMax = _XteInputSwitchCountMax_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 9),
    _XteInputSwitchCountMax_Type()
)
xteInputSwitchCountMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputSwitchCountMax.setStatus("current")
_XteInputSwitchCountCurrent_Type = Integer32
_XteInputSwitchCountCurrent_Object = MibScalar
xteInputSwitchCountCurrent = _XteInputSwitchCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 10),
    _XteInputSwitchCountCurrent_Type()
)
xteInputSwitchCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteInputSwitchCountCurrent.setStatus("current")
_XteInputSwitchCountReset_Type = Integer32
_XteInputSwitchCountReset_Object = MibScalar
xteInputSwitchCountReset = _XteInputSwitchCountReset_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 5, 11),
    _XteInputSwitchCountReset_Type()
)
xteInputSwitchCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputSwitchCountReset.setStatus("current")
_XteOutput_ObjectIdentity = ObjectIdentity
xteOutput = _XteOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6)
)


class _XteOutputPowerLimit_Type(Integer32):
    """Custom type xteOutputPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 110),
    )


_XteOutputPowerLimit_Type.__name__ = "Integer32"
_XteOutputPowerLimit_Object = MibScalar
xteOutputPowerLimit = _XteOutputPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 1),
    _XteOutputPowerLimit_Type()
)
xteOutputPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputPowerLimit.setUnits("mW")


class _XteOutputPowerCutoff_Type(Integer32):
    """Custom type xteOutputPowerCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XteOutputPowerCutoff_Type.__name__ = "Integer32"
_XteOutputPowerCutoff_Object = MibScalar
xteOutputPowerCutoff = _XteOutputPowerCutoff_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 2),
    _XteOutputPowerCutoff_Type()
)
xteOutputPowerCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputPowerCutoff.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputPowerCutoff.setUnits("mW")


class _XteOutputFoldbackLow_Type(Integer32):
    """Custom type xteOutputFoldbackLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_XteOutputFoldbackLow_Type.__name__ = "Integer32"
_XteOutputFoldbackLow_Object = MibScalar
xteOutputFoldbackLow = _XteOutputFoldbackLow_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 3),
    _XteOutputFoldbackLow_Type()
)
xteOutputFoldbackLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputFoldbackLow.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputFoldbackLow.setUnits("mV")


class _XteOutputFoldbackHigh_Type(Integer32):
    """Custom type xteOutputFoldbackHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_XteOutputFoldbackHigh_Type.__name__ = "Integer32"
_XteOutputFoldbackHigh_Object = MibScalar
xteOutputFoldbackHigh = _XteOutputFoldbackHigh_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 4),
    _XteOutputFoldbackHigh_Type()
)
xteOutputFoldbackHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputFoldbackHigh.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputFoldbackHigh.setUnits("mV")


class _XteOutputFoldbackMax_Type(Integer32):
    """Custom type xteOutputFoldbackMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XteOutputFoldbackMax_Type.__name__ = "Integer32"
_XteOutputFoldbackMax_Object = MibScalar
xteOutputFoldbackMax = _XteOutputFoldbackMax_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 5),
    _XteOutputFoldbackMax_Type()
)
xteOutputFoldbackMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputFoldbackMax.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputFoldbackMax.setUnits("%")
_XteOutputPaGain_Type = Integer32
_XteOutputPaGain_Object = MibScalar
xteOutputPaGain = _XteOutputPaGain_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 6),
    _XteOutputPaGain_Type()
)
xteOutputPaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteOutputPaGain.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputPaGain.setUnits("0.1 dB")
_XteOutputLevelInput_Type = Integer32
_XteOutputLevelInput_Object = MibScalar
xteOutputLevelInput = _XteOutputLevelInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 7),
    _XteOutputLevelInput_Type()
)
xteOutputLevelInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteOutputLevelInput.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputLevelInput.setUnits("millidB")
_XteOutputLevelOutput_Type = Integer32
_XteOutputLevelOutput_Object = MibScalar
xteOutputLevelOutput = _XteOutputLevelOutput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 8),
    _XteOutputLevelOutput_Type()
)
xteOutputLevelOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputLevelOutput.setStatus("current")
if mibBuilder.loadTexts:
    xteOutputLevelOutput.setUnits("mW")
_XteOutputPowerPresent_Type = YesNo
_XteOutputPowerPresent_Object = MibScalar
xteOutputPowerPresent = _XteOutputPowerPresent_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 9),
    _XteOutputPowerPresent_Type()
)
xteOutputPowerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteOutputPowerPresent.setStatus("current")
_XteOutputMute_Type = YesNo
_XteOutputMute_Object = MibScalar
xteOutputMute = _XteOutputMute_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 6, 10),
    _XteOutputMute_Type()
)
xteOutputMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputMute.setStatus("current")
_XteRtac_ObjectIdentity = ObjectIdentity
xteRtac = _XteRtac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7)
)
_XteRtacSetup_ObjectIdentity = ObjectIdentity
xteRtacSetup = _XteRtacSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 1)
)
_XteRtacSetupPeakReductionMode_Type = XteAutoManual
_XteRtacSetupPeakReductionMode_Object = MibScalar
xteRtacSetupPeakReductionMode = _XteRtacSetupPeakReductionMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 1, 1),
    _XteRtacSetupPeakReductionMode_Type()
)
xteRtacSetupPeakReductionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacSetupPeakReductionMode.setStatus("current")
_XteRtacSetupNonLinearRange_Type = Integer32
_XteRtacSetupNonLinearRange_Object = MibScalar
xteRtacSetupNonLinearRange = _XteRtacSetupNonLinearRange_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 1, 2),
    _XteRtacSetupNonLinearRange_Type()
)
xteRtacSetupNonLinearRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacSetupNonLinearRange.setStatus("current")
if mibBuilder.loadTexts:
    xteRtacSetupNonLinearRange.setUnits("dB(*0.1)")
_XteRtacSetupMaxCrestFactor_Type = Integer32
_XteRtacSetupMaxCrestFactor_Object = MibScalar
xteRtacSetupMaxCrestFactor = _XteRtacSetupMaxCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 1, 3),
    _XteRtacSetupMaxCrestFactor_Type()
)
xteRtacSetupMaxCrestFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacSetupMaxCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    xteRtacSetupMaxCrestFactor.setUnits("dB(*0.1)")
_XteRtacTable_Object = MibTable
xteRtacTable = _XteRtacTable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    xteRtacTable.setStatus("current")
_XteRtacEntry_Object = MibTableRow
xteRtacEntry = _XteRtacEntry_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1)
)
xteRtacEntry.setIndexNames(
    (0, "GATESAIR-XTE-MIB", "xteRtacIndex"),
)
if mibBuilder.loadTexts:
    xteRtacEntry.setStatus("current")


class _XteRtacIndex_Type(Integer32):
    """Custom type xteRtacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linear", 1),
          ("nonlinear", 2))
    )


_XteRtacIndex_Type.__name__ = "Integer32"
_XteRtacIndex_Object = MibTableColumn
xteRtacIndex = _XteRtacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1, 1),
    _XteRtacIndex_Type()
)
xteRtacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteRtacIndex.setStatus("current")
_XteRtacOpMode_Type = XteRtacMode
_XteRtacOpMode_Object = MibTableColumn
xteRtacOpMode = _XteRtacOpMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1, 2),
    _XteRtacOpMode_Type()
)
xteRtacOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacOpMode.setStatus("current")
_XteRtacSuccess_Type = Integer32
_XteRtacSuccess_Object = MibTableColumn
xteRtacSuccess = _XteRtacSuccess_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1, 3),
    _XteRtacSuccess_Type()
)
xteRtacSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteRtacSuccess.setStatus("current")
_XteRtacAttempts_Type = Integer32
_XteRtacAttempts_Object = MibTableColumn
xteRtacAttempts = _XteRtacAttempts_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1, 4),
    _XteRtacAttempts_Type()
)
xteRtacAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteRtacAttempts.setStatus("current")
_XteRtacOpModeAfterAcLoss_Type = XteRtacModeAfterACLoss
_XteRtacOpModeAfterAcLoss_Object = MibTableColumn
xteRtacOpModeAfterAcLoss = _XteRtacOpModeAfterAcLoss_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 2, 1, 5),
    _XteRtacOpModeAfterAcLoss_Type()
)
xteRtacOpModeAfterAcLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacOpModeAfterAcLoss.setStatus("current")
_XteRtacEnabled_Type = YesNo
_XteRtacEnabled_Object = MibScalar
xteRtacEnabled = _XteRtacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 7, 3),
    _XteRtacEnabled_Type()
)
xteRtacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacEnabled.setStatus("current")
_XtePowerSupplies_ObjectIdentity = ObjectIdentity
xtePowerSupplies = _XtePowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 8)
)
_XtePwrSupplyController_Type = XteSummaryStatus
_XtePwrSupplyController_Object = MibScalar
xtePwrSupplyController = _XtePwrSupplyController_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 8, 1),
    _XtePwrSupplyController_Type()
)
xtePwrSupplyController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtePwrSupplyController.setStatus("current")
_XtePwrSupplyPwrAmp_Type = XteSummaryStatus
_XtePwrSupplyPwrAmp_Object = MibScalar
xtePwrSupplyPwrAmp = _XtePwrSupplyPwrAmp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 8, 2),
    _XtePwrSupplyPwrAmp_Type()
)
xtePwrSupplyPwrAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtePwrSupplyPwrAmp.setStatus("current")
_XtePwrSupplyModulator_Type = XteSummaryStatus
_XtePwrSupplyModulator_Object = MibScalar
xtePwrSupplyModulator = _XtePwrSupplyModulator_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 8, 3),
    _XtePwrSupplyModulator_Type()
)
xtePwrSupplyModulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtePwrSupplyModulator.setStatus("current")
_XteCooling_ObjectIdentity = ObjectIdentity
xteCooling = _XteCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9)
)
_XteCoolingTempAmbient_Type = Integer32
_XteCoolingTempAmbient_Object = MibScalar
xteCoolingTempAmbient = _XteCoolingTempAmbient_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 1),
    _XteCoolingTempAmbient_Type()
)
xteCoolingTempAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingTempAmbient.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingTempAmbient.setUnits("deg C")
_XteCoolingTempPwrAmp_Type = Integer32
_XteCoolingTempPwrAmp_Object = MibScalar
xteCoolingTempPwrAmp = _XteCoolingTempPwrAmp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 2),
    _XteCoolingTempPwrAmp_Type()
)
xteCoolingTempPwrAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingTempPwrAmp.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingTempPwrAmp.setUnits("deg C")
_XteCoolingTempFpga1_Type = Integer32
_XteCoolingTempFpga1_Object = MibScalar
xteCoolingTempFpga1 = _XteCoolingTempFpga1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 3),
    _XteCoolingTempFpga1_Type()
)
xteCoolingTempFpga1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingTempFpga1.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingTempFpga1.setUnits("deg C")
_XteCoolingTempFpga2_Type = Integer32
_XteCoolingTempFpga2_Object = MibScalar
xteCoolingTempFpga2 = _XteCoolingTempFpga2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 4),
    _XteCoolingTempFpga2_Type()
)
xteCoolingTempFpga2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingTempFpga2.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingTempFpga2.setUnits("deg C")
_XteKernelTemp_Type = Integer32
_XteKernelTemp_Object = MibScalar
xteKernelTemp = _XteKernelTemp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 5),
    _XteKernelTemp_Type()
)
xteKernelTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteKernelTemp.setStatus("current")
_XteCoolingTempBattery_Type = Integer32
_XteCoolingTempBattery_Object = MibScalar
xteCoolingTempBattery = _XteCoolingTempBattery_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 6),
    _XteCoolingTempBattery_Type()
)
xteCoolingTempBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingTempBattery.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingTempBattery.setUnits("deg C")
_XteCoolingRpmFan1_Type = Integer32
_XteCoolingRpmFan1_Object = MibScalar
xteCoolingRpmFan1 = _XteCoolingRpmFan1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 7),
    _XteCoolingRpmFan1_Type()
)
xteCoolingRpmFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingRpmFan1.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingRpmFan1.setUnits("rpm")
_XteCoolingRpmFan2_Type = Integer32
_XteCoolingRpmFan2_Object = MibScalar
xteCoolingRpmFan2 = _XteCoolingRpmFan2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 8),
    _XteCoolingRpmFan2_Type()
)
xteCoolingRpmFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingRpmFan2.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingRpmFan2.setUnits("rpm")
_XteCoolingRpmFan3_Type = Integer32
_XteCoolingRpmFan3_Object = MibScalar
xteCoolingRpmFan3 = _XteCoolingRpmFan3_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 9),
    _XteCoolingRpmFan3_Type()
)
xteCoolingRpmFan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingRpmFan3.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingRpmFan3.setUnits("rpm")
_XteCoolingRpmFan4_Type = Integer32
_XteCoolingRpmFan4_Object = MibScalar
xteCoolingRpmFan4 = _XteCoolingRpmFan4_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 9, 10),
    _XteCoolingRpmFan4_Type()
)
xteCoolingRpmFan4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteCoolingRpmFan4.setStatus("current")
if mibBuilder.loadTexts:
    xteCoolingRpmFan4.setUnits("rpm")
_XteNetwork_ObjectIdentity = ObjectIdentity
xteNetwork = _XteNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10)
)
_XteNetworkTable_Object = MibTable
xteNetworkTable = _XteNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    xteNetworkTable.setStatus("current")
_XteNetworkEntry_Object = MibTableRow
xteNetworkEntry = _XteNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1)
)
xteNetworkEntry.setIndexNames(
    (0, "GATESAIR-XTE-MIB", "xteNetworkIndex"),
)
if mibBuilder.loadTexts:
    xteNetworkEntry.setStatus("current")


class _XteNetworkIndex_Type(Integer32):
    """Custom type xteNetworkIndex based on Integer32"""
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
        *(("wan", 1),
          ("lan", 2),
          ("dtiip1", 3),
          ("dtiip2", 4))
    )


_XteNetworkIndex_Type.__name__ = "Integer32"
_XteNetworkIndex_Object = MibTableColumn
xteNetworkIndex = _XteNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 1),
    _XteNetworkIndex_Type()
)
xteNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkIndex.setStatus("current")
_XteNetworkMac_Type = OctetString
_XteNetworkMac_Object = MibTableColumn
xteNetworkMac = _XteNetworkMac_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 2),
    _XteNetworkMac_Type()
)
xteNetworkMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkMac.setStatus("current")
_XteNetworkAddr_Type = IpAddress
_XteNetworkAddr_Object = MibTableColumn
xteNetworkAddr = _XteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 3),
    _XteNetworkAddr_Type()
)
xteNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkAddr.setStatus("current")
_XteNetworkGateway_Type = IpAddress
_XteNetworkGateway_Object = MibTableColumn
xteNetworkGateway = _XteNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 4),
    _XteNetworkGateway_Type()
)
xteNetworkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkGateway.setStatus("current")
_XteNetworkNetmask_Type = IpAddress
_XteNetworkNetmask_Object = MibTableColumn
xteNetworkNetmask = _XteNetworkNetmask_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 5),
    _XteNetworkNetmask_Type()
)
xteNetworkNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkNetmask.setStatus("current")
_XteNetworkLink_Type = YesNo
_XteNetworkLink_Object = MibTableColumn
xteNetworkLink = _XteNetworkLink_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 6),
    _XteNetworkLink_Type()
)
xteNetworkLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkLink.setStatus("current")
_XteNetworkDuplexMode_Type = XteNetworkDuplex
_XteNetworkDuplexMode_Object = MibTableColumn
xteNetworkDuplexMode = _XteNetworkDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 7),
    _XteNetworkDuplexMode_Type()
)
xteNetworkDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkDuplexMode.setStatus("current")
_XteNetworkSpeed_Type = Integer32
_XteNetworkSpeed_Object = MibTableColumn
xteNetworkSpeed = _XteNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 8),
    _XteNetworkSpeed_Type()
)
xteNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkSpeed.setStatus("current")
_XteNetworkAutoNegotiate_Type = XteAutoManual
_XteNetworkAutoNegotiate_Object = MibTableColumn
xteNetworkAutoNegotiate = _XteNetworkAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 10, 1, 1, 9),
    _XteNetworkAutoNegotiate_Type()
)
xteNetworkAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteNetworkAutoNegotiate.setStatus("current")
_XteFTR_ObjectIdentity = ObjectIdentity
xteFTR = _XteFTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11)
)
_XteFtrReadiness_Type = Integer32
_XteFtrReadiness_Object = MibScalar
xteFtrReadiness = _XteFtrReadiness_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 1),
    _XteFtrReadiness_Type()
)
xteFtrReadiness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrReadiness.setStatus("current")
if mibBuilder.loadTexts:
    xteFtrReadiness.setUnits("%")
_XteFtrTimeRemaining_Type = Integer32
_XteFtrTimeRemaining_Object = MibScalar
xteFtrTimeRemaining = _XteFtrTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 2),
    _XteFtrTimeRemaining_Type()
)
xteFtrTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    xteFtrTimeRemaining.setUnits("seconds")
_XteFtrSystemRefInput_Type = XteFtrReferenceStatus
_XteFtrSystemRefInput_Object = MibScalar
xteFtrSystemRefInput = _XteFtrSystemRefInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 3),
    _XteFtrSystemRefInput_Type()
)
xteFtrSystemRefInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrSystemRefInput.setStatus("current")
_XteFtrSystemRefIntGps1pps_Type = XteFtrReferenceStatus
_XteFtrSystemRefIntGps1pps_Object = MibScalar
xteFtrSystemRefIntGps1pps = _XteFtrSystemRefIntGps1pps_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 4),
    _XteFtrSystemRefIntGps1pps_Type()
)
xteFtrSystemRefIntGps1pps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrSystemRefIntGps1pps.setStatus("current")
_XteFtrPllRefClock_Type = XtePllStatus
_XteFtrPllRefClock_Object = MibScalar
xteFtrPllRefClock = _XteFtrPllRefClock_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 5),
    _XteFtrPllRefClock_Type()
)
xteFtrPllRefClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrPllRefClock.setStatus("current")
_XteFtrPllLockRfLo1_Type = XtePllStatus
_XteFtrPllLockRfLo1_Object = MibScalar
xteFtrPllLockRfLo1 = _XteFtrPllLockRfLo1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 6),
    _XteFtrPllLockRfLo1_Type()
)
xteFtrPllLockRfLo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrPllLockRfLo1.setStatus("current")
_XteFtrPllLockRfLo2_Type = XtePllStatus
_XteFtrPllLockRfLo2_Object = MibScalar
xteFtrPllLockRfLo2 = _XteFtrPllLockRfLo2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 7),
    _XteFtrPllLockRfLo2_Type()
)
xteFtrPllLockRfLo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrPllLockRfLo2.setStatus("current")
_XteFtrPllLockDigital_Type = XtePllStatus
_XteFtrPllLockDigital_Object = MibScalar
xteFtrPllLockDigital = _XteFtrPllLockDigital_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 8),
    _XteFtrPllLockDigital_Type()
)
xteFtrPllLockDigital.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteFtrPllLockDigital.setStatus("current")
_XteFtrOcxo_ObjectIdentity = ObjectIdentity
xteFtrOcxo = _XteFtrOcxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9)
)


class _XteOcxoReferenceSystem_Type(Integer32):
    """Custom type xteOcxoReferenceSystem based on Integer32"""
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
        *(("gps", 1),
          ("externalREF", 2),
          ("manual", 3),
          ("auto1PPS", 4))
    )


_XteOcxoReferenceSystem_Type.__name__ = "Integer32"
_XteOcxoReferenceSystem_Object = MibScalar
xteOcxoReferenceSystem = _XteOcxoReferenceSystem_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 1),
    _XteOcxoReferenceSystem_Type()
)
xteOcxoReferenceSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceSystem.setStatus("current")
_XteOcxoTuning_Type = Integer32
_XteOcxoTuning_Object = MibScalar
xteOcxoTuning = _XteOcxoTuning_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 2),
    _XteOcxoTuning_Type()
)
xteOcxoTuning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoTuning.setStatus("current")
_XteOcxoRfOutIfUndisciplined_Type = YesNo
_XteOcxoRfOutIfUndisciplined_Object = MibScalar
xteOcxoRfOutIfUndisciplined = _XteOcxoRfOutIfUndisciplined_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 3),
    _XteOcxoRfOutIfUndisciplined_Type()
)
xteOcxoRfOutIfUndisciplined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoRfOutIfUndisciplined.setStatus("current")


class _XteOcxo1ppsInputPrimary_Type(Integer32):
    """Custom type xteOcxo1ppsInputPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalGPS", 1),
          ("externalGPS", 2))
    )


_XteOcxo1ppsInputPrimary_Type.__name__ = "Integer32"
_XteOcxo1ppsInputPrimary_Object = MibScalar
xteOcxo1ppsInputPrimary = _XteOcxo1ppsInputPrimary_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 4),
    _XteOcxo1ppsInputPrimary_Type()
)
xteOcxo1ppsInputPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxo1ppsInputPrimary.setStatus("current")


class _XteOcxo1ppsInputActual_Type(Integer32):
    """Custom type xteOcxo1ppsInputActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalGPS", 1),
          ("externalGPS", 2))
    )


_XteOcxo1ppsInputActual_Type.__name__ = "Integer32"
_XteOcxo1ppsInputActual_Object = MibScalar
xteOcxo1ppsInputActual = _XteOcxo1ppsInputActual_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 5),
    _XteOcxo1ppsInputActual_Type()
)
xteOcxo1ppsInputActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxo1ppsInputActual.setStatus("current")


class _XteOcxoGnssMode_Type(Integer32):
    """Custom type xteOcxoGnssMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gps", 1),
          ("glonass", 2))
    )


_XteOcxoGnssMode_Type.__name__ = "Integer32"
_XteOcxoGnssMode_Object = MibScalar
xteOcxoGnssMode = _XteOcxoGnssMode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 6),
    _XteOcxoGnssMode_Type()
)
xteOcxoGnssMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoGnssMode.setStatus("current")


class _XteOcxoReferenceInput_Type(Integer32):
    """Custom type xteOcxoReferenceInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ext1PPS", 2),
          ("ext10MHz", 3))
    )


_XteOcxoReferenceInput_Type.__name__ = "Integer32"
_XteOcxoReferenceInput_Object = MibScalar
xteOcxoReferenceInput = _XteOcxoReferenceInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 7),
    _XteOcxoReferenceInput_Type()
)
xteOcxoReferenceInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceInput.setStatus("current")


class _XteOcxoReferenceInputTermination_Type(Integer32):
    """Custom type xteOcxoReferenceInputTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm50", 1),
          ("ohm10K", 2))
    )


_XteOcxoReferenceInputTermination_Type.__name__ = "Integer32"
_XteOcxoReferenceInputTermination_Object = MibScalar
xteOcxoReferenceInputTermination = _XteOcxoReferenceInputTermination_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 8),
    _XteOcxoReferenceInputTermination_Type()
)
xteOcxoReferenceInputTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceInputTermination.setStatus("current")


class _XteOcxoReferenceOutput_Type(Integer32):
    """Custom type xteOcxoReferenceOutput based on Integer32"""
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
        *(("none", 1),
          ("gps1PPS", 2),
          ("synthesized1PPS", 3),
          ("tenMHz", 4))
    )


_XteOcxoReferenceOutput_Type.__name__ = "Integer32"
_XteOcxoReferenceOutput_Object = MibScalar
xteOcxoReferenceOutput = _XteOcxoReferenceOutput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 9),
    _XteOcxoReferenceOutput_Type()
)
xteOcxoReferenceOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceOutput.setStatus("current")


class _XteOcxoReferenceLossMute_Type(Integer32):
    """Custom type xteOcxoReferenceLossMute based on Integer32"""
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
        *(("noMute", 1),
          ("muteImmediatly", 2),
          ("guardIntervalExceeds20Percent", 3),
          ("timeoutExceeded", 4))
    )


_XteOcxoReferenceLossMute_Type.__name__ = "Integer32"
_XteOcxoReferenceLossMute_Object = MibScalar
xteOcxoReferenceLossMute = _XteOcxoReferenceLossMute_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 10),
    _XteOcxoReferenceLossMute_Type()
)
xteOcxoReferenceLossMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceLossMute.setStatus("current")


class _XteOcxoReferenceTimeout_Type(Integer32):
    """Custom type xteOcxoReferenceTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_XteOcxoReferenceTimeout_Type.__name__ = "Integer32"
_XteOcxoReferenceTimeout_Object = MibScalar
xteOcxoReferenceTimeout = _XteOcxoReferenceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 11, 9, 11),
    _XteOcxoReferenceTimeout_Type()
)
xteOcxoReferenceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOcxoReferenceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xteOcxoReferenceTimeout.setUnits("hours")
_XteSnmp_ObjectIdentity = ObjectIdentity
xteSnmp = _XteSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12)
)
_XteSnmpPortNumber_Type = Integer32
_XteSnmpPortNumber_Object = MibScalar
xteSnmpPortNumber = _XteSnmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 1),
    _XteSnmpPortNumber_Type()
)
xteSnmpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpPortNumber.setStatus("current")
_XteSnmpTrapVersion_Type = Integer32
_XteSnmpTrapVersion_Object = MibScalar
xteSnmpTrapVersion = _XteSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 2),
    _XteSnmpTrapVersion_Type()
)
xteSnmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapVersion.setStatus("current")
_XteSnmpTrapHostTable_Object = MibTable
xteSnmpTrapHostTable = _XteSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3)
)
if mibBuilder.loadTexts:
    xteSnmpTrapHostTable.setStatus("current")
_XteSnmpTrapHostEntry_Object = MibTableRow
xteSnmpTrapHostEntry = _XteSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1)
)
xteSnmpTrapHostEntry.setIndexNames(
    (0, "GATESAIR-XTE-MIB", "xteSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    xteSnmpTrapHostEntry.setStatus("current")


class _XteSnmpTrapHostIndex_Type(Integer32):
    """Custom type xteSnmpTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_XteSnmpTrapHostIndex_Type.__name__ = "Integer32"
_XteSnmpTrapHostIndex_Object = MibTableColumn
xteSnmpTrapHostIndex = _XteSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 1),
    _XteSnmpTrapHostIndex_Type()
)
xteSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xteSnmpTrapHostIndex.setStatus("current")
_XteSnmpTrapHostIpAddress_Type = IpAddress
_XteSnmpTrapHostIpAddress_Object = MibTableColumn
xteSnmpTrapHostIpAddress = _XteSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 2),
    _XteSnmpTrapHostIpAddress_Type()
)
xteSnmpTrapHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostIpAddress.setStatus("current")
_XteSnmpTrapHostPort_Type = Integer32
_XteSnmpTrapHostPort_Object = MibTableColumn
xteSnmpTrapHostPort = _XteSnmpTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 3),
    _XteSnmpTrapHostPort_Type()
)
xteSnmpTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostPort.setStatus("current")
_XteSnmpTrapHostPduType_Type = SNMPEventType
_XteSnmpTrapHostPduType_Object = MibTableColumn
xteSnmpTrapHostPduType = _XteSnmpTrapHostPduType_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 4),
    _XteSnmpTrapHostPduType_Type()
)
xteSnmpTrapHostPduType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostPduType.setStatus("current")
_XteSnmpTrapHostInformRetries_Type = Integer32
_XteSnmpTrapHostInformRetries_Object = MibTableColumn
xteSnmpTrapHostInformRetries = _XteSnmpTrapHostInformRetries_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 5),
    _XteSnmpTrapHostInformRetries_Type()
)
xteSnmpTrapHostInformRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostInformRetries.setStatus("current")
_XteSnmpTrapHostInformRetryInterval_Type = Integer32
_XteSnmpTrapHostInformRetryInterval_Object = MibTableColumn
xteSnmpTrapHostInformRetryInterval = _XteSnmpTrapHostInformRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 6),
    _XteSnmpTrapHostInformRetryInterval_Type()
)
xteSnmpTrapHostInformRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostInformRetryInterval.setStatus("current")
_XteSnmpTrapHostOutstandingInforms_Type = Integer32
_XteSnmpTrapHostOutstandingInforms_Object = MibTableColumn
xteSnmpTrapHostOutstandingInforms = _XteSnmpTrapHostOutstandingInforms_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 12, 3, 1, 7),
    _XteSnmpTrapHostOutstandingInforms_Type()
)
xteSnmpTrapHostOutstandingInforms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteSnmpTrapHostOutstandingInforms.setStatus("current")
_XteEventEnable_ObjectIdentity = ObjectIdentity
xteEventEnable = _XteEventEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13)
)
_XteAllEventsEnable_Type = EnabledDisabled
_XteAllEventsEnable_Object = MibScalar
xteAllEventsEnable = _XteAllEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 1),
    _XteAllEventsEnable_Type()
)
xteAllEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteAllEventsEnable.setStatus("current")
_XteActiveEventEnable_Type = EnabledDisabled
_XteActiveEventEnable_Object = MibScalar
xteActiveEventEnable = _XteActiveEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 2),
    _XteActiveEventEnable_Type()
)
xteActiveEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteActiveEventEnable.setStatus("current")
_XteStatusEventEnable_Type = EnabledDisabled
_XteStatusEventEnable_Object = MibScalar
xteStatusEventEnable = _XteStatusEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 3),
    _XteStatusEventEnable_Type()
)
xteStatusEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteStatusEventEnable.setStatus("current")
_XteInputStatusPrimaryEventEnable_Type = EnabledDisabled
_XteInputStatusPrimaryEventEnable_Object = MibScalar
xteInputStatusPrimaryEventEnable = _XteInputStatusPrimaryEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 4),
    _XteInputStatusPrimaryEventEnable_Type()
)
xteInputStatusPrimaryEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputStatusPrimaryEventEnable.setStatus("current")
_XteInputStatusSecondaryEventEnable_Type = Integer32
_XteInputStatusSecondaryEventEnable_Object = MibScalar
xteInputStatusSecondaryEventEnable = _XteInputStatusSecondaryEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 5),
    _XteInputStatusSecondaryEventEnable_Type()
)
xteInputStatusSecondaryEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputStatusSecondaryEventEnable.setStatus("current")
_XteInputSwitchCountCurrentEnable_Type = EnabledDisabled
_XteInputSwitchCountCurrentEnable_Object = MibScalar
xteInputSwitchCountCurrentEnable = _XteInputSwitchCountCurrentEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 6),
    _XteInputSwitchCountCurrentEnable_Type()
)
xteInputSwitchCountCurrentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteInputSwitchCountCurrentEnable.setStatus("current")
_XteOutputPowerPresentEventEnable_Type = EnabledDisabled
_XteOutputPowerPresentEventEnable_Object = MibScalar
xteOutputPowerPresentEventEnable = _XteOutputPowerPresentEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 7),
    _XteOutputPowerPresentEventEnable_Type()
)
xteOutputPowerPresentEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputPowerPresentEventEnable.setStatus("current")
_XteOutputMuteEventEnable_Type = Integer32
_XteOutputMuteEventEnable_Object = MibScalar
xteOutputMuteEventEnable = _XteOutputMuteEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 8),
    _XteOutputMuteEventEnable_Type()
)
xteOutputMuteEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteOutputMuteEventEnable.setStatus("current")
_XteRtacModeEventEnable_Type = EnabledDisabled
_XteRtacModeEventEnable_Object = MibScalar
xteRtacModeEventEnable = _XteRtacModeEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 9),
    _XteRtacModeEventEnable_Type()
)
xteRtacModeEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacModeEventEnable.setStatus("current")
_XteRtacEnabledEventEnable_Type = EnabledDisabled
_XteRtacEnabledEventEnable_Object = MibScalar
xteRtacEnabledEventEnable = _XteRtacEnabledEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 10),
    _XteRtacEnabledEventEnable_Type()
)
xteRtacEnabledEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xteRtacEnabledEventEnable.setStatus("current")
_XtePwrSupplyControllerEventEnable_Type = EnabledDisabled
_XtePwrSupplyControllerEventEnable_Object = MibScalar
xtePwrSupplyControllerEventEnable = _XtePwrSupplyControllerEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 11),
    _XtePwrSupplyControllerEventEnable_Type()
)
xtePwrSupplyControllerEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtePwrSupplyControllerEventEnable.setStatus("current")
_XtePwrSupplyPwrAmpEventEnable_Type = EnabledDisabled
_XtePwrSupplyPwrAmpEventEnable_Object = MibScalar
xtePwrSupplyPwrAmpEventEnable = _XtePwrSupplyPwrAmpEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 12),
    _XtePwrSupplyPwrAmpEventEnable_Type()
)
xtePwrSupplyPwrAmpEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtePwrSupplyPwrAmpEventEnable.setStatus("current")
_XtePwrSupplyModulatorEventEnable_Type = EnabledDisabled
_XtePwrSupplyModulatorEventEnable_Object = MibScalar
xtePwrSupplyModulatorEventEnable = _XtePwrSupplyModulatorEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 2, 13, 13),
    _XtePwrSupplyModulatorEventEnable_Type()
)
xtePwrSupplyModulatorEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtePwrSupplyModulatorEventEnable.setStatus("current")
_XteConformance_ObjectIdentity = ObjectIdentity
xteConformance = _XteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 3)
)

# Managed Objects groups

xteObjectGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 3, 1)
)
xteObjectGroups.setObjects(
      *(("GATESAIR-XTE-MIB", "xteInputMuteOnTsLoss"),
        ("GATESAIR-XTE-MIB", "xteInputPowerOn"),
        ("GATESAIR-XTE-MIB", "xteKernelTemp"),
        ("GATESAIR-XTE-MIB", "xteMibRevision"),
        ("GATESAIR-XTE-MIB", "xteVerSwPartNumber"),
        ("GATESAIR-XTE-MIB", "xteVerSwRev"),
        ("GATESAIR-XTE-MIB", "xteVerSwUboot"),
        ("GATESAIR-XTE-MIB", "xteVerSwWebboot"),
        ("GATESAIR-XTE-MIB", "xteVerSwXtmod"),
        ("GATESAIR-XTE-MIB", "xteVerSwLinux"),
        ("GATESAIR-XTE-MIB", "xteVerSwDevTree"),
        ("GATESAIR-XTE-MIB", "xteVerSwFpga1"),
        ("GATESAIR-XTE-MIB", "xteVerSwFpga2"),
        ("GATESAIR-XTE-MIB", "xteVerSwCpld"),
        ("GATESAIR-XTE-MIB", "xteVerHwModulator"),
        ("GATESAIR-XTE-MIB", "xteVerHwBackplane"),
        ("GATESAIR-XTE-MIB", "xteVerHwPwrSupplyCtrl"),
        ("GATESAIR-XTE-MIB", "xteVerHwPwrAmp"),
        ("GATESAIR-XTE-MIB", "xteActive"),
        ("GATESAIR-XTE-MIB", "xteStatus"),
        ("GATESAIR-XTE-MIB", "xteStationName"),
        ("GATESAIR-XTE-MIB", "xteModelNumber"),
        ("GATESAIR-XTE-MIB", "xteSerialNumber"),
        ("GATESAIR-XTE-MIB", "xteTimeOfDay"),
        ("GATESAIR-XTE-MIB", "xteUTCOffset"),
        ("GATESAIR-XTE-MIB", "xteTimeSource"),
        ("GATESAIR-XTE-MIB", "xteNTPServerName1"),
        ("GATESAIR-XTE-MIB", "xteNTPServerName2"),
        ("GATESAIR-XTE-MIB", "xteNTPServerName3"),
        ("GATESAIR-XTE-MIB", "xteNTPServerName4"),
        ("GATESAIR-XTE-MIB", "xteNTPServerName5"),
        ("GATESAIR-XTE-MIB", "xteInputActive"),
        ("GATESAIR-XTE-MIB", "xteInputStatusPrimary"),
        ("GATESAIR-XTE-MIB", "xteInputStatusSecondary"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchMode"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchTimeout"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchElapsedTime"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchCountMax"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchCountCurrent"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchCountReset"),
        ("GATESAIR-XTE-MIB", "xteOutputPowerLimit"),
        ("GATESAIR-XTE-MIB", "xteOutputPowerCutoff"),
        ("GATESAIR-XTE-MIB", "xteOutputFoldbackLow"),
        ("GATESAIR-XTE-MIB", "xteOutputFoldbackHigh"),
        ("GATESAIR-XTE-MIB", "xteOutputFoldbackMax"),
        ("GATESAIR-XTE-MIB", "xteOutputPaGain"),
        ("GATESAIR-XTE-MIB", "xteOutputLevelInput"),
        ("GATESAIR-XTE-MIB", "xteOutputLevelOutput"),
        ("GATESAIR-XTE-MIB", "xteOutputPowerPresent"),
        ("GATESAIR-XTE-MIB", "xteOutputMute"),
        ("GATESAIR-XTE-MIB", "xteRtacSetupPeakReductionMode"),
        ("GATESAIR-XTE-MIB", "xteRtacSetupNonLinearRange"),
        ("GATESAIR-XTE-MIB", "xteRtacSetupMaxCrestFactor"),
        ("GATESAIR-XTE-MIB", "xteRtacIndex"),
        ("GATESAIR-XTE-MIB", "xteRtacOpMode"),
        ("GATESAIR-XTE-MIB", "xteRtacSuccess"),
        ("GATESAIR-XTE-MIB", "xteRtacAttempts"),
        ("GATESAIR-XTE-MIB", "xteRtacEnabled"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyController"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyPwrAmp"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyModulator"),
        ("GATESAIR-XTE-MIB", "xteCoolingTempAmbient"),
        ("GATESAIR-XTE-MIB", "xteCoolingTempPwrAmp"),
        ("GATESAIR-XTE-MIB", "xteCoolingTempFpga1"),
        ("GATESAIR-XTE-MIB", "xteCoolingTempFpga2"),
        ("GATESAIR-XTE-MIB", "xteCoolingTempBattery"),
        ("GATESAIR-XTE-MIB", "xteCoolingRpmFan1"),
        ("GATESAIR-XTE-MIB", "xteCoolingRpmFan2"),
        ("GATESAIR-XTE-MIB", "xteCoolingRpmFan3"),
        ("GATESAIR-XTE-MIB", "xteCoolingRpmFan4"),
        ("GATESAIR-XTE-MIB", "xteNetworkIndex"),
        ("GATESAIR-XTE-MIB", "xteNetworkMac"),
        ("GATESAIR-XTE-MIB", "xteNetworkAddr"),
        ("GATESAIR-XTE-MIB", "xteNetworkGateway"),
        ("GATESAIR-XTE-MIB", "xteNetworkNetmask"),
        ("GATESAIR-XTE-MIB", "xteNetworkLink"),
        ("GATESAIR-XTE-MIB", "xteNetworkDuplexMode"),
        ("GATESAIR-XTE-MIB", "xteNetworkSpeed"),
        ("GATESAIR-XTE-MIB", "xteNetworkAutoNegotiate"),
        ("GATESAIR-XTE-MIB", "xteFtrReadiness"),
        ("GATESAIR-XTE-MIB", "xteFtrTimeRemaining"),
        ("GATESAIR-XTE-MIB", "xteFtrSystemRefInput"),
        ("GATESAIR-XTE-MIB", "xteFtrSystemRefIntGps1pps"),
        ("GATESAIR-XTE-MIB", "xteFtrPllRefClock"),
        ("GATESAIR-XTE-MIB", "xteFtrPllLockRfLo1"),
        ("GATESAIR-XTE-MIB", "xteFtrPllLockRfLo2"),
        ("GATESAIR-XTE-MIB", "xteFtrPllLockDigital"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceSystem"),
        ("GATESAIR-XTE-MIB", "xteOcxoTuning"),
        ("GATESAIR-XTE-MIB", "xteOcxoRfOutIfUndisciplined"),
        ("GATESAIR-XTE-MIB", "xteOcxo1ppsInputPrimary"),
        ("GATESAIR-XTE-MIB", "xteOcxo1ppsInputActual"),
        ("GATESAIR-XTE-MIB", "xteOcxoGnssMode"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceInput"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceInputTermination"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceOutput"),
        ("GATESAIR-XTE-MIB", "xteSnmpPortNumber"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapVersion"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostIndex"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostIpAddress"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostPort"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostPduType"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostInformRetries"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostInformRetryInterval"),
        ("GATESAIR-XTE-MIB", "xteSnmpTrapHostOutstandingInforms"),
        ("GATESAIR-XTE-MIB", "xteAllEventsEnable"),
        ("GATESAIR-XTE-MIB", "xteActiveEventEnable"),
        ("GATESAIR-XTE-MIB", "xteStatusEventEnable"),
        ("GATESAIR-XTE-MIB", "xteInputStatusPrimaryEventEnable"),
        ("GATESAIR-XTE-MIB", "xteInputStatusSecondaryEventEnable"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchCountCurrentEnable"),
        ("GATESAIR-XTE-MIB", "xteOutputPowerPresentEventEnable"),
        ("GATESAIR-XTE-MIB", "xteOutputMuteEventEnable"),
        ("GATESAIR-XTE-MIB", "xteRtacModeEventEnable"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceLossMute"),
        ("GATESAIR-XTE-MIB", "xteOcxoReferenceTimeout"),
        ("GATESAIR-XTE-MIB", "xteRtacEnabledEventEnable"),
        ("GATESAIR-XTE-MIB", "xteRtacOpModeAfterAcLoss"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyControllerEventEnable"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyPwrAmpEventEnable"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyModulatorEventEnable"))
)
if mibBuilder.loadTexts:
    xteObjectGroups.setStatus("current")


# Notification objects

xteActiveEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 1)
)
xteActiveEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteActive"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteActiveEvent.setStatus(
        "current"
    )

xteStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 2)
)
xteStatusEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteStatus"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteStatusEvent.setStatus(
        "current"
    )

xteInputStatusPrimaryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 3)
)
xteInputStatusPrimaryEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteInputStatusPrimary"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteInputStatusPrimaryEvent.setStatus(
        "current"
    )

xteInputStatusSecondaryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 4)
)
xteInputStatusSecondaryEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteInputStatusSecondary"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteInputStatusSecondaryEvent.setStatus(
        "current"
    )

xteInputSwitchCountCurrentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 5)
)
xteInputSwitchCountCurrentEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteInputSwitchCountCurrent"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteInputSwitchCountCurrentEvent.setStatus(
        "current"
    )

xteOutputPowerPresentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 6)
)
xteOutputPowerPresentEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteOutputPowerPresent"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteOutputPowerPresentEvent.setStatus(
        "current"
    )

xteOutputMuteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 7)
)
xteOutputMuteEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteOutputMute"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteOutputMuteEvent.setStatus(
        "current"
    )

xteRtacOpModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 8)
)
xteRtacOpModeEvent.setObjects(
      *(("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"),
        ("GATESAIR-XTE-MIB", "xteRtacOpMode"))
)
if mibBuilder.loadTexts:
    xteRtacOpModeEvent.setStatus(
        "current"
    )

xteRtacEnabledEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 9)
)
xteRtacEnabledEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xteRtacEnabled"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xteRtacEnabledEvent.setStatus(
        "current"
    )

xtePwrSupplyControllerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 10)
)
xtePwrSupplyControllerEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xtePwrSupplyController"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xtePwrSupplyControllerEvent.setStatus(
        "current"
    )

xtePwrSupplyPwrAmpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 11)
)
xtePwrSupplyPwrAmpEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xtePwrSupplyPwrAmp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xtePwrSupplyPwrAmpEvent.setStatus(
        "current"
    )

xtePwrSupplyModulatorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 1, 0, 12)
)
xtePwrSupplyModulatorEvent.setObjects(
      *(("GATESAIR-XTE-MIB", "xtePwrSupplyModulator"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    xtePwrSupplyModulatorEvent.setStatus(
        "current"
    )


# Notifications groups

xteEventsGroups = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 3, 2)
)
xteEventsGroups.setObjects(
      *(("GATESAIR-XTE-MIB", "xteActiveEvent"),
        ("GATESAIR-XTE-MIB", "xteStatusEvent"),
        ("GATESAIR-XTE-MIB", "xteInputStatusPrimaryEvent"),
        ("GATESAIR-XTE-MIB", "xteInputStatusSecondaryEvent"),
        ("GATESAIR-XTE-MIB", "xteInputSwitchCountCurrentEvent"),
        ("GATESAIR-XTE-MIB", "xteOutputPowerPresentEvent"),
        ("GATESAIR-XTE-MIB", "xteOutputMuteEvent"),
        ("GATESAIR-XTE-MIB", "xteRtacOpModeEvent"),
        ("GATESAIR-XTE-MIB", "xteRtacEnabledEvent"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyControllerEvent"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyPwrAmpEvent"),
        ("GATESAIR-XTE-MIB", "xtePwrSupplyModulatorEvent"))
)
if mibBuilder.loadTexts:
    xteEventsGroups.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

xteCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7, 2, 3, 3)
)
xteCompliances.setObjects(
      *(("GATESAIR-XTE-MIB", "xteObjectGroups"),
        ("GATESAIR-XTE-MIB", "xteEventsGroups"))
)
if mibBuilder.loadTexts:
    xteCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GATESAIR-XTE-MIB",
    **{"XteSummaryStatus": XteSummaryStatus,
       "XteInputSelection": XteInputSelection,
       "XteInputStatus": XteInputStatus,
       "XteInputMode": XteInputMode,
       "XteAutoManual": XteAutoManual,
       "XteRtacMode": XteRtacMode,
       "XteRtacModeAfterACLoss": XteRtacModeAfterACLoss,
       "XteNetworkDuplex": XteNetworkDuplex,
       "XteFtrReferenceStatus": XteFtrReferenceStatus,
       "XtePllStatus": XtePllStatus,
       "XteInputNetworkMode": XteInputNetworkMode,
       "xteBaseMibModule": xteBaseMibModule,
       "xteBaseMib": xteBaseMib,
       "xteEvents": xteEvents,
       "xteEventsV2": xteEventsV2,
       "xteActiveEvent": xteActiveEvent,
       "xteStatusEvent": xteStatusEvent,
       "xteInputStatusPrimaryEvent": xteInputStatusPrimaryEvent,
       "xteInputStatusSecondaryEvent": xteInputStatusSecondaryEvent,
       "xteInputSwitchCountCurrentEvent": xteInputSwitchCountCurrentEvent,
       "xteOutputPowerPresentEvent": xteOutputPowerPresentEvent,
       "xteOutputMuteEvent": xteOutputMuteEvent,
       "xteRtacOpModeEvent": xteRtacOpModeEvent,
       "xteRtacEnabledEvent": xteRtacEnabledEvent,
       "xtePwrSupplyControllerEvent": xtePwrSupplyControllerEvent,
       "xtePwrSupplyPwrAmpEvent": xtePwrSupplyPwrAmpEvent,
       "xtePwrSupplyModulatorEvent": xtePwrSupplyModulatorEvent,
       "xteObjects": xteObjects,
       "xteMibRevision": xteMibRevision,
       "xteVersion": xteVersion,
       "xteVerSoftware": xteVerSoftware,
       "xteVerSwPartNumber": xteVerSwPartNumber,
       "xteVerSwRev": xteVerSwRev,
       "xteVerSwUboot": xteVerSwUboot,
       "xteVerSwWebboot": xteVerSwWebboot,
       "xteVerSwXtmod": xteVerSwXtmod,
       "xteVerSwLinux": xteVerSwLinux,
       "xteVerSwDevTree": xteVerSwDevTree,
       "xteVerSwFpga1": xteVerSwFpga1,
       "xteVerSwFpga2": xteVerSwFpga2,
       "xteVerSwCpld": xteVerSwCpld,
       "xteVerHardware": xteVerHardware,
       "xteVerHwModulator": xteVerHwModulator,
       "xteVerHwBackplane": xteVerHwBackplane,
       "xteVerHwPwrSupplyCtrl": xteVerHwPwrSupplyCtrl,
       "xteVerHwPwrAmp": xteVerHwPwrAmp,
       "xteGeneral": xteGeneral,
       "xteActive": xteActive,
       "xteStatus": xteStatus,
       "xteStationName": xteStationName,
       "xteModelNumber": xteModelNumber,
       "xteSerialNumber": xteSerialNumber,
       "xteDateAndTime": xteDateAndTime,
       "xteTimeOfDay": xteTimeOfDay,
       "xteUTCOffset": xteUTCOffset,
       "xteTimeSource": xteTimeSource,
       "xteNTPServerName1": xteNTPServerName1,
       "xteNTPServerName2": xteNTPServerName2,
       "xteNTPServerName3": xteNTPServerName3,
       "xteNTPServerName4": xteNTPServerName4,
       "xteNTPServerName5": xteNTPServerName5,
       "xteInput": xteInput,
       "xteInputPowerOn": xteInputPowerOn,
       "xteInputActive": xteInputActive,
       "xteInputStatusPrimary": xteInputStatusPrimary,
       "xteInputStatusSecondary": xteInputStatusSecondary,
       "xteInputMuteOnTsLoss": xteInputMuteOnTsLoss,
       "xteInputSwitchMode": xteInputSwitchMode,
       "xteInputSwitchTimeout": xteInputSwitchTimeout,
       "xteInputSwitchElapsedTime": xteInputSwitchElapsedTime,
       "xteInputSwitchCountMax": xteInputSwitchCountMax,
       "xteInputSwitchCountCurrent": xteInputSwitchCountCurrent,
       "xteInputSwitchCountReset": xteInputSwitchCountReset,
       "xteOutput": xteOutput,
       "xteOutputPowerLimit": xteOutputPowerLimit,
       "xteOutputPowerCutoff": xteOutputPowerCutoff,
       "xteOutputFoldbackLow": xteOutputFoldbackLow,
       "xteOutputFoldbackHigh": xteOutputFoldbackHigh,
       "xteOutputFoldbackMax": xteOutputFoldbackMax,
       "xteOutputPaGain": xteOutputPaGain,
       "xteOutputLevelInput": xteOutputLevelInput,
       "xteOutputLevelOutput": xteOutputLevelOutput,
       "xteOutputPowerPresent": xteOutputPowerPresent,
       "xteOutputMute": xteOutputMute,
       "xteRtac": xteRtac,
       "xteRtacSetup": xteRtacSetup,
       "xteRtacSetupPeakReductionMode": xteRtacSetupPeakReductionMode,
       "xteRtacSetupNonLinearRange": xteRtacSetupNonLinearRange,
       "xteRtacSetupMaxCrestFactor": xteRtacSetupMaxCrestFactor,
       "xteRtacTable": xteRtacTable,
       "xteRtacEntry": xteRtacEntry,
       "xteRtacIndex": xteRtacIndex,
       "xteRtacOpMode": xteRtacOpMode,
       "xteRtacSuccess": xteRtacSuccess,
       "xteRtacAttempts": xteRtacAttempts,
       "xteRtacOpModeAfterAcLoss": xteRtacOpModeAfterAcLoss,
       "xteRtacEnabled": xteRtacEnabled,
       "xtePowerSupplies": xtePowerSupplies,
       "xtePwrSupplyController": xtePwrSupplyController,
       "xtePwrSupplyPwrAmp": xtePwrSupplyPwrAmp,
       "xtePwrSupplyModulator": xtePwrSupplyModulator,
       "xteCooling": xteCooling,
       "xteCoolingTempAmbient": xteCoolingTempAmbient,
       "xteCoolingTempPwrAmp": xteCoolingTempPwrAmp,
       "xteCoolingTempFpga1": xteCoolingTempFpga1,
       "xteCoolingTempFpga2": xteCoolingTempFpga2,
       "xteKernelTemp": xteKernelTemp,
       "xteCoolingTempBattery": xteCoolingTempBattery,
       "xteCoolingRpmFan1": xteCoolingRpmFan1,
       "xteCoolingRpmFan2": xteCoolingRpmFan2,
       "xteCoolingRpmFan3": xteCoolingRpmFan3,
       "xteCoolingRpmFan4": xteCoolingRpmFan4,
       "xteNetwork": xteNetwork,
       "xteNetworkTable": xteNetworkTable,
       "xteNetworkEntry": xteNetworkEntry,
       "xteNetworkIndex": xteNetworkIndex,
       "xteNetworkMac": xteNetworkMac,
       "xteNetworkAddr": xteNetworkAddr,
       "xteNetworkGateway": xteNetworkGateway,
       "xteNetworkNetmask": xteNetworkNetmask,
       "xteNetworkLink": xteNetworkLink,
       "xteNetworkDuplexMode": xteNetworkDuplexMode,
       "xteNetworkSpeed": xteNetworkSpeed,
       "xteNetworkAutoNegotiate": xteNetworkAutoNegotiate,
       "xteFTR": xteFTR,
       "xteFtrReadiness": xteFtrReadiness,
       "xteFtrTimeRemaining": xteFtrTimeRemaining,
       "xteFtrSystemRefInput": xteFtrSystemRefInput,
       "xteFtrSystemRefIntGps1pps": xteFtrSystemRefIntGps1pps,
       "xteFtrPllRefClock": xteFtrPllRefClock,
       "xteFtrPllLockRfLo1": xteFtrPllLockRfLo1,
       "xteFtrPllLockRfLo2": xteFtrPllLockRfLo2,
       "xteFtrPllLockDigital": xteFtrPllLockDigital,
       "xteFtrOcxo": xteFtrOcxo,
       "xteOcxoReferenceSystem": xteOcxoReferenceSystem,
       "xteOcxoTuning": xteOcxoTuning,
       "xteOcxoRfOutIfUndisciplined": xteOcxoRfOutIfUndisciplined,
       "xteOcxo1ppsInputPrimary": xteOcxo1ppsInputPrimary,
       "xteOcxo1ppsInputActual": xteOcxo1ppsInputActual,
       "xteOcxoGnssMode": xteOcxoGnssMode,
       "xteOcxoReferenceInput": xteOcxoReferenceInput,
       "xteOcxoReferenceInputTermination": xteOcxoReferenceInputTermination,
       "xteOcxoReferenceOutput": xteOcxoReferenceOutput,
       "xteOcxoReferenceLossMute": xteOcxoReferenceLossMute,
       "xteOcxoReferenceTimeout": xteOcxoReferenceTimeout,
       "xteSnmp": xteSnmp,
       "xteSnmpPortNumber": xteSnmpPortNumber,
       "xteSnmpTrapVersion": xteSnmpTrapVersion,
       "xteSnmpTrapHostTable": xteSnmpTrapHostTable,
       "xteSnmpTrapHostEntry": xteSnmpTrapHostEntry,
       "xteSnmpTrapHostIndex": xteSnmpTrapHostIndex,
       "xteSnmpTrapHostIpAddress": xteSnmpTrapHostIpAddress,
       "xteSnmpTrapHostPort": xteSnmpTrapHostPort,
       "xteSnmpTrapHostPduType": xteSnmpTrapHostPduType,
       "xteSnmpTrapHostInformRetries": xteSnmpTrapHostInformRetries,
       "xteSnmpTrapHostInformRetryInterval": xteSnmpTrapHostInformRetryInterval,
       "xteSnmpTrapHostOutstandingInforms": xteSnmpTrapHostOutstandingInforms,
       "xteEventEnable": xteEventEnable,
       "xteAllEventsEnable": xteAllEventsEnable,
       "xteActiveEventEnable": xteActiveEventEnable,
       "xteStatusEventEnable": xteStatusEventEnable,
       "xteInputStatusPrimaryEventEnable": xteInputStatusPrimaryEventEnable,
       "xteInputStatusSecondaryEventEnable": xteInputStatusSecondaryEventEnable,
       "xteInputSwitchCountCurrentEnable": xteInputSwitchCountCurrentEnable,
       "xteOutputPowerPresentEventEnable": xteOutputPowerPresentEventEnable,
       "xteOutputMuteEventEnable": xteOutputMuteEventEnable,
       "xteRtacModeEventEnable": xteRtacModeEventEnable,
       "xteRtacEnabledEventEnable": xteRtacEnabledEventEnable,
       "xtePwrSupplyControllerEventEnable": xtePwrSupplyControllerEventEnable,
       "xtePwrSupplyPwrAmpEventEnable": xtePwrSupplyPwrAmpEventEnable,
       "xtePwrSupplyModulatorEventEnable": xtePwrSupplyModulatorEventEnable,
       "xteConformance": xteConformance,
       "xteObjectGroups": xteObjectGroups,
       "xteEventsGroups": xteEventsGroups,
       "xteCompliances": xteCompliances}
)
