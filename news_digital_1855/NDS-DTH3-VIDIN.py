# SNMP MIB module (NDS-DTH3-VIDIN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-VIDIN.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VidinEnc_ObjectIdentity = ObjectIdentity
vidinEnc = _VidinEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4)
)


class _VidinHardwareRelease_Type(DisplayString):
    """Custom type vidinHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VidinHardwareRelease_Type.__name__ = "DisplayString"
_VidinHardwareRelease_Object = MibScalar
vidinHardwareRelease = _VidinHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 1),
    _VidinHardwareRelease_Type()
)
vidinHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidinHardwareRelease.setStatus("current")


class _VidinSoftwareRelease_Type(DisplayString):
    """Custom type vidinSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VidinSoftwareRelease_Type.__name__ = "DisplayString"
_VidinSoftwareRelease_Object = MibScalar
vidinSoftwareRelease = _VidinSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 2),
    _VidinSoftwareRelease_Type()
)
vidinSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidinSoftwareRelease.setStatus("current")


class _VidinFirmwareRelease_Type(DisplayString):
    """Custom type vidinFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VidinFirmwareRelease_Type.__name__ = "DisplayString"
_VidinFirmwareRelease_Object = MibScalar
vidinFirmwareRelease = _VidinFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 3),
    _VidinFirmwareRelease_Type()
)
vidinFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidinFirmwareRelease.setStatus("current")
_VidinnextTimeDate_Type = DateAndTime
_VidinnextTimeDate_Object = MibScalar
vidinnextTimeDate = _VidinnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 4),
    _VidinnextTimeDate_Type()
)
vidinnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinnextTimeDate.setStatus("current")
_VidinTable_Object = MibTable
vidinTable = _VidinTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    vidinTable.setStatus("current")
_VidinEntry_Object = MibTableRow
vidinEntry = _VidinEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1)
)
vidinEntry.setIndexNames(
    (0, "NDS-DTH3-VIDIN", "vidinCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    vidinEntry.setStatus("current")


class _VidinCurrentNextIndex_Type(Integer32):
    """Custom type vidinCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_VidinCurrentNextIndex_Type.__name__ = "Integer32"
_VidinCurrentNextIndex_Object = MibTableColumn
vidinCurrentNextIndex = _VidinCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 1),
    _VidinCurrentNextIndex_Type()
)
vidinCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidinCurrentNextIndex.setStatus("current")


class _VidinSource_Type(Integer32):
    """Custom type vidinSource based on Integer32"""
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
        *(("off-serial-test-pattern", 0),
          ("composite", 1),
          ("component-YCrCb", 2),
          ("component-YPrPb-Pedastal", 3),
          ("component-YPrPb-BetaLevels", 4))
    )


_VidinSource_Type.__name__ = "Integer32"
_VidinSource_Object = MibTableColumn
vidinSource = _VidinSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 2),
    _VidinSource_Type()
)
vidinSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinSource.setStatus("current")


class _VidinCompositeMode_Type(Integer32):
    """Custom type vidinCompositeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pAL-I", 0),
          ("nTSC", 1),
          ("nTSCnoPedastal", 2),
          ("pAL-M", 3),
          ("pAL-N-Argentina-Uruguay-Paraguay", 6),
          ("pAL-N-Jamaica", 7),
          ("pAL-D-China", 8))
    )


_VidinCompositeMode_Type.__name__ = "Integer32"
_VidinCompositeMode_Object = MibTableColumn
vidinCompositeMode = _VidinCompositeMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 3),
    _VidinCompositeMode_Type()
)
vidinCompositeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinCompositeMode.setStatus("current")


class _VidinAGC_Type(Integer32):
    """Custom type vidinAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("off", 0)
    )


_VidinAGC_Type.__name__ = "Integer32"
_VidinAGC_Object = MibTableColumn
vidinAGC = _VidinAGC_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 4),
    _VidinAGC_Type()
)
vidinAGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinAGC.setStatus("current")


class _VidinSetup_Type(Integer32):
    """Custom type vidinSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("setupmode", 1))
    )


_VidinSetup_Type.__name__ = "Integer32"
_VidinSetup_Object = MibTableColumn
vidinSetup = _VidinSetup_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 5),
    _VidinSetup_Type()
)
vidinSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinSetup.setStatus("current")


class _VidinTermination_Type(Integer32):
    """Custom type vidinTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VidinTermination_Type.__name__ = "Integer32"
_VidinTermination_Object = MibTableColumn
vidinTermination = _VidinTermination_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 4, 5, 1, 6),
    _VidinTermination_Type()
)
vidinTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidinTermination.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-VIDIN",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "vidinEnc": vidinEnc,
       "vidinHardwareRelease": vidinHardwareRelease,
       "vidinSoftwareRelease": vidinSoftwareRelease,
       "vidinFirmwareRelease": vidinFirmwareRelease,
       "vidinnextTimeDate": vidinnextTimeDate,
       "vidinTable": vidinTable,
       "vidinEntry": vidinEntry,
       "vidinCurrentNextIndex": vidinCurrentNextIndex,
       "vidinSource": vidinSource,
       "vidinCompositeMode": vidinCompositeMode,
       "vidinAGC": vidinAGC,
       "vidinSetup": vidinSetup,
       "vidinTermination": vidinTermination}
)
