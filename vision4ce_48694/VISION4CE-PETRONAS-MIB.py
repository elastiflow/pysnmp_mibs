# SNMP MIB module (VISION4CE-PETRONAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vision4ce_48694/VISION4CE-PETRONAS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:07:06 2025
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

v4cePetronasMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3)
)
if mibBuilder.loadTexts:
    v4cePetronasMIB.setRevisions(
        ("2016-10-19 07:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vision4ceTopLevel_ObjectIdentity = ObjectIdentity
vision4ceTopLevel = _Vision4ceTopLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694)
)
_V4cePetronasNotifications_ObjectIdentity = ObjectIdentity
v4cePetronasNotifications = _V4cePetronasNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 0)
)
_V4cePetronasObjects_ObjectIdentity = ObjectIdentity
v4cePetronasObjects = _V4cePetronasObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1)
)
_V4cePetronasObjects0_ObjectIdentity = ObjectIdentity
v4cePetronasObjects0 = _V4cePetronasObjects0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 0)
)
_V4cePetronasAbout_Type = OctetString
_V4cePetronasAbout_Object = MibScalar
v4cePetronasAbout = _V4cePetronasAbout_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 0, 1),
    _V4cePetronasAbout_Type()
)
v4cePetronasAbout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasAbout.setStatus("current")


class _V4cePetronasName_Type(OctetString):
    """Custom type v4cePetronasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_V4cePetronasName_Type.__name__ = "OctetString"
_V4cePetronasName_Object = MibScalar
v4cePetronasName = _V4cePetronasName_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 0, 2),
    _V4cePetronasName_Type()
)
v4cePetronasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4cePetronasName.setStatus("current")


class _V4cePetronasAge_Type(Integer32):
    """Custom type v4cePetronasAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V4cePetronasAge_Type.__name__ = "Integer32"
_V4cePetronasAge_Object = MibScalar
v4cePetronasAge = _V4cePetronasAge_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 0, 3),
    _V4cePetronasAge_Type()
)
v4cePetronasAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4cePetronasAge.setStatus("current")
_V4cePetronasObjectsSystem_ObjectIdentity = ObjectIdentity
v4cePetronasObjectsSystem = _V4cePetronasObjectsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1)
)
_V4cePetronasSysManAloftSw_Type = TruthValue
_V4cePetronasSysManAloftSw_Object = MibScalar
v4cePetronasSysManAloftSw = _V4cePetronasSysManAloftSw_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1, 1),
    _V4cePetronasSysManAloftSw_Type()
)
v4cePetronasSysManAloftSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSysManAloftSw.setStatus("current")
_V4cePetronasSysHeloOpsSw_Type = TruthValue
_V4cePetronasSysHeloOpsSw_Object = MibScalar
v4cePetronasSysHeloOpsSw = _V4cePetronasSysHeloOpsSw_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1, 2),
    _V4cePetronasSysHeloOpsSw_Type()
)
v4cePetronasSysHeloOpsSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSysHeloOpsSw.setStatus("current")
_V4cePetronasSysPlatCab_Type = TruthValue
_V4cePetronasSysPlatCab_Object = MibScalar
v4cePetronasSysPlatCab = _V4cePetronasSysPlatCab_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1, 3),
    _V4cePetronasSysPlatCab_Type()
)
v4cePetronasSysPlatCab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSysPlatCab.setStatus("current")
_V4cePetronasSysLightCab_Type = TruthValue
_V4cePetronasSysLightCab_Object = MibScalar
v4cePetronasSysLightCab = _V4cePetronasSysLightCab_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1, 4),
    _V4cePetronasSysLightCab_Type()
)
v4cePetronasSysLightCab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSysLightCab.setStatus("current")
_V4cePetronasSysLightningSpd_Type = TruthValue
_V4cePetronasSysLightningSpd_Object = MibScalar
v4cePetronasSysLightningSpd = _V4cePetronasSysLightningSpd_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 1, 5),
    _V4cePetronasSysLightningSpd_Type()
)
v4cePetronasSysLightningSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSysLightningSpd.setStatus("current")
_V4cePetronasPsuTable_Object = MibTable
v4cePetronasPsuTable = _V4cePetronasPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2)
)
if mibBuilder.loadTexts:
    v4cePetronasPsuTable.setStatus("current")
