# SNMP MIB module (ME1200-MEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-MEP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200MepDmTimeUnit,
 ME1200MepInstanceDirection,
 ME1200MepTxRate,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200MepDmTimeUnit",
    "ME1200MepInstanceDirection",
    "ME1200MepTxRate",
    "ME1200RowEditorState",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200MepMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46)
)
if mibBuilder.loadTexts:
    me1200MepMib.setRevisions(
        ("2016-12-13 00:00",
         "2016-11-23 00:00",
         "2016-11-03 00:00",
         "2016-10-12 00:00",
         "2016-07-22 00:00",
         "2016-05-16 00:00",
         "2016-05-11 00:00",
         "2014-12-03 00:00",
         "2014-06-30 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-30 00:00",
         "2014-01-29 00:00",
         "2013-10-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200Action(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableDm", 0),
          ("continueDm", 1))
    )



class ME1200ApsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalidAps", 0),
          ("linearAps", 1),
          ("ringAps", 2))
    )



class ME1200AvailState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )



class ME1200CalcWay(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("roundTrip", 0),
          ("flow", 1))
    )



class ME1200Cast(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uniCast", 0),
          ("multiCast", 1))
    )



class ME1200Ended(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("singleEnded", 0),
          ("dualEnded", 1))
    )



class ME1200InstanceDomain(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("evc", 1),
          ("vlan", 2))
    )



class ME1200InstanceMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mep", 0),
          ("mip", 1))
    )



class ME1200MegIdFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ituIcc", 0),
          ("ieeeString", 1),
          ("ituCcIcc", 2))
    )



class ME1200RelayAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("relayUnknown", 0),
          ("relayHit", 1),
          ("relayFdb", 2),
          ("relayMpdb", 3))
    )



class ME1200TstPattern(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allZero", 0),
          ("allOne", 1),
          ("hexAA", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200MepMibObjects_ObjectIdentity = ObjectIdentity
me1200MepMibObjects = _Me1200MepMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1)
)
_Me1200MepCapabilities_ObjectIdentity = ObjectIdentity
me1200MepCapabilities = _Me1200MepCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1)
)
_Me1200MepCapabilitiesInstanceMax_Type = Unsigned32
_Me1200MepCapabilitiesInstanceMax_Object = MibScalar
me1200MepCapabilitiesInstanceMax = _Me1200MepCapabilitiesInstanceMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 1),
    _Me1200MepCapabilitiesInstanceMax_Type()
)
me1200MepCapabilitiesInstanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesInstanceMax.setStatus("current")
_Me1200MepCapabilitiesPeerMax_Type = Unsigned32
_Me1200MepCapabilitiesPeerMax_Object = MibScalar
me1200MepCapabilitiesPeerMax = _Me1200MepCapabilitiesPeerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 2),
    _Me1200MepCapabilitiesPeerMax_Type()
)
me1200MepCapabilitiesPeerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesPeerMax.setStatus("current")
_Me1200MepCapabilitiesTransactionMax_Type = Unsigned32
_Me1200MepCapabilitiesTransactionMax_Object = MibScalar
me1200MepCapabilitiesTransactionMax = _Me1200MepCapabilitiesTransactionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 3),
    _Me1200MepCapabilitiesTransactionMax_Type()
)
me1200MepCapabilitiesTransactionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesTransactionMax.setStatus("current")
_Me1200MepCapabilitiesReplyMax_Type = Unsigned32
_Me1200MepCapabilitiesReplyMax_Object = MibScalar
me1200MepCapabilitiesReplyMax = _Me1200MepCapabilitiesReplyMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 4),
    _Me1200MepCapabilitiesReplyMax_Type()
)
me1200MepCapabilitiesReplyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesReplyMax.setStatus("current")
_Me1200MepCapabilitiesClientFlowsMax_Type = Unsigned32
_Me1200MepCapabilitiesClientFlowsMax_Object = MibScalar
me1200MepCapabilitiesClientFlowsMax = _Me1200MepCapabilitiesClientFlowsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 5),
    _Me1200MepCapabilitiesClientFlowsMax_Type()
)
me1200MepCapabilitiesClientFlowsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesClientFlowsMax.setStatus("current")
_Me1200MepCapabilitiesMacMength_Type = Unsigned32
_Me1200MepCapabilitiesMacMength_Object = MibScalar
me1200MepCapabilitiesMacMength = _Me1200MepCapabilitiesMacMength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 6),
    _Me1200MepCapabilitiesMacMength_Type()
)
me1200MepCapabilitiesMacMength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesMacMength.setStatus("current")
_Me1200MepCapabilitiesMegCodeLength_Type = Unsigned32
_Me1200MepCapabilitiesMegCodeLength_Object = MibScalar
me1200MepCapabilitiesMegCodeLength = _Me1200MepCapabilitiesMegCodeLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 7),
    _Me1200MepCapabilitiesMegCodeLength_Type()
)
me1200MepCapabilitiesMegCodeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesMegCodeLength.setStatus("current")
_Me1200MepCapabilitiesDmIntervalMin_Type = Unsigned32
_Me1200MepCapabilitiesDmIntervalMin_Object = MibScalar
me1200MepCapabilitiesDmIntervalMin = _Me1200MepCapabilitiesDmIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 8),
    _Me1200MepCapabilitiesDmIntervalMin_Type()
)
me1200MepCapabilitiesDmIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmIntervalMin.setStatus("current")
_Me1200MepCapabilitiesDmIntervalMax_Type = Unsigned32
_Me1200MepCapabilitiesDmIntervalMax_Object = MibScalar
me1200MepCapabilitiesDmIntervalMax = _Me1200MepCapabilitiesDmIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 9),
    _Me1200MepCapabilitiesDmIntervalMax_Type()
)
me1200MepCapabilitiesDmIntervalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmIntervalMax.setStatus("current")
_Me1200MepCapabilitiesDmLastnMin_Type = Unsigned32
_Me1200MepCapabilitiesDmLastnMin_Object = MibScalar
me1200MepCapabilitiesDmLastnMin = _Me1200MepCapabilitiesDmLastnMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 10),
    _Me1200MepCapabilitiesDmLastnMin_Type()
)
me1200MepCapabilitiesDmLastnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmLastnMin.setStatus("current")
_Me1200MepCapabilitiesDmLastnMax_Type = Unsigned32
_Me1200MepCapabilitiesDmLastnMax_Object = MibScalar
me1200MepCapabilitiesDmLastnMax = _Me1200MepCapabilitiesDmLastnMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 11),
    _Me1200MepCapabilitiesDmLastnMax_Type()
)
me1200MepCapabilitiesDmLastnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmLastnMax.setStatus("current")
_Me1200MepCapabilitiesLbmSizeMax_Type = Unsigned32
_Me1200MepCapabilitiesLbmSizeMax_Object = MibScalar
me1200MepCapabilitiesLbmSizeMax = _Me1200MepCapabilitiesLbmSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 12),
    _Me1200MepCapabilitiesLbmSizeMax_Type()
)
me1200MepCapabilitiesLbmSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesLbmSizeMax.setStatus("current")
_Me1200MepCapabilitiesLbmSizeMin_Type = Unsigned32
_Me1200MepCapabilitiesLbmSizeMin_Object = MibScalar
me1200MepCapabilitiesLbmSizeMin = _Me1200MepCapabilitiesLbmSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 13),
    _Me1200MepCapabilitiesLbmSizeMin_Type()
)
me1200MepCapabilitiesLbmSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesLbmSizeMin.setStatus("current")
_Me1200MepCapabilitiesTstSizeMax_Type = Unsigned32
_Me1200MepCapabilitiesTstSizeMax_Object = MibScalar
me1200MepCapabilitiesTstSizeMax = _Me1200MepCapabilitiesTstSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 14),
    _Me1200MepCapabilitiesTstSizeMax_Type()
)
me1200MepCapabilitiesTstSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesTstSizeMax.setStatus("current")
_Me1200MepCapabilitiesTstSizeMin_Type = Unsigned32
_Me1200MepCapabilitiesTstSizeMin_Object = MibScalar
me1200MepCapabilitiesTstSizeMin = _Me1200MepCapabilitiesTstSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 15),
    _Me1200MepCapabilitiesTstSizeMin_Type()
)
me1200MepCapabilitiesTstSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesTstSizeMin.setStatus("current")
_Me1200MepCapabilitiesTstRateMax_Type = Unsigned32
_Me1200MepCapabilitiesTstRateMax_Object = MibScalar
me1200MepCapabilitiesTstRateMax = _Me1200MepCapabilitiesTstRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 16),
    _Me1200MepCapabilitiesTstRateMax_Type()
)
me1200MepCapabilitiesTstRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesTstRateMax.setStatus("current")
_Me1200MepCapabilitiesClientPrioHighest_Type = Unsigned32
_Me1200MepCapabilitiesClientPrioHighest_Object = MibScalar
me1200MepCapabilitiesClientPrioHighest = _Me1200MepCapabilitiesClientPrioHighest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 17),
    _Me1200MepCapabilitiesClientPrioHighest_Type()
)
me1200MepCapabilitiesClientPrioHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesClientPrioHighest.setStatus("current")
_Me1200MepCapabilitiesLbToSendInfinite_Type = Unsigned32
_Me1200MepCapabilitiesLbToSendInfinite_Object = MibScalar
me1200MepCapabilitiesLbToSendInfinite = _Me1200MepCapabilitiesLbToSendInfinite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 18),
    _Me1200MepCapabilitiesLbToSendInfinite_Type()
)
me1200MepCapabilitiesLbToSendInfinite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesLbToSendInfinite.setStatus("current")
_Me1200MepCapabilitiesLmLossRatioThresholdMin_Type = Unsigned32
_Me1200MepCapabilitiesLmLossRatioThresholdMin_Object = MibScalar
me1200MepCapabilitiesLmLossRatioThresholdMin = _Me1200MepCapabilitiesLmLossRatioThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 19),
    _Me1200MepCapabilitiesLmLossRatioThresholdMin_Type()
)
me1200MepCapabilitiesLmLossRatioThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesLmLossRatioThresholdMin.setStatus("current")
_Me1200MepCapabilitiesLmLossRatioThresholdMax_Type = Unsigned32
_Me1200MepCapabilitiesLmLossRatioThresholdMax_Object = MibScalar
me1200MepCapabilitiesLmLossRatioThresholdMax = _Me1200MepCapabilitiesLmLossRatioThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 20),
    _Me1200MepCapabilitiesLmLossRatioThresholdMax_Type()
)
me1200MepCapabilitiesLmLossRatioThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesLmLossRatioThresholdMax.setStatus("current")
_Me1200MepCapabilitiesDmAverageDelayThresholdMin_Type = Unsigned32
_Me1200MepCapabilitiesDmAverageDelayThresholdMin_Object = MibScalar
me1200MepCapabilitiesDmAverageDelayThresholdMin = _Me1200MepCapabilitiesDmAverageDelayThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 21),
    _Me1200MepCapabilitiesDmAverageDelayThresholdMin_Type()
)
me1200MepCapabilitiesDmAverageDelayThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmAverageDelayThresholdMin.setStatus("current")
_Me1200MepCapabilitiesDmAverageDelayThresholdMax_Type = Unsigned32
_Me1200MepCapabilitiesDmAverageDelayThresholdMax_Object = MibScalar
me1200MepCapabilitiesDmAverageDelayThresholdMax = _Me1200MepCapabilitiesDmAverageDelayThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 22),
    _Me1200MepCapabilitiesDmAverageDelayThresholdMax_Type()
)
me1200MepCapabilitiesDmAverageDelayThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesDmAverageDelayThresholdMax.setStatus("current")
_Me1200MepCapabilitiesSlmSizeMax_Type = Unsigned32
_Me1200MepCapabilitiesSlmSizeMax_Object = MibScalar
me1200MepCapabilitiesSlmSizeMax = _Me1200MepCapabilitiesSlmSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 23),
    _Me1200MepCapabilitiesSlmSizeMax_Type()
)
me1200MepCapabilitiesSlmSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesSlmSizeMax.setStatus("current")
_Me1200MepCapabilitiesSlmSizeMin_Type = Unsigned32
_Me1200MepCapabilitiesSlmSizeMin_Object = MibScalar
me1200MepCapabilitiesSlmSizeMin = _Me1200MepCapabilitiesSlmSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 1, 24),
    _Me1200MepCapabilitiesSlmSizeMin_Type()
)
me1200MepCapabilitiesSlmSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MepCapabilitiesSlmSizeMin.setStatus("current")
_Me1200MepConfig_ObjectIdentity = ObjectIdentity
me1200MepConfig = _Me1200MepConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2)
)
_Me1200ConfigInstance_ObjectIdentity = ObjectIdentity
me1200ConfigInstance = _Me1200ConfigInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1)
)
_Me1200ConfigInstanceTable_Object = MibTable
me1200ConfigInstanceTable = _Me1200ConfigInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigInstanceTable.setStatus("current")
_Me1200ConfigInstanceEntry_Object = MibTableRow
me1200ConfigInstanceEntry = _Me1200ConfigInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1)
)
me1200ConfigInstanceEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigInstanceId"),
)
if mibBuilder.loadTexts:
    me1200ConfigInstanceEntry.setStatus("current")


class _Me1200ConfigInstanceId_Type(Integer32):
    """Custom type me1200ConfigInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstanceId_Type.__name__ = "Integer32"
_Me1200ConfigInstanceId_Object = MibTableColumn
me1200ConfigInstanceId = _Me1200ConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 1),
    _Me1200ConfigInstanceId_Type()
)
me1200ConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigInstanceId.setStatus("current")
_Me1200ConfigInstanceMode_Type = ME1200InstanceMode
_Me1200ConfigInstanceMode_Object = MibTableColumn
me1200ConfigInstanceMode = _Me1200ConfigInstanceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 2),
    _Me1200ConfigInstanceMode_Type()
)
me1200ConfigInstanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceMode.setStatus("current")
_Me1200ConfigInstanceDirection_Type = ME1200MepInstanceDirection
_Me1200ConfigInstanceDirection_Object = MibTableColumn
me1200ConfigInstanceDirection = _Me1200ConfigInstanceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 3),
    _Me1200ConfigInstanceDirection_Type()
)
me1200ConfigInstanceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceDirection.setStatus("current")
_Me1200ConfigInstanceDomain_Type = ME1200InstanceDomain
_Me1200ConfigInstanceDomain_Object = MibTableColumn
me1200ConfigInstanceDomain = _Me1200ConfigInstanceDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 4),
    _Me1200ConfigInstanceDomain_Type()
)
me1200ConfigInstanceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceDomain.setStatus("current")
_Me1200ConfigInstanceFlow_Type = Unsigned32
_Me1200ConfigInstanceFlow_Object = MibTableColumn
me1200ConfigInstanceFlow = _Me1200ConfigInstanceFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 5),
    _Me1200ConfigInstanceFlow_Type()
)
me1200ConfigInstanceFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceFlow.setStatus("current")
_Me1200ConfigInstancePort_Type = ME1200InterfaceIndex
_Me1200ConfigInstancePort_Object = MibTableColumn
me1200ConfigInstancePort = _Me1200ConfigInstancePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 6),
    _Me1200ConfigInstancePort_Type()
)
me1200ConfigInstancePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePort.setStatus("current")
_Me1200ConfigInstanceLevel_Type = Unsigned32
_Me1200ConfigInstanceLevel_Object = MibTableColumn
me1200ConfigInstanceLevel = _Me1200ConfigInstanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 7),
    _Me1200ConfigInstanceLevel_Type()
)
me1200ConfigInstanceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceLevel.setStatus("current")
_Me1200ConfigInstanceVid_Type = ME1200Unsigned16
_Me1200ConfigInstanceVid_Object = MibTableColumn
me1200ConfigInstanceVid = _Me1200ConfigInstanceVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 8),
    _Me1200ConfigInstanceVid_Type()
)
me1200ConfigInstanceVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceVid.setStatus("current")
_Me1200ConfigInstanceVoe_Type = TruthValue
_Me1200ConfigInstanceVoe_Object = MibTableColumn
me1200ConfigInstanceVoe = _Me1200ConfigInstanceVoe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 9),
    _Me1200ConfigInstanceVoe_Type()
)
me1200ConfigInstanceVoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceVoe.setStatus("current")
_Me1200ConfigInstanceMac_Type = MacAddress
_Me1200ConfigInstanceMac_Object = MibTableColumn
me1200ConfigInstanceMac = _Me1200ConfigInstanceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 10),
    _Me1200ConfigInstanceMac_Type()
)
me1200ConfigInstanceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceMac.setStatus("current")
_Me1200ConfigInstanceFormat_Type = ME1200MegIdFormat
_Me1200ConfigInstanceFormat_Object = MibTableColumn
me1200ConfigInstanceFormat = _Me1200ConfigInstanceFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 11),
    _Me1200ConfigInstanceFormat_Type()
)
me1200ConfigInstanceFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceFormat.setStatus("current")


class _Me1200ConfigInstanceName_Type(ME1200DisplayString):
    """Custom type me1200ConfigInstanceName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200ConfigInstanceName_Type.__name__ = "ME1200DisplayString"
_Me1200ConfigInstanceName_Object = MibTableColumn
me1200ConfigInstanceName = _Me1200ConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 12),
    _Me1200ConfigInstanceName_Type()
)
me1200ConfigInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceName.setStatus("current")


class _Me1200ConfigInstanceMeg_Type(ME1200DisplayString):
    """Custom type me1200ConfigInstanceMeg based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200ConfigInstanceMeg_Type.__name__ = "ME1200DisplayString"
_Me1200ConfigInstanceMeg_Object = MibTableColumn
me1200ConfigInstanceMeg = _Me1200ConfigInstanceMeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 13),
    _Me1200ConfigInstanceMeg_Type()
)
me1200ConfigInstanceMeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceMeg.setStatus("current")
_Me1200ConfigInstanceMep_Type = Unsigned32
_Me1200ConfigInstanceMep_Object = MibTableColumn
me1200ConfigInstanceMep = _Me1200ConfigInstanceMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 14),
    _Me1200ConfigInstanceMep_Type()
)
me1200ConfigInstanceMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceMep.setStatus("current")
_Me1200ConfigInstanceAction_Type = ME1200RowEditorState
_Me1200ConfigInstanceAction_Object = MibTableColumn
me1200ConfigInstanceAction = _Me1200ConfigInstanceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 1, 1, 100),
    _Me1200ConfigInstanceAction_Type()
)
me1200ConfigInstanceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceAction.setStatus("current")
_Me1200ConfigInstanceRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigInstanceRowEditor = _Me1200ConfigInstanceRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2)
)


class _Me1200ConfigInstanceRowEditorId_Type(Integer32):
    """Custom type me1200ConfigInstanceRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstanceRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigInstanceRowEditorId_Object = MibScalar
me1200ConfigInstanceRowEditorId = _Me1200ConfigInstanceRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 1),
    _Me1200ConfigInstanceRowEditorId_Type()
)
me1200ConfigInstanceRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorId.setStatus("current")
_Me1200ConfigInstanceRowEditorMode_Type = ME1200InstanceMode
_Me1200ConfigInstanceRowEditorMode_Object = MibScalar
me1200ConfigInstanceRowEditorMode = _Me1200ConfigInstanceRowEditorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 2),
    _Me1200ConfigInstanceRowEditorMode_Type()
)
me1200ConfigInstanceRowEditorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorMode.setStatus("current")
_Me1200ConfigInstanceRowEditorDirection_Type = ME1200MepInstanceDirection
_Me1200ConfigInstanceRowEditorDirection_Object = MibScalar
me1200ConfigInstanceRowEditorDirection = _Me1200ConfigInstanceRowEditorDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 3),
    _Me1200ConfigInstanceRowEditorDirection_Type()
)
me1200ConfigInstanceRowEditorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorDirection.setStatus("current")
_Me1200ConfigInstanceRowEditorDomain_Type = ME1200InstanceDomain
_Me1200ConfigInstanceRowEditorDomain_Object = MibScalar
me1200ConfigInstanceRowEditorDomain = _Me1200ConfigInstanceRowEditorDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 4),
    _Me1200ConfigInstanceRowEditorDomain_Type()
)
me1200ConfigInstanceRowEditorDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorDomain.setStatus("current")
_Me1200ConfigInstanceRowEditorFlow_Type = Unsigned32
_Me1200ConfigInstanceRowEditorFlow_Object = MibScalar
me1200ConfigInstanceRowEditorFlow = _Me1200ConfigInstanceRowEditorFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 5),
    _Me1200ConfigInstanceRowEditorFlow_Type()
)
me1200ConfigInstanceRowEditorFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorFlow.setStatus("current")
_Me1200ConfigInstanceRowEditorPort_Type = ME1200InterfaceIndex
_Me1200ConfigInstanceRowEditorPort_Object = MibScalar
me1200ConfigInstanceRowEditorPort = _Me1200ConfigInstanceRowEditorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 6),
    _Me1200ConfigInstanceRowEditorPort_Type()
)
me1200ConfigInstanceRowEditorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorPort.setStatus("current")
_Me1200ConfigInstanceRowEditorLevel_Type = Unsigned32
_Me1200ConfigInstanceRowEditorLevel_Object = MibScalar
me1200ConfigInstanceRowEditorLevel = _Me1200ConfigInstanceRowEditorLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 7),
    _Me1200ConfigInstanceRowEditorLevel_Type()
)
me1200ConfigInstanceRowEditorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorLevel.setStatus("current")
_Me1200ConfigInstanceRowEditorVid_Type = ME1200Unsigned16
_Me1200ConfigInstanceRowEditorVid_Object = MibScalar
me1200ConfigInstanceRowEditorVid = _Me1200ConfigInstanceRowEditorVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 8),
    _Me1200ConfigInstanceRowEditorVid_Type()
)
me1200ConfigInstanceRowEditorVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorVid.setStatus("current")
_Me1200ConfigInstanceRowEditorVoe_Type = TruthValue
_Me1200ConfigInstanceRowEditorVoe_Object = MibScalar
me1200ConfigInstanceRowEditorVoe = _Me1200ConfigInstanceRowEditorVoe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 9),
    _Me1200ConfigInstanceRowEditorVoe_Type()
)
me1200ConfigInstanceRowEditorVoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorVoe.setStatus("current")
_Me1200ConfigInstanceRowEditorMac_Type = MacAddress
_Me1200ConfigInstanceRowEditorMac_Object = MibScalar
me1200ConfigInstanceRowEditorMac = _Me1200ConfigInstanceRowEditorMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 10),
    _Me1200ConfigInstanceRowEditorMac_Type()
)
me1200ConfigInstanceRowEditorMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorMac.setStatus("current")
_Me1200ConfigInstanceRowEditorFormat_Type = ME1200MegIdFormat
_Me1200ConfigInstanceRowEditorFormat_Object = MibScalar
me1200ConfigInstanceRowEditorFormat = _Me1200ConfigInstanceRowEditorFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 11),
    _Me1200ConfigInstanceRowEditorFormat_Type()
)
me1200ConfigInstanceRowEditorFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorFormat.setStatus("current")


class _Me1200ConfigInstanceRowEditorName_Type(ME1200DisplayString):
    """Custom type me1200ConfigInstanceRowEditorName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200ConfigInstanceRowEditorName_Type.__name__ = "ME1200DisplayString"
_Me1200ConfigInstanceRowEditorName_Object = MibScalar
me1200ConfigInstanceRowEditorName = _Me1200ConfigInstanceRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 12),
    _Me1200ConfigInstanceRowEditorName_Type()
)
me1200ConfigInstanceRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorName.setStatus("current")


class _Me1200ConfigInstanceRowEditorMeg_Type(ME1200DisplayString):
    """Custom type me1200ConfigInstanceRowEditorMeg based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200ConfigInstanceRowEditorMeg_Type.__name__ = "ME1200DisplayString"
_Me1200ConfigInstanceRowEditorMeg_Object = MibScalar
me1200ConfigInstanceRowEditorMeg = _Me1200ConfigInstanceRowEditorMeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 13),
    _Me1200ConfigInstanceRowEditorMeg_Type()
)
me1200ConfigInstanceRowEditorMeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorMeg.setStatus("current")
_Me1200ConfigInstanceRowEditorMep_Type = Unsigned32
_Me1200ConfigInstanceRowEditorMep_Object = MibScalar
me1200ConfigInstanceRowEditorMep = _Me1200ConfigInstanceRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 14),
    _Me1200ConfigInstanceRowEditorMep_Type()
)
me1200ConfigInstanceRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorMep.setStatus("current")
_Me1200ConfigInstanceRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigInstanceRowEditorAction_Object = MibScalar
me1200ConfigInstanceRowEditorAction = _Me1200ConfigInstanceRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 2, 100),
    _Me1200ConfigInstanceRowEditorAction_Type()
)
me1200ConfigInstanceRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorAction.setStatus("current")
_Me1200ConfigInstancePeerTable_Object = MibTable
me1200ConfigInstancePeerTable = _Me1200ConfigInstancePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerTable.setStatus("current")
_Me1200ConfigInstancePeerEntry_Object = MibTableRow
me1200ConfigInstancePeerEntry = _Me1200ConfigInstancePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3, 1)
)
me1200ConfigInstancePeerEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigInstancePeerId"),
    (0, "ME1200-MEP-MIB", "me1200ConfigInstancePeerPeerId"),
)
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerEntry.setStatus("current")


class _Me1200ConfigInstancePeerId_Type(Integer32):
    """Custom type me1200ConfigInstancePeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstancePeerId_Type.__name__ = "Integer32"
_Me1200ConfigInstancePeerId_Object = MibTableColumn
me1200ConfigInstancePeerId = _Me1200ConfigInstancePeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3, 1, 1),
    _Me1200ConfigInstancePeerId_Type()
)
me1200ConfigInstancePeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerId.setStatus("current")


class _Me1200ConfigInstancePeerPeerId_Type(Integer32):
    """Custom type me1200ConfigInstancePeerPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstancePeerPeerId_Type.__name__ = "Integer32"
_Me1200ConfigInstancePeerPeerId_Object = MibTableColumn
me1200ConfigInstancePeerPeerId = _Me1200ConfigInstancePeerPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3, 1, 2),
    _Me1200ConfigInstancePeerPeerId_Type()
)
me1200ConfigInstancePeerPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerPeerId.setStatus("current")
_Me1200ConfigInstancePeerMac_Type = MacAddress
_Me1200ConfigInstancePeerMac_Object = MibTableColumn
me1200ConfigInstancePeerMac = _Me1200ConfigInstancePeerMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3, 1, 3),
    _Me1200ConfigInstancePeerMac_Type()
)
me1200ConfigInstancePeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerMac.setStatus("current")
_Me1200ConfigInstancePeerAction_Type = ME1200RowEditorState
_Me1200ConfigInstancePeerAction_Object = MibTableColumn
me1200ConfigInstancePeerAction = _Me1200ConfigInstancePeerAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 3, 1, 100),
    _Me1200ConfigInstancePeerAction_Type()
)
me1200ConfigInstancePeerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerAction.setStatus("current")
_Me1200ConfigInstancePeerRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigInstancePeerRowEditor = _Me1200ConfigInstancePeerRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 4)
)


class _Me1200ConfigInstancePeerRowEditorId_Type(Integer32):
    """Custom type me1200ConfigInstancePeerRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstancePeerRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigInstancePeerRowEditorId_Object = MibScalar
me1200ConfigInstancePeerRowEditorId = _Me1200ConfigInstancePeerRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 4, 1),
    _Me1200ConfigInstancePeerRowEditorId_Type()
)
me1200ConfigInstancePeerRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerRowEditorId.setStatus("current")


class _Me1200ConfigInstancePeerRowEditorPeerId_Type(Integer32):
    """Custom type me1200ConfigInstancePeerRowEditorPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigInstancePeerRowEditorPeerId_Type.__name__ = "Integer32"
_Me1200ConfigInstancePeerRowEditorPeerId_Object = MibScalar
me1200ConfigInstancePeerRowEditorPeerId = _Me1200ConfigInstancePeerRowEditorPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 4, 2),
    _Me1200ConfigInstancePeerRowEditorPeerId_Type()
)
me1200ConfigInstancePeerRowEditorPeerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerRowEditorPeerId.setStatus("current")
_Me1200ConfigInstancePeerRowEditorMac_Type = MacAddress
_Me1200ConfigInstancePeerRowEditorMac_Object = MibScalar
me1200ConfigInstancePeerRowEditorMac = _Me1200ConfigInstancePeerRowEditorMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 4, 3),
    _Me1200ConfigInstancePeerRowEditorMac_Type()
)
me1200ConfigInstancePeerRowEditorMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerRowEditorMac.setStatus("current")
_Me1200ConfigInstancePeerRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigInstancePeerRowEditorAction_Object = MibScalar
me1200ConfigInstancePeerRowEditorAction = _Me1200ConfigInstancePeerRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 1, 4, 100),
    _Me1200ConfigInstancePeerRowEditorAction_Type()
)
me1200ConfigInstancePeerRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerRowEditorAction.setStatus("current")
_Me1200ConfigPerfMon_ObjectIdentity = ObjectIdentity
me1200ConfigPerfMon = _Me1200ConfigPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 2)
)
_Me1200ConfigPmTable_Object = MibTable
me1200ConfigPmTable = _Me1200ConfigPmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigPmTable.setStatus("current")
_Me1200ConfigPmEntry_Object = MibTableRow
me1200ConfigPmEntry = _Me1200ConfigPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 2, 1, 1)
)
me1200ConfigPmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigPmId"),
)
if mibBuilder.loadTexts:
    me1200ConfigPmEntry.setStatus("current")


class _Me1200ConfigPmId_Type(Integer32):
    """Custom type me1200ConfigPmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigPmId_Type.__name__ = "Integer32"
_Me1200ConfigPmId_Object = MibTableColumn
me1200ConfigPmId = _Me1200ConfigPmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 2, 1, 1, 1),
    _Me1200ConfigPmId_Type()
)
me1200ConfigPmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigPmId.setStatus("current")
_Me1200ConfigPmEnable_Type = TruthValue
_Me1200ConfigPmEnable_Object = MibTableColumn
me1200ConfigPmEnable = _Me1200ConfigPmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 2, 1, 1, 2),
    _Me1200ConfigPmEnable_Type()
)
me1200ConfigPmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigPmEnable.setStatus("current")
_Me1200ConfigContinuityCheck_ObjectIdentity = ObjectIdentity
me1200ConfigContinuityCheck = _Me1200ConfigContinuityCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3)
)
_Me1200ConfigCcTable_Object = MibTable
me1200ConfigCcTable = _Me1200ConfigCcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigCcTable.setStatus("current")
_Me1200ConfigCcEntry_Object = MibTableRow
me1200ConfigCcEntry = _Me1200ConfigCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1)
)
me1200ConfigCcEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigCcId"),
)
if mibBuilder.loadTexts:
    me1200ConfigCcEntry.setStatus("current")


class _Me1200ConfigCcId_Type(Integer32):
    """Custom type me1200ConfigCcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigCcId_Type.__name__ = "Integer32"
_Me1200ConfigCcId_Object = MibTableColumn
me1200ConfigCcId = _Me1200ConfigCcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 1),
    _Me1200ConfigCcId_Type()
)
me1200ConfigCcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigCcId.setStatus("current")
_Me1200ConfigCcDei_Type = ME1200Unsigned8
_Me1200ConfigCcDei_Object = MibTableColumn
me1200ConfigCcDei = _Me1200ConfigCcDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 2),
    _Me1200ConfigCcDei_Type()
)
me1200ConfigCcDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcDei.setStatus("current")
_Me1200ConfigCcPrio_Type = Unsigned32
_Me1200ConfigCcPrio_Object = MibTableColumn
me1200ConfigCcPrio = _Me1200ConfigCcPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 3),
    _Me1200ConfigCcPrio_Type()
)
me1200ConfigCcPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcPrio.setStatus("current")
_Me1200ConfigCcRate_Type = ME1200MepTxRate
_Me1200ConfigCcRate_Object = MibTableColumn
me1200ConfigCcRate = _Me1200ConfigCcRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 4),
    _Me1200ConfigCcRate_Type()
)
me1200ConfigCcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRate.setStatus("current")
_Me1200ConfigCcTlv_Type = TruthValue
_Me1200ConfigCcTlv_Object = MibTableColumn
me1200ConfigCcTlv = _Me1200ConfigCcTlv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 5),
    _Me1200ConfigCcTlv_Type()
)
me1200ConfigCcTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcTlv.setStatus("current")
_Me1200ConfigCcAction_Type = ME1200RowEditorState
_Me1200ConfigCcAction_Object = MibTableColumn
me1200ConfigCcAction = _Me1200ConfigCcAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 1, 1, 100),
    _Me1200ConfigCcAction_Type()
)
me1200ConfigCcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcAction.setStatus("current")
_Me1200ConfigCcRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigCcRowEditor = _Me1200ConfigCcRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2)
)


