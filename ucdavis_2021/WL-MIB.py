# SNMP MIB module (WL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/WL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class WlNWID(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



# MIB Managed Objects in the order of their OIDs

_Wavelan_ObjectIdentity = ObjectIdentity
wavelan = _Wavelan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3)
)
_WlIntTable_Object = MibTable
wlIntTable = _WlIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1)
)
if mibBuilder.loadTexts:
    wlIntTable.setStatus("mandatory")
_WlIntEntry_Object = MibTableRow
wlIntEntry = _WlIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1)
)
wlIntEntry.setIndexNames(
    (0, "WL-MIB", "wlIntIndex"),
)
if mibBuilder.loadTexts:
    wlIntEntry.setStatus("mandatory")
_WlIntIndex_Type = Integer32
_WlIntIndex_Object = MibTableColumn
wlIntIndex = _WlIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 1),
    _WlIntIndex_Type()
)
wlIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlIntIndex.setStatus("mandatory")


class _WlName_Type(DisplayString):
    """Custom type wlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_WlName_Type.__name__ = "DisplayString"
_WlName_Object = MibTableColumn
wlName = _WlName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 2),
    _WlName_Type()
)
wlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlName.setStatus("mandatory")


class _WlBrdType_Type(Integer32):
    """Custom type wlBrdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("MCA", 1),
          ("PCMCIA", 2),
          ("ISA", 3))
    )


_WlBrdType_Type.__name__ = "Integer32"
_WlBrdType_Object = MibTableColumn
wlBrdType = _WlBrdType_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 3),
    _WlBrdType_Type()
)
wlBrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBrdType.setStatus("mandatory")
_WlDefMAC_Type = MacAddress
_WlDefMAC_Object = MibTableColumn
wlDefMAC = _WlDefMAC_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 4),
    _WlDefMAC_Type()
)
wlDefMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlDefMAC.setStatus("mandatory")
_WlSoftMAC_Type = MacAddress
_WlSoftMAC_Object = MibTableColumn
wlSoftMAC = _WlSoftMAC_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 5),
    _WlSoftMAC_Type()
)
wlSoftMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlSoftMAC.setStatus("mandatory")