_V4cePetronasPsuEntry_Object = MibTableRow
v4cePetronasPsuEntry = _V4cePetronasPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2, 1)
)
v4cePetronasPsuEntry.setIndexNames(
    (0, "VISION4CE-PETRONAS-MIB", "v4cePetronasPsuInstance"),
)
if mibBuilder.loadTexts:
    v4cePetronasPsuEntry.setStatus("current")


class _V4cePetronasPsuInstance_Type(Integer32):
    """Custom type v4cePetronasPsuInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_V4cePetronasPsuInstance_Type.__name__ = "Integer32"
_V4cePetronasPsuInstance_Object = MibTableColumn
v4cePetronasPsuInstance = _V4cePetronasPsuInstance_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2, 1, 1),
    _V4cePetronasPsuInstance_Type()
)
v4cePetronasPsuInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v4cePetronasPsuInstance.setStatus("current")
_V4cePetronasPsuOn_Type = TruthValue
_V4cePetronasPsuOn_Object = MibTableColumn
v4cePetronasPsuOn = _V4cePetronasPsuOn_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2, 1, 2),
    _V4cePetronasPsuOn_Type()
)
v4cePetronasPsuOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasPsuOn.setStatus("current")
_V4cePetronasPsuHealthy_Type = TruthValue
_V4cePetronasPsuHealthy_Object = MibTableColumn
v4cePetronasPsuHealthy = _V4cePetronasPsuHealthy_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2, 1, 3),
    _V4cePetronasPsuHealthy_Type()
)
v4cePetronasPsuHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasPsuHealthy.setStatus("current")
_V4cePetronasPsuTempOk_Type = TruthValue
_V4cePetronasPsuTempOk_Object = MibTableColumn
v4cePetronasPsuTempOk = _V4cePetronasPsuTempOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 2, 1, 4),
    _V4cePetronasPsuTempOk_Type()
)
v4cePetronasPsuTempOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasPsuTempOk.setStatus("current")
_V4cePetronasObjectsZeta_ObjectIdentity = ObjectIdentity
v4cePetronasObjectsZeta = _V4cePetronasObjectsZeta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 3)
)
_V4cePetronasZetaPowerOn_Type = TruthValue
_V4cePetronasZetaPowerOn_Object = MibScalar
v4cePetronasZetaPowerOn = _V4cePetronasZetaPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 3, 1),
    _V4cePetronasZetaPowerOn_Type()
)
v4cePetronasZetaPowerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasZetaPowerOn.setStatus("current")
_V4cePetronasZetaCommsOk_Type = TruthValue
_V4cePetronasZetaCommsOk_Object = MibScalar
v4cePetronasZetaCommsOk = _V4cePetronasZetaCommsOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 3, 2),
    _V4cePetronasZetaCommsOk_Type()
)
v4cePetronasZetaCommsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasZetaCommsOk.setStatus("current")
_V4cePetronasZetaBitWarnings_Type = Unsigned32
_V4cePetronasZetaBitWarnings_Object = MibScalar
v4cePetronasZetaBitWarnings = _V4cePetronasZetaBitWarnings_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 3, 3),
    _V4cePetronasZetaBitWarnings_Type()
)
v4cePetronasZetaBitWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasZetaBitWarnings.setStatus("current")
_V4cePetronasZetaBitErrors_Type = Unsigned32
_V4cePetronasZetaBitErrors_Object = MibScalar
v4cePetronasZetaBitErrors = _V4cePetronasZetaBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 3, 4),
    _V4cePetronasZetaBitErrors_Type()
)
v4cePetronasZetaBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasZetaBitErrors.setStatus("current")
_V4cePetronasCameraTable_Object = MibTable
v4cePetronasCameraTable = _V4cePetronasCameraTable_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4)
)
if mibBuilder.loadTexts:
    v4cePetronasCameraTable.setStatus("current")
_V4cePetronasCameraEntry_Object = MibTableRow
v4cePetronasCameraEntry = _V4cePetronasCameraEntry_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1)
)
v4cePetronasCameraEntry.setIndexNames(
    (0, "VISION4CE-PETRONAS-MIB", "v4cePetronasCameraInstance"),
)
if mibBuilder.loadTexts:
    v4cePetronasCameraEntry.setStatus("current")


class _V4cePetronasCameraInstance_Type(Integer32):
    """Custom type v4cePetronasCameraInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizonTI", 1),
          ("indraLRTV", 2))
    )