class _Me1200ConfigCcRowEditorId_Type(Integer32):
    """Custom type me1200ConfigCcRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigCcRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigCcRowEditorId_Object = MibScalar
me1200ConfigCcRowEditorId = _Me1200ConfigCcRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 1),
    _Me1200ConfigCcRowEditorId_Type()
)
me1200ConfigCcRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorId.setStatus("current")
_Me1200ConfigCcRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigCcRowEditorDei_Object = MibScalar
me1200ConfigCcRowEditorDei = _Me1200ConfigCcRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 2),
    _Me1200ConfigCcRowEditorDei_Type()
)
me1200ConfigCcRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorDei.setStatus("current")
_Me1200ConfigCcRowEditorPrio_Type = Unsigned32
_Me1200ConfigCcRowEditorPrio_Object = MibScalar
me1200ConfigCcRowEditorPrio = _Me1200ConfigCcRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 3),
    _Me1200ConfigCcRowEditorPrio_Type()
)
me1200ConfigCcRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorPrio.setStatus("current")
_Me1200ConfigCcRowEditorRate_Type = ME1200MepTxRate
_Me1200ConfigCcRowEditorRate_Object = MibScalar
me1200ConfigCcRowEditorRate = _Me1200ConfigCcRowEditorRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 4),
    _Me1200ConfigCcRowEditorRate_Type()
)
me1200ConfigCcRowEditorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorRate.setStatus("current")
_Me1200ConfigCcRowEditorTlv_Type = TruthValue
_Me1200ConfigCcRowEditorTlv_Object = MibScalar
me1200ConfigCcRowEditorTlv = _Me1200ConfigCcRowEditorTlv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 5),
    _Me1200ConfigCcRowEditorTlv_Type()
)
me1200ConfigCcRowEditorTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorTlv.setStatus("current")
_Me1200ConfigCcRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigCcRowEditorAction_Object = MibScalar
me1200ConfigCcRowEditorAction = _Me1200ConfigCcRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 3, 2, 100),
    _Me1200ConfigCcRowEditorAction_Type()
)
me1200ConfigCcRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorAction.setStatus("current")
_Me1200ConfigLossMeasurement_ObjectIdentity = ObjectIdentity
me1200ConfigLossMeasurement = _Me1200ConfigLossMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4)
)
_Me1200ConfigLmTable_Object = MibTable
me1200ConfigLmTable = _Me1200ConfigLmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLmTable.setStatus("current")
_Me1200ConfigLmEntry_Object = MibTableRow
me1200ConfigLmEntry = _Me1200ConfigLmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1)
)
me1200ConfigLmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLmId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLmEntry.setStatus("current")


class _Me1200ConfigLmId_Type(Integer32):
    """Custom type me1200ConfigLmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLmId_Type.__name__ = "Integer32"
_Me1200ConfigLmId_Object = MibTableColumn
me1200ConfigLmId = _Me1200ConfigLmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 1),
    _Me1200ConfigLmId_Type()
)
me1200ConfigLmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLmId.setStatus("current")
_Me1200ConfigLmEnded_Type = ME1200Ended
_Me1200ConfigLmEnded_Object = MibTableColumn
me1200ConfigLmEnded = _Me1200ConfigLmEnded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 2),
    _Me1200ConfigLmEnded_Type()
)
me1200ConfigLmEnded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmEnded.setStatus("current")
_Me1200ConfigLmDei_Type = ME1200Unsigned8
_Me1200ConfigLmDei_Object = MibTableColumn
me1200ConfigLmDei = _Me1200ConfigLmDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 3),
    _Me1200ConfigLmDei_Type()
)
me1200ConfigLmDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmDei.setStatus("current")
_Me1200ConfigLmPrio_Type = Unsigned32
_Me1200ConfigLmPrio_Object = MibTableColumn
me1200ConfigLmPrio = _Me1200ConfigLmPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 4),
    _Me1200ConfigLmPrio_Type()
)
me1200ConfigLmPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmPrio.setStatus("current")
_Me1200ConfigLmRate_Type = ME1200MepTxRate
_Me1200ConfigLmRate_Object = MibTableColumn
me1200ConfigLmRate = _Me1200ConfigLmRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 5),
    _Me1200ConfigLmRate_Type()
)
me1200ConfigLmRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRate.setStatus("current")
_Me1200ConfigLmCast_Type = ME1200Cast
_Me1200ConfigLmCast_Object = MibTableColumn
me1200ConfigLmCast = _Me1200ConfigLmCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 6),
    _Me1200ConfigLmCast_Type()
)
me1200ConfigLmCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmCast.setStatus("current")
_Me1200ConfigLmFlrInterval_Type = Unsigned32
_Me1200ConfigLmFlrInterval_Object = MibTableColumn
me1200ConfigLmFlrInterval = _Me1200ConfigLmFlrInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 7),
    _Me1200ConfigLmFlrInterval_Type()
)
me1200ConfigLmFlrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmFlrInterval.setStatus("current")
_Me1200ConfigLmLossRatioThreshold_Type = Unsigned32
_Me1200ConfigLmLossRatioThreshold_Object = MibTableColumn
me1200ConfigLmLossRatioThreshold = _Me1200ConfigLmLossRatioThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 8),
    _Me1200ConfigLmLossRatioThreshold_Type()
)
me1200ConfigLmLossRatioThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmLossRatioThreshold.setStatus("current")
_Me1200ConfigLmRxEnable_Type = TruthValue
_Me1200ConfigLmRxEnable_Object = MibTableColumn
me1200ConfigLmRxEnable = _Me1200ConfigLmRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 9),
    _Me1200ConfigLmRxEnable_Type()
)
me1200ConfigLmRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRxEnable.setStatus("current")
_Me1200ConfigLmSynthetic_Type = TruthValue
_Me1200ConfigLmSynthetic_Object = MibTableColumn
me1200ConfigLmSynthetic = _Me1200ConfigLmSynthetic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 10),
    _Me1200ConfigLmSynthetic_Type()
)
me1200ConfigLmSynthetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmSynthetic.setStatus("current")
_Me1200ConfigLmMep_Type = Unsigned32
_Me1200ConfigLmMep_Object = MibTableColumn
me1200ConfigLmMep = _Me1200ConfigLmMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 11),
    _Me1200ConfigLmMep_Type()
)
me1200ConfigLmMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmMep.setStatus("current")
_Me1200ConfigLmFrameSize_Type = Unsigned32
_Me1200ConfigLmFrameSize_Object = MibTableColumn
me1200ConfigLmFrameSize = _Me1200ConfigLmFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 12),
    _Me1200ConfigLmFrameSize_Type()
)
me1200ConfigLmFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmFrameSize.setStatus("current")
_Me1200ConfigLmMeasInterval_Type = Unsigned32
_Me1200ConfigLmMeasInterval_Object = MibTableColumn
me1200ConfigLmMeasInterval = _Me1200ConfigLmMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 13),
    _Me1200ConfigLmMeasInterval_Type()
)
me1200ConfigLmMeasInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmMeasInterval.setStatus("current")
_Me1200ConfigLmAction_Type = ME1200RowEditorState
_Me1200ConfigLmAction_Object = MibTableColumn
me1200ConfigLmAction = _Me1200ConfigLmAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 1, 1, 101),
    _Me1200ConfigLmAction_Type()
)
me1200ConfigLmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAction.setStatus("current")
_Me1200ConfigLmRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigLmRowEditor = _Me1200ConfigLmRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2)
)


class _Me1200ConfigLmRowEditorId_Type(Integer32):
    """Custom type me1200ConfigLmRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLmRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigLmRowEditorId_Object = MibScalar
me1200ConfigLmRowEditorId = _Me1200ConfigLmRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 1),
    _Me1200ConfigLmRowEditorId_Type()
)
me1200ConfigLmRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorId.setStatus("current")
_Me1200ConfigLmRowEditorEnded_Type = ME1200Ended
_Me1200ConfigLmRowEditorEnded_Object = MibScalar
me1200ConfigLmRowEditorEnded = _Me1200ConfigLmRowEditorEnded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 2),
    _Me1200ConfigLmRowEditorEnded_Type()
)
me1200ConfigLmRowEditorEnded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorEnded.setStatus("current")
_Me1200ConfigLmRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigLmRowEditorDei_Object = MibScalar
me1200ConfigLmRowEditorDei = _Me1200ConfigLmRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 3),
    _Me1200ConfigLmRowEditorDei_Type()
)
me1200ConfigLmRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorDei.setStatus("current")
_Me1200ConfigLmRowEditorPrio_Type = Unsigned32
_Me1200ConfigLmRowEditorPrio_Object = MibScalar
me1200ConfigLmRowEditorPrio = _Me1200ConfigLmRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 4),
    _Me1200ConfigLmRowEditorPrio_Type()
)
me1200ConfigLmRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorPrio.setStatus("current")
_Me1200ConfigLmRowEditorRate_Type = ME1200MepTxRate
_Me1200ConfigLmRowEditorRate_Object = MibScalar
me1200ConfigLmRowEditorRate = _Me1200ConfigLmRowEditorRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 5),
    _Me1200ConfigLmRowEditorRate_Type()
)
me1200ConfigLmRowEditorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorRate.setStatus("current")
_Me1200ConfigLmRowEditorCast_Type = ME1200Cast
_Me1200ConfigLmRowEditorCast_Object = MibScalar
me1200ConfigLmRowEditorCast = _Me1200ConfigLmRowEditorCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 6),
    _Me1200ConfigLmRowEditorCast_Type()
)
me1200ConfigLmRowEditorCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorCast.setStatus("current")
_Me1200ConfigLmRowEditorFlrInterval_Type = Unsigned32
_Me1200ConfigLmRowEditorFlrInterval_Object = MibScalar
me1200ConfigLmRowEditorFlrInterval = _Me1200ConfigLmRowEditorFlrInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 7),
    _Me1200ConfigLmRowEditorFlrInterval_Type()
)
me1200ConfigLmRowEditorFlrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorFlrInterval.setStatus("current")
_Me1200ConfigLmRowEditorLossRatioThreshold_Type = Unsigned32
_Me1200ConfigLmRowEditorLossRatioThreshold_Object = MibScalar
me1200ConfigLmRowEditorLossRatioThreshold = _Me1200ConfigLmRowEditorLossRatioThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 8),
    _Me1200ConfigLmRowEditorLossRatioThreshold_Type()
)
me1200ConfigLmRowEditorLossRatioThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorLossRatioThreshold.setStatus("current")
_Me1200ConfigLmRowEditorRxEnable_Type = TruthValue
_Me1200ConfigLmRowEditorRxEnable_Object = MibScalar
me1200ConfigLmRowEditorRxEnable = _Me1200ConfigLmRowEditorRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 9),
    _Me1200ConfigLmRowEditorRxEnable_Type()
)
me1200ConfigLmRowEditorRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorRxEnable.setStatus("current")
_Me1200ConfigLmRowEditorSynthetic_Type = TruthValue
_Me1200ConfigLmRowEditorSynthetic_Object = MibScalar
me1200ConfigLmRowEditorSynthetic = _Me1200ConfigLmRowEditorSynthetic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 10),
    _Me1200ConfigLmRowEditorSynthetic_Type()
)
me1200ConfigLmRowEditorSynthetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorSynthetic.setStatus("current")
_Me1200ConfigLmRowEditorMep_Type = Unsigned32
_Me1200ConfigLmRowEditorMep_Object = MibScalar
me1200ConfigLmRowEditorMep = _Me1200ConfigLmRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 11),
    _Me1200ConfigLmRowEditorMep_Type()
)
me1200ConfigLmRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorMep.setStatus("current")
_Me1200ConfigLmRowEditorFrameSize_Type = Unsigned32
_Me1200ConfigLmRowEditorFrameSize_Object = MibScalar
me1200ConfigLmRowEditorFrameSize = _Me1200ConfigLmRowEditorFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 12),
    _Me1200ConfigLmRowEditorFrameSize_Type()
)
me1200ConfigLmRowEditorFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorFrameSize.setStatus("current")
_Me1200ConfigLmRowEditorMeasInterval_Type = Unsigned32
_Me1200ConfigLmRowEditorMeasInterval_Object = MibScalar
me1200ConfigLmRowEditorMeasInterval = _Me1200ConfigLmRowEditorMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 13),
    _Me1200ConfigLmRowEditorMeasInterval_Type()
)
me1200ConfigLmRowEditorMeasInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorMeasInterval.setStatus("current")
_Me1200ConfigLmRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigLmRowEditorAction_Object = MibScalar
me1200ConfigLmRowEditorAction = _Me1200ConfigLmRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 4, 2, 101),
    _Me1200ConfigLmRowEditorAction_Type()
)
me1200ConfigLmRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorAction.setStatus("current")
_Me1200ConfigDelayMeasurement_ObjectIdentity = ObjectIdentity
me1200ConfigDelayMeasurement = _Me1200ConfigDelayMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5)
)
_Me1200ConfigDmTable_Object = MibTable
me1200ConfigDmTable = _Me1200ConfigDmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigDmTable.setStatus("current")
_Me1200ConfigDmEntry_Object = MibTableRow
me1200ConfigDmEntry = _Me1200ConfigDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1)
)
me1200ConfigDmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigDmId"),
)
if mibBuilder.loadTexts:
    me1200ConfigDmEntry.setStatus("current")


class _Me1200ConfigDmId_Type(Integer32):
    """Custom type me1200ConfigDmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigDmId_Type.__name__ = "Integer32"
_Me1200ConfigDmId_Object = MibTableColumn
me1200ConfigDmId = _Me1200ConfigDmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 1),
    _Me1200ConfigDmId_Type()
)
me1200ConfigDmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigDmId.setStatus("current")
_Me1200ConfigDmEnded_Type = ME1200Ended
_Me1200ConfigDmEnded_Object = MibTableColumn
me1200ConfigDmEnded = _Me1200ConfigDmEnded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 2),
    _Me1200ConfigDmEnded_Type()
)
me1200ConfigDmEnded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmEnded.setStatus("current")
_Me1200ConfigDmDei_Type = ME1200Unsigned8
_Me1200ConfigDmDei_Object = MibTableColumn
me1200ConfigDmDei = _Me1200ConfigDmDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 3),
    _Me1200ConfigDmDei_Type()
)
me1200ConfigDmDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmDei.setStatus("current")
_Me1200ConfigDmPrio_Type = Unsigned32
_Me1200ConfigDmPrio_Object = MibTableColumn
me1200ConfigDmPrio = _Me1200ConfigDmPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 4),
    _Me1200ConfigDmPrio_Type()
)
me1200ConfigDmPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmPrio.setStatus("current")
_Me1200ConfigDmCast_Type = ME1200Cast
_Me1200ConfigDmCast_Object = MibTableColumn
me1200ConfigDmCast = _Me1200ConfigDmCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 5),
    _Me1200ConfigDmCast_Type()
)
me1200ConfigDmCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmCast.setStatus("current")
_Me1200ConfigDmMep_Type = Unsigned32
_Me1200ConfigDmMep_Object = MibTableColumn
me1200ConfigDmMep = _Me1200ConfigDmMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 6),
    _Me1200ConfigDmMep_Type()
)
me1200ConfigDmMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmMep.setStatus("current")
_Me1200ConfigDmCalcWay_Type = ME1200CalcWay
_Me1200ConfigDmCalcWay_Object = MibTableColumn
me1200ConfigDmCalcWay = _Me1200ConfigDmCalcWay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 7),
    _Me1200ConfigDmCalcWay_Type()
)
me1200ConfigDmCalcWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmCalcWay.setStatus("current")
_Me1200ConfigDmInterval_Type = Unsigned32
_Me1200ConfigDmInterval_Object = MibTableColumn
me1200ConfigDmInterval = _Me1200ConfigDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 8),
    _Me1200ConfigDmInterval_Type()
)
me1200ConfigDmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmInterval.setStatus("current")
_Me1200ConfigDmLastN_Type = Unsigned32
_Me1200ConfigDmLastN_Object = MibTableColumn
me1200ConfigDmLastN = _Me1200ConfigDmLastN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 9),
    _Me1200ConfigDmLastN_Type()
)
me1200ConfigDmLastN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmLastN.setStatus("current")
_Me1200ConfigDmTimeUnit_Type = ME1200MepDmTimeUnit
_Me1200ConfigDmTimeUnit_Object = MibTableColumn
me1200ConfigDmTimeUnit = _Me1200ConfigDmTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 10),
    _Me1200ConfigDmTimeUnit_Type()
)
me1200ConfigDmTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmTimeUnit.setStatus("current")
_Me1200ConfigDmOverflowAct_Type = ME1200Action
_Me1200ConfigDmOverflowAct_Object = MibTableColumn
me1200ConfigDmOverflowAct = _Me1200ConfigDmOverflowAct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 11),
    _Me1200ConfigDmOverflowAct_Type()
)
me1200ConfigDmOverflowAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmOverflowAct.setStatus("current")
_Me1200ConfigDmSynchronized_Type = TruthValue
_Me1200ConfigDmSynchronized_Object = MibTableColumn
me1200ConfigDmSynchronized = _Me1200ConfigDmSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 12),
    _Me1200ConfigDmSynchronized_Type()
)
me1200ConfigDmSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmSynchronized.setStatus("current")
_Me1200ConfigDmOneWayAverageLastnDelayThreshold_Type = Unsigned32
_Me1200ConfigDmOneWayAverageLastnDelayThreshold_Object = MibTableColumn
me1200ConfigDmOneWayAverageLastnDelayThreshold = _Me1200ConfigDmOneWayAverageLastnDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 13),
    _Me1200ConfigDmOneWayAverageLastnDelayThreshold_Type()
)
me1200ConfigDmOneWayAverageLastnDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmOneWayAverageLastnDelayThreshold.setStatus("current")
_Me1200ConfigDmOneWayAverageLastnDelayVariationThreshold_Type = Unsigned32
_Me1200ConfigDmOneWayAverageLastnDelayVariationThreshold_Object = MibTableColumn
me1200ConfigDmOneWayAverageLastnDelayVariationThreshold = _Me1200ConfigDmOneWayAverageLastnDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 14),
    _Me1200ConfigDmOneWayAverageLastnDelayVariationThreshold_Type()
)
me1200ConfigDmOneWayAverageLastnDelayVariationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmOneWayAverageLastnDelayVariationThreshold.setStatus("current")
_Me1200ConfigDmTwoWayAverageLastnDelayThreshold_Type = Unsigned32
_Me1200ConfigDmTwoWayAverageLastnDelayThreshold_Object = MibTableColumn
me1200ConfigDmTwoWayAverageLastnDelayThreshold = _Me1200ConfigDmTwoWayAverageLastnDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 15),
    _Me1200ConfigDmTwoWayAverageLastnDelayThreshold_Type()
)
me1200ConfigDmTwoWayAverageLastnDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmTwoWayAverageLastnDelayThreshold.setStatus("current")
_Me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold_Type = Unsigned32
_Me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold_Object = MibTableColumn
me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold = _Me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 16),
    _Me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold_Type()
)
me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold.setStatus("current")
_Me1200ConfigDmNumOfBinFD_Type = ME1200Unsigned16
_Me1200ConfigDmNumOfBinFD_Object = MibTableColumn
me1200ConfigDmNumOfBinFD = _Me1200ConfigDmNumOfBinFD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 17),
    _Me1200ConfigDmNumOfBinFD_Type()
)
me1200ConfigDmNumOfBinFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmNumOfBinFD.setStatus("current")
_Me1200ConfigDmNumOfBinIFDV_Type = ME1200Unsigned16
_Me1200ConfigDmNumOfBinIFDV_Object = MibTableColumn
me1200ConfigDmNumOfBinIFDV = _Me1200ConfigDmNumOfBinIFDV_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 18),
    _Me1200ConfigDmNumOfBinIFDV_Type()
)
me1200ConfigDmNumOfBinIFDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmNumOfBinIFDV.setStatus("current")
_Me1200ConfigDmMThreshold_Type = Unsigned32
_Me1200ConfigDmMThreshold_Object = MibTableColumn
me1200ConfigDmMThreshold = _Me1200ConfigDmMThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 19),
    _Me1200ConfigDmMThreshold_Type()
)
me1200ConfigDmMThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmMThreshold.setStatus("current")
_Me1200ConfigDmAction_Type = ME1200RowEditorState
_Me1200ConfigDmAction_Object = MibTableColumn
me1200ConfigDmAction = _Me1200ConfigDmAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 1, 1, 101),
    _Me1200ConfigDmAction_Type()
)
me1200ConfigDmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmAction.setStatus("current")
_Me1200ConfigDmRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigDmRowEditor = _Me1200ConfigDmRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2)
)


class _Me1200ConfigDmRowEditorId_Type(Integer32):
    """Custom type me1200ConfigDmRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigDmRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigDmRowEditorId_Object = MibScalar
me1200ConfigDmRowEditorId = _Me1200ConfigDmRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 1),
    _Me1200ConfigDmRowEditorId_Type()
)
me1200ConfigDmRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorId.setStatus("current")
_Me1200ConfigDmRowEditorEnded_Type = ME1200Ended
_Me1200ConfigDmRowEditorEnded_Object = MibScalar
me1200ConfigDmRowEditorEnded = _Me1200ConfigDmRowEditorEnded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 2),
    _Me1200ConfigDmRowEditorEnded_Type()
)
me1200ConfigDmRowEditorEnded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorEnded.setStatus("current")
_Me1200ConfigDmRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigDmRowEditorDei_Object = MibScalar
me1200ConfigDmRowEditorDei = _Me1200ConfigDmRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 3),
    _Me1200ConfigDmRowEditorDei_Type()
)
me1200ConfigDmRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorDei.setStatus("current")
_Me1200ConfigDmRowEditorPrio_Type = Unsigned32
_Me1200ConfigDmRowEditorPrio_Object = MibScalar
me1200ConfigDmRowEditorPrio = _Me1200ConfigDmRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 4),
    _Me1200ConfigDmRowEditorPrio_Type()
)
me1200ConfigDmRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorPrio.setStatus("current")
_Me1200ConfigDmRowEditorCast_Type = ME1200Cast
_Me1200ConfigDmRowEditorCast_Object = MibScalar
me1200ConfigDmRowEditorCast = _Me1200ConfigDmRowEditorCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 5),
    _Me1200ConfigDmRowEditorCast_Type()
)
me1200ConfigDmRowEditorCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorCast.setStatus("current")
_Me1200ConfigDmRowEditorMep_Type = Unsigned32
_Me1200ConfigDmRowEditorMep_Object = MibScalar
me1200ConfigDmRowEditorMep = _Me1200ConfigDmRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 6),
    _Me1200ConfigDmRowEditorMep_Type()
)
me1200ConfigDmRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorMep.setStatus("current")
_Me1200ConfigDmRowEditorCalcWay_Type = ME1200CalcWay
_Me1200ConfigDmRowEditorCalcWay_Object = MibScalar
me1200ConfigDmRowEditorCalcWay = _Me1200ConfigDmRowEditorCalcWay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 7),
    _Me1200ConfigDmRowEditorCalcWay_Type()
)
me1200ConfigDmRowEditorCalcWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorCalcWay.setStatus("current")
_Me1200ConfigDmRowEditorInterval_Type = Unsigned32
_Me1200ConfigDmRowEditorInterval_Object = MibScalar
me1200ConfigDmRowEditorInterval = _Me1200ConfigDmRowEditorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 8),
    _Me1200ConfigDmRowEditorInterval_Type()
)
me1200ConfigDmRowEditorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorInterval.setStatus("current")
_Me1200ConfigDmRowEditorLastN_Type = Unsigned32
_Me1200ConfigDmRowEditorLastN_Object = MibScalar
me1200ConfigDmRowEditorLastN = _Me1200ConfigDmRowEditorLastN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 9),
    _Me1200ConfigDmRowEditorLastN_Type()
)
me1200ConfigDmRowEditorLastN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorLastN.setStatus("current")
_Me1200ConfigDmRowEditorTimeUnit_Type = ME1200MepDmTimeUnit
_Me1200ConfigDmRowEditorTimeUnit_Object = MibScalar
me1200ConfigDmRowEditorTimeUnit = _Me1200ConfigDmRowEditorTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 10),
    _Me1200ConfigDmRowEditorTimeUnit_Type()
)
me1200ConfigDmRowEditorTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorTimeUnit.setStatus("current")
_Me1200ConfigDmRowEditorOverflowAct_Type = ME1200Action
_Me1200ConfigDmRowEditorOverflowAct_Object = MibScalar
me1200ConfigDmRowEditorOverflowAct = _Me1200ConfigDmRowEditorOverflowAct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 11),
    _Me1200ConfigDmRowEditorOverflowAct_Type()
)
me1200ConfigDmRowEditorOverflowAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorOverflowAct.setStatus("current")
_Me1200ConfigDmRowEditorSynchronized_Type = TruthValue
_Me1200ConfigDmRowEditorSynchronized_Object = MibScalar
me1200ConfigDmRowEditorSynchronized = _Me1200ConfigDmRowEditorSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 12),
    _Me1200ConfigDmRowEditorSynchronized_Type()
)
me1200ConfigDmRowEditorSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorSynchronized.setStatus("current")
_Me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold_Type = Unsigned32
_Me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold_Object = MibScalar
me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold = _Me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 13),
    _Me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold_Type()
)
me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold.setStatus("current")
_Me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold_Type = Unsigned32
_Me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold_Object = MibScalar
me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold = _Me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 14),
    _Me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold_Type()
)
me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold.setStatus("current")
_Me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold_Type = Unsigned32
_Me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold_Object = MibScalar
me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold = _Me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 15),
    _Me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold_Type()
)
me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold.setStatus("current")
_Me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold_Type = Unsigned32
_Me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold_Object = MibScalar
me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold = _Me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 16),
    _Me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold_Type()
)
me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold.setStatus("current")
_Me1200ConfigDmRowEditorNumOfBinFD_Type = ME1200Unsigned16
_Me1200ConfigDmRowEditorNumOfBinFD_Object = MibScalar
me1200ConfigDmRowEditorNumOfBinFD = _Me1200ConfigDmRowEditorNumOfBinFD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 17),
    _Me1200ConfigDmRowEditorNumOfBinFD_Type()
)
me1200ConfigDmRowEditorNumOfBinFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorNumOfBinFD.setStatus("current")
_Me1200ConfigDmRowEditorNumOfBinIFDV_Type = ME1200Unsigned16
_Me1200ConfigDmRowEditorNumOfBinIFDV_Object = MibScalar
me1200ConfigDmRowEditorNumOfBinIFDV = _Me1200ConfigDmRowEditorNumOfBinIFDV_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 18),
    _Me1200ConfigDmRowEditorNumOfBinIFDV_Type()
)
me1200ConfigDmRowEditorNumOfBinIFDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorNumOfBinIFDV.setStatus("current")
_Me1200ConfigDmRowEditorMThreshold_Type = Unsigned32
_Me1200ConfigDmRowEditorMThreshold_Object = MibScalar
me1200ConfigDmRowEditorMThreshold = _Me1200ConfigDmRowEditorMThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 19),
    _Me1200ConfigDmRowEditorMThreshold_Type()
)
me1200ConfigDmRowEditorMThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorMThreshold.setStatus("current")
_Me1200ConfigDmRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigDmRowEditorAction_Object = MibScalar
me1200ConfigDmRowEditorAction = _Me1200ConfigDmRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 5, 2, 101),
    _Me1200ConfigDmRowEditorAction_Type()
)
me1200ConfigDmRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorAction.setStatus("current")
_Me1200ConfigLoopBack_ObjectIdentity = ObjectIdentity
me1200ConfigLoopBack = _Me1200ConfigLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6)
)
_Me1200ConfigLbTable_Object = MibTable
me1200ConfigLbTable = _Me1200ConfigLbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLbTable.setStatus("current")
_Me1200ConfigLbEntry_Object = MibTableRow
me1200ConfigLbEntry = _Me1200ConfigLbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1)
)
me1200ConfigLbEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLbId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLbEntry.setStatus("current")


class _Me1200ConfigLbId_Type(Integer32):
    """Custom type me1200ConfigLbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLbId_Type.__name__ = "Integer32"
_Me1200ConfigLbId_Object = MibTableColumn
me1200ConfigLbId = _Me1200ConfigLbId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 1),
    _Me1200ConfigLbId_Type()
)
me1200ConfigLbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLbId.setStatus("current")
_Me1200ConfigLbDei_Type = ME1200Unsigned8
_Me1200ConfigLbDei_Object = MibTableColumn
me1200ConfigLbDei = _Me1200ConfigLbDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 2),
    _Me1200ConfigLbDei_Type()
)
me1200ConfigLbDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbDei.setStatus("current")
_Me1200ConfigLbPrio_Type = Unsigned32
_Me1200ConfigLbPrio_Object = MibTableColumn
me1200ConfigLbPrio = _Me1200ConfigLbPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 3),
    _Me1200ConfigLbPrio_Type()
)
me1200ConfigLbPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbPrio.setStatus("current")
_Me1200ConfigLbCast_Type = ME1200Cast
_Me1200ConfigLbCast_Object = MibTableColumn
me1200ConfigLbCast = _Me1200ConfigLbCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 4),
    _Me1200ConfigLbCast_Type()
)
me1200ConfigLbCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbCast.setStatus("current")
_Me1200ConfigLbMep_Type = Unsigned32
_Me1200ConfigLbMep_Object = MibTableColumn
me1200ConfigLbMep = _Me1200ConfigLbMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 5),
    _Me1200ConfigLbMep_Type()
)
me1200ConfigLbMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbMep.setStatus("current")
_Me1200ConfigLbMac_Type = MacAddress
_Me1200ConfigLbMac_Object = MibTableColumn
me1200ConfigLbMac = _Me1200ConfigLbMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 6),
    _Me1200ConfigLbMac_Type()
)
me1200ConfigLbMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbMac.setStatus("current")
_Me1200ConfigLbToSend_Type = Unsigned32
_Me1200ConfigLbToSend_Object = MibTableColumn
me1200ConfigLbToSend = _Me1200ConfigLbToSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 7),
    _Me1200ConfigLbToSend_Type()
)
me1200ConfigLbToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbToSend.setStatus("current")
_Me1200ConfigLbSize_Type = Unsigned32
_Me1200ConfigLbSize_Object = MibTableColumn
me1200ConfigLbSize = _Me1200ConfigLbSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 8),
    _Me1200ConfigLbSize_Type()
)
me1200ConfigLbSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbSize.setStatus("current")
_Me1200ConfigLbInterval_Type = Unsigned32
_Me1200ConfigLbInterval_Object = MibTableColumn
me1200ConfigLbInterval = _Me1200ConfigLbInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 9),
    _Me1200ConfigLbInterval_Type()
)
me1200ConfigLbInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbInterval.setStatus("current")
_Me1200ConfigLbAction_Type = ME1200RowEditorState
_Me1200ConfigLbAction_Object = MibTableColumn
me1200ConfigLbAction = _Me1200ConfigLbAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 1, 1, 101),
    _Me1200ConfigLbAction_Type()
)
me1200ConfigLbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbAction.setStatus("current")
_Me1200ConfigLbRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigLbRowEditor = _Me1200ConfigLbRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2)
)