class _WlCurrMAC_Type(Integer32):
    """Custom type wlCurrMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("soft", 2))
    )


_WlCurrMAC_Type.__name__ = "Integer32"
_WlCurrMAC_Object = MibTableColumn
wlCurrMAC = _WlCurrMAC_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 6),
    _WlCurrMAC_Type()
)
wlCurrMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCurrMAC.setStatus("mandatory")


class _WlAdapter_Type(Integer32):
    """Custom type wlAdapter based on Integer32"""
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
        *(("pcat915", 1),
          ("pcmc915", 2),
          ("pcat24", 3),
          ("pcmc24", 4),
          ("pccard24", 5),
          ("unknown", 6))
    )


_WlAdapter_Type.__name__ = "Integer32"
_WlAdapter_Object = MibTableColumn
wlAdapter = _WlAdapter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 7),
    _WlAdapter_Type()
)
wlAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAdapter.setStatus("mandatory")


class _WlSubband_Type(Integer32):
    """Custom type wlSubband based on Integer32"""
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
        *(("wm915", 1),
          ("wl2425", 2),
          ("wl2460", 3),
          ("wl2484", 4),
          ("wl2430", 5),
          ("unknown", 6))
    )


_WlSubband_Type.__name__ = "Integer32"
_WlSubband_Object = MibTableColumn
wlSubband = _WlSubband_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 8),
    _WlSubband_Type()
)
wlSubband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlSubband.setStatus("mandatory")
_WlNWID_Type = WlNWID
_WlNWID_Object = MibTableColumn
wlNWID = _WlNWID_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 9),
    _WlNWID_Type()
)
wlNWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlNWID.setStatus("mandatory")
_WlNWIDen_Type = Integer32
_WlNWIDen_Object = MibTableColumn
wlNWIDen = _WlNWIDen_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 10),
    _WlNWIDen_Type()
)
wlNWIDen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlNWIDen.setStatus("mandatory")
_WlDESkey_Type = OctetString
_WlDESkey_Object = MibTableColumn
wlDESkey = _WlDESkey_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 11),
    _WlDESkey_Type()
)
wlDESkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlDESkey.setStatus("mandatory")
_WlDESen_Type = Integer32
_WlDESen_Object = MibTableColumn
wlDESen = _WlDESen_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 1, 1, 12),
    _WlDESen_Type()
)
wlDESen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlDESen.setStatus("mandatory")
_WlCacheTable_Object = MibTable
wlCacheTable = _WlCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2)
)
if mibBuilder.loadTexts:
    wlCacheTable.setStatus("mandatory")
_WlCacheEntry_Object = MibTableRow
wlCacheEntry = _WlCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1)
)
wlCacheEntry.setIndexNames(
    (0, "WL-MIB", "wlCacheMAC"),
)
if mibBuilder.loadTexts:
    wlCacheEntry.setStatus("mandatory")
_WlCacheMAC_Type = MacAddress
_WlCacheMAC_Object = MibTableColumn
wlCacheMAC = _WlCacheMAC_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 1),
    _WlCacheMAC_Type()
)
wlCacheMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheMAC.setStatus("mandatory")
_WlCacheIntIndex_Type = Integer32
_WlCacheIntIndex_Object = MibTableColumn
wlCacheIntIndex = _WlCacheIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 2),
    _WlCacheIntIndex_Type()
)
wlCacheIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheIntIndex.setStatus("mandatory")
_WlCacheIntName_Type = DisplayString
_WlCacheIntName_Object = MibTableColumn
wlCacheIntName = _WlCacheIntName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 3),
    _WlCacheIntName_Type()
)
wlCacheIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheIntName.setStatus("mandatory")
_WlCacheIP_Type = IpAddress
_WlCacheIP_Object = MibTableColumn
wlCacheIP = _WlCacheIP_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 4),
    _WlCacheIP_Type()
)
wlCacheIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheIP.setStatus("mandatory")
_WlCacheSignal_Type = Gauge32
_WlCacheSignal_Object = MibTableColumn
wlCacheSignal = _WlCacheSignal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 5),
    _WlCacheSignal_Type()
)
wlCacheSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheSignal.setStatus("mandatory")
_WlCacheSilence_Type = Gauge32
_WlCacheSilence_Object = MibTableColumn
wlCacheSilence = _WlCacheSilence_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 6),
    _WlCacheSilence_Type()
)
wlCacheSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheSilence.setStatus("mandatory")
_WlCacheQuality_Type = Gauge32
_WlCacheQuality_Object = MibTableColumn
wlCacheQuality = _WlCacheQuality_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 7),
    _WlCacheQuality_Type()
)
wlCacheQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheQuality.setStatus("mandatory")
_WlCacheSNR_Type = Gauge32
_WlCacheSNR_Object = MibTableColumn
wlCacheSNR = _WlCacheSNR_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 3, 2, 1, 8),
    _WlCacheSNR_Type()
)
wlCacheSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlCacheSNR.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WL-MIB",
    **{"WlNWID": WlNWID,
       "wavelan": wavelan,
       "wlIntTable": wlIntTable,
       "wlIntEntry": wlIntEntry,
       "wlIntIndex": wlIntIndex,
       "wlName": wlName,
       "wlBrdType": wlBrdType,
       "wlDefMAC": wlDefMAC,
       "wlSoftMAC": wlSoftMAC,
       "wlCurrMAC": wlCurrMAC,
       "wlAdapter": wlAdapter,
       "wlSubband": wlSubband,
       "wlNWID": wlNWID,
       "wlNWIDen": wlNWIDen,
       "wlDESkey": wlDESkey,
       "wlDESen": wlDESen,
       "wlCacheTable": wlCacheTable,
       "wlCacheEntry": wlCacheEntry,
       "wlCacheMAC": wlCacheMAC,
       "wlCacheIntIndex": wlCacheIntIndex,
       "wlCacheIntName": wlCacheIntName,
       "wlCacheIP": wlCacheIP,
       "wlCacheSignal": wlCacheSignal,
       "wlCacheSilence": wlCacheSilence,
       "wlCacheQuality": wlCacheQuality,
       "wlCacheSNR": wlCacheSNR}
)