_V4cePetronasCameraInstance_Type.__name__ = "Integer32"
_V4cePetronasCameraInstance_Object = MibTableColumn
v4cePetronasCameraInstance = _V4cePetronasCameraInstance_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 1),
    _V4cePetronasCameraInstance_Type()
)
v4cePetronasCameraInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v4cePetronasCameraInstance.setStatus("current")
_V4cePetronasCameraPowerOn_Type = TruthValue
_V4cePetronasCameraPowerOn_Object = MibTableColumn
v4cePetronasCameraPowerOn = _V4cePetronasCameraPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 2),
    _V4cePetronasCameraPowerOn_Type()
)
v4cePetronasCameraPowerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraPowerOn.setStatus("current")
_V4cePetronasCameraCommsOk_Type = TruthValue
_V4cePetronasCameraCommsOk_Object = MibTableColumn
v4cePetronasCameraCommsOk = _V4cePetronasCameraCommsOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 3),
    _V4cePetronasCameraCommsOk_Type()
)
v4cePetronasCameraCommsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraCommsOk.setStatus("current")
_V4cePetronasCameraBitWarnings_Type = Unsigned32
_V4cePetronasCameraBitWarnings_Object = MibTableColumn
v4cePetronasCameraBitWarnings = _V4cePetronasCameraBitWarnings_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 4),
    _V4cePetronasCameraBitWarnings_Type()
)
v4cePetronasCameraBitWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraBitWarnings.setStatus("current")
_V4cePetronasCameraBitErrors_Type = Unsigned32
_V4cePetronasCameraBitErrors_Object = MibTableColumn
v4cePetronasCameraBitErrors = _V4cePetronasCameraBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 5),
    _V4cePetronasCameraBitErrors_Type()
)
v4cePetronasCameraBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraBitErrors.setStatus("current")
_V4cePetronasCameraVideoOk_Type = TruthValue
_V4cePetronasCameraVideoOk_Object = MibTableColumn
v4cePetronasCameraVideoOk = _V4cePetronasCameraVideoOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 6),
    _V4cePetronasCameraVideoOk_Type()
)
v4cePetronasCameraVideoOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraVideoOk.setStatus("current")
_V4cePetronasCameraHoursOn_Type = Unsigned32
_V4cePetronasCameraHoursOn_Object = MibTableColumn
v4cePetronasCameraHoursOn = _V4cePetronasCameraHoursOn_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 4, 1, 7),
    _V4cePetronasCameraHoursOn_Type()
)
v4cePetronasCameraHoursOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasCameraHoursOn.setStatus("current")
_V4cePetronasSpotlightTable_Object = MibTable
v4cePetronasSpotlightTable = _V4cePetronasSpotlightTable_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5)
)
if mibBuilder.loadTexts:
    v4cePetronasSpotlightTable.setStatus("current")
_V4cePetronasSpotlightEntry_Object = MibTableRow
v4cePetronasSpotlightEntry = _V4cePetronasSpotlightEntry_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5, 1)
)
v4cePetronasSpotlightEntry.setIndexNames(
    (0, "VISION4CE-PETRONAS-MIB", "v4cePetronasSpotlightInstance"),
)
if mibBuilder.loadTexts:
    v4cePetronasSpotlightEntry.setStatus("current")