class _Me1200ConfigLbRowEditorId_Type(Integer32):
    """Custom type me1200ConfigLbRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLbRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigLbRowEditorId_Object = MibScalar
me1200ConfigLbRowEditorId = _Me1200ConfigLbRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 1),
    _Me1200ConfigLbRowEditorId_Type()
)
me1200ConfigLbRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorId.setStatus("current")
_Me1200ConfigLbRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigLbRowEditorDei_Object = MibScalar
me1200ConfigLbRowEditorDei = _Me1200ConfigLbRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 2),
    _Me1200ConfigLbRowEditorDei_Type()
)
me1200ConfigLbRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorDei.setStatus("current")
_Me1200ConfigLbRowEditorPrio_Type = Unsigned32
_Me1200ConfigLbRowEditorPrio_Object = MibScalar
me1200ConfigLbRowEditorPrio = _Me1200ConfigLbRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 3),
    _Me1200ConfigLbRowEditorPrio_Type()
)
me1200ConfigLbRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorPrio.setStatus("current")
_Me1200ConfigLbRowEditorCast_Type = ME1200Cast
_Me1200ConfigLbRowEditorCast_Object = MibScalar
me1200ConfigLbRowEditorCast = _Me1200ConfigLbRowEditorCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 4),
    _Me1200ConfigLbRowEditorCast_Type()
)
me1200ConfigLbRowEditorCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorCast.setStatus("current")
_Me1200ConfigLbRowEditorMep_Type = Unsigned32
_Me1200ConfigLbRowEditorMep_Object = MibScalar
me1200ConfigLbRowEditorMep = _Me1200ConfigLbRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 5),
    _Me1200ConfigLbRowEditorMep_Type()
)
me1200ConfigLbRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorMep.setStatus("current")
_Me1200ConfigLbRowEditorMac_Type = MacAddress
_Me1200ConfigLbRowEditorMac_Object = MibScalar
me1200ConfigLbRowEditorMac = _Me1200ConfigLbRowEditorMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 6),
    _Me1200ConfigLbRowEditorMac_Type()
)
me1200ConfigLbRowEditorMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorMac.setStatus("current")
_Me1200ConfigLbRowEditorToSend_Type = Unsigned32
_Me1200ConfigLbRowEditorToSend_Object = MibScalar
me1200ConfigLbRowEditorToSend = _Me1200ConfigLbRowEditorToSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 7),
    _Me1200ConfigLbRowEditorToSend_Type()
)
me1200ConfigLbRowEditorToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorToSend.setStatus("current")
_Me1200ConfigLbRowEditorSize_Type = Unsigned32
_Me1200ConfigLbRowEditorSize_Object = MibScalar
me1200ConfigLbRowEditorSize = _Me1200ConfigLbRowEditorSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 8),
    _Me1200ConfigLbRowEditorSize_Type()
)
me1200ConfigLbRowEditorSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorSize.setStatus("current")
_Me1200ConfigLbRowEditorInterval_Type = Unsigned32
_Me1200ConfigLbRowEditorInterval_Object = MibScalar
me1200ConfigLbRowEditorInterval = _Me1200ConfigLbRowEditorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 9),
    _Me1200ConfigLbRowEditorInterval_Type()
)
me1200ConfigLbRowEditorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorInterval.setStatus("current")
_Me1200ConfigLbRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigLbRowEditorAction_Object = MibScalar
me1200ConfigLbRowEditorAction = _Me1200ConfigLbRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 6, 2, 101),
    _Me1200ConfigLbRowEditorAction_Type()
)
me1200ConfigLbRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorAction.setStatus("current")
_Me1200ConfigTestSignal_ObjectIdentity = ObjectIdentity
me1200ConfigTestSignal = _Me1200ConfigTestSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7)
)
_Me1200ConfigTstTable_Object = MibTable
me1200ConfigTstTable = _Me1200ConfigTstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigTstTable.setStatus("current")
_Me1200ConfigTstEntry_Object = MibTableRow
me1200ConfigTstEntry = _Me1200ConfigTstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1)
)
me1200ConfigTstEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigTstId"),
)
if mibBuilder.loadTexts:
    me1200ConfigTstEntry.setStatus("current")


class _Me1200ConfigTstId_Type(Integer32):
    """Custom type me1200ConfigTstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigTstId_Type.__name__ = "Integer32"
_Me1200ConfigTstId_Object = MibTableColumn
me1200ConfigTstId = _Me1200ConfigTstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 1),
    _Me1200ConfigTstId_Type()
)
me1200ConfigTstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigTstId.setStatus("current")
_Me1200ConfigTstTxEnable_Type = TruthValue
_Me1200ConfigTstTxEnable_Object = MibTableColumn
me1200ConfigTstTxEnable = _Me1200ConfigTstTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 2),
    _Me1200ConfigTstTxEnable_Type()
)
me1200ConfigTstTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstTxEnable.setStatus("current")
_Me1200ConfigTstRxEnable_Type = TruthValue
_Me1200ConfigTstRxEnable_Object = MibTableColumn
me1200ConfigTstRxEnable = _Me1200ConfigTstRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 3),
    _Me1200ConfigTstRxEnable_Type()
)
me1200ConfigTstRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRxEnable.setStatus("current")
_Me1200ConfigTstDei_Type = ME1200Unsigned8
_Me1200ConfigTstDei_Object = MibTableColumn
me1200ConfigTstDei = _Me1200ConfigTstDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 4),
    _Me1200ConfigTstDei_Type()
)
me1200ConfigTstDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstDei.setStatus("current")
_Me1200ConfigTstPrio_Type = Unsigned32
_Me1200ConfigTstPrio_Object = MibTableColumn
me1200ConfigTstPrio = _Me1200ConfigTstPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 5),
    _Me1200ConfigTstPrio_Type()
)
me1200ConfigTstPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstPrio.setStatus("current")
_Me1200ConfigTstMep_Type = Unsigned32
_Me1200ConfigTstMep_Object = MibTableColumn
me1200ConfigTstMep = _Me1200ConfigTstMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 6),
    _Me1200ConfigTstMep_Type()
)
me1200ConfigTstMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstMep.setStatus("current")
_Me1200ConfigTstRate_Type = Unsigned32
_Me1200ConfigTstRate_Object = MibTableColumn
me1200ConfigTstRate = _Me1200ConfigTstRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 7),
    _Me1200ConfigTstRate_Type()
)
me1200ConfigTstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRate.setStatus("current")
_Me1200ConfigTstSize_Type = Unsigned32
_Me1200ConfigTstSize_Object = MibTableColumn
me1200ConfigTstSize = _Me1200ConfigTstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 8),
    _Me1200ConfigTstSize_Type()
)
me1200ConfigTstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstSize.setStatus("current")
_Me1200ConfigTstPattern_Type = ME1200TstPattern
_Me1200ConfigTstPattern_Object = MibTableColumn
me1200ConfigTstPattern = _Me1200ConfigTstPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 9),
    _Me1200ConfigTstPattern_Type()
)
me1200ConfigTstPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstPattern.setStatus("current")
_Me1200ConfigTstSequence_Type = TruthValue
_Me1200ConfigTstSequence_Object = MibTableColumn
me1200ConfigTstSequence = _Me1200ConfigTstSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 10),
    _Me1200ConfigTstSequence_Type()
)
me1200ConfigTstSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstSequence.setStatus("current")
_Me1200ConfigTstAction_Type = ME1200RowEditorState
_Me1200ConfigTstAction_Object = MibTableColumn
me1200ConfigTstAction = _Me1200ConfigTstAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 1, 1, 101),
    _Me1200ConfigTstAction_Type()
)
me1200ConfigTstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstAction.setStatus("current")
_Me1200ConfigTstRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigTstRowEditor = _Me1200ConfigTstRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2)
)


class _Me1200ConfigTstRowEditorId_Type(Integer32):
    """Custom type me1200ConfigTstRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigTstRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigTstRowEditorId_Object = MibScalar
me1200ConfigTstRowEditorId = _Me1200ConfigTstRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 1),
    _Me1200ConfigTstRowEditorId_Type()
)
me1200ConfigTstRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorId.setStatus("current")
_Me1200ConfigTstRowEditorTxEnable_Type = TruthValue
_Me1200ConfigTstRowEditorTxEnable_Object = MibScalar
me1200ConfigTstRowEditorTxEnable = _Me1200ConfigTstRowEditorTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 2),
    _Me1200ConfigTstRowEditorTxEnable_Type()
)
me1200ConfigTstRowEditorTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorTxEnable.setStatus("current")
_Me1200ConfigTstRowEditorRxEnable_Type = TruthValue
_Me1200ConfigTstRowEditorRxEnable_Object = MibScalar
me1200ConfigTstRowEditorRxEnable = _Me1200ConfigTstRowEditorRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 3),
    _Me1200ConfigTstRowEditorRxEnable_Type()
)
me1200ConfigTstRowEditorRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorRxEnable.setStatus("current")
_Me1200ConfigTstRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigTstRowEditorDei_Object = MibScalar
me1200ConfigTstRowEditorDei = _Me1200ConfigTstRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 4),
    _Me1200ConfigTstRowEditorDei_Type()
)
me1200ConfigTstRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorDei.setStatus("current")
_Me1200ConfigTstRowEditorPrio_Type = Unsigned32
_Me1200ConfigTstRowEditorPrio_Object = MibScalar
me1200ConfigTstRowEditorPrio = _Me1200ConfigTstRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 5),
    _Me1200ConfigTstRowEditorPrio_Type()
)
me1200ConfigTstRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorPrio.setStatus("current")
_Me1200ConfigTstRowEditorMep_Type = Unsigned32
_Me1200ConfigTstRowEditorMep_Object = MibScalar
me1200ConfigTstRowEditorMep = _Me1200ConfigTstRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 6),
    _Me1200ConfigTstRowEditorMep_Type()
)
me1200ConfigTstRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorMep.setStatus("current")
_Me1200ConfigTstRowEditorRate_Type = Unsigned32
_Me1200ConfigTstRowEditorRate_Object = MibScalar
me1200ConfigTstRowEditorRate = _Me1200ConfigTstRowEditorRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 7),
    _Me1200ConfigTstRowEditorRate_Type()
)
me1200ConfigTstRowEditorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorRate.setStatus("current")
_Me1200ConfigTstRowEditorSize_Type = Unsigned32
_Me1200ConfigTstRowEditorSize_Object = MibScalar
me1200ConfigTstRowEditorSize = _Me1200ConfigTstRowEditorSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 8),
    _Me1200ConfigTstRowEditorSize_Type()
)
me1200ConfigTstRowEditorSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorSize.setStatus("current")
_Me1200ConfigTstRowEditorPattern_Type = ME1200TstPattern
_Me1200ConfigTstRowEditorPattern_Object = MibScalar
me1200ConfigTstRowEditorPattern = _Me1200ConfigTstRowEditorPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 9),
    _Me1200ConfigTstRowEditorPattern_Type()
)
me1200ConfigTstRowEditorPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorPattern.setStatus("current")
_Me1200ConfigTstRowEditorSequence_Type = TruthValue
_Me1200ConfigTstRowEditorSequence_Object = MibScalar
me1200ConfigTstRowEditorSequence = _Me1200ConfigTstRowEditorSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 10),
    _Me1200ConfigTstRowEditorSequence_Type()
)
me1200ConfigTstRowEditorSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorSequence.setStatus("current")
_Me1200ConfigTstRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigTstRowEditorAction_Object = MibScalar
me1200ConfigTstRowEditorAction = _Me1200ConfigTstRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 7, 2, 101),
    _Me1200ConfigTstRowEditorAction_Type()
)
me1200ConfigTstRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorAction.setStatus("current")
_Me1200ConfigLinkTrace_ObjectIdentity = ObjectIdentity
me1200ConfigLinkTrace = _Me1200ConfigLinkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8)
)
_Me1200ConfigLtTable_Object = MibTable
me1200ConfigLtTable = _Me1200ConfigLtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLtTable.setStatus("current")
_Me1200ConfigLtEntry_Object = MibTableRow
me1200ConfigLtEntry = _Me1200ConfigLtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1)
)
me1200ConfigLtEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLtId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLtEntry.setStatus("current")


class _Me1200ConfigLtId_Type(Integer32):
    """Custom type me1200ConfigLtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLtId_Type.__name__ = "Integer32"
_Me1200ConfigLtId_Object = MibTableColumn
me1200ConfigLtId = _Me1200ConfigLtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 1),
    _Me1200ConfigLtId_Type()
)
me1200ConfigLtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLtId.setStatus("current")
_Me1200ConfigLtDei_Type = ME1200Unsigned8
_Me1200ConfigLtDei_Object = MibTableColumn
me1200ConfigLtDei = _Me1200ConfigLtDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 2),
    _Me1200ConfigLtDei_Type()
)
me1200ConfigLtDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtDei.setStatus("current")
_Me1200ConfigLtPrio_Type = Unsigned32
_Me1200ConfigLtPrio_Object = MibTableColumn
me1200ConfigLtPrio = _Me1200ConfigLtPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 3),
    _Me1200ConfigLtPrio_Type()
)
me1200ConfigLtPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtPrio.setStatus("current")
_Me1200ConfigLtMep_Type = Unsigned32
_Me1200ConfigLtMep_Object = MibTableColumn
me1200ConfigLtMep = _Me1200ConfigLtMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 4),
    _Me1200ConfigLtMep_Type()
)
me1200ConfigLtMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtMep.setStatus("current")
_Me1200ConfigLtMac_Type = MacAddress
_Me1200ConfigLtMac_Object = MibTableColumn
me1200ConfigLtMac = _Me1200ConfigLtMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 5),
    _Me1200ConfigLtMac_Type()
)
me1200ConfigLtMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtMac.setStatus("current")
_Me1200ConfigLtTimeToLive_Type = Unsigned32
_Me1200ConfigLtTimeToLive_Object = MibTableColumn
me1200ConfigLtTimeToLive = _Me1200ConfigLtTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 6),
    _Me1200ConfigLtTimeToLive_Type()
)
me1200ConfigLtTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtTimeToLive.setStatus("current")
_Me1200ConfigLtAction_Type = ME1200RowEditorState
_Me1200ConfigLtAction_Object = MibTableColumn
me1200ConfigLtAction = _Me1200ConfigLtAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 1, 1, 101),
    _Me1200ConfigLtAction_Type()
)
me1200ConfigLtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtAction.setStatus("current")
_Me1200ConfigLtRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigLtRowEditor = _Me1200ConfigLtRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2)
)


class _Me1200ConfigLtRowEditorId_Type(Integer32):
    """Custom type me1200ConfigLtRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLtRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigLtRowEditorId_Object = MibScalar
me1200ConfigLtRowEditorId = _Me1200ConfigLtRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 1),
    _Me1200ConfigLtRowEditorId_Type()
)
me1200ConfigLtRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorId.setStatus("current")
_Me1200ConfigLtRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigLtRowEditorDei_Object = MibScalar
me1200ConfigLtRowEditorDei = _Me1200ConfigLtRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 2),
    _Me1200ConfigLtRowEditorDei_Type()
)
me1200ConfigLtRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorDei.setStatus("current")
_Me1200ConfigLtRowEditorPrio_Type = Unsigned32
_Me1200ConfigLtRowEditorPrio_Object = MibScalar
me1200ConfigLtRowEditorPrio = _Me1200ConfigLtRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 3),
    _Me1200ConfigLtRowEditorPrio_Type()
)
me1200ConfigLtRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorPrio.setStatus("current")
_Me1200ConfigLtRowEditorMep_Type = Unsigned32
_Me1200ConfigLtRowEditorMep_Object = MibScalar
me1200ConfigLtRowEditorMep = _Me1200ConfigLtRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 4),
    _Me1200ConfigLtRowEditorMep_Type()
)
me1200ConfigLtRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorMep.setStatus("current")
_Me1200ConfigLtRowEditorMac_Type = MacAddress
_Me1200ConfigLtRowEditorMac_Object = MibScalar
me1200ConfigLtRowEditorMac = _Me1200ConfigLtRowEditorMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 5),
    _Me1200ConfigLtRowEditorMac_Type()
)
me1200ConfigLtRowEditorMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorMac.setStatus("current")
_Me1200ConfigLtRowEditorTimeToLive_Type = Unsigned32
_Me1200ConfigLtRowEditorTimeToLive_Object = MibScalar
me1200ConfigLtRowEditorTimeToLive = _Me1200ConfigLtRowEditorTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 6),
    _Me1200ConfigLtRowEditorTimeToLive_Type()
)
me1200ConfigLtRowEditorTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorTimeToLive.setStatus("current")
_Me1200ConfigLtRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigLtRowEditorAction_Object = MibScalar
me1200ConfigLtRowEditorAction = _Me1200ConfigLtRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 8, 2, 101),
    _Me1200ConfigLtRowEditorAction_Type()
)
me1200ConfigLtRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorAction.setStatus("current")
_Me1200ConfigAutomaticProtectionSwitching_ObjectIdentity = ObjectIdentity
me1200ConfigAutomaticProtectionSwitching = _Me1200ConfigAutomaticProtectionSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9)
)
_Me1200ConfigApsTable_Object = MibTable
me1200ConfigApsTable = _Me1200ConfigApsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigApsTable.setStatus("current")
_Me1200ConfigApsEntry_Object = MibTableRow
me1200ConfigApsEntry = _Me1200ConfigApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1)
)
me1200ConfigApsEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigApsId"),
)
if mibBuilder.loadTexts:
    me1200ConfigApsEntry.setStatus("current")


class _Me1200ConfigApsId_Type(Integer32):
    """Custom type me1200ConfigApsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigApsId_Type.__name__ = "Integer32"
_Me1200ConfigApsId_Object = MibTableColumn
me1200ConfigApsId = _Me1200ConfigApsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 1),
    _Me1200ConfigApsId_Type()
)
me1200ConfigApsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigApsId.setStatus("current")
_Me1200ConfigApsDei_Type = ME1200Unsigned8
_Me1200ConfigApsDei_Object = MibTableColumn
me1200ConfigApsDei = _Me1200ConfigApsDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 2),
    _Me1200ConfigApsDei_Type()
)
me1200ConfigApsDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsDei.setStatus("current")
_Me1200ConfigApsPrio_Type = Unsigned32
_Me1200ConfigApsPrio_Object = MibTableColumn
me1200ConfigApsPrio = _Me1200ConfigApsPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 3),
    _Me1200ConfigApsPrio_Type()
)
me1200ConfigApsPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsPrio.setStatus("current")
_Me1200ConfigApsApsType_Type = ME1200ApsType
_Me1200ConfigApsApsType_Object = MibTableColumn
me1200ConfigApsApsType = _Me1200ConfigApsApsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 4),
    _Me1200ConfigApsApsType_Type()
)
me1200ConfigApsApsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsApsType.setStatus("current")
_Me1200ConfigApsCast_Type = ME1200Cast
_Me1200ConfigApsCast_Object = MibTableColumn
me1200ConfigApsCast = _Me1200ConfigApsCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 5),
    _Me1200ConfigApsCast_Type()
)
me1200ConfigApsCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsCast.setStatus("current")
_Me1200ConfigApsRapsOctet_Type = Unsigned32
_Me1200ConfigApsRapsOctet_Object = MibTableColumn
me1200ConfigApsRapsOctet = _Me1200ConfigApsRapsOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 6),
    _Me1200ConfigApsRapsOctet_Type()
)
me1200ConfigApsRapsOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRapsOctet.setStatus("current")
_Me1200ConfigApsAction_Type = ME1200RowEditorState
_Me1200ConfigApsAction_Object = MibTableColumn
me1200ConfigApsAction = _Me1200ConfigApsAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 1, 1, 101),
    _Me1200ConfigApsAction_Type()
)
me1200ConfigApsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsAction.setStatus("current")
_Me1200ConfigApsRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigApsRowEditor = _Me1200ConfigApsRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2)
)


class _Me1200ConfigApsRowEditorId_Type(Integer32):
    """Custom type me1200ConfigApsRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigApsRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigApsRowEditorId_Object = MibScalar
me1200ConfigApsRowEditorId = _Me1200ConfigApsRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 1),
    _Me1200ConfigApsRowEditorId_Type()
)
me1200ConfigApsRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorId.setStatus("current")
_Me1200ConfigApsRowEditorDei_Type = ME1200Unsigned8
_Me1200ConfigApsRowEditorDei_Object = MibScalar
me1200ConfigApsRowEditorDei = _Me1200ConfigApsRowEditorDei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 2),
    _Me1200ConfigApsRowEditorDei_Type()
)
me1200ConfigApsRowEditorDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorDei.setStatus("current")
_Me1200ConfigApsRowEditorPrio_Type = Unsigned32
_Me1200ConfigApsRowEditorPrio_Object = MibScalar
me1200ConfigApsRowEditorPrio = _Me1200ConfigApsRowEditorPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 3),
    _Me1200ConfigApsRowEditorPrio_Type()
)
me1200ConfigApsRowEditorPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorPrio.setStatus("current")
_Me1200ConfigApsRowEditorApsType_Type = ME1200ApsType
_Me1200ConfigApsRowEditorApsType_Object = MibScalar
me1200ConfigApsRowEditorApsType = _Me1200ConfigApsRowEditorApsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 4),
    _Me1200ConfigApsRowEditorApsType_Type()
)
me1200ConfigApsRowEditorApsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorApsType.setStatus("current")
_Me1200ConfigApsRowEditorCast_Type = ME1200Cast
_Me1200ConfigApsRowEditorCast_Object = MibScalar
me1200ConfigApsRowEditorCast = _Me1200ConfigApsRowEditorCast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 5),
    _Me1200ConfigApsRowEditorCast_Type()
)
me1200ConfigApsRowEditorCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorCast.setStatus("current")
_Me1200ConfigApsRowEditorRapsOctet_Type = Unsigned32
_Me1200ConfigApsRowEditorRapsOctet_Object = MibScalar
me1200ConfigApsRowEditorRapsOctet = _Me1200ConfigApsRowEditorRapsOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 6),
    _Me1200ConfigApsRowEditorRapsOctet_Type()
)
me1200ConfigApsRowEditorRapsOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorRapsOctet.setStatus("current")
_Me1200ConfigApsRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigApsRowEditorAction_Object = MibScalar
me1200ConfigApsRowEditorAction = _Me1200ConfigApsRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 9, 2, 101),
    _Me1200ConfigApsRowEditorAction_Type()
)
me1200ConfigApsRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorAction.setStatus("current")
_Me1200ConfigAlarmIndicationSignal_ObjectIdentity = ObjectIdentity
me1200ConfigAlarmIndicationSignal = _Me1200ConfigAlarmIndicationSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10)
)
_Me1200ConfigAisTable_Object = MibTable
me1200ConfigAisTable = _Me1200ConfigAisTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigAisTable.setStatus("current")
_Me1200ConfigAisEntry_Object = MibTableRow
me1200ConfigAisEntry = _Me1200ConfigAisEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1, 1)
)
me1200ConfigAisEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigAisId"),
)
if mibBuilder.loadTexts:
    me1200ConfigAisEntry.setStatus("current")


class _Me1200ConfigAisId_Type(Integer32):
    """Custom type me1200ConfigAisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigAisId_Type.__name__ = "Integer32"
_Me1200ConfigAisId_Object = MibTableColumn
me1200ConfigAisId = _Me1200ConfigAisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1, 1, 1),
    _Me1200ConfigAisId_Type()
)
me1200ConfigAisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigAisId.setStatus("current")
_Me1200ConfigAisProtection_Type = TruthValue
_Me1200ConfigAisProtection_Object = MibTableColumn
me1200ConfigAisProtection = _Me1200ConfigAisProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1, 1, 2),
    _Me1200ConfigAisProtection_Type()
)
me1200ConfigAisProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisProtection.setStatus("current")
_Me1200ConfigAisRate_Type = ME1200MepTxRate
_Me1200ConfigAisRate_Object = MibTableColumn
me1200ConfigAisRate = _Me1200ConfigAisRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1, 1, 3),
    _Me1200ConfigAisRate_Type()
)
me1200ConfigAisRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisRate.setStatus("current")
_Me1200ConfigAisAction_Type = ME1200RowEditorState
_Me1200ConfigAisAction_Object = MibTableColumn
me1200ConfigAisAction = _Me1200ConfigAisAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 1, 1, 101),
    _Me1200ConfigAisAction_Type()
)
me1200ConfigAisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisAction.setStatus("current")
_Me1200ConfigAisRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigAisRowEditor = _Me1200ConfigAisRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 2)
)


class _Me1200ConfigAisRowEditorId_Type(Integer32):
    """Custom type me1200ConfigAisRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigAisRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigAisRowEditorId_Object = MibScalar
me1200ConfigAisRowEditorId = _Me1200ConfigAisRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 2, 1),
    _Me1200ConfigAisRowEditorId_Type()
)
me1200ConfigAisRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisRowEditorId.setStatus("current")
_Me1200ConfigAisRowEditorProtection_Type = TruthValue
_Me1200ConfigAisRowEditorProtection_Object = MibScalar
me1200ConfigAisRowEditorProtection = _Me1200ConfigAisRowEditorProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 2, 2),
    _Me1200ConfigAisRowEditorProtection_Type()
)
me1200ConfigAisRowEditorProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisRowEditorProtection.setStatus("current")
_Me1200ConfigAisRowEditorRate_Type = ME1200MepTxRate
_Me1200ConfigAisRowEditorRate_Object = MibScalar
me1200ConfigAisRowEditorRate = _Me1200ConfigAisRowEditorRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 2, 3),
    _Me1200ConfigAisRowEditorRate_Type()
)
me1200ConfigAisRowEditorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisRowEditorRate.setStatus("current")
_Me1200ConfigAisRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigAisRowEditorAction_Object = MibScalar
me1200ConfigAisRowEditorAction = _Me1200ConfigAisRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 10, 2, 101),
    _Me1200ConfigAisRowEditorAction_Type()
)
me1200ConfigAisRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigAisRowEditorAction.setStatus("current")
_Me1200ConfigLockedSignal_ObjectIdentity = ObjectIdentity
me1200ConfigLockedSignal = _Me1200ConfigLockedSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11)
)
_Me1200ConfigLckTable_Object = MibTable
me1200ConfigLckTable = _Me1200ConfigLckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLckTable.setStatus("current")
_Me1200ConfigLckEntry_Object = MibTableRow
me1200ConfigLckEntry = _Me1200ConfigLckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 1, 1)
)
me1200ConfigLckEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLckId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLckEntry.setStatus("current")


class _Me1200ConfigLckId_Type(Integer32):
    """Custom type me1200ConfigLckId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLckId_Type.__name__ = "Integer32"
_Me1200ConfigLckId_Object = MibTableColumn
me1200ConfigLckId = _Me1200ConfigLckId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 1, 1, 1),
    _Me1200ConfigLckId_Type()
)
me1200ConfigLckId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLckId.setStatus("current")
_Me1200ConfigLckRate_Type = ME1200MepTxRate
_Me1200ConfigLckRate_Object = MibTableColumn
me1200ConfigLckRate = _Me1200ConfigLckRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 1, 1, 2),
    _Me1200ConfigLckRate_Type()
)
me1200ConfigLckRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLckRate.setStatus("current")
_Me1200ConfigLckAction_Type = ME1200RowEditorState
_Me1200ConfigLckAction_Object = MibTableColumn
me1200ConfigLckAction = _Me1200ConfigLckAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 1, 1, 101),
    _Me1200ConfigLckAction_Type()
)
me1200ConfigLckAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLckAction.setStatus("current")
_Me1200ConfigLckRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigLckRowEditor = _Me1200ConfigLckRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 2)
)


class _Me1200ConfigLckRowEditorId_Type(Integer32):
    """Custom type me1200ConfigLckRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLckRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigLckRowEditorId_Object = MibScalar
me1200ConfigLckRowEditorId = _Me1200ConfigLckRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 2, 1),
    _Me1200ConfigLckRowEditorId_Type()
)
me1200ConfigLckRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLckRowEditorId.setStatus("current")
_Me1200ConfigLckRowEditorRate_Type = ME1200MepTxRate
_Me1200ConfigLckRowEditorRate_Object = MibScalar
me1200ConfigLckRowEditorRate = _Me1200ConfigLckRowEditorRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 2, 2),
    _Me1200ConfigLckRowEditorRate_Type()
)
me1200ConfigLckRowEditorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLckRowEditorRate.setStatus("current")
_Me1200ConfigLckRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigLckRowEditorAction_Object = MibScalar
me1200ConfigLckRowEditorAction = _Me1200ConfigLckRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 11, 2, 101),
    _Me1200ConfigLckRowEditorAction_Type()
)
me1200ConfigLckRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLckRowEditorAction.setStatus("current")
_Me1200ConfigClient_ObjectIdentity = ObjectIdentity
me1200ConfigClient = _Me1200ConfigClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12)
)
_Me1200ConfigClientTable_Object = MibTable
me1200ConfigClientTable = _Me1200ConfigClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigClientTable.setStatus("current")
_Me1200ConfigClientEntry_Object = MibTableRow
me1200ConfigClientEntry = _Me1200ConfigClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 1, 1)
)
me1200ConfigClientEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigClientId"),
)
if mibBuilder.loadTexts:
    me1200ConfigClientEntry.setStatus("current")


class _Me1200ConfigClientId_Type(Integer32):
    """Custom type me1200ConfigClientId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigClientId_Type.__name__ = "Integer32"
_Me1200ConfigClientId_Object = MibTableColumn
me1200ConfigClientId = _Me1200ConfigClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 1, 1, 1),
    _Me1200ConfigClientId_Type()
)
me1200ConfigClientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigClientId.setStatus("current")
_Me1200ConfigClientDomain_Type = ME1200InstanceDomain
_Me1200ConfigClientDomain_Object = MibTableColumn
me1200ConfigClientDomain = _Me1200ConfigClientDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 1, 1, 2),
    _Me1200ConfigClientDomain_Type()
)
me1200ConfigClientDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientDomain.setStatus("current")
_Me1200ConfigClientFlowTable_Object = MibTable
me1200ConfigClientFlowTable = _Me1200ConfigClientFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    me1200ConfigClientFlowTable.setStatus("current")
_Me1200ConfigClientFlowEntry_Object = MibTableRow
me1200ConfigClientFlowEntry = _Me1200ConfigClientFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1)
)
me1200ConfigClientFlowEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigClientFlowId"),
    (0, "ME1200-MEP-MIB", "me1200ConfigClientFlowFlowId"),
)
if mibBuilder.loadTexts:
    me1200ConfigClientFlowEntry.setStatus("current")


class _Me1200ConfigClientFlowId_Type(Integer32):
    """Custom type me1200ConfigClientFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigClientFlowId_Type.__name__ = "Integer32"
_Me1200ConfigClientFlowId_Object = MibTableColumn
me1200ConfigClientFlowId = _Me1200ConfigClientFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 1),
    _Me1200ConfigClientFlowId_Type()
)
me1200ConfigClientFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowId.setStatus("current")


class _Me1200ConfigClientFlowFlowId_Type(Integer32):
    """Custom type me1200ConfigClientFlowFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigClientFlowFlowId_Type.__name__ = "Integer32"
_Me1200ConfigClientFlowFlowId_Object = MibTableColumn
me1200ConfigClientFlowFlowId = _Me1200ConfigClientFlowFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 2),
    _Me1200ConfigClientFlowFlowId_Type()
)
me1200ConfigClientFlowFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowFlowId.setStatus("current")
_Me1200ConfigClientFlowAisPrio_Type = ME1200Unsigned8
_Me1200ConfigClientFlowAisPrio_Object = MibTableColumn
me1200ConfigClientFlowAisPrio = _Me1200ConfigClientFlowAisPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 3),
    _Me1200ConfigClientFlowAisPrio_Type()
)
me1200ConfigClientFlowAisPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowAisPrio.setStatus("current")
_Me1200ConfigClientFlowLckPrio_Type = ME1200Unsigned8
_Me1200ConfigClientFlowLckPrio_Object = MibTableColumn
me1200ConfigClientFlowLckPrio = _Me1200ConfigClientFlowLckPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 4),
    _Me1200ConfigClientFlowLckPrio_Type()
)
me1200ConfigClientFlowLckPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowLckPrio.setStatus("current")
_Me1200ConfigClientFlowLevel_Type = ME1200Unsigned8
_Me1200ConfigClientFlowLevel_Object = MibTableColumn
me1200ConfigClientFlowLevel = _Me1200ConfigClientFlowLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 5),
    _Me1200ConfigClientFlowLevel_Type()
)
me1200ConfigClientFlowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowLevel.setStatus("current")
_Me1200ConfigClientFlowAction_Type = ME1200RowEditorState
_Me1200ConfigClientFlowAction_Object = MibTableColumn
me1200ConfigClientFlowAction = _Me1200ConfigClientFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 2, 1, 100),
    _Me1200ConfigClientFlowAction_Type()
)
me1200ConfigClientFlowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowAction.setStatus("current")
_Me1200ConfigClientFlowRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigClientFlowRowEditor = _Me1200ConfigClientFlowRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3)
)


class _Me1200ConfigClientFlowRowEditorId_Type(Integer32):
    """Custom type me1200ConfigClientFlowRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigClientFlowRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigClientFlowRowEditorId_Object = MibScalar
me1200ConfigClientFlowRowEditorId = _Me1200ConfigClientFlowRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 1),
    _Me1200ConfigClientFlowRowEditorId_Type()
)
me1200ConfigClientFlowRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorId.setStatus("current")


class _Me1200ConfigClientFlowRowEditorFlowId_Type(Integer32):
    """Custom type me1200ConfigClientFlowRowEditorFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigClientFlowRowEditorFlowId_Type.__name__ = "Integer32"
_Me1200ConfigClientFlowRowEditorFlowId_Object = MibScalar
me1200ConfigClientFlowRowEditorFlowId = _Me1200ConfigClientFlowRowEditorFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 2),
    _Me1200ConfigClientFlowRowEditorFlowId_Type()
)
me1200ConfigClientFlowRowEditorFlowId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorFlowId.setStatus("current")
_Me1200ConfigClientFlowRowEditorAisPrio_Type = ME1200Unsigned8
_Me1200ConfigClientFlowRowEditorAisPrio_Object = MibScalar
me1200ConfigClientFlowRowEditorAisPrio = _Me1200ConfigClientFlowRowEditorAisPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 3),
    _Me1200ConfigClientFlowRowEditorAisPrio_Type()
)
me1200ConfigClientFlowRowEditorAisPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorAisPrio.setStatus("current")
_Me1200ConfigClientFlowRowEditorLckPrio_Type = ME1200Unsigned8
_Me1200ConfigClientFlowRowEditorLckPrio_Object = MibScalar
me1200ConfigClientFlowRowEditorLckPrio = _Me1200ConfigClientFlowRowEditorLckPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 4),
    _Me1200ConfigClientFlowRowEditorLckPrio_Type()
)
me1200ConfigClientFlowRowEditorLckPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorLckPrio.setStatus("current")
_Me1200ConfigClientFlowRowEditorLevel_Type = ME1200Unsigned8
_Me1200ConfigClientFlowRowEditorLevel_Object = MibScalar
me1200ConfigClientFlowRowEditorLevel = _Me1200ConfigClientFlowRowEditorLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 5),
    _Me1200ConfigClientFlowRowEditorLevel_Type()
)
me1200ConfigClientFlowRowEditorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorLevel.setStatus("current")
_Me1200ConfigClientFlowRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigClientFlowRowEditorAction_Object = MibScalar
me1200ConfigClientFlowRowEditorAction = _Me1200ConfigClientFlowRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 12, 3, 100),
    _Me1200ConfigClientFlowRowEditorAction_Type()
)
me1200ConfigClientFlowRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorAction.setStatus("current")
_Me1200ConfigSyslog_ObjectIdentity = ObjectIdentity
me1200ConfigSyslog = _Me1200ConfigSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 13)
)
_Me1200ConfigSyslogTable_Object = MibTable
me1200ConfigSyslogTable = _Me1200ConfigSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigSyslogTable.setStatus("current")
_Me1200ConfigSyslogEntry_Object = MibTableRow
me1200ConfigSyslogEntry = _Me1200ConfigSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 13, 1, 1)
)
me1200ConfigSyslogEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigSyslogId"),
)
if mibBuilder.loadTexts:
    me1200ConfigSyslogEntry.setStatus("current")


class _Me1200ConfigSyslogId_Type(Integer32):
    """Custom type me1200ConfigSyslogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigSyslogId_Type.__name__ = "Integer32"
_Me1200ConfigSyslogId_Object = MibTableColumn
me1200ConfigSyslogId = _Me1200ConfigSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 13, 1, 1, 1),
    _Me1200ConfigSyslogId_Type()
)
me1200ConfigSyslogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigSyslogId.setStatus("current")
_Me1200ConfigSyslogEnable_Type = TruthValue
_Me1200ConfigSyslogEnable_Object = MibTableColumn
me1200ConfigSyslogEnable = _Me1200ConfigSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 13, 1, 1, 2),
    _Me1200ConfigSyslogEnable_Type()
)
me1200ConfigSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigSyslogEnable.setStatus("current")
_Me1200ConfigTlv_ObjectIdentity = ObjectIdentity
me1200ConfigTlv = _Me1200ConfigTlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14)
)
_Me1200ConfigTlvLeaf_ObjectIdentity = ObjectIdentity
me1200ConfigTlvLeaf = _Me1200ConfigTlvLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1)
)
_Me1200ConfigTlvLeafOsTlvOuiFirst_Type = ME1200Unsigned8
_Me1200ConfigTlvLeafOsTlvOuiFirst_Object = MibScalar
me1200ConfigTlvLeafOsTlvOuiFirst = _Me1200ConfigTlvLeafOsTlvOuiFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1, 2),
    _Me1200ConfigTlvLeafOsTlvOuiFirst_Type()
)
me1200ConfigTlvLeafOsTlvOuiFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafOsTlvOuiFirst.setStatus("current")
_Me1200ConfigTlvLeafOsTlvOuiSecond_Type = ME1200Unsigned8
_Me1200ConfigTlvLeafOsTlvOuiSecond_Object = MibScalar
me1200ConfigTlvLeafOsTlvOuiSecond = _Me1200ConfigTlvLeafOsTlvOuiSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1, 3),
    _Me1200ConfigTlvLeafOsTlvOuiSecond_Type()
)
me1200ConfigTlvLeafOsTlvOuiSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafOsTlvOuiSecond.setStatus("current")
_Me1200ConfigTlvLeafOsTlvOuiThird_Type = ME1200Unsigned8
_Me1200ConfigTlvLeafOsTlvOuiThird_Object = MibScalar
me1200ConfigTlvLeafOsTlvOuiThird = _Me1200ConfigTlvLeafOsTlvOuiThird_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1, 4),
    _Me1200ConfigTlvLeafOsTlvOuiThird_Type()
)
me1200ConfigTlvLeafOsTlvOuiThird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafOsTlvOuiThird.setStatus("current")
_Me1200ConfigTlvLeafOsTlvSubType_Type = ME1200Unsigned8
_Me1200ConfigTlvLeafOsTlvSubType_Object = MibScalar
me1200ConfigTlvLeafOsTlvSubType = _Me1200ConfigTlvLeafOsTlvSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1, 5),
    _Me1200ConfigTlvLeafOsTlvSubType_Type()
)
me1200ConfigTlvLeafOsTlvSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafOsTlvSubType.setStatus("current")
_Me1200ConfigTlvLeafOsTlvValue_Type = ME1200Unsigned8
_Me1200ConfigTlvLeafOsTlvValue_Object = MibScalar
me1200ConfigTlvLeafOsTlvValue = _Me1200ConfigTlvLeafOsTlvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 14, 1, 6),
    _Me1200ConfigTlvLeafOsTlvValue_Type()
)
me1200ConfigTlvLeafOsTlvValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafOsTlvValue.setStatus("current")
_Me1200ConfigLinkStateTracking_ObjectIdentity = ObjectIdentity
me1200ConfigLinkStateTracking = _Me1200ConfigLinkStateTracking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 15)
)
_Me1200ConfigLstTable_Object = MibTable
me1200ConfigLstTable = _Me1200ConfigLstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLstTable.setStatus("current")
_Me1200ConfigLstEntry_Object = MibTableRow
me1200ConfigLstEntry = _Me1200ConfigLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 15, 1, 1)
)
me1200ConfigLstEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLstId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLstEntry.setStatus("current")


class _Me1200ConfigLstId_Type(Integer32):
    """Custom type me1200ConfigLstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLstId_Type.__name__ = "Integer32"
_Me1200ConfigLstId_Object = MibTableColumn
me1200ConfigLstId = _Me1200ConfigLstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 15, 1, 1, 1),
    _Me1200ConfigLstId_Type()
)
me1200ConfigLstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLstId.setStatus("current")
_Me1200ConfigLstEnable_Type = TruthValue
_Me1200ConfigLstEnable_Object = MibTableColumn
me1200ConfigLstEnable = _Me1200ConfigLstEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 15, 1, 1, 2),
    _Me1200ConfigLstEnable_Type()
)
me1200ConfigLstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLstEnable.setStatus("current")
_Me1200ConfigLmAvailability_ObjectIdentity = ObjectIdentity
me1200ConfigLmAvailability = _Me1200ConfigLmAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16)
)
_Me1200ConfigLmAvailTable_Object = MibTable
me1200ConfigLmAvailTable = _Me1200ConfigLmAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    me1200ConfigLmAvailTable.setStatus("current")
_Me1200ConfigLmAvailEntry_Object = MibTableRow
me1200ConfigLmAvailEntry = _Me1200ConfigLmAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1)
)
me1200ConfigLmAvailEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ConfigLmAvailId"),
)
if mibBuilder.loadTexts:
    me1200ConfigLmAvailEntry.setStatus("current")


class _Me1200ConfigLmAvailId_Type(Integer32):
    """Custom type me1200ConfigLmAvailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLmAvailId_Type.__name__ = "Integer32"
_Me1200ConfigLmAvailId_Object = MibTableColumn
me1200ConfigLmAvailId = _Me1200ConfigLmAvailId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 1),
    _Me1200ConfigLmAvailId_Type()
)
me1200ConfigLmAvailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailId.setStatus("current")
_Me1200ConfigLmAvailEnable_Type = TruthValue
_Me1200ConfigLmAvailEnable_Object = MibTableColumn
me1200ConfigLmAvailEnable = _Me1200ConfigLmAvailEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 2),
    _Me1200ConfigLmAvailEnable_Type()
)
me1200ConfigLmAvailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailEnable.setStatus("current")
_Me1200ConfigLmAvailLosRatioThr_Type = Unsigned32
_Me1200ConfigLmAvailLosRatioThr_Object = MibTableColumn
me1200ConfigLmAvailLosRatioThr = _Me1200ConfigLmAvailLosRatioThr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 3),
    _Me1200ConfigLmAvailLosRatioThr_Type()
)
me1200ConfigLmAvailLosRatioThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailLosRatioThr.setStatus("current")
_Me1200ConfigLmAvailInterval_Type = Unsigned32
_Me1200ConfigLmAvailInterval_Object = MibTableColumn
me1200ConfigLmAvailInterval = _Me1200ConfigLmAvailInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 4),
    _Me1200ConfigLmAvailInterval_Type()
)
me1200ConfigLmAvailInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailInterval.setStatus("current")
_Me1200ConfigLmAvailMaintenance_Type = TruthValue
_Me1200ConfigLmAvailMaintenance_Object = MibTableColumn
me1200ConfigLmAvailMaintenance = _Me1200ConfigLmAvailMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 5),
    _Me1200ConfigLmAvailMaintenance_Type()
)
me1200ConfigLmAvailMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailMaintenance.setStatus("current")
_Me1200ConfigLmAvailAction_Type = ME1200RowEditorState
_Me1200ConfigLmAvailAction_Object = MibTableColumn
me1200ConfigLmAvailAction = _Me1200ConfigLmAvailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 1, 1, 101),
    _Me1200ConfigLmAvailAction_Type()
)
me1200ConfigLmAvailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailAction.setStatus("current")
_Me1200ConfigLmAvailRowEditor_ObjectIdentity = ObjectIdentity
me1200ConfigLmAvailRowEditor = _Me1200ConfigLmAvailRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2)
)


class _Me1200ConfigLmAvailRowEditorId_Type(Integer32):
    """Custom type me1200ConfigLmAvailRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigLmAvailRowEditorId_Type.__name__ = "Integer32"
_Me1200ConfigLmAvailRowEditorId_Object = MibScalar
me1200ConfigLmAvailRowEditorId = _Me1200ConfigLmAvailRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 1),
    _Me1200ConfigLmAvailRowEditorId_Type()
)
me1200ConfigLmAvailRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorId.setStatus("current")
_Me1200ConfigLmAvailRowEditorEnable_Type = TruthValue
_Me1200ConfigLmAvailRowEditorEnable_Object = MibScalar
me1200ConfigLmAvailRowEditorEnable = _Me1200ConfigLmAvailRowEditorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 2),
    _Me1200ConfigLmAvailRowEditorEnable_Type()
)
me1200ConfigLmAvailRowEditorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorEnable.setStatus("current")
_Me1200ConfigLmAvailRowEditorLosRatioThr_Type = Unsigned32
_Me1200ConfigLmAvailRowEditorLosRatioThr_Object = MibScalar
me1200ConfigLmAvailRowEditorLosRatioThr = _Me1200ConfigLmAvailRowEditorLosRatioThr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 3),
    _Me1200ConfigLmAvailRowEditorLosRatioThr_Type()
)
me1200ConfigLmAvailRowEditorLosRatioThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorLosRatioThr.setStatus("current")
_Me1200ConfigLmAvailRowEditorInterval_Type = Unsigned32
_Me1200ConfigLmAvailRowEditorInterval_Object = MibScalar
me1200ConfigLmAvailRowEditorInterval = _Me1200ConfigLmAvailRowEditorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 4),
    _Me1200ConfigLmAvailRowEditorInterval_Type()
)
me1200ConfigLmAvailRowEditorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorInterval.setStatus("current")
_Me1200ConfigLmAvailRowEditorMaintenance_Type = TruthValue
_Me1200ConfigLmAvailRowEditorMaintenance_Object = MibScalar
me1200ConfigLmAvailRowEditorMaintenance = _Me1200ConfigLmAvailRowEditorMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 5),
    _Me1200ConfigLmAvailRowEditorMaintenance_Type()
)
me1200ConfigLmAvailRowEditorMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorMaintenance.setStatus("current")
_Me1200ConfigLmAvailRowEditorAction_Type = ME1200RowEditorState
_Me1200ConfigLmAvailRowEditorAction_Object = MibScalar
me1200ConfigLmAvailRowEditorAction = _Me1200ConfigLmAvailRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 2, 16, 2, 101),
    _Me1200ConfigLmAvailRowEditorAction_Type()
)
me1200ConfigLmAvailRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorAction.setStatus("current")
_Me1200MepStatus_ObjectIdentity = ObjectIdentity
me1200MepStatus = _Me1200MepStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3)
)
_Me1200StatusInstance_ObjectIdentity = ObjectIdentity
me1200StatusInstance = _Me1200StatusInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1)
)
_Me1200StatusInstanceTable_Object = MibTable
me1200StatusInstanceTable = _Me1200StatusInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200StatusInstanceTable.setStatus("current")
_Me1200StatusInstanceEntry_Object = MibTableRow
me1200StatusInstanceEntry = _Me1200StatusInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1)
)
me1200StatusInstanceEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusInstanceId"),
)
if mibBuilder.loadTexts:
    me1200StatusInstanceEntry.setStatus("current")


class _Me1200StatusInstanceId_Type(Integer32):
    """Custom type me1200StatusInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusInstanceId_Type.__name__ = "Integer32"
_Me1200StatusInstanceId_Object = MibTableColumn
me1200StatusInstanceId = _Me1200StatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 1),
    _Me1200StatusInstanceId_Type()
)
me1200StatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusInstanceId.setStatus("current")
_Me1200StatusInstanceClevel_Type = TruthValue
_Me1200StatusInstanceClevel_Object = MibTableColumn
me1200StatusInstanceClevel = _Me1200StatusInstanceClevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 2),
    _Me1200StatusInstanceClevel_Type()
)
me1200StatusInstanceClevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceClevel.setStatus("current")
_Me1200StatusInstanceCmeg_Type = TruthValue
_Me1200StatusInstanceCmeg_Object = MibTableColumn
me1200StatusInstanceCmeg = _Me1200StatusInstanceCmeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 3),
    _Me1200StatusInstanceCmeg_Type()
)
me1200StatusInstanceCmeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCmeg.setStatus("current")
_Me1200StatusInstanceCmep_Type = TruthValue
_Me1200StatusInstanceCmep_Object = MibTableColumn
me1200StatusInstanceCmep = _Me1200StatusInstanceCmep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 4),
    _Me1200StatusInstanceCmep_Type()
)
me1200StatusInstanceCmep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCmep.setStatus("current")
_Me1200StatusInstanceCssf_Type = TruthValue
_Me1200StatusInstanceCssf_Object = MibTableColumn
me1200StatusInstanceCssf = _Me1200StatusInstanceCssf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 5),
    _Me1200StatusInstanceCssf_Type()
)
me1200StatusInstanceCssf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCssf.setStatus("current")
_Me1200StatusInstanceCais_Type = TruthValue
_Me1200StatusInstanceCais_Object = MibTableColumn
me1200StatusInstanceCais = _Me1200StatusInstanceCais_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 6),
    _Me1200StatusInstanceCais_Type()
)
me1200StatusInstanceCais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCais.setStatus("current")
_Me1200StatusInstanceClck_Type = TruthValue
_Me1200StatusInstanceClck_Object = MibTableColumn
me1200StatusInstanceClck = _Me1200StatusInstanceClck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 7),
    _Me1200StatusInstanceClck_Type()
)
me1200StatusInstanceClck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceClck.setStatus("current")
_Me1200StatusInstanceAtsf_Type = TruthValue
_Me1200StatusInstanceAtsf_Object = MibTableColumn
me1200StatusInstanceAtsf = _Me1200StatusInstanceAtsf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 8),
    _Me1200StatusInstanceAtsf_Type()
)
me1200StatusInstanceAtsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceAtsf.setStatus("current")
_Me1200StatusInstanceAtsd_Type = TruthValue
_Me1200StatusInstanceAtsd_Object = MibTableColumn
me1200StatusInstanceAtsd = _Me1200StatusInstanceAtsd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 9),
    _Me1200StatusInstanceAtsd_Type()
)
me1200StatusInstanceAtsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceAtsd.setStatus("current")
_Me1200StatusInstanceAblk_Type = TruthValue
_Me1200StatusInstanceAblk_Object = MibTableColumn
me1200StatusInstanceAblk = _Me1200StatusInstanceAblk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 10),
    _Me1200StatusInstanceAblk_Type()
)
me1200StatusInstanceAblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceAblk.setStatus("current")
_Me1200StatusInstanceCloop_Type = TruthValue
_Me1200StatusInstanceCloop_Object = MibTableColumn
me1200StatusInstanceCloop = _Me1200StatusInstanceCloop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 11),
    _Me1200StatusInstanceCloop_Type()
)
me1200StatusInstanceCloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCloop.setStatus("current")
_Me1200StatusInstanceCconfig_Type = TruthValue
_Me1200StatusInstanceCconfig_Object = MibTableColumn
me1200StatusInstanceCconfig = _Me1200StatusInstanceCconfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 1, 1, 12),
    _Me1200StatusInstanceCconfig_Type()
)
me1200StatusInstanceCconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstanceCconfig.setStatus("current")
_Me1200StatusInstancePeerTable_Object = MibTable
me1200StatusInstancePeerTable = _Me1200StatusInstancePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    me1200StatusInstancePeerTable.setStatus("current")
_Me1200StatusInstancePeerEntry_Object = MibTableRow
me1200StatusInstancePeerEntry = _Me1200StatusInstancePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1)
)
me1200StatusInstancePeerEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusInstancePeerId"),
    (0, "ME1200-MEP-MIB", "me1200StatusInstancePeerPeerId"),
)
if mibBuilder.loadTexts:
    me1200StatusInstancePeerEntry.setStatus("current")


class _Me1200StatusInstancePeerId_Type(Integer32):
    """Custom type me1200StatusInstancePeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusInstancePeerId_Type.__name__ = "Integer32"
_Me1200StatusInstancePeerId_Object = MibTableColumn
me1200StatusInstancePeerId = _Me1200StatusInstancePeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 1),
    _Me1200StatusInstancePeerId_Type()
)
me1200StatusInstancePeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerId.setStatus("current")


class _Me1200StatusInstancePeerPeerId_Type(Integer32):
    """Custom type me1200StatusInstancePeerPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusInstancePeerPeerId_Type.__name__ = "Integer32"
_Me1200StatusInstancePeerPeerId_Object = MibTableColumn
me1200StatusInstancePeerPeerId = _Me1200StatusInstancePeerPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 2),
    _Me1200StatusInstancePeerPeerId_Type()
)
me1200StatusInstancePeerPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerPeerId.setStatus("current")
_Me1200StatusInstancePeerCloc_Type = TruthValue
_Me1200StatusInstancePeerCloc_Object = MibTableColumn
me1200StatusInstancePeerCloc = _Me1200StatusInstancePeerCloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 3),
    _Me1200StatusInstancePeerCloc_Type()
)
me1200StatusInstancePeerCloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerCloc.setStatus("current")
_Me1200StatusInstancePeerCrdi_Type = TruthValue
_Me1200StatusInstancePeerCrdi_Object = MibTableColumn
me1200StatusInstancePeerCrdi = _Me1200StatusInstancePeerCrdi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 4),
    _Me1200StatusInstancePeerCrdi_Type()
)
me1200StatusInstancePeerCrdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerCrdi.setStatus("current")
_Me1200StatusInstancePeerCperiod_Type = TruthValue
_Me1200StatusInstancePeerCperiod_Object = MibTableColumn
me1200StatusInstancePeerCperiod = _Me1200StatusInstancePeerCperiod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 5),
    _Me1200StatusInstancePeerCperiod_Type()
)
me1200StatusInstancePeerCperiod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerCperiod.setStatus("current")
_Me1200StatusInstancePeerCprio_Type = TruthValue
_Me1200StatusInstancePeerCprio_Object = MibTableColumn
me1200StatusInstancePeerCprio = _Me1200StatusInstancePeerCprio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 1, 2, 1, 6),
    _Me1200StatusInstancePeerCprio_Type()
)
me1200StatusInstancePeerCprio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusInstancePeerCprio.setStatus("current")
_Me1200StatusLossMeasurement_ObjectIdentity = ObjectIdentity
me1200StatusLossMeasurement = _Me1200StatusLossMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2)
)
_Me1200StatusLmTable_Object = MibTable
me1200StatusLmTable = _Me1200StatusLmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200StatusLmTable.setStatus("current")
_Me1200StatusLmEntry_Object = MibTableRow
me1200StatusLmEntry = _Me1200StatusLmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1)
)
me1200StatusLmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLmId"),
)
if mibBuilder.loadTexts:
    me1200StatusLmEntry.setStatus("current")


class _Me1200StatusLmId_Type(Integer32):
    """Custom type me1200StatusLmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLmId_Type.__name__ = "Integer32"
_Me1200StatusLmId_Object = MibTableColumn
me1200StatusLmId = _Me1200StatusLmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 1),
    _Me1200StatusLmId_Type()
)
me1200StatusLmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLmId.setStatus("current")
_Me1200StatusLmTxCounter_Type = Unsigned32
_Me1200StatusLmTxCounter_Object = MibTableColumn
me1200StatusLmTxCounter = _Me1200StatusLmTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 2),
    _Me1200StatusLmTxCounter_Type()
)
me1200StatusLmTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmTxCounter.setStatus("current")
_Me1200StatusLmRxCounter_Type = Unsigned32
_Me1200StatusLmRxCounter_Object = MibTableColumn
me1200StatusLmRxCounter = _Me1200StatusLmRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 3),
    _Me1200StatusLmRxCounter_Type()
)
me1200StatusLmRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmRxCounter.setStatus("current")
_Me1200StatusLmNearEndLosCounter_Type = Integer32
_Me1200StatusLmNearEndLosCounter_Object = MibTableColumn
me1200StatusLmNearEndLosCounter = _Me1200StatusLmNearEndLosCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 4),
    _Me1200StatusLmNearEndLosCounter_Type()
)
me1200StatusLmNearEndLosCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmNearEndLosCounter.setStatus("current")
_Me1200StatusLmFarEndLosCounter_Type = Integer32
_Me1200StatusLmFarEndLosCounter_Object = MibTableColumn
me1200StatusLmFarEndLosCounter = _Me1200StatusLmFarEndLosCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 5),
    _Me1200StatusLmFarEndLosCounter_Type()
)
me1200StatusLmFarEndLosCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmFarEndLosCounter.setStatus("current")
_Me1200StatusLmNearEndLosRatio_Type = Unsigned32
_Me1200StatusLmNearEndLosRatio_Object = MibTableColumn
me1200StatusLmNearEndLosRatio = _Me1200StatusLmNearEndLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 6),
    _Me1200StatusLmNearEndLosRatio_Type()
)
me1200StatusLmNearEndLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmNearEndLosRatio.setStatus("current")
_Me1200StatusLmFarEndLosRatio_Type = Unsigned32
_Me1200StatusLmFarEndLosRatio_Object = MibTableColumn
me1200StatusLmFarEndLosRatio = _Me1200StatusLmFarEndLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 7),
    _Me1200StatusLmFarEndLosRatio_Type()
)
me1200StatusLmFarEndLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmFarEndLosRatio.setStatus("current")
_Me1200StatusLmNearEndTotalLosRatio_Type = Unsigned32
_Me1200StatusLmNearEndTotalLosRatio_Object = MibTableColumn
me1200StatusLmNearEndTotalLosRatio = _Me1200StatusLmNearEndTotalLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 8),
    _Me1200StatusLmNearEndTotalLosRatio_Type()
)
me1200StatusLmNearEndTotalLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmNearEndTotalLosRatio.setStatus("current")
_Me1200StatusLmFarEndtotalLosRatio_Type = Unsigned32
_Me1200StatusLmFarEndtotalLosRatio_Object = MibTableColumn
me1200StatusLmFarEndtotalLosRatio = _Me1200StatusLmFarEndtotalLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 9),
    _Me1200StatusLmFarEndtotalLosRatio_Type()
)
me1200StatusLmFarEndtotalLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmFarEndtotalLosRatio.setStatus("current")
_Me1200StatusLmIntervalElapsed_Type = Unsigned32
_Me1200StatusLmIntervalElapsed_Object = MibTableColumn
me1200StatusLmIntervalElapsed = _Me1200StatusLmIntervalElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 1, 1, 10),
    _Me1200StatusLmIntervalElapsed_Type()
)
me1200StatusLmIntervalElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmIntervalElapsed.setStatus("current")
_Me1200StatusLmPeerTable_Object = MibTable
me1200StatusLmPeerTable = _Me1200StatusLmPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    me1200StatusLmPeerTable.setStatus("current")
_Me1200StatusLmPeerEntry_Object = MibTableRow
me1200StatusLmPeerEntry = _Me1200StatusLmPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1)
)
me1200StatusLmPeerEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLmPeerId"),
    (0, "ME1200-MEP-MIB", "me1200StatusLmPeerPeerId"),
)
if mibBuilder.loadTexts:
    me1200StatusLmPeerEntry.setStatus("current")


class _Me1200StatusLmPeerId_Type(Integer32):
    """Custom type me1200StatusLmPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLmPeerId_Type.__name__ = "Integer32"
_Me1200StatusLmPeerId_Object = MibTableColumn
me1200StatusLmPeerId = _Me1200StatusLmPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 1),
    _Me1200StatusLmPeerId_Type()
)
me1200StatusLmPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLmPeerId.setStatus("current")


class _Me1200StatusLmPeerPeerId_Type(Integer32):
    """Custom type me1200StatusLmPeerPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLmPeerPeerId_Type.__name__ = "Integer32"
_Me1200StatusLmPeerPeerId_Object = MibTableColumn
me1200StatusLmPeerPeerId = _Me1200StatusLmPeerPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 2),
    _Me1200StatusLmPeerPeerId_Type()
)
me1200StatusLmPeerPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLmPeerPeerId.setStatus("current")
_Me1200StatusLmPeerTxCounter_Type = Unsigned32
_Me1200StatusLmPeerTxCounter_Object = MibTableColumn
me1200StatusLmPeerTxCounter = _Me1200StatusLmPeerTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 3),
    _Me1200StatusLmPeerTxCounter_Type()
)
me1200StatusLmPeerTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerTxCounter.setStatus("current")
_Me1200StatusLmPeerRxCounter_Type = Unsigned32
_Me1200StatusLmPeerRxCounter_Object = MibTableColumn
me1200StatusLmPeerRxCounter = _Me1200StatusLmPeerRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 4),
    _Me1200StatusLmPeerRxCounter_Type()
)
me1200StatusLmPeerRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerRxCounter.setStatus("current")
_Me1200StatusLmPeerNearEndLosCounter_Type = Integer32
_Me1200StatusLmPeerNearEndLosCounter_Object = MibTableColumn
me1200StatusLmPeerNearEndLosCounter = _Me1200StatusLmPeerNearEndLosCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 5),
    _Me1200StatusLmPeerNearEndLosCounter_Type()
)
me1200StatusLmPeerNearEndLosCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerNearEndLosCounter.setStatus("current")
_Me1200StatusLmPeerFarEndLosCounter_Type = Integer32
_Me1200StatusLmPeerFarEndLosCounter_Object = MibTableColumn
me1200StatusLmPeerFarEndLosCounter = _Me1200StatusLmPeerFarEndLosCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 6),
    _Me1200StatusLmPeerFarEndLosCounter_Type()
)
me1200StatusLmPeerFarEndLosCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerFarEndLosCounter.setStatus("current")
_Me1200StatusLmPeerNearEndLosRatio_Type = Unsigned32
_Me1200StatusLmPeerNearEndLosRatio_Object = MibTableColumn
me1200StatusLmPeerNearEndLosRatio = _Me1200StatusLmPeerNearEndLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 7),
    _Me1200StatusLmPeerNearEndLosRatio_Type()
)
me1200StatusLmPeerNearEndLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerNearEndLosRatio.setStatus("current")
_Me1200StatusLmPeerFarEndLosRatio_Type = Unsigned32
_Me1200StatusLmPeerFarEndLosRatio_Object = MibTableColumn
me1200StatusLmPeerFarEndLosRatio = _Me1200StatusLmPeerFarEndLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 8),
    _Me1200StatusLmPeerFarEndLosRatio_Type()
)
me1200StatusLmPeerFarEndLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerFarEndLosRatio.setStatus("current")
_Me1200StatusLmPeerNearEndTotalLosRatio_Type = Unsigned32
_Me1200StatusLmPeerNearEndTotalLosRatio_Object = MibTableColumn
me1200StatusLmPeerNearEndTotalLosRatio = _Me1200StatusLmPeerNearEndTotalLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 9),
    _Me1200StatusLmPeerNearEndTotalLosRatio_Type()
)
me1200StatusLmPeerNearEndTotalLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerNearEndTotalLosRatio.setStatus("current")
_Me1200StatusLmPeerFarEndtotalLosRatio_Type = Unsigned32
_Me1200StatusLmPeerFarEndtotalLosRatio_Object = MibTableColumn
me1200StatusLmPeerFarEndtotalLosRatio = _Me1200StatusLmPeerFarEndtotalLosRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 10),
    _Me1200StatusLmPeerFarEndtotalLosRatio_Type()
)
me1200StatusLmPeerFarEndtotalLosRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerFarEndtotalLosRatio.setStatus("current")
_Me1200StatusLmPeerIntervalElapsed_Type = Unsigned32
_Me1200StatusLmPeerIntervalElapsed_Object = MibTableColumn
me1200StatusLmPeerIntervalElapsed = _Me1200StatusLmPeerIntervalElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 2, 2, 1, 11),
    _Me1200StatusLmPeerIntervalElapsed_Type()
)
me1200StatusLmPeerIntervalElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmPeerIntervalElapsed.setStatus("current")
_Me1200StatusDelayMeasurement_ObjectIdentity = ObjectIdentity
me1200StatusDelayMeasurement = _Me1200StatusDelayMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3)
)
_Me1200StatusDmTwoWayTable_Object = MibTable
me1200StatusDmTwoWayTable = _Me1200StatusDmTwoWayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayTable.setStatus("current")
_Me1200StatusDmTwoWayEntry_Object = MibTableRow
me1200StatusDmTwoWayEntry = _Me1200StatusDmTwoWayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1)
)
me1200StatusDmTwoWayEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusDmTwoWayId"),
)
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayEntry.setStatus("current")