class _V4cePetronasSpotlightInstance_Type(Integer32):
    """Custom type v4cePetronasSpotlightInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wide", 1),
          ("narrow", 2))
    )


_V4cePetronasSpotlightInstance_Type.__name__ = "Integer32"
_V4cePetronasSpotlightInstance_Object = MibTableColumn
v4cePetronasSpotlightInstance = _V4cePetronasSpotlightInstance_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5, 1, 1),
    _V4cePetronasSpotlightInstance_Type()
)
v4cePetronasSpotlightInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v4cePetronasSpotlightInstance.setStatus("current")
_V4cePetronasSpotlightOn_Type = TruthValue
_V4cePetronasSpotlightOn_Object = MibTableColumn
v4cePetronasSpotlightOn = _V4cePetronasSpotlightOn_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5, 1, 2),
    _V4cePetronasSpotlightOn_Type()
)
v4cePetronasSpotlightOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSpotlightOn.setStatus("current")
_V4cePetronasSpotlightBulbOk_Type = TruthValue
_V4cePetronasSpotlightBulbOk_Object = MibTableColumn
v4cePetronasSpotlightBulbOk = _V4cePetronasSpotlightBulbOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5, 1, 3),
    _V4cePetronasSpotlightBulbOk_Type()
)
v4cePetronasSpotlightBulbOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSpotlightBulbOk.setStatus("current")
_V4cePetronasSpotlightHoursLeft_Type = Unsigned32
_V4cePetronasSpotlightHoursLeft_Object = MibTableColumn
v4cePetronasSpotlightHoursLeft = _V4cePetronasSpotlightHoursLeft_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 5, 1, 4),
    _V4cePetronasSpotlightHoursLeft_Type()
)
v4cePetronasSpotlightHoursLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasSpotlightHoursLeft.setStatus("current")
_V4cePetronasObjectsAhd_ObjectIdentity = ObjectIdentity
v4cePetronasObjectsAhd = _V4cePetronasObjectsAhd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 6)
)
_V4cePetronasAhdCommsOk_Type = TruthValue
_V4cePetronasAhdCommsOk_Object = MibScalar
v4cePetronasAhdCommsOk = _V4cePetronasAhdCommsOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 6, 1),
    _V4cePetronasAhdCommsOk_Type()
)
v4cePetronasAhdCommsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasAhdCommsOk.setStatus("current")
_V4cePetronasAhdBitWarnings_Type = Unsigned32
_V4cePetronasAhdBitWarnings_Object = MibScalar
v4cePetronasAhdBitWarnings = _V4cePetronasAhdBitWarnings_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 6, 2),
    _V4cePetronasAhdBitWarnings_Type()
)
v4cePetronasAhdBitWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasAhdBitWarnings.setStatus("current")
_V4cePetronasAhdBitErrors_Type = Unsigned32
_V4cePetronasAhdBitErrors_Object = MibScalar
v4cePetronasAhdBitErrors = _V4cePetronasAhdBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 6, 3),
    _V4cePetronasAhdBitErrors_Type()
)
v4cePetronasAhdBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasAhdBitErrors.setStatus("current")
_V4cePetronasObjectsWash_ObjectIdentity = ObjectIdentity
v4cePetronasObjectsWash = _V4cePetronasObjectsWash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 7)
)
_V4cePetronasWashLevelOk_Type = TruthValue
_V4cePetronasWashLevelOk_Object = MibScalar
v4cePetronasWashLevelOk = _V4cePetronasWashLevelOk_Object(
    (1, 3, 6, 1, 4, 1, 48694, 3, 1, 7, 1),
    _V4cePetronasWashLevelOk_Type()
)
v4cePetronasWashLevelOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v4cePetronasWashLevelOk.setStatus("current")
_V4cePetronasComformance_ObjectIdentity = ObjectIdentity
v4cePetronasComformance = _V4cePetronasComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2)
)
_V4cePetronasCompliances_ObjectIdentity = ObjectIdentity
v4cePetronasCompliances = _V4cePetronasCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 1)
)
_V4cePetronasGroups_ObjectIdentity = ObjectIdentity
v4cePetronasGroups = _V4cePetronasGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2)
)

# Managed Objects groups

v4cePetronasSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 1)
)
v4cePetronasSystemGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasSysManAloftSw"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSysHeloOpsSw"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSysPlatCab"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSysLightCab"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSysLightningSpd"))
)
if mibBuilder.loadTexts:
    v4cePetronasSystemGroup.setStatus("current")

v4cePetronasPsuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 2)
)
v4cePetronasPsuGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasPsuOn"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasPsuHealthy"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasPsuTempOk"))
)
if mibBuilder.loadTexts:
    v4cePetronasPsuGroup.setStatus("current")

v4cePetronasZetaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 3)
)
v4cePetronasZetaGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasZetaPowerOn"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasZetaCommsOk"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasZetaBitWarnings"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasZetaBitErrors"))
)
if mibBuilder.loadTexts:
    v4cePetronasZetaGroup.setStatus("current")

v4cePetronasCameraGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 4)
)
v4cePetronasCameraGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraPowerOn"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraCommsOk"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraBitWarnings"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraBitErrors"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraVideoOk"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraHoursOn"))
)
if mibBuilder.loadTexts:
    v4cePetronasCameraGroup.setStatus("current")

v4cePetronasSpotlightGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 5)
)
v4cePetronasSpotlightGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasSpotlightOn"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSpotlightBulbOk"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSpotlightHoursLeft"))
)
if mibBuilder.loadTexts:
    v4cePetronasSpotlightGroup.setStatus("current")

v4cePetronasAhdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 6)
)
v4cePetronasAhdGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasAhdCommsOk"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasAhdBitWarnings"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasAhdBitErrors"))
)
if mibBuilder.loadTexts:
    v4cePetronasAhdGroup.setStatus("current")

v4cePetronasWashGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 7)
)
v4cePetronasWashGroup.setObjects(
    ("VISION4CE-PETRONAS-MIB", "v4cePetronasWashLevelOk")
)
if mibBuilder.loadTexts:
    v4cePetronasWashGroup.setStatus("current")

v4cePetronasMyAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 2, 8)
)
v4cePetronasMyAgentGroup.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasAbout"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasName"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasAge"))
)
if mibBuilder.loadTexts:
    v4cePetronasMyAgentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

v4cePetronasMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48694, 3, 2, 1, 1)
)
v4cePetronasMIBCompliance.setObjects(
      *(("VISION4CE-PETRONAS-MIB", "v4cePetronasSystemGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasPsuGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasZetaGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasCameraGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasSpotlightGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasAhdGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasWashGroup"),
        ("VISION4CE-PETRONAS-MIB", "v4cePetronasMyAgentGroup"))
)
if mibBuilder.loadTexts:
    v4cePetronasMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISION4CE-PETRONAS-MIB",
    **{"vision4ceTopLevel": vision4ceTopLevel,
       "v4cePetronasMIB": v4cePetronasMIB,
       "v4cePetronasNotifications": v4cePetronasNotifications,
       "v4cePetronasObjects": v4cePetronasObjects,
       "v4cePetronasObjects0": v4cePetronasObjects0,
       "v4cePetronasAbout": v4cePetronasAbout,
       "v4cePetronasName": v4cePetronasName,
       "v4cePetronasAge": v4cePetronasAge,
       "v4cePetronasObjectsSystem": v4cePetronasObjectsSystem,
       "v4cePetronasSysManAloftSw": v4cePetronasSysManAloftSw,
       "v4cePetronasSysHeloOpsSw": v4cePetronasSysHeloOpsSw,
       "v4cePetronasSysPlatCab": v4cePetronasSysPlatCab,
       "v4cePetronasSysLightCab": v4cePetronasSysLightCab,
       "v4cePetronasSysLightningSpd": v4cePetronasSysLightningSpd,
       "v4cePetronasPsuTable": v4cePetronasPsuTable,
       "v4cePetronasPsuEntry": v4cePetronasPsuEntry,
       "v4cePetronasPsuInstance": v4cePetronasPsuInstance,
       "v4cePetronasPsuOn": v4cePetronasPsuOn,
       "v4cePetronasPsuHealthy": v4cePetronasPsuHealthy,
       "v4cePetronasPsuTempOk": v4cePetronasPsuTempOk,
       "v4cePetronasObjectsZeta": v4cePetronasObjectsZeta,
       "v4cePetronasZetaPowerOn": v4cePetronasZetaPowerOn,
       "v4cePetronasZetaCommsOk": v4cePetronasZetaCommsOk,
       "v4cePetronasZetaBitWarnings": v4cePetronasZetaBitWarnings,
       "v4cePetronasZetaBitErrors": v4cePetronasZetaBitErrors,
       "v4cePetronasCameraTable": v4cePetronasCameraTable,
       "v4cePetronasCameraEntry": v4cePetronasCameraEntry,
       "v4cePetronasCameraInstance": v4cePetronasCameraInstance,
       "v4cePetronasCameraPowerOn": v4cePetronasCameraPowerOn,
       "v4cePetronasCameraCommsOk": v4cePetronasCameraCommsOk,
       "v4cePetronasCameraBitWarnings": v4cePetronasCameraBitWarnings,
       "v4cePetronasCameraBitErrors": v4cePetronasCameraBitErrors,
       "v4cePetronasCameraVideoOk": v4cePetronasCameraVideoOk,
       "v4cePetronasCameraHoursOn": v4cePetronasCameraHoursOn,
       "v4cePetronasSpotlightTable": v4cePetronasSpotlightTable,
       "v4cePetronasSpotlightEntry": v4cePetronasSpotlightEntry,
       "v4cePetronasSpotlightInstance": v4cePetronasSpotlightInstance,
       "v4cePetronasSpotlightOn": v4cePetronasSpotlightOn,
       "v4cePetronasSpotlightBulbOk": v4cePetronasSpotlightBulbOk,
       "v4cePetronasSpotlightHoursLeft": v4cePetronasSpotlightHoursLeft,
       "v4cePetronasObjectsAhd": v4cePetronasObjectsAhd,
       "v4cePetronasAhdCommsOk": v4cePetronasAhdCommsOk,
       "v4cePetronasAhdBitWarnings": v4cePetronasAhdBitWarnings,
       "v4cePetronasAhdBitErrors": v4cePetronasAhdBitErrors,
       "v4cePetronasObjectsWash": v4cePetronasObjectsWash,
       "v4cePetronasWashLevelOk": v4cePetronasWashLevelOk,
       "v4cePetronasComformance": v4cePetronasComformance,
       "v4cePetronasCompliances": v4cePetronasCompliances,
       "v4cePetronasMIBCompliance": v4cePetronasMIBCompliance,
       "v4cePetronasGroups": v4cePetronasGroups,
       "v4cePetronasSystemGroup": v4cePetronasSystemGroup,
       "v4cePetronasPsuGroup": v4cePetronasPsuGroup,
       "v4cePetronasZetaGroup": v4cePetronasZetaGroup,
       "v4cePetronasCameraGroup": v4cePetronasCameraGroup,
       "v4cePetronasSpotlightGroup": v4cePetronasSpotlightGroup,
       "v4cePetronasAhdGroup": v4cePetronasAhdGroup,
       "v4cePetronasWashGroup": v4cePetronasWashGroup,
       "v4cePetronasMyAgentGroup": v4cePetronasMyAgentGroup}
)