class _Me1200StatusDmTwoWayId_Type(Integer32):
    """Custom type me1200StatusDmTwoWayId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusDmTwoWayId_Type.__name__ = "Integer32"
_Me1200StatusDmTwoWayId_Object = MibTableColumn
me1200StatusDmTwoWayId = _Me1200StatusDmTwoWayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 1),
    _Me1200StatusDmTwoWayId_Type()
)
me1200StatusDmTwoWayId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayId.setStatus("current")
_Me1200StatusDmTwoWayTxCounter_Type = Unsigned32
_Me1200StatusDmTwoWayTxCounter_Object = MibTableColumn
me1200StatusDmTwoWayTxCounter = _Me1200StatusDmTwoWayTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 2),
    _Me1200StatusDmTwoWayTxCounter_Type()
)
me1200StatusDmTwoWayTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayTxCounter.setStatus("current")
_Me1200StatusDmTwoWayRxCounter_Type = Unsigned32
_Me1200StatusDmTwoWayRxCounter_Object = MibTableColumn
me1200StatusDmTwoWayRxCounter = _Me1200StatusDmTwoWayRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 3),
    _Me1200StatusDmTwoWayRxCounter_Type()
)
me1200StatusDmTwoWayRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayRxCounter.setStatus("current")
_Me1200StatusDmTwoWayRxTimeOutCounter_Type = Unsigned32
_Me1200StatusDmTwoWayRxTimeOutCounter_Object = MibTableColumn
me1200StatusDmTwoWayRxTimeOutCounter = _Me1200StatusDmTwoWayRxTimeOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 4),
    _Me1200StatusDmTwoWayRxTimeOutCounter_Type()
)
me1200StatusDmTwoWayRxTimeOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayRxTimeOutCounter.setStatus("current")
_Me1200StatusDmTwoWayRxErrorCounter_Type = Unsigned32
_Me1200StatusDmTwoWayRxErrorCounter_Object = MibTableColumn
me1200StatusDmTwoWayRxErrorCounter = _Me1200StatusDmTwoWayRxErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 5),
    _Me1200StatusDmTwoWayRxErrorCounter_Type()
)
me1200StatusDmTwoWayRxErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayRxErrorCounter.setStatus("current")
_Me1200StatusDmTwoWayInternalOverflowCounter_Type = Unsigned32
_Me1200StatusDmTwoWayInternalOverflowCounter_Object = MibTableColumn
me1200StatusDmTwoWayInternalOverflowCounter = _Me1200StatusDmTwoWayInternalOverflowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 6),
    _Me1200StatusDmTwoWayInternalOverflowCounter_Type()
)
me1200StatusDmTwoWayInternalOverflowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayInternalOverflowCounter.setStatus("current")
_Me1200StatusDmTwoWayAverageDelay_Type = Unsigned32
_Me1200StatusDmTwoWayAverageDelay_Object = MibTableColumn
me1200StatusDmTwoWayAverageDelay = _Me1200StatusDmTwoWayAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 7),
    _Me1200StatusDmTwoWayAverageDelay_Type()
)
me1200StatusDmTwoWayAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayAverageDelay.setStatus("current")
_Me1200StatusDmTwoWayAverageLastnDelay_Type = Unsigned32
_Me1200StatusDmTwoWayAverageLastnDelay_Object = MibTableColumn
me1200StatusDmTwoWayAverageLastnDelay = _Me1200StatusDmTwoWayAverageLastnDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 8),
    _Me1200StatusDmTwoWayAverageLastnDelay_Type()
)
me1200StatusDmTwoWayAverageLastnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayAverageLastnDelay.setStatus("current")
_Me1200StatusDmTwoWayAverageDelayVariation_Type = Unsigned32
_Me1200StatusDmTwoWayAverageDelayVariation_Object = MibTableColumn
me1200StatusDmTwoWayAverageDelayVariation = _Me1200StatusDmTwoWayAverageDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 9),
    _Me1200StatusDmTwoWayAverageDelayVariation_Type()
)
me1200StatusDmTwoWayAverageDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayAverageDelayVariation.setStatus("current")
_Me1200StatusDmTwoWayAverageLastnDelayVariation_Type = Unsigned32
_Me1200StatusDmTwoWayAverageLastnDelayVariation_Object = MibTableColumn
me1200StatusDmTwoWayAverageLastnDelayVariation = _Me1200StatusDmTwoWayAverageLastnDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 10),
    _Me1200StatusDmTwoWayAverageLastnDelayVariation_Type()
)
me1200StatusDmTwoWayAverageLastnDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayAverageLastnDelayVariation.setStatus("current")
_Me1200StatusDmTwoWayMinimumDelay_Type = Unsigned32
_Me1200StatusDmTwoWayMinimumDelay_Object = MibTableColumn
me1200StatusDmTwoWayMinimumDelay = _Me1200StatusDmTwoWayMinimumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 11),
    _Me1200StatusDmTwoWayMinimumDelay_Type()
)
me1200StatusDmTwoWayMinimumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayMinimumDelay.setStatus("current")
_Me1200StatusDmTwoWayMaximumDelay_Type = Unsigned32
_Me1200StatusDmTwoWayMaximumDelay_Object = MibTableColumn
me1200StatusDmTwoWayMaximumDelay = _Me1200StatusDmTwoWayMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 12),
    _Me1200StatusDmTwoWayMaximumDelay_Type()
)
me1200StatusDmTwoWayMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayMaximumDelay.setStatus("current")
_Me1200StatusDmTwoWayMinimumDelayVariation_Type = Unsigned32
_Me1200StatusDmTwoWayMinimumDelayVariation_Object = MibTableColumn
me1200StatusDmTwoWayMinimumDelayVariation = _Me1200StatusDmTwoWayMinimumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 13),
    _Me1200StatusDmTwoWayMinimumDelayVariation_Type()
)
me1200StatusDmTwoWayMinimumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayMinimumDelayVariation.setStatus("current")
_Me1200StatusDmTwoWayMaximumDelayVariation_Type = Unsigned32
_Me1200StatusDmTwoWayMaximumDelayVariation_Object = MibTableColumn
me1200StatusDmTwoWayMaximumDelayVariation = _Me1200StatusDmTwoWayMaximumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 14),
    _Me1200StatusDmTwoWayMaximumDelayVariation_Type()
)
me1200StatusDmTwoWayMaximumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayMaximumDelayVariation.setStatus("current")
_Me1200StatusDmTwoWayTimeUnit_Type = ME1200MepDmTimeUnit
_Me1200StatusDmTwoWayTimeUnit_Object = MibTableColumn
me1200StatusDmTwoWayTimeUnit = _Me1200StatusDmTwoWayTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 1, 1, 15),
    _Me1200StatusDmTwoWayTimeUnit_Type()
)
me1200StatusDmTwoWayTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayTimeUnit.setStatus("current")
_Me1200StatusDmOneWayFarNearTable_Object = MibTable
me1200StatusDmOneWayFarNearTable = _Me1200StatusDmOneWayFarNearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearTable.setStatus("current")
_Me1200StatusDmOneWayFarNearEntry_Object = MibTableRow
me1200StatusDmOneWayFarNearEntry = _Me1200StatusDmOneWayFarNearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1)
)
me1200StatusDmOneWayFarNearEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearId"),
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearEntry.setStatus("current")


class _Me1200StatusDmOneWayFarNearId_Type(Integer32):
    """Custom type me1200StatusDmOneWayFarNearId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusDmOneWayFarNearId_Type.__name__ = "Integer32"
_Me1200StatusDmOneWayFarNearId_Object = MibTableColumn
me1200StatusDmOneWayFarNearId = _Me1200StatusDmOneWayFarNearId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 1),
    _Me1200StatusDmOneWayFarNearId_Type()
)
me1200StatusDmOneWayFarNearId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearId.setStatus("current")
_Me1200StatusDmOneWayFarNearTxCounter_Type = Unsigned32
_Me1200StatusDmOneWayFarNearTxCounter_Object = MibTableColumn
me1200StatusDmOneWayFarNearTxCounter = _Me1200StatusDmOneWayFarNearTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 2),
    _Me1200StatusDmOneWayFarNearTxCounter_Type()
)
me1200StatusDmOneWayFarNearTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearTxCounter.setStatus("current")
_Me1200StatusDmOneWayFarNearRxCounter_Type = Unsigned32
_Me1200StatusDmOneWayFarNearRxCounter_Object = MibTableColumn
me1200StatusDmOneWayFarNearRxCounter = _Me1200StatusDmOneWayFarNearRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 3),
    _Me1200StatusDmOneWayFarNearRxCounter_Type()
)
me1200StatusDmOneWayFarNearRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearRxCounter.setStatus("current")
_Me1200StatusDmOneWayFarNearRxTimeOutCounter_Type = Unsigned32
_Me1200StatusDmOneWayFarNearRxTimeOutCounter_Object = MibTableColumn
me1200StatusDmOneWayFarNearRxTimeOutCounter = _Me1200StatusDmOneWayFarNearRxTimeOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 4),
    _Me1200StatusDmOneWayFarNearRxTimeOutCounter_Type()
)
me1200StatusDmOneWayFarNearRxTimeOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearRxTimeOutCounter.setStatus("current")
_Me1200StatusDmOneWayFarNearRxErrorCounter_Type = Unsigned32
_Me1200StatusDmOneWayFarNearRxErrorCounter_Object = MibTableColumn
me1200StatusDmOneWayFarNearRxErrorCounter = _Me1200StatusDmOneWayFarNearRxErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 5),
    _Me1200StatusDmOneWayFarNearRxErrorCounter_Type()
)
me1200StatusDmOneWayFarNearRxErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearRxErrorCounter.setStatus("current")
_Me1200StatusDmOneWayFarNearInternalOverflowCounter_Type = Unsigned32
_Me1200StatusDmOneWayFarNearInternalOverflowCounter_Object = MibTableColumn
me1200StatusDmOneWayFarNearInternalOverflowCounter = _Me1200StatusDmOneWayFarNearInternalOverflowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 6),
    _Me1200StatusDmOneWayFarNearInternalOverflowCounter_Type()
)
me1200StatusDmOneWayFarNearInternalOverflowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearInternalOverflowCounter.setStatus("current")
_Me1200StatusDmOneWayFarNearAverageDelay_Type = Unsigned32
_Me1200StatusDmOneWayFarNearAverageDelay_Object = MibTableColumn
me1200StatusDmOneWayFarNearAverageDelay = _Me1200StatusDmOneWayFarNearAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 7),
    _Me1200StatusDmOneWayFarNearAverageDelay_Type()
)
me1200StatusDmOneWayFarNearAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearAverageDelay.setStatus("current")
_Me1200StatusDmOneWayFarNearAverageLastnDelay_Type = Unsigned32
_Me1200StatusDmOneWayFarNearAverageLastnDelay_Object = MibTableColumn
me1200StatusDmOneWayFarNearAverageLastnDelay = _Me1200StatusDmOneWayFarNearAverageLastnDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 8),
    _Me1200StatusDmOneWayFarNearAverageLastnDelay_Type()
)
me1200StatusDmOneWayFarNearAverageLastnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearAverageLastnDelay.setStatus("current")
_Me1200StatusDmOneWayFarNearAverageDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayFarNearAverageDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayFarNearAverageDelayVariation = _Me1200StatusDmOneWayFarNearAverageDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 9),
    _Me1200StatusDmOneWayFarNearAverageDelayVariation_Type()
)
me1200StatusDmOneWayFarNearAverageDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearAverageDelayVariation.setStatus("current")
_Me1200StatusDmOneWayFarNearAverageLastnDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayFarNearAverageLastnDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayFarNearAverageLastnDelayVariation = _Me1200StatusDmOneWayFarNearAverageLastnDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 10),
    _Me1200StatusDmOneWayFarNearAverageLastnDelayVariation_Type()
)
me1200StatusDmOneWayFarNearAverageLastnDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearAverageLastnDelayVariation.setStatus("current")
_Me1200StatusDmOneWayFarNearMinimumDelay_Type = Unsigned32
_Me1200StatusDmOneWayFarNearMinimumDelay_Object = MibTableColumn
me1200StatusDmOneWayFarNearMinimumDelay = _Me1200StatusDmOneWayFarNearMinimumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 11),
    _Me1200StatusDmOneWayFarNearMinimumDelay_Type()
)
me1200StatusDmOneWayFarNearMinimumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearMinimumDelay.setStatus("current")
_Me1200StatusDmOneWayFarNearMaximumDelay_Type = Unsigned32
_Me1200StatusDmOneWayFarNearMaximumDelay_Object = MibTableColumn
me1200StatusDmOneWayFarNearMaximumDelay = _Me1200StatusDmOneWayFarNearMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 12),
    _Me1200StatusDmOneWayFarNearMaximumDelay_Type()
)
me1200StatusDmOneWayFarNearMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearMaximumDelay.setStatus("current")
_Me1200StatusDmOneWayFarNearMinimumDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayFarNearMinimumDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayFarNearMinimumDelayVariation = _Me1200StatusDmOneWayFarNearMinimumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 13),
    _Me1200StatusDmOneWayFarNearMinimumDelayVariation_Type()
)
me1200StatusDmOneWayFarNearMinimumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearMinimumDelayVariation.setStatus("current")
_Me1200StatusDmOneWayFarNearMaximumDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayFarNearMaximumDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayFarNearMaximumDelayVariation = _Me1200StatusDmOneWayFarNearMaximumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 14),
    _Me1200StatusDmOneWayFarNearMaximumDelayVariation_Type()
)
me1200StatusDmOneWayFarNearMaximumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearMaximumDelayVariation.setStatus("current")
_Me1200StatusDmOneWayFarNearTimeUnit_Type = ME1200MepDmTimeUnit
_Me1200StatusDmOneWayFarNearTimeUnit_Object = MibTableColumn
me1200StatusDmOneWayFarNearTimeUnit = _Me1200StatusDmOneWayFarNearTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 2, 1, 15),
    _Me1200StatusDmOneWayFarNearTimeUnit_Type()
)
me1200StatusDmOneWayFarNearTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearTimeUnit.setStatus("current")
_Me1200StatusDmOneWayNearFarTable_Object = MibTable
me1200StatusDmOneWayNearFarTable = _Me1200StatusDmOneWayNearFarTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarTable.setStatus("current")
_Me1200StatusDmOneWayNearFarEntry_Object = MibTableRow
me1200StatusDmOneWayNearFarEntry = _Me1200StatusDmOneWayNearFarEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1)
)
me1200StatusDmOneWayNearFarEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarId"),
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarEntry.setStatus("current")


class _Me1200StatusDmOneWayNearFarId_Type(Integer32):
    """Custom type me1200StatusDmOneWayNearFarId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusDmOneWayNearFarId_Type.__name__ = "Integer32"
_Me1200StatusDmOneWayNearFarId_Object = MibTableColumn
me1200StatusDmOneWayNearFarId = _Me1200StatusDmOneWayNearFarId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 1),
    _Me1200StatusDmOneWayNearFarId_Type()
)
me1200StatusDmOneWayNearFarId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarId.setStatus("current")
_Me1200StatusDmOneWayNearFarTxCounter_Type = Unsigned32
_Me1200StatusDmOneWayNearFarTxCounter_Object = MibTableColumn
me1200StatusDmOneWayNearFarTxCounter = _Me1200StatusDmOneWayNearFarTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 2),
    _Me1200StatusDmOneWayNearFarTxCounter_Type()
)
me1200StatusDmOneWayNearFarTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarTxCounter.setStatus("current")
_Me1200StatusDmOneWayNearFarRxCounter_Type = Unsigned32
_Me1200StatusDmOneWayNearFarRxCounter_Object = MibTableColumn
me1200StatusDmOneWayNearFarRxCounter = _Me1200StatusDmOneWayNearFarRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 3),
    _Me1200StatusDmOneWayNearFarRxCounter_Type()
)
me1200StatusDmOneWayNearFarRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarRxCounter.setStatus("current")
_Me1200StatusDmOneWayNearFarRxTimeOutCounter_Type = Unsigned32
_Me1200StatusDmOneWayNearFarRxTimeOutCounter_Object = MibTableColumn
me1200StatusDmOneWayNearFarRxTimeOutCounter = _Me1200StatusDmOneWayNearFarRxTimeOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 4),
    _Me1200StatusDmOneWayNearFarRxTimeOutCounter_Type()
)
me1200StatusDmOneWayNearFarRxTimeOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarRxTimeOutCounter.setStatus("current")
_Me1200StatusDmOneWayNearFarRxErrorCounter_Type = Unsigned32
_Me1200StatusDmOneWayNearFarRxErrorCounter_Object = MibTableColumn
me1200StatusDmOneWayNearFarRxErrorCounter = _Me1200StatusDmOneWayNearFarRxErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 5),
    _Me1200StatusDmOneWayNearFarRxErrorCounter_Type()
)
me1200StatusDmOneWayNearFarRxErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarRxErrorCounter.setStatus("current")
_Me1200StatusDmOneWayNearFarInternalOverflowCounter_Type = Unsigned32
_Me1200StatusDmOneWayNearFarInternalOverflowCounter_Object = MibTableColumn
me1200StatusDmOneWayNearFarInternalOverflowCounter = _Me1200StatusDmOneWayNearFarInternalOverflowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 6),
    _Me1200StatusDmOneWayNearFarInternalOverflowCounter_Type()
)
me1200StatusDmOneWayNearFarInternalOverflowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarInternalOverflowCounter.setStatus("current")
_Me1200StatusDmOneWayNearFarAverageDelay_Type = Unsigned32
_Me1200StatusDmOneWayNearFarAverageDelay_Object = MibTableColumn
me1200StatusDmOneWayNearFarAverageDelay = _Me1200StatusDmOneWayNearFarAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 7),
    _Me1200StatusDmOneWayNearFarAverageDelay_Type()
)
me1200StatusDmOneWayNearFarAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarAverageDelay.setStatus("current")
_Me1200StatusDmOneWayNearFarAverageLastnDelay_Type = Unsigned32
_Me1200StatusDmOneWayNearFarAverageLastnDelay_Object = MibTableColumn
me1200StatusDmOneWayNearFarAverageLastnDelay = _Me1200StatusDmOneWayNearFarAverageLastnDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 8),
    _Me1200StatusDmOneWayNearFarAverageLastnDelay_Type()
)
me1200StatusDmOneWayNearFarAverageLastnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarAverageLastnDelay.setStatus("current")
_Me1200StatusDmOneWayNearFarAverageDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayNearFarAverageDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayNearFarAverageDelayVariation = _Me1200StatusDmOneWayNearFarAverageDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 9),
    _Me1200StatusDmOneWayNearFarAverageDelayVariation_Type()
)
me1200StatusDmOneWayNearFarAverageDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarAverageDelayVariation.setStatus("current")
_Me1200StatusDmOneWayNearFarAverageLastnDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayNearFarAverageLastnDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayNearFarAverageLastnDelayVariation = _Me1200StatusDmOneWayNearFarAverageLastnDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 10),
    _Me1200StatusDmOneWayNearFarAverageLastnDelayVariation_Type()
)
me1200StatusDmOneWayNearFarAverageLastnDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarAverageLastnDelayVariation.setStatus("current")
_Me1200StatusDmOneWayNearFarMinimumDelay_Type = Unsigned32
_Me1200StatusDmOneWayNearFarMinimumDelay_Object = MibTableColumn
me1200StatusDmOneWayNearFarMinimumDelay = _Me1200StatusDmOneWayNearFarMinimumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 11),
    _Me1200StatusDmOneWayNearFarMinimumDelay_Type()
)
me1200StatusDmOneWayNearFarMinimumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarMinimumDelay.setStatus("current")
_Me1200StatusDmOneWayNearFarMaximumDelay_Type = Unsigned32
_Me1200StatusDmOneWayNearFarMaximumDelay_Object = MibTableColumn
me1200StatusDmOneWayNearFarMaximumDelay = _Me1200StatusDmOneWayNearFarMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 12),
    _Me1200StatusDmOneWayNearFarMaximumDelay_Type()
)
me1200StatusDmOneWayNearFarMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarMaximumDelay.setStatus("current")
_Me1200StatusDmOneWayNearFarMinimumDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayNearFarMinimumDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayNearFarMinimumDelayVariation = _Me1200StatusDmOneWayNearFarMinimumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 13),
    _Me1200StatusDmOneWayNearFarMinimumDelayVariation_Type()
)
me1200StatusDmOneWayNearFarMinimumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarMinimumDelayVariation.setStatus("current")
_Me1200StatusDmOneWayNearFarMaximumDelayVariation_Type = Unsigned32
_Me1200StatusDmOneWayNearFarMaximumDelayVariation_Object = MibTableColumn
me1200StatusDmOneWayNearFarMaximumDelayVariation = _Me1200StatusDmOneWayNearFarMaximumDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 14),
    _Me1200StatusDmOneWayNearFarMaximumDelayVariation_Type()
)
me1200StatusDmOneWayNearFarMaximumDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarMaximumDelayVariation.setStatus("current")
_Me1200StatusDmOneWayNearFarTimeUnit_Type = ME1200MepDmTimeUnit
_Me1200StatusDmOneWayNearFarTimeUnit_Object = MibTableColumn
me1200StatusDmOneWayNearFarTimeUnit = _Me1200StatusDmOneWayNearFarTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 3, 1, 15),
    _Me1200StatusDmOneWayNearFarTimeUnit_Type()
)
me1200StatusDmOneWayNearFarTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarTimeUnit.setStatus("current")
_Me1200StatusDmFdBinsTable_Object = MibTable
me1200StatusDmFdBinsTable = _Me1200StatusDmFdBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsTable.setStatus("current")
_Me1200StatusDmFdBinsEntry_Object = MibTableRow
me1200StatusDmFdBinsEntry = _Me1200StatusDmFdBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1)
)
me1200StatusDmFdBinsEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusDmFdBinsId"),
    (0, "ME1200-MEP-MIB", "me1200StatusDmFdBinsBinNumber"),
)
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsEntry.setStatus("current")


class _Me1200StatusDmFdBinsId_Type(Integer32):
    """Custom type me1200StatusDmFdBinsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusDmFdBinsId_Type.__name__ = "Integer32"
_Me1200StatusDmFdBinsId_Object = MibTableColumn
me1200StatusDmFdBinsId = _Me1200StatusDmFdBinsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1, 1),
    _Me1200StatusDmFdBinsId_Type()
)
me1200StatusDmFdBinsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsId.setStatus("current")


class _Me1200StatusDmFdBinsBinNumber_Type(Integer32):
    """Custom type me1200StatusDmFdBinsBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Me1200StatusDmFdBinsBinNumber_Type.__name__ = "Integer32"
_Me1200StatusDmFdBinsBinNumber_Object = MibTableColumn
me1200StatusDmFdBinsBinNumber = _Me1200StatusDmFdBinsBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1, 2),
    _Me1200StatusDmFdBinsBinNumber_Type()
)
me1200StatusDmFdBinsBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsBinNumber.setStatus("current")
_Me1200StatusDmFdBinsTwValue_Type = Unsigned32
_Me1200StatusDmFdBinsTwValue_Object = MibTableColumn
me1200StatusDmFdBinsTwValue = _Me1200StatusDmFdBinsTwValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1, 3),
    _Me1200StatusDmFdBinsTwValue_Type()
)
me1200StatusDmFdBinsTwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsTwValue.setStatus("current")
_Me1200StatusDmFdBinsOwFtNValue_Type = Unsigned32
_Me1200StatusDmFdBinsOwFtNValue_Object = MibTableColumn
me1200StatusDmFdBinsOwFtNValue = _Me1200StatusDmFdBinsOwFtNValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1, 4),
    _Me1200StatusDmFdBinsOwFtNValue_Type()
)
me1200StatusDmFdBinsOwFtNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsOwFtNValue.setStatus("current")
_Me1200StatusDmFdBinsOwNtFValue_Type = Unsigned32
_Me1200StatusDmFdBinsOwNtFValue_Object = MibTableColumn
me1200StatusDmFdBinsOwNtFValue = _Me1200StatusDmFdBinsOwNtFValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 4, 1, 5),
    _Me1200StatusDmFdBinsOwNtFValue_Type()
)
me1200StatusDmFdBinsOwNtFValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsOwNtFValue.setStatus("current")
_Me1200StatusDmIfdvBinsTable_Object = MibTable
me1200StatusDmIfdvBinsTable = _Me1200StatusDmIfdvBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsTable.setStatus("current")
_Me1200StatusDmIfdvBinsEntry_Object = MibTableRow
me1200StatusDmIfdvBinsEntry = _Me1200StatusDmIfdvBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1)
)
me1200StatusDmIfdvBinsEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusDmIfdvBinsId"),
    (0, "ME1200-MEP-MIB", "me1200StatusDmIfdvBinsBinNumber"),
)
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsEntry.setStatus("current")


class _Me1200StatusDmIfdvBinsId_Type(Integer32):
    """Custom type me1200StatusDmIfdvBinsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusDmIfdvBinsId_Type.__name__ = "Integer32"
_Me1200StatusDmIfdvBinsId_Object = MibTableColumn
me1200StatusDmIfdvBinsId = _Me1200StatusDmIfdvBinsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1, 1),
    _Me1200StatusDmIfdvBinsId_Type()
)
me1200StatusDmIfdvBinsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsId.setStatus("current")


class _Me1200StatusDmIfdvBinsBinNumber_Type(Integer32):
    """Custom type me1200StatusDmIfdvBinsBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Me1200StatusDmIfdvBinsBinNumber_Type.__name__ = "Integer32"
_Me1200StatusDmIfdvBinsBinNumber_Object = MibTableColumn
me1200StatusDmIfdvBinsBinNumber = _Me1200StatusDmIfdvBinsBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1, 2),
    _Me1200StatusDmIfdvBinsBinNumber_Type()
)
me1200StatusDmIfdvBinsBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsBinNumber.setStatus("current")
_Me1200StatusDmIfdvBinsTwValue_Type = Unsigned32
_Me1200StatusDmIfdvBinsTwValue_Object = MibTableColumn
me1200StatusDmIfdvBinsTwValue = _Me1200StatusDmIfdvBinsTwValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1, 3),
    _Me1200StatusDmIfdvBinsTwValue_Type()
)
me1200StatusDmIfdvBinsTwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsTwValue.setStatus("current")
_Me1200StatusDmIfdvBinsOwFtNValue_Type = Unsigned32
_Me1200StatusDmIfdvBinsOwFtNValue_Object = MibTableColumn
me1200StatusDmIfdvBinsOwFtNValue = _Me1200StatusDmIfdvBinsOwFtNValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1, 4),
    _Me1200StatusDmIfdvBinsOwFtNValue_Type()
)
me1200StatusDmIfdvBinsOwFtNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsOwFtNValue.setStatus("current")
_Me1200StatusDmIfdvBinsOwNtFValue_Type = Unsigned32
_Me1200StatusDmIfdvBinsOwNtFValue_Object = MibTableColumn
me1200StatusDmIfdvBinsOwNtFValue = _Me1200StatusDmIfdvBinsOwNtFValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 3, 5, 1, 5),
    _Me1200StatusDmIfdvBinsOwNtFValue_Type()
)
me1200StatusDmIfdvBinsOwNtFValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsOwNtFValue.setStatus("current")
_Me1200StatusLoopBack_ObjectIdentity = ObjectIdentity
me1200StatusLoopBack = _Me1200StatusLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4)
)
_Me1200StatusLbTable_Object = MibTable
me1200StatusLbTable = _Me1200StatusLbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    me1200StatusLbTable.setStatus("current")
_Me1200StatusLbEntry_Object = MibTableRow
me1200StatusLbEntry = _Me1200StatusLbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1, 1)
)
me1200StatusLbEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLbId"),
)
if mibBuilder.loadTexts:
    me1200StatusLbEntry.setStatus("current")


class _Me1200StatusLbId_Type(Integer32):
    """Custom type me1200StatusLbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLbId_Type.__name__ = "Integer32"
_Me1200StatusLbId_Object = MibTableColumn
me1200StatusLbId = _Me1200StatusLbId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1, 1, 1),
    _Me1200StatusLbId_Type()
)
me1200StatusLbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLbId.setStatus("current")
_Me1200StatusLbTransactionId_Type = Unsigned32
_Me1200StatusLbTransactionId_Object = MibTableColumn
me1200StatusLbTransactionId = _Me1200StatusLbTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1, 1, 2),
    _Me1200StatusLbTransactionId_Type()
)
me1200StatusLbTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbTransactionId.setStatus("current")
_Me1200StatusLbReplyCounter_Type = Unsigned32
_Me1200StatusLbReplyCounter_Object = MibTableColumn
me1200StatusLbReplyCounter = _Me1200StatusLbReplyCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1, 1, 3),
    _Me1200StatusLbReplyCounter_Type()
)
me1200StatusLbReplyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbReplyCounter.setStatus("current")
_Me1200StatusLbLbmTransmitted_Type = Counter64
_Me1200StatusLbLbmTransmitted_Object = MibTableColumn
me1200StatusLbLbmTransmitted = _Me1200StatusLbLbmTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 1, 1, 4),
    _Me1200StatusLbLbmTransmitted_Type()
)
me1200StatusLbLbmTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbLbmTransmitted.setStatus("current")
_Me1200StatusLbReplyTable_Object = MibTable
me1200StatusLbReplyTable = _Me1200StatusLbReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    me1200StatusLbReplyTable.setStatus("current")
_Me1200StatusLbReplyEntry_Object = MibTableRow
me1200StatusLbReplyEntry = _Me1200StatusLbReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1)
)
me1200StatusLbReplyEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLbReplyId"),
    (0, "ME1200-MEP-MIB", "me1200StatusLbReplyReplyId"),
)
if mibBuilder.loadTexts:
    me1200StatusLbReplyEntry.setStatus("current")


class _Me1200StatusLbReplyId_Type(Integer32):
    """Custom type me1200StatusLbReplyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLbReplyId_Type.__name__ = "Integer32"
_Me1200StatusLbReplyId_Object = MibTableColumn
me1200StatusLbReplyId = _Me1200StatusLbReplyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1, 1),
    _Me1200StatusLbReplyId_Type()
)
me1200StatusLbReplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLbReplyId.setStatus("current")


class _Me1200StatusLbReplyReplyId_Type(Integer32):
    """Custom type me1200StatusLbReplyReplyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLbReplyReplyId_Type.__name__ = "Integer32"
_Me1200StatusLbReplyReplyId_Object = MibTableColumn
me1200StatusLbReplyReplyId = _Me1200StatusLbReplyReplyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1, 2),
    _Me1200StatusLbReplyReplyId_Type()
)
me1200StatusLbReplyReplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLbReplyReplyId.setStatus("current")
_Me1200StatusLbReplyMac_Type = MacAddress
_Me1200StatusLbReplyMac_Object = MibTableColumn
me1200StatusLbReplyMac = _Me1200StatusLbReplyMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1, 3),
    _Me1200StatusLbReplyMac_Type()
)
me1200StatusLbReplyMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbReplyMac.setStatus("current")
_Me1200StatusLbReplyLbrReceived_Type = Counter64
_Me1200StatusLbReplyLbrReceived_Object = MibTableColumn
me1200StatusLbReplyLbrReceived = _Me1200StatusLbReplyLbrReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1, 4),
    _Me1200StatusLbReplyLbrReceived_Type()
)
me1200StatusLbReplyLbrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbReplyLbrReceived.setStatus("current")
_Me1200StatusLbReplyOutOfOrder_Type = Counter64
_Me1200StatusLbReplyOutOfOrder_Object = MibTableColumn
me1200StatusLbReplyOutOfOrder = _Me1200StatusLbReplyOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 4, 2, 1, 5),
    _Me1200StatusLbReplyOutOfOrder_Type()
)
me1200StatusLbReplyOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLbReplyOutOfOrder.setStatus("current")
_Me1200StatusTestSignal_ObjectIdentity = ObjectIdentity
me1200StatusTestSignal = _Me1200StatusTestSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5)
)
_Me1200StatusTstTable_Object = MibTable
me1200StatusTstTable = _Me1200StatusTstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    me1200StatusTstTable.setStatus("current")
_Me1200StatusTstEntry_Object = MibTableRow
me1200StatusTstEntry = _Me1200StatusTstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1)
)
me1200StatusTstEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusTstId"),
)
if mibBuilder.loadTexts:
    me1200StatusTstEntry.setStatus("current")


class _Me1200StatusTstId_Type(Integer32):
    """Custom type me1200StatusTstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusTstId_Type.__name__ = "Integer32"
_Me1200StatusTstId_Object = MibTableColumn
me1200StatusTstId = _Me1200StatusTstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 1),
    _Me1200StatusTstId_Type()
)
me1200StatusTstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusTstId.setStatus("current")
_Me1200StatusTstTxCounter_Type = Counter64
_Me1200StatusTstTxCounter_Object = MibTableColumn
me1200StatusTstTxCounter = _Me1200StatusTstTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 2),
    _Me1200StatusTstTxCounter_Type()
)
me1200StatusTstTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTstTxCounter.setStatus("current")
_Me1200StatusTstRxCounter_Type = Counter64
_Me1200StatusTstRxCounter_Object = MibTableColumn
me1200StatusTstRxCounter = _Me1200StatusTstRxCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 3),
    _Me1200StatusTstRxCounter_Type()
)
me1200StatusTstRxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTstRxCounter.setStatus("current")
_Me1200StatusTstOutOfOrderCounter_Type = Counter64
_Me1200StatusTstOutOfOrderCounter_Object = MibTableColumn
me1200StatusTstOutOfOrderCounter = _Me1200StatusTstOutOfOrderCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 4),
    _Me1200StatusTstOutOfOrderCounter_Type()
)
me1200StatusTstOutOfOrderCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTstOutOfOrderCounter.setStatus("current")
_Me1200StatusTstRxRate_Type = Unsigned32
_Me1200StatusTstRxRate_Object = MibTableColumn
me1200StatusTstRxRate = _Me1200StatusTstRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 5),
    _Me1200StatusTstRxRate_Type()
)
me1200StatusTstRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTstRxRate.setStatus("current")
_Me1200StatusTstTestTime_Type = Unsigned32
_Me1200StatusTstTestTime_Object = MibTableColumn
me1200StatusTstTestTime = _Me1200StatusTstTestTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 5, 1, 1, 6),
    _Me1200StatusTstTestTime_Type()
)
me1200StatusTstTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTstTestTime.setStatus("current")
_Me1200StatusLinkTrace_ObjectIdentity = ObjectIdentity
me1200StatusLinkTrace = _Me1200StatusLinkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6)
)
_Me1200StatusLtTable_Object = MibTable
me1200StatusLtTable = _Me1200StatusLtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    me1200StatusLtTable.setStatus("current")
_Me1200StatusLtEntry_Object = MibTableRow
me1200StatusLtEntry = _Me1200StatusLtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 1, 1)
)
me1200StatusLtEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLtId"),
)
if mibBuilder.loadTexts:
    me1200StatusLtEntry.setStatus("current")


class _Me1200StatusLtId_Type(Integer32):
    """Custom type me1200StatusLtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLtId_Type.__name__ = "Integer32"
_Me1200StatusLtId_Object = MibTableColumn
me1200StatusLtId = _Me1200StatusLtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 1, 1, 1),
    _Me1200StatusLtId_Type()
)
me1200StatusLtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLtId.setStatus("current")
_Me1200StatusLtTransactionId_Type = Unsigned32
_Me1200StatusLtTransactionId_Object = MibTableColumn
me1200StatusLtTransactionId = _Me1200StatusLtTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 1, 1, 2),
    _Me1200StatusLtTransactionId_Type()
)
me1200StatusLtTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtTransactionId.setStatus("current")
_Me1200StatusLtReplyCount_Type = Unsigned32
_Me1200StatusLtReplyCount_Object = MibTableColumn
me1200StatusLtReplyCount = _Me1200StatusLtReplyCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 1, 1, 3),
    _Me1200StatusLtReplyCount_Type()
)
me1200StatusLtReplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyCount.setStatus("current")
_Me1200StatusLtReplyTable_Object = MibTable
me1200StatusLtReplyTable = _Me1200StatusLtReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    me1200StatusLtReplyTable.setStatus("current")
_Me1200StatusLtReplyEntry_Object = MibTableRow
me1200StatusLtReplyEntry = _Me1200StatusLtReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1)
)
me1200StatusLtReplyEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLtReplyId"),
    (0, "ME1200-MEP-MIB", "me1200StatusLtReplyReplyId"),
)
if mibBuilder.loadTexts:
    me1200StatusLtReplyEntry.setStatus("current")


class _Me1200StatusLtReplyId_Type(Integer32):
    """Custom type me1200StatusLtReplyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLtReplyId_Type.__name__ = "Integer32"
_Me1200StatusLtReplyId_Object = MibTableColumn
me1200StatusLtReplyId = _Me1200StatusLtReplyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 1),
    _Me1200StatusLtReplyId_Type()
)
me1200StatusLtReplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLtReplyId.setStatus("current")


class _Me1200StatusLtReplyReplyId_Type(Integer32):
    """Custom type me1200StatusLtReplyReplyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLtReplyReplyId_Type.__name__ = "Integer32"
_Me1200StatusLtReplyReplyId_Object = MibTableColumn
me1200StatusLtReplyReplyId = _Me1200StatusLtReplyReplyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 2),
    _Me1200StatusLtReplyReplyId_Type()
)
me1200StatusLtReplyReplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLtReplyReplyId.setStatus("current")
_Me1200StatusLtReplyMode_Type = ME1200InstanceMode
_Me1200StatusLtReplyMode_Object = MibTableColumn
me1200StatusLtReplyMode = _Me1200StatusLtReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 3),
    _Me1200StatusLtReplyMode_Type()
)
me1200StatusLtReplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyMode.setStatus("current")
_Me1200StatusLtReplyDirection_Type = ME1200MepInstanceDirection
_Me1200StatusLtReplyDirection_Object = MibTableColumn
me1200StatusLtReplyDirection = _Me1200StatusLtReplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 4),
    _Me1200StatusLtReplyDirection_Type()
)
me1200StatusLtReplyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyDirection.setStatus("current")
_Me1200StatusLtReplyTtl_Type = ME1200Unsigned8
_Me1200StatusLtReplyTtl_Object = MibTableColumn
me1200StatusLtReplyTtl = _Me1200StatusLtReplyTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 5),
    _Me1200StatusLtReplyTtl_Type()
)
me1200StatusLtReplyTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyTtl.setStatus("current")
_Me1200StatusLtReplyForwarded_Type = TruthValue
_Me1200StatusLtReplyForwarded_Object = MibTableColumn
me1200StatusLtReplyForwarded = _Me1200StatusLtReplyForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 6),
    _Me1200StatusLtReplyForwarded_Type()
)
me1200StatusLtReplyForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyForwarded.setStatus("current")
_Me1200StatusLtReplyRelayAction_Type = ME1200RelayAction
_Me1200StatusLtReplyRelayAction_Object = MibTableColumn
me1200StatusLtReplyRelayAction = _Me1200StatusLtReplyRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 7),
    _Me1200StatusLtReplyRelayAction_Type()
)
me1200StatusLtReplyRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyRelayAction.setStatus("current")
_Me1200StatusLtReplyLastEgressMac_Type = MacAddress
_Me1200StatusLtReplyLastEgressMac_Object = MibTableColumn
me1200StatusLtReplyLastEgressMac = _Me1200StatusLtReplyLastEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 8),
    _Me1200StatusLtReplyLastEgressMac_Type()
)
me1200StatusLtReplyLastEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyLastEgressMac.setStatus("current")
_Me1200StatusLtReplyNextEgressMac_Type = MacAddress
_Me1200StatusLtReplyNextEgressMac_Object = MibTableColumn
me1200StatusLtReplyNextEgressMac = _Me1200StatusLtReplyNextEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 6, 2, 1, 9),
    _Me1200StatusLtReplyNextEgressMac_Type()
)
me1200StatusLtReplyNextEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLtReplyNextEgressMac.setStatus("current")
_Me1200StatusContinuityCheck_ObjectIdentity = ObjectIdentity
me1200StatusContinuityCheck = _Me1200StatusContinuityCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7)
)
_Me1200StatusCCPeerTable_Object = MibTable
me1200StatusCCPeerTable = _Me1200StatusCCPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    me1200StatusCCPeerTable.setStatus("current")
_Me1200StatusCCPeerEntry_Object = MibTableRow
me1200StatusCCPeerEntry = _Me1200StatusCCPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1)
)
me1200StatusCCPeerEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusCCPeerId"),
    (0, "ME1200-MEP-MIB", "me1200StatusCCPeerPeerId"),
)
if mibBuilder.loadTexts:
    me1200StatusCCPeerEntry.setStatus("current")


class _Me1200StatusCCPeerId_Type(Integer32):
    """Custom type me1200StatusCCPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusCCPeerId_Type.__name__ = "Integer32"
_Me1200StatusCCPeerId_Object = MibTableColumn
me1200StatusCCPeerId = _Me1200StatusCCPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 1),
    _Me1200StatusCCPeerId_Type()
)
me1200StatusCCPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusCCPeerId.setStatus("current")


class _Me1200StatusCCPeerPeerId_Type(Integer32):
    """Custom type me1200StatusCCPeerPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusCCPeerPeerId_Type.__name__ = "Integer32"
_Me1200StatusCCPeerPeerId_Object = MibTableColumn
me1200StatusCCPeerPeerId = _Me1200StatusCCPeerPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 2),
    _Me1200StatusCCPeerPeerId_Type()
)
me1200StatusCCPeerPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusCCPeerPeerId.setStatus("current")
_Me1200StatusCCPeerOsTlvOuiFirst_Type = ME1200Unsigned8
_Me1200StatusCCPeerOsTlvOuiFirst_Object = MibTableColumn
me1200StatusCCPeerOsTlvOuiFirst = _Me1200StatusCCPeerOsTlvOuiFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 3),
    _Me1200StatusCCPeerOsTlvOuiFirst_Type()
)
me1200StatusCCPeerOsTlvOuiFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvOuiFirst.setStatus("current")
_Me1200StatusCCPeerOsTlvOuiSecond_Type = ME1200Unsigned8
_Me1200StatusCCPeerOsTlvOuiSecond_Object = MibTableColumn
me1200StatusCCPeerOsTlvOuiSecond = _Me1200StatusCCPeerOsTlvOuiSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 4),
    _Me1200StatusCCPeerOsTlvOuiSecond_Type()
)
me1200StatusCCPeerOsTlvOuiSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvOuiSecond.setStatus("current")
_Me1200StatusCCPeerOsTlvOuiThird_Type = ME1200Unsigned8
_Me1200StatusCCPeerOsTlvOuiThird_Object = MibTableColumn
me1200StatusCCPeerOsTlvOuiThird = _Me1200StatusCCPeerOsTlvOuiThird_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 5),
    _Me1200StatusCCPeerOsTlvOuiThird_Type()
)
me1200StatusCCPeerOsTlvOuiThird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvOuiThird.setStatus("current")
_Me1200StatusCCPeerOsTlvSubType_Type = ME1200Unsigned8
_Me1200StatusCCPeerOsTlvSubType_Object = MibTableColumn
me1200StatusCCPeerOsTlvSubType = _Me1200StatusCCPeerOsTlvSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 6),
    _Me1200StatusCCPeerOsTlvSubType_Type()
)
me1200StatusCCPeerOsTlvSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvSubType.setStatus("current")
_Me1200StatusCCPeerOsTlvValue_Type = ME1200Unsigned8
_Me1200StatusCCPeerOsTlvValue_Object = MibTableColumn
me1200StatusCCPeerOsTlvValue = _Me1200StatusCCPeerOsTlvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 7),
    _Me1200StatusCCPeerOsTlvValue_Type()
)
me1200StatusCCPeerOsTlvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvValue.setStatus("current")
_Me1200StatusCCPeerIsTlvValue_Type = ME1200Unsigned8
_Me1200StatusCCPeerIsTlvValue_Object = MibTableColumn
me1200StatusCCPeerIsTlvValue = _Me1200StatusCCPeerIsTlvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 8),
    _Me1200StatusCCPeerIsTlvValue_Type()
)
me1200StatusCCPeerIsTlvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerIsTlvValue.setStatus("current")
_Me1200StatusCCPeerPsTlvValue_Type = ME1200Unsigned8
_Me1200StatusCCPeerPsTlvValue_Object = MibTableColumn
me1200StatusCCPeerPsTlvValue = _Me1200StatusCCPeerPsTlvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 9),
    _Me1200StatusCCPeerPsTlvValue_Type()
)
me1200StatusCCPeerPsTlvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerPsTlvValue.setStatus("current")
_Me1200StatusCCPeerOsTlvReceived_Type = TruthValue
_Me1200StatusCCPeerOsTlvReceived_Object = MibTableColumn
me1200StatusCCPeerOsTlvReceived = _Me1200StatusCCPeerOsTlvReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 10),
    _Me1200StatusCCPeerOsTlvReceived_Type()
)
me1200StatusCCPeerOsTlvReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerOsTlvReceived.setStatus("current")
_Me1200StatusCCPeerIsTlvReceived_Type = TruthValue
_Me1200StatusCCPeerIsTlvReceived_Object = MibTableColumn
me1200StatusCCPeerIsTlvReceived = _Me1200StatusCCPeerIsTlvReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 11),
    _Me1200StatusCCPeerIsTlvReceived_Type()
)
me1200StatusCCPeerIsTlvReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerIsTlvReceived.setStatus("current")
_Me1200StatusCCPeerPsTlvReceived_Type = TruthValue
_Me1200StatusCCPeerPsTlvReceived_Object = MibTableColumn
me1200StatusCCPeerPsTlvReceived = _Me1200StatusCCPeerPsTlvReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 7, 2, 1, 12),
    _Me1200StatusCCPeerPsTlvReceived_Type()
)
me1200StatusCCPeerPsTlvReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusCCPeerPsTlvReceived.setStatus("current")
_Me1200StatusLmAvailability_ObjectIdentity = ObjectIdentity
me1200StatusLmAvailability = _Me1200StatusLmAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8)
)
_Me1200StatusLmAvailTable_Object = MibTable
me1200StatusLmAvailTable = _Me1200StatusLmAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    me1200StatusLmAvailTable.setStatus("current")
_Me1200StatusLmAvailEntry_Object = MibTableRow
me1200StatusLmAvailEntry = _Me1200StatusLmAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1)
)
me1200StatusLmAvailEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200StatusLmAvailId"),
    (0, "ME1200-MEP-MIB", "me1200StatusLmAvailPeerId"),
)
if mibBuilder.loadTexts:
    me1200StatusLmAvailEntry.setStatus("current")


class _Me1200StatusLmAvailId_Type(Integer32):
    """Custom type me1200StatusLmAvailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLmAvailId_Type.__name__ = "Integer32"
_Me1200StatusLmAvailId_Object = MibTableColumn
me1200StatusLmAvailId = _Me1200StatusLmAvailId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 1),
    _Me1200StatusLmAvailId_Type()
)
me1200StatusLmAvailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLmAvailId.setStatus("current")


class _Me1200StatusLmAvailPeerId_Type(Integer32):
    """Custom type me1200StatusLmAvailPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusLmAvailPeerId_Type.__name__ = "Integer32"
_Me1200StatusLmAvailPeerId_Object = MibTableColumn
me1200StatusLmAvailPeerId = _Me1200StatusLmAvailPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 2),
    _Me1200StatusLmAvailPeerId_Type()
)
me1200StatusLmAvailPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusLmAvailPeerId.setStatus("current")
_Me1200StatusLmAvailNearEndAvailState_Type = ME1200AvailState
_Me1200StatusLmAvailNearEndAvailState_Object = MibTableColumn
me1200StatusLmAvailNearEndAvailState = _Me1200StatusLmAvailNearEndAvailState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 3),
    _Me1200StatusLmAvailNearEndAvailState_Type()
)
me1200StatusLmAvailNearEndAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailNearEndAvailState.setStatus("current")
_Me1200StatusLmAvailFarEndAvailState_Type = ME1200AvailState
_Me1200StatusLmAvailFarEndAvailState_Object = MibTableColumn
me1200StatusLmAvailFarEndAvailState = _Me1200StatusLmAvailFarEndAvailState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 4),
    _Me1200StatusLmAvailFarEndAvailState_Type()
)
me1200StatusLmAvailFarEndAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailFarEndAvailState.setStatus("current")
_Me1200StatusLmAvailNearEndAvailCnt_Type = Unsigned32
_Me1200StatusLmAvailNearEndAvailCnt_Object = MibTableColumn
me1200StatusLmAvailNearEndAvailCnt = _Me1200StatusLmAvailNearEndAvailCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 5),
    _Me1200StatusLmAvailNearEndAvailCnt_Type()
)
me1200StatusLmAvailNearEndAvailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailNearEndAvailCnt.setStatus("current")
_Me1200StatusLmAvailFarEndAvailCnt_Type = Unsigned32
_Me1200StatusLmAvailFarEndAvailCnt_Object = MibTableColumn
me1200StatusLmAvailFarEndAvailCnt = _Me1200StatusLmAvailFarEndAvailCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 6),
    _Me1200StatusLmAvailFarEndAvailCnt_Type()
)
me1200StatusLmAvailFarEndAvailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailFarEndAvailCnt.setStatus("current")
_Me1200StatusLmAvailNearEndUnAvailCnt_Type = Unsigned32
_Me1200StatusLmAvailNearEndUnAvailCnt_Object = MibTableColumn
me1200StatusLmAvailNearEndUnAvailCnt = _Me1200StatusLmAvailNearEndUnAvailCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 7),
    _Me1200StatusLmAvailNearEndUnAvailCnt_Type()
)
me1200StatusLmAvailNearEndUnAvailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailNearEndUnAvailCnt.setStatus("current")
_Me1200StatusLmAvailFarEndUnAvailCnt_Type = Unsigned32
_Me1200StatusLmAvailFarEndUnAvailCnt_Object = MibTableColumn
me1200StatusLmAvailFarEndUnAvailCnt = _Me1200StatusLmAvailFarEndUnAvailCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 8),
    _Me1200StatusLmAvailFarEndUnAvailCnt_Type()
)
me1200StatusLmAvailFarEndUnAvailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailFarEndUnAvailCnt.setStatus("current")
_Me1200StatusLmAvailNearEndWindowCnt_Type = Unsigned32
_Me1200StatusLmAvailNearEndWindowCnt_Object = MibTableColumn
me1200StatusLmAvailNearEndWindowCnt = _Me1200StatusLmAvailNearEndWindowCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 9),
    _Me1200StatusLmAvailNearEndWindowCnt_Type()
)
me1200StatusLmAvailNearEndWindowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailNearEndWindowCnt.setStatus("current")
_Me1200StatusLmAvailFarEndWindowCnt_Type = Unsigned32
_Me1200StatusLmAvailFarEndWindowCnt_Object = MibTableColumn
me1200StatusLmAvailFarEndWindowCnt = _Me1200StatusLmAvailFarEndWindowCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 3, 8, 2, 1, 10),
    _Me1200StatusLmAvailFarEndWindowCnt_Type()
)
me1200StatusLmAvailFarEndWindowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusLmAvailFarEndWindowCnt.setStatus("current")
_Me1200MepControl_ObjectIdentity = ObjectIdentity
me1200MepControl = _Me1200MepControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4)
)
_Me1200ControlLossMeasurement_ObjectIdentity = ObjectIdentity
me1200ControlLossMeasurement = _Me1200ControlLossMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 1)
)
_Me1200ControlLmTable_Object = MibTable
me1200ControlLmTable = _Me1200ControlLmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    me1200ControlLmTable.setStatus("current")
_Me1200ControlLmEntry_Object = MibTableRow
me1200ControlLmEntry = _Me1200ControlLmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 1, 1, 1)
)
me1200ControlLmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ControlLmId"),
)
if mibBuilder.loadTexts:
    me1200ControlLmEntry.setStatus("current")


class _Me1200ControlLmId_Type(Integer32):
    """Custom type me1200ControlLmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ControlLmId_Type.__name__ = "Integer32"
_Me1200ControlLmId_Object = MibTableColumn
me1200ControlLmId = _Me1200ControlLmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 1, 1, 1, 1),
    _Me1200ControlLmId_Type()
)
me1200ControlLmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ControlLmId.setStatus("current")
_Me1200ControlLmClear_Type = TruthValue
_Me1200ControlLmClear_Object = MibTableColumn
me1200ControlLmClear = _Me1200ControlLmClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 1, 1, 1, 2),
    _Me1200ControlLmClear_Type()
)
me1200ControlLmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ControlLmClear.setStatus("current")
_Me1200ControlDelayMeasurement_ObjectIdentity = ObjectIdentity
me1200ControlDelayMeasurement = _Me1200ControlDelayMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 2)
)
_Me1200ControlDmTable_Object = MibTable
me1200ControlDmTable = _Me1200ControlDmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    me1200ControlDmTable.setStatus("current")
_Me1200ControlDmEntry_Object = MibTableRow
me1200ControlDmEntry = _Me1200ControlDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 2, 1, 1)
)
me1200ControlDmEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ControlDmId"),
)
if mibBuilder.loadTexts:
    me1200ControlDmEntry.setStatus("current")


class _Me1200ControlDmId_Type(Integer32):
    """Custom type me1200ControlDmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ControlDmId_Type.__name__ = "Integer32"
_Me1200ControlDmId_Object = MibTableColumn
me1200ControlDmId = _Me1200ControlDmId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 2, 1, 1, 1),
    _Me1200ControlDmId_Type()
)
me1200ControlDmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ControlDmId.setStatus("current")
_Me1200ControlDmClear_Type = TruthValue
_Me1200ControlDmClear_Object = MibTableColumn
me1200ControlDmClear = _Me1200ControlDmClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 2, 1, 1, 2),
    _Me1200ControlDmClear_Type()
)
me1200ControlDmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ControlDmClear.setStatus("current")
_Me1200ControlTestSignal_ObjectIdentity = ObjectIdentity
me1200ControlTestSignal = _Me1200ControlTestSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 3)
)
_Me1200ControlTstTable_Object = MibTable
me1200ControlTstTable = _Me1200ControlTstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    me1200ControlTstTable.setStatus("current")
_Me1200ControlTstEntry_Object = MibTableRow
me1200ControlTstEntry = _Me1200ControlTstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 3, 1, 1)
)
me1200ControlTstEntry.setIndexNames(
    (0, "ME1200-MEP-MIB", "me1200ControlTstId"),
)
if mibBuilder.loadTexts:
    me1200ControlTstEntry.setStatus("current")


class _Me1200ControlTstId_Type(Integer32):
    """Custom type me1200ControlTstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ControlTstId_Type.__name__ = "Integer32"
_Me1200ControlTstId_Object = MibTableColumn
me1200ControlTstId = _Me1200ControlTstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 3, 1, 1, 1),
    _Me1200ControlTstId_Type()
)
me1200ControlTstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ControlTstId.setStatus("current")
_Me1200ControlTstClear_Type = TruthValue
_Me1200ControlTstClear_Object = MibTableColumn
me1200ControlTstClear = _Me1200ControlTstClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 4, 3, 1, 1, 2),
    _Me1200ControlTstClear_Type()
)
me1200ControlTstClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ControlTstClear.setStatus("current")
_Me1200MepNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200MepNotificationPrefix = _Me1200MepNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5)
)
_Me1200MeptNotification_ObjectIdentity = ObjectIdentity
me1200MeptNotification = _Me1200MeptNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0)
)
_Me1200MepMibConformance_ObjectIdentity = ObjectIdentity
me1200MepMibConformance = _Me1200MepMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3)
)
_Me1200MepMibCompliances_ObjectIdentity = ObjectIdentity
me1200MepMibCompliances = _Me1200MepMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 1)
)
_Me1200MepMibGroups_ObjectIdentity = ObjectIdentity
me1200MepMibGroups = _Me1200MepMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2)
)

# Managed Objects groups

me1200MepCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 1)
)
me1200MepCapabilitiesInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200MepCapabilitiesInstanceMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesPeerMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesTransactionMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesReplyMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesClientFlowsMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesMacMength"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesMegCodeLength"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmIntervalMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmIntervalMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmLastnMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmLastnMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesLbmSizeMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesLbmSizeMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesTstSizeMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesTstSizeMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesTstRateMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesClientPrioHighest"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesLbToSendInfinite"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesLmLossRatioThresholdMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesLmLossRatioThresholdMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmAverageDelayThresholdMin"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesDmAverageDelayThresholdMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesSlmSizeMax"),
        ("ME1200-MEP-MIB", "me1200MepCapabilitiesSlmSizeMin"))
)
if mibBuilder.loadTexts:
    me1200MepCapabilitiesInfoGroup.setStatus("current")

me1200ConfigInstanceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 2)
)
me1200ConfigInstanceTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigInstanceMode"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceDirection"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceDomain"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceFlow"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePort"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceLevel"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceVid"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceVoe"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceMac"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceFormat"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceName"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceMeg"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceMep"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigInstanceTableInfoGroup.setStatus("current")

me1200ConfigInstanceRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 3)
)
me1200ConfigInstanceRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorMode"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorDirection"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorDomain"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorFlow"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorPort"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorLevel"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorVid"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorVoe"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorMac"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorFormat"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorName"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorMeg"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigInstanceRowEditorInfoGroup.setStatus("current")

me1200ConfigInstancePeerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 4)
)
me1200ConfigInstancePeerTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigInstancePeerMac"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerTableInfoGroup.setStatus("current")

me1200ConfigInstancePeerRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 5)
)
me1200ConfigInstancePeerRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigInstancePeerRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerRowEditorPeerId"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerRowEditorMac"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigInstancePeerRowEditorInfoGroup.setStatus("current")

me1200ConfigPmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 6)
)
me1200ConfigPmTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ConfigPmEnable")
)
if mibBuilder.loadTexts:
    me1200ConfigPmTableInfoGroup.setStatus("current")

me1200ConfigCcTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 7)
)
me1200ConfigCcTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigCcDei"),
        ("ME1200-MEP-MIB", "me1200ConfigCcPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRate"),
        ("ME1200-MEP-MIB", "me1200ConfigCcTlv"),
        ("ME1200-MEP-MIB", "me1200ConfigCcAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigCcTableInfoGroup.setStatus("current")

me1200ConfigCcRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 8)
)
me1200ConfigCcRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigCcRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorRate"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorTlv"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigCcRowEditorInfoGroup.setStatus("current")

me1200ConfigLmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 9)
)
me1200ConfigLmTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigLmDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLmPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLmFlrInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmLossRatioThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigLmSynthetic"),
        ("ME1200-MEP-MIB", "me1200ConfigLmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLmFrameSize"),
        ("ME1200-MEP-MIB", "me1200ConfigLmMeasInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLmTableInfoGroup.setStatus("current")

me1200ConfigLmRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 10)
)
me1200ConfigLmRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorFlrInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorLossRatioThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorRxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorSynthetic"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorFrameSize"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorMeasInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLmRowEditorInfoGroup.setStatus("current")

me1200ConfigDmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 11)
)
me1200ConfigDmTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigDmDei"),
        ("ME1200-MEP-MIB", "me1200ConfigDmPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmNumOfBinFD"),
        ("ME1200-MEP-MIB", "me1200ConfigDmNumOfBinIFDV"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigDmTableInfoGroup.setStatus("current")

me1200ConfigDmRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 12)
)
me1200ConfigDmRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorNumOfBinFD"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorNumOfBinIFDV"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorMThreshold"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigDmRowEditorInfoGroup.setStatus("current")

me1200ConfigLbTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 13)
)
me1200ConfigLbTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLbDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLbPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLbCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLbMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLbMac"),
        ("ME1200-MEP-MIB", "me1200ConfigLbToSend"),
        ("ME1200-MEP-MIB", "me1200ConfigLbSize"),
        ("ME1200-MEP-MIB", "me1200ConfigLbInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLbAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLbTableInfoGroup.setStatus("current")

me1200ConfigLbRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 14)
)
me1200ConfigLbRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLbRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorMac"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorToSend"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorSize"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLbRowEditorInfoGroup.setStatus("current")

me1200ConfigTstTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 15)
)
me1200ConfigTstTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigTstTxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigTstDei"),
        ("ME1200-MEP-MIB", "me1200ConfigTstPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigTstMep"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRate"),
        ("ME1200-MEP-MIB", "me1200ConfigTstSize"),
        ("ME1200-MEP-MIB", "me1200ConfigTstPattern"),
        ("ME1200-MEP-MIB", "me1200ConfigTstSequence"),
        ("ME1200-MEP-MIB", "me1200ConfigTstAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigTstTableInfoGroup.setStatus("current")

me1200ConfigTstRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 16)
)
me1200ConfigTstRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigTstRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorTxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorRxEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorRate"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorSize"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorPattern"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorSequence"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigTstRowEditorInfoGroup.setStatus("current")

me1200ConfigLtTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 17)
)
me1200ConfigLtTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLtDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLtPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLtMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLtMac"),
        ("ME1200-MEP-MIB", "me1200ConfigLtTimeToLive"),
        ("ME1200-MEP-MIB", "me1200ConfigLtAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLtTableInfoGroup.setStatus("current")

me1200ConfigLtRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 18)
)
me1200ConfigLtRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLtRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorMep"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorMac"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorTimeToLive"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLtRowEditorInfoGroup.setStatus("current")

me1200ConfigApsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 19)
)
me1200ConfigApsTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigApsDei"),
        ("ME1200-MEP-MIB", "me1200ConfigApsPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigApsApsType"),
        ("ME1200-MEP-MIB", "me1200ConfigApsCast"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRapsOctet"),
        ("ME1200-MEP-MIB", "me1200ConfigApsAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigApsTableInfoGroup.setStatus("current")

me1200ConfigApsRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 20)
)
me1200ConfigApsRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigApsRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorDei"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorApsType"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorCast"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorRapsOctet"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigApsRowEditorInfoGroup.setStatus("current")

me1200ConfigAisTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 21)
)
me1200ConfigAisTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigAisProtection"),
        ("ME1200-MEP-MIB", "me1200ConfigAisRate"),
        ("ME1200-MEP-MIB", "me1200ConfigAisAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigAisTableInfoGroup.setStatus("current")

me1200ConfigAisRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 22)
)
me1200ConfigAisRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigAisRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigAisRowEditorProtection"),
        ("ME1200-MEP-MIB", "me1200ConfigAisRowEditorRate"),
        ("ME1200-MEP-MIB", "me1200ConfigAisRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigAisRowEditorInfoGroup.setStatus("current")

me1200ConfigLckTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 23)
)
me1200ConfigLckTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLckRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLckAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLckTableInfoGroup.setStatus("current")

me1200ConfigLckRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 24)
)
me1200ConfigLckRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLckRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigLckRowEditorRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLckRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLckRowEditorInfoGroup.setStatus("current")

me1200ConfigClientTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 25)
)
me1200ConfigClientTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ConfigClientDomain")
)
if mibBuilder.loadTexts:
    me1200ConfigClientTableInfoGroup.setStatus("current")

me1200ConfigClientFlowTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 26)
)
me1200ConfigClientFlowTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigClientFlowAisPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowLckPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowLevel"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigClientFlowTableInfoGroup.setStatus("current")

me1200ConfigClientFlowRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 27)
)
me1200ConfigClientFlowRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorFlowId"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorAisPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorLckPrio"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorLevel"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigClientFlowRowEditorInfoGroup.setStatus("current")

me1200ConfigSyslogTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 28)
)
me1200ConfigSyslogTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ConfigSyslogEnable")
)
if mibBuilder.loadTexts:
    me1200ConfigSyslogTableInfoGroup.setStatus("current")

me1200ConfigTlvLeafInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 29)
)
me1200ConfigTlvLeafInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigTlvLeafOsTlvOuiFirst"),
        ("ME1200-MEP-MIB", "me1200ConfigTlvLeafOsTlvOuiSecond"),
        ("ME1200-MEP-MIB", "me1200ConfigTlvLeafOsTlvOuiThird"),
        ("ME1200-MEP-MIB", "me1200ConfigTlvLeafOsTlvSubType"),
        ("ME1200-MEP-MIB", "me1200ConfigTlvLeafOsTlvValue"))
)
if mibBuilder.loadTexts:
    me1200ConfigTlvLeafInfoGroup.setStatus("current")

me1200ConfigLstTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 30)
)
me1200ConfigLstTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ConfigLstEnable")
)
if mibBuilder.loadTexts:
    me1200ConfigLstTableInfoGroup.setStatus("current")

me1200ConfigLmAvailTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 31)
)
me1200ConfigLmAvailTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmAvailEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailLosRatioThr"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailMaintenance"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLmAvailTableInfoGroup.setStatus("current")

me1200ConfigLmAvailRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 32)
)
me1200ConfigLmAvailRowEditorInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorId"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorEnable"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorLosRatioThr"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorMaintenance"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ConfigLmAvailRowEditorInfoGroup.setStatus("current")

me1200StatusInstanceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 33)
)
me1200StatusInstanceTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusInstanceClevel"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCmeg"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCmep"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCssf"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCais"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceClck"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceAtsf"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceAtsd"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceAblk"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCloop"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceCconfig"))
)
if mibBuilder.loadTexts:
    me1200StatusInstanceTableInfoGroup.setStatus("current")

me1200StatusInstancePeerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 34)
)
me1200StatusInstancePeerTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusInstancePeerCloc"),
        ("ME1200-MEP-MIB", "me1200StatusInstancePeerCrdi"),
        ("ME1200-MEP-MIB", "me1200StatusInstancePeerCperiod"),
        ("ME1200-MEP-MIB", "me1200StatusInstancePeerCprio"))
)
if mibBuilder.loadTexts:
    me1200StatusInstancePeerTableInfoGroup.setStatus("current")

me1200StatusLmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 35)
)
me1200StatusLmTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLmTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmNearEndLosCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmFarEndLosCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmNearEndLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmFarEndLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmNearEndTotalLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmFarEndtotalLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmIntervalElapsed"))
)
if mibBuilder.loadTexts:
    me1200StatusLmTableInfoGroup.setStatus("current")

me1200StatusLmPeerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 36)
)
me1200StatusLmPeerTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLmPeerTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerNearEndLosCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerFarEndLosCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerNearEndLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerFarEndLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerNearEndTotalLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerFarEndtotalLosRatio"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerIntervalElapsed"))
)
if mibBuilder.loadTexts:
    me1200StatusLmPeerTableInfoGroup.setStatus("current")

me1200StatusDmTwoWayTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 37)
)
me1200StatusDmTwoWayTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusDmTwoWayTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayRxTimeOutCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayRxErrorCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayInternalOverflowCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayMinimumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayMaximumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayMinimumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayMaximumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayTimeUnit"))
)
if mibBuilder.loadTexts:
    me1200StatusDmTwoWayTableInfoGroup.setStatus("current")

me1200StatusDmOneWayFarNearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 38)
)
me1200StatusDmOneWayFarNearTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearRxTimeOutCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearRxErrorCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearInternalOverflowCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearMinimumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearMaximumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearMinimumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearMaximumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearTimeUnit"))
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayFarNearTableInfoGroup.setStatus("current")

me1200StatusDmOneWayNearFarTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 39)
)
me1200StatusDmOneWayNearFarTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarRxTimeOutCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarRxErrorCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarInternalOverflowCounter"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarMinimumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarMaximumDelay"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarMinimumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarMaximumDelayVariation"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarTimeUnit"))
)
if mibBuilder.loadTexts:
    me1200StatusDmOneWayNearFarTableInfoGroup.setStatus("current")

me1200StatusDmFdBinsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 40)
)
me1200StatusDmFdBinsTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusDmFdBinsTwValue"),
        ("ME1200-MEP-MIB", "me1200StatusDmFdBinsOwFtNValue"),
        ("ME1200-MEP-MIB", "me1200StatusDmFdBinsOwNtFValue"))
)
if mibBuilder.loadTexts:
    me1200StatusDmFdBinsTableInfoGroup.setStatus("current")

me1200StatusDmIfdvBinsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 41)
)
me1200StatusDmIfdvBinsTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusDmIfdvBinsTwValue"),
        ("ME1200-MEP-MIB", "me1200StatusDmIfdvBinsOwFtNValue"),
        ("ME1200-MEP-MIB", "me1200StatusDmIfdvBinsOwNtFValue"))
)
if mibBuilder.loadTexts:
    me1200StatusDmIfdvBinsTableInfoGroup.setStatus("current")

me1200StatusLbTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 42)
)
me1200StatusLbTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLbTransactionId"),
        ("ME1200-MEP-MIB", "me1200StatusLbReplyCounter"),
        ("ME1200-MEP-MIB", "me1200StatusLbLbmTransmitted"))
)
if mibBuilder.loadTexts:
    me1200StatusLbTableInfoGroup.setStatus("current")

me1200StatusLbReplyTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 43)
)
me1200StatusLbReplyTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLbReplyMac"),
        ("ME1200-MEP-MIB", "me1200StatusLbReplyLbrReceived"),
        ("ME1200-MEP-MIB", "me1200StatusLbReplyOutOfOrder"))
)
if mibBuilder.loadTexts:
    me1200StatusLbReplyTableInfoGroup.setStatus("current")

me1200StatusTstTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 44)
)
me1200StatusTstTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusTstTxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusTstRxCounter"),
        ("ME1200-MEP-MIB", "me1200StatusTstOutOfOrderCounter"),
        ("ME1200-MEP-MIB", "me1200StatusTstRxRate"),
        ("ME1200-MEP-MIB", "me1200StatusTstTestTime"))
)
if mibBuilder.loadTexts:
    me1200StatusTstTableInfoGroup.setStatus("current")

me1200StatusLtTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 45)
)
me1200StatusLtTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLtTransactionId"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyCount"))
)
if mibBuilder.loadTexts:
    me1200StatusLtTableInfoGroup.setStatus("current")

me1200StatusLtReplyTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 46)
)
me1200StatusLtReplyTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLtReplyMode"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyDirection"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyTtl"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyForwarded"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyRelayAction"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyLastEgressMac"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyNextEgressMac"))
)
if mibBuilder.loadTexts:
    me1200StatusLtReplyTableInfoGroup.setStatus("current")

me1200StatusCCPeerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 47)
)
me1200StatusCCPeerTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvOuiFirst"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvOuiSecond"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvOuiThird"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvSubType"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvValue"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerIsTlvValue"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerPsTlvValue"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerOsTlvReceived"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerIsTlvReceived"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerPsTlvReceived"))
)
if mibBuilder.loadTexts:
    me1200StatusCCPeerTableInfoGroup.setStatus("current")

me1200StatusLmAvailTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 48)
)
me1200StatusLmAvailTableInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200StatusLmAvailNearEndAvailState"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailFarEndAvailState"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailNearEndAvailCnt"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailFarEndAvailCnt"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailNearEndUnAvailCnt"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailFarEndUnAvailCnt"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailNearEndWindowCnt"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailFarEndWindowCnt"))
)
if mibBuilder.loadTexts:
    me1200StatusLmAvailTableInfoGroup.setStatus("current")

me1200ControlLmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 49)
)
me1200ControlLmTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ControlLmClear")
)
if mibBuilder.loadTexts:
    me1200ControlLmTableInfoGroup.setStatus("current")

me1200ControlDmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 50)
)
me1200ControlDmTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ControlDmClear")
)
if mibBuilder.loadTexts:
    me1200ControlDmTableInfoGroup.setStatus("current")

me1200ControlTstTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 51)
)
me1200ControlTstTableInfoGroup.setObjects(
    ("ME1200-MEP-MIB", "me1200ControlTstClear")
)
if mibBuilder.loadTexts:
    me1200ControlTstTableInfoGroup.setStatus("current")


# Notification objects

me1200MepNotificationLmNearEndLossRatioThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 1)
)
me1200MepNotificationLmNearEndLossRatioThresholdExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLmFlrInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmLossRatioThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusLmNearEndLosRatio"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationLmNearEndLossRatioThresholdExceed.setStatus(
        "current"
    )

me1200MepNotificationLmFarEndLossRatioThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 2)
)
me1200MepNotificationLmFarEndLossRatioThresholdExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigLmEnded"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRate"),
        ("ME1200-MEP-MIB", "me1200ConfigLmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigLmFlrInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigLmLossRatioThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusLmFarEndLosRatio"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationLmFarEndLossRatioThresholdExceed.setStatus(
        "current"
    )

me1200MepNotificationDmTwoWayAvgLastnDelayExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 3)
)
me1200MepNotificationDmTwoWayAvgLastnDelayExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmTwoWayAvgLastnDelayExceed.setStatus(
        "current"
    )

me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 4)
)
me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery.setStatus(
        "current"
    )

me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 5)
)
me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed.setStatus(
        "current"
    )

me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 6)
)
me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 7)
)
me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 8)
)
me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 9)
)
me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 10)
)
me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 11)
)
me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 12)
)
me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelay"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 13)
)
me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed.setStatus(
        "current"
    )

me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 1, 5, 0, 14)
)
me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery.setObjects(
      *(("ME1200-MEP-MIB", "me1200ConfigDmCast"),
        ("ME1200-MEP-MIB", "me1200ConfigDmMep"),
        ("ME1200-MEP-MIB", "me1200ConfigDmCalcWay"),
        ("ME1200-MEP-MIB", "me1200ConfigDmInterval"),
        ("ME1200-MEP-MIB", "me1200ConfigDmLastN"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTimeUnit"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOverflowAct"),
        ("ME1200-MEP-MIB", "me1200ConfigDmSynchronized"),
        ("ME1200-MEP-MIB", "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarAverageLastnDelayVariation"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery.setStatus(
        "current"
    )


# Notifications groups

me1200MepNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 2, 52)
)
me1200MepNotificationInfoGroup.setObjects(
      *(("ME1200-MEP-MIB", "me1200MepNotificationLmNearEndLossRatioThresholdExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationLmFarEndLossRatioThresholdExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmTwoWayAvgLastnDelayExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed"),
        ("ME1200-MEP-MIB", "me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery"))
)
if mibBuilder.loadTexts:
    me1200MepNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200MepMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 46, 3, 1, 1)
)
me1200MepMibCompliance.setObjects(
      *(("ME1200-MEP-MIB", "me1200MepCapabilitiesInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigInstanceRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigInstancePeerRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigPmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigCcTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigCcRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLmRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigDmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigDmRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLbTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLbRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigTstTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigTstRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLtTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLtRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigApsTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigApsRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigAisTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigAisRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLckTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLckRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigClientTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigClientFlowRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigSyslogTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigTlvLeafInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLstTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ConfigLmAvailRowEditorInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusInstanceTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusInstancePeerTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLmPeerTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusDmTwoWayTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayFarNearTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusDmOneWayNearFarTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusDmFdBinsTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusDmIfdvBinsTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLbTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLbReplyTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusTstTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLtTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLtReplyTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusCCPeerTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200StatusLmAvailTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ControlLmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ControlDmTableInfoGroup"),
        ("ME1200-MEP-MIB", "me1200ControlTstTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200MepMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-MEP-MIB",
    **{"ME1200Action": ME1200Action,
       "ME1200ApsType": ME1200ApsType,
       "ME1200AvailState": ME1200AvailState,
       "ME1200CalcWay": ME1200CalcWay,
       "ME1200Cast": ME1200Cast,
       "ME1200Ended": ME1200Ended,
       "ME1200InstanceDomain": ME1200InstanceDomain,
       "ME1200InstanceMode": ME1200InstanceMode,
       "ME1200MegIdFormat": ME1200MegIdFormat,
       "ME1200RelayAction": ME1200RelayAction,
       "ME1200TstPattern": ME1200TstPattern,
       "me1200MepMib": me1200MepMib,
       "me1200MepMibObjects": me1200MepMibObjects,
       "me1200MepCapabilities": me1200MepCapabilities,
       "me1200MepCapabilitiesInstanceMax": me1200MepCapabilitiesInstanceMax,
       "me1200MepCapabilitiesPeerMax": me1200MepCapabilitiesPeerMax,
       "me1200MepCapabilitiesTransactionMax": me1200MepCapabilitiesTransactionMax,
       "me1200MepCapabilitiesReplyMax": me1200MepCapabilitiesReplyMax,
       "me1200MepCapabilitiesClientFlowsMax": me1200MepCapabilitiesClientFlowsMax,
       "me1200MepCapabilitiesMacMength": me1200MepCapabilitiesMacMength,
       "me1200MepCapabilitiesMegCodeLength": me1200MepCapabilitiesMegCodeLength,
       "me1200MepCapabilitiesDmIntervalMin": me1200MepCapabilitiesDmIntervalMin,
       "me1200MepCapabilitiesDmIntervalMax": me1200MepCapabilitiesDmIntervalMax,
       "me1200MepCapabilitiesDmLastnMin": me1200MepCapabilitiesDmLastnMin,
       "me1200MepCapabilitiesDmLastnMax": me1200MepCapabilitiesDmLastnMax,
       "me1200MepCapabilitiesLbmSizeMax": me1200MepCapabilitiesLbmSizeMax,
       "me1200MepCapabilitiesLbmSizeMin": me1200MepCapabilitiesLbmSizeMin,
       "me1200MepCapabilitiesTstSizeMax": me1200MepCapabilitiesTstSizeMax,
       "me1200MepCapabilitiesTstSizeMin": me1200MepCapabilitiesTstSizeMin,
       "me1200MepCapabilitiesTstRateMax": me1200MepCapabilitiesTstRateMax,
       "me1200MepCapabilitiesClientPrioHighest": me1200MepCapabilitiesClientPrioHighest,
       "me1200MepCapabilitiesLbToSendInfinite": me1200MepCapabilitiesLbToSendInfinite,
       "me1200MepCapabilitiesLmLossRatioThresholdMin": me1200MepCapabilitiesLmLossRatioThresholdMin,
       "me1200MepCapabilitiesLmLossRatioThresholdMax": me1200MepCapabilitiesLmLossRatioThresholdMax,
       "me1200MepCapabilitiesDmAverageDelayThresholdMin": me1200MepCapabilitiesDmAverageDelayThresholdMin,
       "me1200MepCapabilitiesDmAverageDelayThresholdMax": me1200MepCapabilitiesDmAverageDelayThresholdMax,
       "me1200MepCapabilitiesSlmSizeMax": me1200MepCapabilitiesSlmSizeMax,
       "me1200MepCapabilitiesSlmSizeMin": me1200MepCapabilitiesSlmSizeMin,
       "me1200MepConfig": me1200MepConfig,
       "me1200ConfigInstance": me1200ConfigInstance,
       "me1200ConfigInstanceTable": me1200ConfigInstanceTable,
       "me1200ConfigInstanceEntry": me1200ConfigInstanceEntry,
       "me1200ConfigInstanceId": me1200ConfigInstanceId,
       "me1200ConfigInstanceMode": me1200ConfigInstanceMode,
       "me1200ConfigInstanceDirection": me1200ConfigInstanceDirection,
       "me1200ConfigInstanceDomain": me1200ConfigInstanceDomain,
       "me1200ConfigInstanceFlow": me1200ConfigInstanceFlow,
       "me1200ConfigInstancePort": me1200ConfigInstancePort,
       "me1200ConfigInstanceLevel": me1200ConfigInstanceLevel,
       "me1200ConfigInstanceVid": me1200ConfigInstanceVid,
       "me1200ConfigInstanceVoe": me1200ConfigInstanceVoe,
       "me1200ConfigInstanceMac": me1200ConfigInstanceMac,
       "me1200ConfigInstanceFormat": me1200ConfigInstanceFormat,
       "me1200ConfigInstanceName": me1200ConfigInstanceName,
       "me1200ConfigInstanceMeg": me1200ConfigInstanceMeg,
       "me1200ConfigInstanceMep": me1200ConfigInstanceMep,
       "me1200ConfigInstanceAction": me1200ConfigInstanceAction,
       "me1200ConfigInstanceRowEditor": me1200ConfigInstanceRowEditor,
       "me1200ConfigInstanceRowEditorId": me1200ConfigInstanceRowEditorId,
       "me1200ConfigInstanceRowEditorMode": me1200ConfigInstanceRowEditorMode,
       "me1200ConfigInstanceRowEditorDirection": me1200ConfigInstanceRowEditorDirection,
       "me1200ConfigInstanceRowEditorDomain": me1200ConfigInstanceRowEditorDomain,
       "me1200ConfigInstanceRowEditorFlow": me1200ConfigInstanceRowEditorFlow,
       "me1200ConfigInstanceRowEditorPort": me1200ConfigInstanceRowEditorPort,
       "me1200ConfigInstanceRowEditorLevel": me1200ConfigInstanceRowEditorLevel,
       "me1200ConfigInstanceRowEditorVid": me1200ConfigInstanceRowEditorVid,
       "me1200ConfigInstanceRowEditorVoe": me1200ConfigInstanceRowEditorVoe,
       "me1200ConfigInstanceRowEditorMac": me1200ConfigInstanceRowEditorMac,
       "me1200ConfigInstanceRowEditorFormat": me1200ConfigInstanceRowEditorFormat,
       "me1200ConfigInstanceRowEditorName": me1200ConfigInstanceRowEditorName,
       "me1200ConfigInstanceRowEditorMeg": me1200ConfigInstanceRowEditorMeg,
       "me1200ConfigInstanceRowEditorMep": me1200ConfigInstanceRowEditorMep,
       "me1200ConfigInstanceRowEditorAction": me1200ConfigInstanceRowEditorAction,
       "me1200ConfigInstancePeerTable": me1200ConfigInstancePeerTable,
       "me1200ConfigInstancePeerEntry": me1200ConfigInstancePeerEntry,
       "me1200ConfigInstancePeerId": me1200ConfigInstancePeerId,
       "me1200ConfigInstancePeerPeerId": me1200ConfigInstancePeerPeerId,
       "me1200ConfigInstancePeerMac": me1200ConfigInstancePeerMac,
       "me1200ConfigInstancePeerAction": me1200ConfigInstancePeerAction,
       "me1200ConfigInstancePeerRowEditor": me1200ConfigInstancePeerRowEditor,
       "me1200ConfigInstancePeerRowEditorId": me1200ConfigInstancePeerRowEditorId,
       "me1200ConfigInstancePeerRowEditorPeerId": me1200ConfigInstancePeerRowEditorPeerId,
       "me1200ConfigInstancePeerRowEditorMac": me1200ConfigInstancePeerRowEditorMac,
       "me1200ConfigInstancePeerRowEditorAction": me1200ConfigInstancePeerRowEditorAction,
       "me1200ConfigPerfMon": me1200ConfigPerfMon,
       "me1200ConfigPmTable": me1200ConfigPmTable,
       "me1200ConfigPmEntry": me1200ConfigPmEntry,
       "me1200ConfigPmId": me1200ConfigPmId,
       "me1200ConfigPmEnable": me1200ConfigPmEnable,
       "me1200ConfigContinuityCheck": me1200ConfigContinuityCheck,
       "me1200ConfigCcTable": me1200ConfigCcTable,
       "me1200ConfigCcEntry": me1200ConfigCcEntry,
       "me1200ConfigCcId": me1200ConfigCcId,
       "me1200ConfigCcDei": me1200ConfigCcDei,
       "me1200ConfigCcPrio": me1200ConfigCcPrio,
       "me1200ConfigCcRate": me1200ConfigCcRate,
       "me1200ConfigCcTlv": me1200ConfigCcTlv,
       "me1200ConfigCcAction": me1200ConfigCcAction,
       "me1200ConfigCcRowEditor": me1200ConfigCcRowEditor,
       "me1200ConfigCcRowEditorId": me1200ConfigCcRowEditorId,
       "me1200ConfigCcRowEditorDei": me1200ConfigCcRowEditorDei,
       "me1200ConfigCcRowEditorPrio": me1200ConfigCcRowEditorPrio,
       "me1200ConfigCcRowEditorRate": me1200ConfigCcRowEditorRate,
       "me1200ConfigCcRowEditorTlv": me1200ConfigCcRowEditorTlv,
       "me1200ConfigCcRowEditorAction": me1200ConfigCcRowEditorAction,
       "me1200ConfigLossMeasurement": me1200ConfigLossMeasurement,
       "me1200ConfigLmTable": me1200ConfigLmTable,
       "me1200ConfigLmEntry": me1200ConfigLmEntry,
       "me1200ConfigLmId": me1200ConfigLmId,
       "me1200ConfigLmEnded": me1200ConfigLmEnded,
       "me1200ConfigLmDei": me1200ConfigLmDei,
       "me1200ConfigLmPrio": me1200ConfigLmPrio,
       "me1200ConfigLmRate": me1200ConfigLmRate,
       "me1200ConfigLmCast": me1200ConfigLmCast,
       "me1200ConfigLmFlrInterval": me1200ConfigLmFlrInterval,
       "me1200ConfigLmLossRatioThreshold": me1200ConfigLmLossRatioThreshold,
       "me1200ConfigLmRxEnable": me1200ConfigLmRxEnable,
       "me1200ConfigLmSynthetic": me1200ConfigLmSynthetic,
       "me1200ConfigLmMep": me1200ConfigLmMep,
       "me1200ConfigLmFrameSize": me1200ConfigLmFrameSize,
       "me1200ConfigLmMeasInterval": me1200ConfigLmMeasInterval,
       "me1200ConfigLmAction": me1200ConfigLmAction,
       "me1200ConfigLmRowEditor": me1200ConfigLmRowEditor,
       "me1200ConfigLmRowEditorId": me1200ConfigLmRowEditorId,
       "me1200ConfigLmRowEditorEnded": me1200ConfigLmRowEditorEnded,
       "me1200ConfigLmRowEditorDei": me1200ConfigLmRowEditorDei,
       "me1200ConfigLmRowEditorPrio": me1200ConfigLmRowEditorPrio,
       "me1200ConfigLmRowEditorRate": me1200ConfigLmRowEditorRate,
       "me1200ConfigLmRowEditorCast": me1200ConfigLmRowEditorCast,
       "me1200ConfigLmRowEditorFlrInterval": me1200ConfigLmRowEditorFlrInterval,
       "me1200ConfigLmRowEditorLossRatioThreshold": me1200ConfigLmRowEditorLossRatioThreshold,
       "me1200ConfigLmRowEditorRxEnable": me1200ConfigLmRowEditorRxEnable,
       "me1200ConfigLmRowEditorSynthetic": me1200ConfigLmRowEditorSynthetic,
       "me1200ConfigLmRowEditorMep": me1200ConfigLmRowEditorMep,
       "me1200ConfigLmRowEditorFrameSize": me1200ConfigLmRowEditorFrameSize,
       "me1200ConfigLmRowEditorMeasInterval": me1200ConfigLmRowEditorMeasInterval,
       "me1200ConfigLmRowEditorAction": me1200ConfigLmRowEditorAction,
       "me1200ConfigDelayMeasurement": me1200ConfigDelayMeasurement,
       "me1200ConfigDmTable": me1200ConfigDmTable,
       "me1200ConfigDmEntry": me1200ConfigDmEntry,
       "me1200ConfigDmId": me1200ConfigDmId,
       "me1200ConfigDmEnded": me1200ConfigDmEnded,
       "me1200ConfigDmDei": me1200ConfigDmDei,
       "me1200ConfigDmPrio": me1200ConfigDmPrio,
       "me1200ConfigDmCast": me1200ConfigDmCast,
       "me1200ConfigDmMep": me1200ConfigDmMep,
       "me1200ConfigDmCalcWay": me1200ConfigDmCalcWay,
       "me1200ConfigDmInterval": me1200ConfigDmInterval,
       "me1200ConfigDmLastN": me1200ConfigDmLastN,
       "me1200ConfigDmTimeUnit": me1200ConfigDmTimeUnit,
       "me1200ConfigDmOverflowAct": me1200ConfigDmOverflowAct,
       "me1200ConfigDmSynchronized": me1200ConfigDmSynchronized,
       "me1200ConfigDmOneWayAverageLastnDelayThreshold": me1200ConfigDmOneWayAverageLastnDelayThreshold,
       "me1200ConfigDmOneWayAverageLastnDelayVariationThreshold": me1200ConfigDmOneWayAverageLastnDelayVariationThreshold,
       "me1200ConfigDmTwoWayAverageLastnDelayThreshold": me1200ConfigDmTwoWayAverageLastnDelayThreshold,
       "me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold": me1200ConfigDmTwoWayAverageLastnDelayVariationThreshold,
       "me1200ConfigDmNumOfBinFD": me1200ConfigDmNumOfBinFD,
       "me1200ConfigDmNumOfBinIFDV": me1200ConfigDmNumOfBinIFDV,
       "me1200ConfigDmMThreshold": me1200ConfigDmMThreshold,
       "me1200ConfigDmAction": me1200ConfigDmAction,
       "me1200ConfigDmRowEditor": me1200ConfigDmRowEditor,
       "me1200ConfigDmRowEditorId": me1200ConfigDmRowEditorId,
       "me1200ConfigDmRowEditorEnded": me1200ConfigDmRowEditorEnded,
       "me1200ConfigDmRowEditorDei": me1200ConfigDmRowEditorDei,
       "me1200ConfigDmRowEditorPrio": me1200ConfigDmRowEditorPrio,
       "me1200ConfigDmRowEditorCast": me1200ConfigDmRowEditorCast,
       "me1200ConfigDmRowEditorMep": me1200ConfigDmRowEditorMep,
       "me1200ConfigDmRowEditorCalcWay": me1200ConfigDmRowEditorCalcWay,
       "me1200ConfigDmRowEditorInterval": me1200ConfigDmRowEditorInterval,
       "me1200ConfigDmRowEditorLastN": me1200ConfigDmRowEditorLastN,
       "me1200ConfigDmRowEditorTimeUnit": me1200ConfigDmRowEditorTimeUnit,
       "me1200ConfigDmRowEditorOverflowAct": me1200ConfigDmRowEditorOverflowAct,
       "me1200ConfigDmRowEditorSynchronized": me1200ConfigDmRowEditorSynchronized,
       "me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold": me1200ConfigDmRowEditorOneWayAverageLastnDelayThreshold,
       "me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold": me1200ConfigDmRowEditorOneWayAverageLastnDelayVariationThreshold,
       "me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold": me1200ConfigDmRowEditorTwoWayAverageLastnDelayThreshold,
       "me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold": me1200ConfigDmRowEditorTwoWayAverageLastnDelayVariationThreshold,
       "me1200ConfigDmRowEditorNumOfBinFD": me1200ConfigDmRowEditorNumOfBinFD,
       "me1200ConfigDmRowEditorNumOfBinIFDV": me1200ConfigDmRowEditorNumOfBinIFDV,
       "me1200ConfigDmRowEditorMThreshold": me1200ConfigDmRowEditorMThreshold,
       "me1200ConfigDmRowEditorAction": me1200ConfigDmRowEditorAction,
       "me1200ConfigLoopBack": me1200ConfigLoopBack,
       "me1200ConfigLbTable": me1200ConfigLbTable,
       "me1200ConfigLbEntry": me1200ConfigLbEntry,
       "me1200ConfigLbId": me1200ConfigLbId,
       "me1200ConfigLbDei": me1200ConfigLbDei,
       "me1200ConfigLbPrio": me1200ConfigLbPrio,
       "me1200ConfigLbCast": me1200ConfigLbCast,
       "me1200ConfigLbMep": me1200ConfigLbMep,
       "me1200ConfigLbMac": me1200ConfigLbMac,
       "me1200ConfigLbToSend": me1200ConfigLbToSend,
       "me1200ConfigLbSize": me1200ConfigLbSize,
       "me1200ConfigLbInterval": me1200ConfigLbInterval,
       "me1200ConfigLbAction": me1200ConfigLbAction,
       "me1200ConfigLbRowEditor": me1200ConfigLbRowEditor,
       "me1200ConfigLbRowEditorId": me1200ConfigLbRowEditorId,
       "me1200ConfigLbRowEditorDei": me1200ConfigLbRowEditorDei,
       "me1200ConfigLbRowEditorPrio": me1200ConfigLbRowEditorPrio,
       "me1200ConfigLbRowEditorCast": me1200ConfigLbRowEditorCast,
       "me1200ConfigLbRowEditorMep": me1200ConfigLbRowEditorMep,
       "me1200ConfigLbRowEditorMac": me1200ConfigLbRowEditorMac,
       "me1200ConfigLbRowEditorToSend": me1200ConfigLbRowEditorToSend,
       "me1200ConfigLbRowEditorSize": me1200ConfigLbRowEditorSize,
       "me1200ConfigLbRowEditorInterval": me1200ConfigLbRowEditorInterval,
       "me1200ConfigLbRowEditorAction": me1200ConfigLbRowEditorAction,
       "me1200ConfigTestSignal": me1200ConfigTestSignal,
       "me1200ConfigTstTable": me1200ConfigTstTable,
       "me1200ConfigTstEntry": me1200ConfigTstEntry,
       "me1200ConfigTstId": me1200ConfigTstId,
       "me1200ConfigTstTxEnable": me1200ConfigTstTxEnable,
       "me1200ConfigTstRxEnable": me1200ConfigTstRxEnable,
       "me1200ConfigTstDei": me1200ConfigTstDei,
       "me1200ConfigTstPrio": me1200ConfigTstPrio,
       "me1200ConfigTstMep": me1200ConfigTstMep,
       "me1200ConfigTstRate": me1200ConfigTstRate,
       "me1200ConfigTstSize": me1200ConfigTstSize,
       "me1200ConfigTstPattern": me1200ConfigTstPattern,
       "me1200ConfigTstSequence": me1200ConfigTstSequence,
       "me1200ConfigTstAction": me1200ConfigTstAction,
       "me1200ConfigTstRowEditor": me1200ConfigTstRowEditor,
       "me1200ConfigTstRowEditorId": me1200ConfigTstRowEditorId,
       "me1200ConfigTstRowEditorTxEnable": me1200ConfigTstRowEditorTxEnable,
       "me1200ConfigTstRowEditorRxEnable": me1200ConfigTstRowEditorRxEnable,
       "me1200ConfigTstRowEditorDei": me1200ConfigTstRowEditorDei,
       "me1200ConfigTstRowEditorPrio": me1200ConfigTstRowEditorPrio,
       "me1200ConfigTstRowEditorMep": me1200ConfigTstRowEditorMep,
       "me1200ConfigTstRowEditorRate": me1200ConfigTstRowEditorRate,
       "me1200ConfigTstRowEditorSize": me1200ConfigTstRowEditorSize,
       "me1200ConfigTstRowEditorPattern": me1200ConfigTstRowEditorPattern,
       "me1200ConfigTstRowEditorSequence": me1200ConfigTstRowEditorSequence,
       "me1200ConfigTstRowEditorAction": me1200ConfigTstRowEditorAction,
       "me1200ConfigLinkTrace": me1200ConfigLinkTrace,
       "me1200ConfigLtTable": me1200ConfigLtTable,
       "me1200ConfigLtEntry": me1200ConfigLtEntry,
       "me1200ConfigLtId": me1200ConfigLtId,
       "me1200ConfigLtDei": me1200ConfigLtDei,
       "me1200ConfigLtPrio": me1200ConfigLtPrio,
       "me1200ConfigLtMep": me1200ConfigLtMep,
       "me1200ConfigLtMac": me1200ConfigLtMac,
       "me1200ConfigLtTimeToLive": me1200ConfigLtTimeToLive,
       "me1200ConfigLtAction": me1200ConfigLtAction,
       "me1200ConfigLtRowEditor": me1200ConfigLtRowEditor,
       "me1200ConfigLtRowEditorId": me1200ConfigLtRowEditorId,
       "me1200ConfigLtRowEditorDei": me1200ConfigLtRowEditorDei,
       "me1200ConfigLtRowEditorPrio": me1200ConfigLtRowEditorPrio,
       "me1200ConfigLtRowEditorMep": me1200ConfigLtRowEditorMep,
       "me1200ConfigLtRowEditorMac": me1200ConfigLtRowEditorMac,
       "me1200ConfigLtRowEditorTimeToLive": me1200ConfigLtRowEditorTimeToLive,
       "me1200ConfigLtRowEditorAction": me1200ConfigLtRowEditorAction,
       "me1200ConfigAutomaticProtectionSwitching": me1200ConfigAutomaticProtectionSwitching,
       "me1200ConfigApsTable": me1200ConfigApsTable,
       "me1200ConfigApsEntry": me1200ConfigApsEntry,
       "me1200ConfigApsId": me1200ConfigApsId,
       "me1200ConfigApsDei": me1200ConfigApsDei,
       "me1200ConfigApsPrio": me1200ConfigApsPrio,
       "me1200ConfigApsApsType": me1200ConfigApsApsType,
       "me1200ConfigApsCast": me1200ConfigApsCast,
       "me1200ConfigApsRapsOctet": me1200ConfigApsRapsOctet,
       "me1200ConfigApsAction": me1200ConfigApsAction,
       "me1200ConfigApsRowEditor": me1200ConfigApsRowEditor,
       "me1200ConfigApsRowEditorId": me1200ConfigApsRowEditorId,
       "me1200ConfigApsRowEditorDei": me1200ConfigApsRowEditorDei,
       "me1200ConfigApsRowEditorPrio": me1200ConfigApsRowEditorPrio,
       "me1200ConfigApsRowEditorApsType": me1200ConfigApsRowEditorApsType,
       "me1200ConfigApsRowEditorCast": me1200ConfigApsRowEditorCast,
       "me1200ConfigApsRowEditorRapsOctet": me1200ConfigApsRowEditorRapsOctet,
       "me1200ConfigApsRowEditorAction": me1200ConfigApsRowEditorAction,
       "me1200ConfigAlarmIndicationSignal": me1200ConfigAlarmIndicationSignal,
       "me1200ConfigAisTable": me1200ConfigAisTable,
       "me1200ConfigAisEntry": me1200ConfigAisEntry,
       "me1200ConfigAisId": me1200ConfigAisId,
       "me1200ConfigAisProtection": me1200ConfigAisProtection,
       "me1200ConfigAisRate": me1200ConfigAisRate,
       "me1200ConfigAisAction": me1200ConfigAisAction,
       "me1200ConfigAisRowEditor": me1200ConfigAisRowEditor,
       "me1200ConfigAisRowEditorId": me1200ConfigAisRowEditorId,
       "me1200ConfigAisRowEditorProtection": me1200ConfigAisRowEditorProtection,
       "me1200ConfigAisRowEditorRate": me1200ConfigAisRowEditorRate,
       "me1200ConfigAisRowEditorAction": me1200ConfigAisRowEditorAction,
       "me1200ConfigLockedSignal": me1200ConfigLockedSignal,
       "me1200ConfigLckTable": me1200ConfigLckTable,
       "me1200ConfigLckEntry": me1200ConfigLckEntry,
       "me1200ConfigLckId": me1200ConfigLckId,
       "me1200ConfigLckRate": me1200ConfigLckRate,
       "me1200ConfigLckAction": me1200ConfigLckAction,
       "me1200ConfigLckRowEditor": me1200ConfigLckRowEditor,
       "me1200ConfigLckRowEditorId": me1200ConfigLckRowEditorId,
       "me1200ConfigLckRowEditorRate": me1200ConfigLckRowEditorRate,
       "me1200ConfigLckRowEditorAction": me1200ConfigLckRowEditorAction,
       "me1200ConfigClient": me1200ConfigClient,
       "me1200ConfigClientTable": me1200ConfigClientTable,
       "me1200ConfigClientEntry": me1200ConfigClientEntry,
       "me1200ConfigClientId": me1200ConfigClientId,
       "me1200ConfigClientDomain": me1200ConfigClientDomain,
       "me1200ConfigClientFlowTable": me1200ConfigClientFlowTable,
       "me1200ConfigClientFlowEntry": me1200ConfigClientFlowEntry,
       "me1200ConfigClientFlowId": me1200ConfigClientFlowId,
       "me1200ConfigClientFlowFlowId": me1200ConfigClientFlowFlowId,
       "me1200ConfigClientFlowAisPrio": me1200ConfigClientFlowAisPrio,
       "me1200ConfigClientFlowLckPrio": me1200ConfigClientFlowLckPrio,
       "me1200ConfigClientFlowLevel": me1200ConfigClientFlowLevel,
       "me1200ConfigClientFlowAction": me1200ConfigClientFlowAction,
       "me1200ConfigClientFlowRowEditor": me1200ConfigClientFlowRowEditor,
       "me1200ConfigClientFlowRowEditorId": me1200ConfigClientFlowRowEditorId,
       "me1200ConfigClientFlowRowEditorFlowId": me1200ConfigClientFlowRowEditorFlowId,
       "me1200ConfigClientFlowRowEditorAisPrio": me1200ConfigClientFlowRowEditorAisPrio,
       "me1200ConfigClientFlowRowEditorLckPrio": me1200ConfigClientFlowRowEditorLckPrio,
       "me1200ConfigClientFlowRowEditorLevel": me1200ConfigClientFlowRowEditorLevel,
       "me1200ConfigClientFlowRowEditorAction": me1200ConfigClientFlowRowEditorAction,
       "me1200ConfigSyslog": me1200ConfigSyslog,
       "me1200ConfigSyslogTable": me1200ConfigSyslogTable,
       "me1200ConfigSyslogEntry": me1200ConfigSyslogEntry,
       "me1200ConfigSyslogId": me1200ConfigSyslogId,
       "me1200ConfigSyslogEnable": me1200ConfigSyslogEnable,
       "me1200ConfigTlv": me1200ConfigTlv,
       "me1200ConfigTlvLeaf": me1200ConfigTlvLeaf,
       "me1200ConfigTlvLeafOsTlvOuiFirst": me1200ConfigTlvLeafOsTlvOuiFirst,
       "me1200ConfigTlvLeafOsTlvOuiSecond": me1200ConfigTlvLeafOsTlvOuiSecond,
       "me1200ConfigTlvLeafOsTlvOuiThird": me1200ConfigTlvLeafOsTlvOuiThird,
       "me1200ConfigTlvLeafOsTlvSubType": me1200ConfigTlvLeafOsTlvSubType,
       "me1200ConfigTlvLeafOsTlvValue": me1200ConfigTlvLeafOsTlvValue,
       "me1200ConfigLinkStateTracking": me1200ConfigLinkStateTracking,
       "me1200ConfigLstTable": me1200ConfigLstTable,
       "me1200ConfigLstEntry": me1200ConfigLstEntry,
       "me1200ConfigLstId": me1200ConfigLstId,
       "me1200ConfigLstEnable": me1200ConfigLstEnable,
       "me1200ConfigLmAvailability": me1200ConfigLmAvailability,
       "me1200ConfigLmAvailTable": me1200ConfigLmAvailTable,
       "me1200ConfigLmAvailEntry": me1200ConfigLmAvailEntry,
       "me1200ConfigLmAvailId": me1200ConfigLmAvailId,
       "me1200ConfigLmAvailEnable": me1200ConfigLmAvailEnable,
       "me1200ConfigLmAvailLosRatioThr": me1200ConfigLmAvailLosRatioThr,
       "me1200ConfigLmAvailInterval": me1200ConfigLmAvailInterval,
       "me1200ConfigLmAvailMaintenance": me1200ConfigLmAvailMaintenance,
       "me1200ConfigLmAvailAction": me1200ConfigLmAvailAction,
       "me1200ConfigLmAvailRowEditor": me1200ConfigLmAvailRowEditor,
       "me1200ConfigLmAvailRowEditorId": me1200ConfigLmAvailRowEditorId,
       "me1200ConfigLmAvailRowEditorEnable": me1200ConfigLmAvailRowEditorEnable,
       "me1200ConfigLmAvailRowEditorLosRatioThr": me1200ConfigLmAvailRowEditorLosRatioThr,
       "me1200ConfigLmAvailRowEditorInterval": me1200ConfigLmAvailRowEditorInterval,
       "me1200ConfigLmAvailRowEditorMaintenance": me1200ConfigLmAvailRowEditorMaintenance,
       "me1200ConfigLmAvailRowEditorAction": me1200ConfigLmAvailRowEditorAction,
       "me1200MepStatus": me1200MepStatus,
       "me1200StatusInstance": me1200StatusInstance,
       "me1200StatusInstanceTable": me1200StatusInstanceTable,
       "me1200StatusInstanceEntry": me1200StatusInstanceEntry,
       "me1200StatusInstanceId": me1200StatusInstanceId,
       "me1200StatusInstanceClevel": me1200StatusInstanceClevel,
       "me1200StatusInstanceCmeg": me1200StatusInstanceCmeg,
       "me1200StatusInstanceCmep": me1200StatusInstanceCmep,
       "me1200StatusInstanceCssf": me1200StatusInstanceCssf,
       "me1200StatusInstanceCais": me1200StatusInstanceCais,
       "me1200StatusInstanceClck": me1200StatusInstanceClck,
       "me1200StatusInstanceAtsf": me1200StatusInstanceAtsf,
       "me1200StatusInstanceAtsd": me1200StatusInstanceAtsd,
       "me1200StatusInstanceAblk": me1200StatusInstanceAblk,
       "me1200StatusInstanceCloop": me1200StatusInstanceCloop,
       "me1200StatusInstanceCconfig": me1200StatusInstanceCconfig,
       "me1200StatusInstancePeerTable": me1200StatusInstancePeerTable,
       "me1200StatusInstancePeerEntry": me1200StatusInstancePeerEntry,
       "me1200StatusInstancePeerId": me1200StatusInstancePeerId,
       "me1200StatusInstancePeerPeerId": me1200StatusInstancePeerPeerId,
       "me1200StatusInstancePeerCloc": me1200StatusInstancePeerCloc,
       "me1200StatusInstancePeerCrdi": me1200StatusInstancePeerCrdi,
       "me1200StatusInstancePeerCperiod": me1200StatusInstancePeerCperiod,
       "me1200StatusInstancePeerCprio": me1200StatusInstancePeerCprio,
       "me1200StatusLossMeasurement": me1200StatusLossMeasurement,
       "me1200StatusLmTable": me1200StatusLmTable,
       "me1200StatusLmEntry": me1200StatusLmEntry,
       "me1200StatusLmId": me1200StatusLmId,
       "me1200StatusLmTxCounter": me1200StatusLmTxCounter,
       "me1200StatusLmRxCounter": me1200StatusLmRxCounter,
       "me1200StatusLmNearEndLosCounter": me1200StatusLmNearEndLosCounter,
       "me1200StatusLmFarEndLosCounter": me1200StatusLmFarEndLosCounter,
       "me1200StatusLmNearEndLosRatio": me1200StatusLmNearEndLosRatio,
       "me1200StatusLmFarEndLosRatio": me1200StatusLmFarEndLosRatio,
       "me1200StatusLmNearEndTotalLosRatio": me1200StatusLmNearEndTotalLosRatio,
       "me1200StatusLmFarEndtotalLosRatio": me1200StatusLmFarEndtotalLosRatio,
       "me1200StatusLmIntervalElapsed": me1200StatusLmIntervalElapsed,
       "me1200StatusLmPeerTable": me1200StatusLmPeerTable,
       "me1200StatusLmPeerEntry": me1200StatusLmPeerEntry,
       "me1200StatusLmPeerId": me1200StatusLmPeerId,
       "me1200StatusLmPeerPeerId": me1200StatusLmPeerPeerId,
       "me1200StatusLmPeerTxCounter": me1200StatusLmPeerTxCounter,
       "me1200StatusLmPeerRxCounter": me1200StatusLmPeerRxCounter,
       "me1200StatusLmPeerNearEndLosCounter": me1200StatusLmPeerNearEndLosCounter,
       "me1200StatusLmPeerFarEndLosCounter": me1200StatusLmPeerFarEndLosCounter,
       "me1200StatusLmPeerNearEndLosRatio": me1200StatusLmPeerNearEndLosRatio,
       "me1200StatusLmPeerFarEndLosRatio": me1200StatusLmPeerFarEndLosRatio,
       "me1200StatusLmPeerNearEndTotalLosRatio": me1200StatusLmPeerNearEndTotalLosRatio,
       "me1200StatusLmPeerFarEndtotalLosRatio": me1200StatusLmPeerFarEndtotalLosRatio,
       "me1200StatusLmPeerIntervalElapsed": me1200StatusLmPeerIntervalElapsed,
       "me1200StatusDelayMeasurement": me1200StatusDelayMeasurement,
       "me1200StatusDmTwoWayTable": me1200StatusDmTwoWayTable,
       "me1200StatusDmTwoWayEntry": me1200StatusDmTwoWayEntry,
       "me1200StatusDmTwoWayId": me1200StatusDmTwoWayId,
       "me1200StatusDmTwoWayTxCounter": me1200StatusDmTwoWayTxCounter,
       "me1200StatusDmTwoWayRxCounter": me1200StatusDmTwoWayRxCounter,
       "me1200StatusDmTwoWayRxTimeOutCounter": me1200StatusDmTwoWayRxTimeOutCounter,
       "me1200StatusDmTwoWayRxErrorCounter": me1200StatusDmTwoWayRxErrorCounter,
       "me1200StatusDmTwoWayInternalOverflowCounter": me1200StatusDmTwoWayInternalOverflowCounter,
       "me1200StatusDmTwoWayAverageDelay": me1200StatusDmTwoWayAverageDelay,
       "me1200StatusDmTwoWayAverageLastnDelay": me1200StatusDmTwoWayAverageLastnDelay,
       "me1200StatusDmTwoWayAverageDelayVariation": me1200StatusDmTwoWayAverageDelayVariation,
       "me1200StatusDmTwoWayAverageLastnDelayVariation": me1200StatusDmTwoWayAverageLastnDelayVariation,
       "me1200StatusDmTwoWayMinimumDelay": me1200StatusDmTwoWayMinimumDelay,
       "me1200StatusDmTwoWayMaximumDelay": me1200StatusDmTwoWayMaximumDelay,
       "me1200StatusDmTwoWayMinimumDelayVariation": me1200StatusDmTwoWayMinimumDelayVariation,
       "me1200StatusDmTwoWayMaximumDelayVariation": me1200StatusDmTwoWayMaximumDelayVariation,
       "me1200StatusDmTwoWayTimeUnit": me1200StatusDmTwoWayTimeUnit,
       "me1200StatusDmOneWayFarNearTable": me1200StatusDmOneWayFarNearTable,
       "me1200StatusDmOneWayFarNearEntry": me1200StatusDmOneWayFarNearEntry,
       "me1200StatusDmOneWayFarNearId": me1200StatusDmOneWayFarNearId,
       "me1200StatusDmOneWayFarNearTxCounter": me1200StatusDmOneWayFarNearTxCounter,
       "me1200StatusDmOneWayFarNearRxCounter": me1200StatusDmOneWayFarNearRxCounter,
       "me1200StatusDmOneWayFarNearRxTimeOutCounter": me1200StatusDmOneWayFarNearRxTimeOutCounter,
       "me1200StatusDmOneWayFarNearRxErrorCounter": me1200StatusDmOneWayFarNearRxErrorCounter,
       "me1200StatusDmOneWayFarNearInternalOverflowCounter": me1200StatusDmOneWayFarNearInternalOverflowCounter,
       "me1200StatusDmOneWayFarNearAverageDelay": me1200StatusDmOneWayFarNearAverageDelay,
       "me1200StatusDmOneWayFarNearAverageLastnDelay": me1200StatusDmOneWayFarNearAverageLastnDelay,
       "me1200StatusDmOneWayFarNearAverageDelayVariation": me1200StatusDmOneWayFarNearAverageDelayVariation,
       "me1200StatusDmOneWayFarNearAverageLastnDelayVariation": me1200StatusDmOneWayFarNearAverageLastnDelayVariation,
       "me1200StatusDmOneWayFarNearMinimumDelay": me1200StatusDmOneWayFarNearMinimumDelay,
       "me1200StatusDmOneWayFarNearMaximumDelay": me1200StatusDmOneWayFarNearMaximumDelay,
       "me1200StatusDmOneWayFarNearMinimumDelayVariation": me1200StatusDmOneWayFarNearMinimumDelayVariation,
       "me1200StatusDmOneWayFarNearMaximumDelayVariation": me1200StatusDmOneWayFarNearMaximumDelayVariation,
       "me1200StatusDmOneWayFarNearTimeUnit": me1200StatusDmOneWayFarNearTimeUnit,
       "me1200StatusDmOneWayNearFarTable": me1200StatusDmOneWayNearFarTable,
       "me1200StatusDmOneWayNearFarEntry": me1200StatusDmOneWayNearFarEntry,
       "me1200StatusDmOneWayNearFarId": me1200StatusDmOneWayNearFarId,
       "me1200StatusDmOneWayNearFarTxCounter": me1200StatusDmOneWayNearFarTxCounter,
       "me1200StatusDmOneWayNearFarRxCounter": me1200StatusDmOneWayNearFarRxCounter,
       "me1200StatusDmOneWayNearFarRxTimeOutCounter": me1200StatusDmOneWayNearFarRxTimeOutCounter,
       "me1200StatusDmOneWayNearFarRxErrorCounter": me1200StatusDmOneWayNearFarRxErrorCounter,
       "me1200StatusDmOneWayNearFarInternalOverflowCounter": me1200StatusDmOneWayNearFarInternalOverflowCounter,
       "me1200StatusDmOneWayNearFarAverageDelay": me1200StatusDmOneWayNearFarAverageDelay,
       "me1200StatusDmOneWayNearFarAverageLastnDelay": me1200StatusDmOneWayNearFarAverageLastnDelay,
       "me1200StatusDmOneWayNearFarAverageDelayVariation": me1200StatusDmOneWayNearFarAverageDelayVariation,
       "me1200StatusDmOneWayNearFarAverageLastnDelayVariation": me1200StatusDmOneWayNearFarAverageLastnDelayVariation,
       "me1200StatusDmOneWayNearFarMinimumDelay": me1200StatusDmOneWayNearFarMinimumDelay,
       "me1200StatusDmOneWayNearFarMaximumDelay": me1200StatusDmOneWayNearFarMaximumDelay,
       "me1200StatusDmOneWayNearFarMinimumDelayVariation": me1200StatusDmOneWayNearFarMinimumDelayVariation,
       "me1200StatusDmOneWayNearFarMaximumDelayVariation": me1200StatusDmOneWayNearFarMaximumDelayVariation,
       "me1200StatusDmOneWayNearFarTimeUnit": me1200StatusDmOneWayNearFarTimeUnit,
       "me1200StatusDmFdBinsTable": me1200StatusDmFdBinsTable,
       "me1200StatusDmFdBinsEntry": me1200StatusDmFdBinsEntry,
       "me1200StatusDmFdBinsId": me1200StatusDmFdBinsId,
       "me1200StatusDmFdBinsBinNumber": me1200StatusDmFdBinsBinNumber,
       "me1200StatusDmFdBinsTwValue": me1200StatusDmFdBinsTwValue,
       "me1200StatusDmFdBinsOwFtNValue": me1200StatusDmFdBinsOwFtNValue,
       "me1200StatusDmFdBinsOwNtFValue": me1200StatusDmFdBinsOwNtFValue,
       "me1200StatusDmIfdvBinsTable": me1200StatusDmIfdvBinsTable,
       "me1200StatusDmIfdvBinsEntry": me1200StatusDmIfdvBinsEntry,
       "me1200StatusDmIfdvBinsId": me1200StatusDmIfdvBinsId,
       "me1200StatusDmIfdvBinsBinNumber": me1200StatusDmIfdvBinsBinNumber,
       "me1200StatusDmIfdvBinsTwValue": me1200StatusDmIfdvBinsTwValue,
       "me1200StatusDmIfdvBinsOwFtNValue": me1200StatusDmIfdvBinsOwFtNValue,
       "me1200StatusDmIfdvBinsOwNtFValue": me1200StatusDmIfdvBinsOwNtFValue,
       "me1200StatusLoopBack": me1200StatusLoopBack,
       "me1200StatusLbTable": me1200StatusLbTable,
       "me1200StatusLbEntry": me1200StatusLbEntry,
       "me1200StatusLbId": me1200StatusLbId,
       "me1200StatusLbTransactionId": me1200StatusLbTransactionId,
       "me1200StatusLbReplyCounter": me1200StatusLbReplyCounter,
       "me1200StatusLbLbmTransmitted": me1200StatusLbLbmTransmitted,
       "me1200StatusLbReplyTable": me1200StatusLbReplyTable,
       "me1200StatusLbReplyEntry": me1200StatusLbReplyEntry,
       "me1200StatusLbReplyId": me1200StatusLbReplyId,
       "me1200StatusLbReplyReplyId": me1200StatusLbReplyReplyId,
       "me1200StatusLbReplyMac": me1200StatusLbReplyMac,
       "me1200StatusLbReplyLbrReceived": me1200StatusLbReplyLbrReceived,
       "me1200StatusLbReplyOutOfOrder": me1200StatusLbReplyOutOfOrder,
       "me1200StatusTestSignal": me1200StatusTestSignal,
       "me1200StatusTstTable": me1200StatusTstTable,
       "me1200StatusTstEntry": me1200StatusTstEntry,
       "me1200StatusTstId": me1200StatusTstId,
       "me1200StatusTstTxCounter": me1200StatusTstTxCounter,
       "me1200StatusTstRxCounter": me1200StatusTstRxCounter,
       "me1200StatusTstOutOfOrderCounter": me1200StatusTstOutOfOrderCounter,
       "me1200StatusTstRxRate": me1200StatusTstRxRate,
       "me1200StatusTstTestTime": me1200StatusTstTestTime,
       "me1200StatusLinkTrace": me1200StatusLinkTrace,
       "me1200StatusLtTable": me1200StatusLtTable,
       "me1200StatusLtEntry": me1200StatusLtEntry,
       "me1200StatusLtId": me1200StatusLtId,
       "me1200StatusLtTransactionId": me1200StatusLtTransactionId,
       "me1200StatusLtReplyCount": me1200StatusLtReplyCount,
       "me1200StatusLtReplyTable": me1200StatusLtReplyTable,
       "me1200StatusLtReplyEntry": me1200StatusLtReplyEntry,
       "me1200StatusLtReplyId": me1200StatusLtReplyId,
       "me1200StatusLtReplyReplyId": me1200StatusLtReplyReplyId,
       "me1200StatusLtReplyMode": me1200StatusLtReplyMode,
       "me1200StatusLtReplyDirection": me1200StatusLtReplyDirection,
       "me1200StatusLtReplyTtl": me1200StatusLtReplyTtl,
       "me1200StatusLtReplyForwarded": me1200StatusLtReplyForwarded,
       "me1200StatusLtReplyRelayAction": me1200StatusLtReplyRelayAction,
       "me1200StatusLtReplyLastEgressMac": me1200StatusLtReplyLastEgressMac,
       "me1200StatusLtReplyNextEgressMac": me1200StatusLtReplyNextEgressMac,
       "me1200StatusContinuityCheck": me1200StatusContinuityCheck,
       "me1200StatusCCPeerTable": me1200StatusCCPeerTable,
       "me1200StatusCCPeerEntry": me1200StatusCCPeerEntry,
       "me1200StatusCCPeerId": me1200StatusCCPeerId,
       "me1200StatusCCPeerPeerId": me1200StatusCCPeerPeerId,
       "me1200StatusCCPeerOsTlvOuiFirst": me1200StatusCCPeerOsTlvOuiFirst,
       "me1200StatusCCPeerOsTlvOuiSecond": me1200StatusCCPeerOsTlvOuiSecond,
       "me1200StatusCCPeerOsTlvOuiThird": me1200StatusCCPeerOsTlvOuiThird,
       "me1200StatusCCPeerOsTlvSubType": me1200StatusCCPeerOsTlvSubType,
       "me1200StatusCCPeerOsTlvValue": me1200StatusCCPeerOsTlvValue,
       "me1200StatusCCPeerIsTlvValue": me1200StatusCCPeerIsTlvValue,
       "me1200StatusCCPeerPsTlvValue": me1200StatusCCPeerPsTlvValue,
       "me1200StatusCCPeerOsTlvReceived": me1200StatusCCPeerOsTlvReceived,
       "me1200StatusCCPeerIsTlvReceived": me1200StatusCCPeerIsTlvReceived,
       "me1200StatusCCPeerPsTlvReceived": me1200StatusCCPeerPsTlvReceived,
       "me1200StatusLmAvailability": me1200StatusLmAvailability,
       "me1200StatusLmAvailTable": me1200StatusLmAvailTable,
       "me1200StatusLmAvailEntry": me1200StatusLmAvailEntry,
       "me1200StatusLmAvailId": me1200StatusLmAvailId,
       "me1200StatusLmAvailPeerId": me1200StatusLmAvailPeerId,
       "me1200StatusLmAvailNearEndAvailState": me1200StatusLmAvailNearEndAvailState,
       "me1200StatusLmAvailFarEndAvailState": me1200StatusLmAvailFarEndAvailState,
       "me1200StatusLmAvailNearEndAvailCnt": me1200StatusLmAvailNearEndAvailCnt,
       "me1200StatusLmAvailFarEndAvailCnt": me1200StatusLmAvailFarEndAvailCnt,
       "me1200StatusLmAvailNearEndUnAvailCnt": me1200StatusLmAvailNearEndUnAvailCnt,
       "me1200StatusLmAvailFarEndUnAvailCnt": me1200StatusLmAvailFarEndUnAvailCnt,
       "me1200StatusLmAvailNearEndWindowCnt": me1200StatusLmAvailNearEndWindowCnt,
       "me1200StatusLmAvailFarEndWindowCnt": me1200StatusLmAvailFarEndWindowCnt,
       "me1200MepControl": me1200MepControl,
       "me1200ControlLossMeasurement": me1200ControlLossMeasurement,
       "me1200ControlLmTable": me1200ControlLmTable,
       "me1200ControlLmEntry": me1200ControlLmEntry,
       "me1200ControlLmId": me1200ControlLmId,
       "me1200ControlLmClear": me1200ControlLmClear,
       "me1200ControlDelayMeasurement": me1200ControlDelayMeasurement,
       "me1200ControlDmTable": me1200ControlDmTable,
       "me1200ControlDmEntry": me1200ControlDmEntry,
       "me1200ControlDmId": me1200ControlDmId,
       "me1200ControlDmClear": me1200ControlDmClear,
       "me1200ControlTestSignal": me1200ControlTestSignal,
       "me1200ControlTstTable": me1200ControlTstTable,
       "me1200ControlTstEntry": me1200ControlTstEntry,
       "me1200ControlTstId": me1200ControlTstId,
       "me1200ControlTstClear": me1200ControlTstClear,
       "me1200MepNotificationPrefix": me1200MepNotificationPrefix,
       "me1200MeptNotification": me1200MeptNotification,
       "me1200MepNotificationLmNearEndLossRatioThresholdExceed": me1200MepNotificationLmNearEndLossRatioThresholdExceed,
       "me1200MepNotificationLmFarEndLossRatioThresholdExceed": me1200MepNotificationLmFarEndLossRatioThresholdExceed,
       "me1200MepNotificationDmTwoWayAvgLastnDelayExceed": me1200MepNotificationDmTwoWayAvgLastnDelayExceed,
       "me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery": me1200MepNotificationDmTwoWayAvgLastnDelayExceedRecovery,
       "me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed": me1200MepNotificationDmTwoWayAvgLastnDelayVarExceed,
       "me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery": me1200MepNotificationDmTwoWayAvgLastnDelayVarExceedRecovery,
       "me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed": me1200MepNotificationDmOneWayF2NAvgLastnDelayExceed,
       "me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery": me1200MepNotificationDmOneWayF2NAvgLastnDelayExceedRecovery,
       "me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed": me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceed,
       "me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery": me1200MepNotificationDmOneWayF2NAvgLastnDelayVarExceedRecovery,
       "me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed": me1200MepNotificationDmOneWayN2FAvgLastnDelayExceed,
       "me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery": me1200MepNotificationDmOneWayN2FAvgLastnDelayExceedRecovery,
       "me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed": me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceed,
       "me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery": me1200MepNotificationDmOneWayN2FAvgLastnDelayVarExceedRecovery,
       "me1200MepMibConformance": me1200MepMibConformance,
       "me1200MepMibCompliances": me1200MepMibCompliances,
       "me1200MepMibCompliance": me1200MepMibCompliance,
       "me1200MepMibGroups": me1200MepMibGroups,
       "me1200MepCapabilitiesInfoGroup": me1200MepCapabilitiesInfoGroup,
       "me1200ConfigInstanceTableInfoGroup": me1200ConfigInstanceTableInfoGroup,
       "me1200ConfigInstanceRowEditorInfoGroup": me1200ConfigInstanceRowEditorInfoGroup,
       "me1200ConfigInstancePeerTableInfoGroup": me1200ConfigInstancePeerTableInfoGroup,
       "me1200ConfigInstancePeerRowEditorInfoGroup": me1200ConfigInstancePeerRowEditorInfoGroup,
       "me1200ConfigPmTableInfoGroup": me1200ConfigPmTableInfoGroup,
       "me1200ConfigCcTableInfoGroup": me1200ConfigCcTableInfoGroup,
       "me1200ConfigCcRowEditorInfoGroup": me1200ConfigCcRowEditorInfoGroup,
       "me1200ConfigLmTableInfoGroup": me1200ConfigLmTableInfoGroup,
       "me1200ConfigLmRowEditorInfoGroup": me1200ConfigLmRowEditorInfoGroup,
       "me1200ConfigDmTableInfoGroup": me1200ConfigDmTableInfoGroup,
       "me1200ConfigDmRowEditorInfoGroup": me1200ConfigDmRowEditorInfoGroup,
       "me1200ConfigLbTableInfoGroup": me1200ConfigLbTableInfoGroup,
       "me1200ConfigLbRowEditorInfoGroup": me1200ConfigLbRowEditorInfoGroup,
       "me1200ConfigTstTableInfoGroup": me1200ConfigTstTableInfoGroup,
       "me1200ConfigTstRowEditorInfoGroup": me1200ConfigTstRowEditorInfoGroup,
       "me1200ConfigLtTableInfoGroup": me1200ConfigLtTableInfoGroup,
       "me1200ConfigLtRowEditorInfoGroup": me1200ConfigLtRowEditorInfoGroup,
       "me1200ConfigApsTableInfoGroup": me1200ConfigApsTableInfoGroup,
       "me1200ConfigApsRowEditorInfoGroup": me1200ConfigApsRowEditorInfoGroup,
       "me1200ConfigAisTableInfoGroup": me1200ConfigAisTableInfoGroup,
       "me1200ConfigAisRowEditorInfoGroup": me1200ConfigAisRowEditorInfoGroup,
       "me1200ConfigLckTableInfoGroup": me1200ConfigLckTableInfoGroup,
       "me1200ConfigLckRowEditorInfoGroup": me1200ConfigLckRowEditorInfoGroup,
       "me1200ConfigClientTableInfoGroup": me1200ConfigClientTableInfoGroup,
       "me1200ConfigClientFlowTableInfoGroup": me1200ConfigClientFlowTableInfoGroup,
       "me1200ConfigClientFlowRowEditorInfoGroup": me1200ConfigClientFlowRowEditorInfoGroup,
       "me1200ConfigSyslogTableInfoGroup": me1200ConfigSyslogTableInfoGroup,
       "me1200ConfigTlvLeafInfoGroup": me1200ConfigTlvLeafInfoGroup,
       "me1200ConfigLstTableInfoGroup": me1200ConfigLstTableInfoGroup,
       "me1200ConfigLmAvailTableInfoGroup": me1200ConfigLmAvailTableInfoGroup,
       "me1200ConfigLmAvailRowEditorInfoGroup": me1200ConfigLmAvailRowEditorInfoGroup,
       "me1200StatusInstanceTableInfoGroup": me1200StatusInstanceTableInfoGroup,
       "me1200StatusInstancePeerTableInfoGroup": me1200StatusInstancePeerTableInfoGroup,
       "me1200StatusLmTableInfoGroup": me1200StatusLmTableInfoGroup,
       "me1200StatusLmPeerTableInfoGroup": me1200StatusLmPeerTableInfoGroup,
       "me1200StatusDmTwoWayTableInfoGroup": me1200StatusDmTwoWayTableInfoGroup,
       "me1200StatusDmOneWayFarNearTableInfoGroup": me1200StatusDmOneWayFarNearTableInfoGroup,
       "me1200StatusDmOneWayNearFarTableInfoGroup": me1200StatusDmOneWayNearFarTableInfoGroup,
       "me1200StatusDmFdBinsTableInfoGroup": me1200StatusDmFdBinsTableInfoGroup,
       "me1200StatusDmIfdvBinsTableInfoGroup": me1200StatusDmIfdvBinsTableInfoGroup,
       "me1200StatusLbTableInfoGroup": me1200StatusLbTableInfoGroup,
       "me1200StatusLbReplyTableInfoGroup": me1200StatusLbReplyTableInfoGroup,
       "me1200StatusTstTableInfoGroup": me1200StatusTstTableInfoGroup,
       "me1200StatusLtTableInfoGroup": me1200StatusLtTableInfoGroup,
       "me1200StatusLtReplyTableInfoGroup": me1200StatusLtReplyTableInfoGroup,
       "me1200StatusCCPeerTableInfoGroup": me1200StatusCCPeerTableInfoGroup,
       "me1200StatusLmAvailTableInfoGroup": me1200StatusLmAvailTableInfoGroup,
       "me1200ControlLmTableInfoGroup": me1200ControlLmTableInfoGroup,
       "me1200ControlDmTableInfoGroup": me1200ControlDmTableInfoGroup,
       "me1200ControlTstTableInfoGroup": me1200ControlTstTableInfoGroup,
       "me1200MepNotificationInfoGroup": me1200MepNotificationInfoGroup}
)
